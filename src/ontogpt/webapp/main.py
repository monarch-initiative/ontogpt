"""OntoGPT Webapp main function.

This module sets up a FastAPI web application for
the OntoGPT project. It includes routes for handling
GET and POST requests, and integrates with components
such as SPIRESEngine and HTMLExporter to process and
display data.

Classes:
    Query: A Pydantic model representing the structure
    of the form data.

Functions:
    get_engine(datamodel: str, llm_model: str) -> SPIRESEngine:
        Retrieves or initializes a SPIRESEngine instance for
        the given datamodel and LLM model.

    read_root(request: Request) -> TemplateResponse:
        Handles GET requests to the root URL,
        rendering the form.html template.

    form_post(request: Request, datamodel: str = Form(...),
        text: str = Form(...), llm_model: str = Form(...))
        -> TemplateResponse:
        Handles POST requests to the root URL, processing
        the form data and rendering the results.html template.

    start():
        Launches the FastAPI application using Uvicorn.
"""

from io import StringIO
from pathlib import Path
from typing import Dict

import uvicorn
from fastapi import FastAPI, Form, Request
from pydantic import BaseModel
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from ontogpt.cli import _get_templates
from ontogpt.engines.spires_engine import SPIRESEngine
from ontogpt.io.html_exporter import HTMLExporter
from ontogpt.io.template_loader import get_template_details

this_path = Path(__file__).parent
static_dir = this_path / "static"
html_dir = this_path / "html"

# Populate the dict of available models
DATAMODELS = {}
all_templates = _get_templates()
all_templates = dict(sorted(all_templates.items()))
for template_id, (_name, description) in all_templates.items():
    DATAMODELS[template_id] = f"{description}"

LLM_MODELS = [
    "gpt-4o-mini",
    "gpt-4o",
    "gpt-4",
    "gpt-4-turbo",
    "ollama/llama2",
    "ollama/llama3",
    "ollama/orca-mini",
]


class Query(BaseModel):
    text: str
    datamodel: str
    model: str


app = FastAPI()
static_dir.mkdir(parents=True, exist_ok=True)
app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")
templates = Jinja2Templates(directory=str(html_dir))

html_exporter = HTMLExporter(output=None)
engines: Dict[str, SPIRESEngine] = {}


def get_engine(datamodel: str, llm_model: str):
    if datamodel not in engines:
        template_details = get_template_details(template=datamodel)
        engines[datamodel] = SPIRESEngine(model=llm_model, template_details=template_details)
    return engines[datamodel]


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse(
        "form.html",
        context={"request": request, "datamodels": DATAMODELS, "llm_models": LLM_MODELS},
    )


@app.post("/")
def form_post(
    request: Request, datamodel: str = Form(...), text: str = Form(...), llm_model: str = Form(...)
):
    print(f"Received request with schema {datamodel}")
    print(f"Received request with text {text}")
    print(f"Received request to be sent to {llm_model}")
    engine = get_engine(datamodel, llm_model)
    ann = engine.extract_from_text(text)
    print(f"Got {ann}")
    output = StringIO()
    html_exporter.export(extraction_output=ann, output=output)
    return templates.TemplateResponse(
        "results.html", context={"request": request, "inner_html": output.getvalue()}
    )


def start():
    """Launch with `uv run start` at root level."""
    uvicorn.run("ontogpt.webapp.main:app", host="127.0.0.1", port=8000, reload=True)
