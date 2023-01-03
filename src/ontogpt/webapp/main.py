from io import StringIO
from pathlib import Path
from typing import Dict

import uvicorn
from fastapi import FastAPI, Form, Request
from pydantic import BaseModel
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from ontogpt.engines.knowledge_engine import DATAMODELS
from ontogpt.engines.spires_engine import SPIRESEngine
from ontogpt.io.html_exporter import HTMLExporter

this_path = Path(__file__).parent
static_dir = this_path / "static"
html_dir = this_path / "html"


class Query(BaseModel):
    text: str
    datamodel: str


app = FastAPI()

app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")
templates = Jinja2Templates(directory=str(html_dir))

html_exporter = HTMLExporter()
engines: Dict[str, SPIRESEngine] = {}


def get_engine(datamodel: str):
    if datamodel not in engines:
        engines[datamodel] = SPIRESEngine(datamodel)
    return engines[datamodel]


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse(
        "form.html", context={"request": request, "datamodels": DATAMODELS}
    )


@app.post("/")
def form_post(request: Request, datamodel: str = Form(...), text: str = Form(...)):
    print(f"Received request with schema {datamodel}")
    print(f"Received request with text {text}")
    engine = get_engine(datamodel)
    ann = engine.extract_from_text(text)
    print(f"Got {ann}")
    output = StringIO()
    html_exporter.export(ann, output)
    return templates.TemplateResponse(
        "results.html", context={"request": request, "inner_html": output.getvalue()}
    )


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("ontogpt.webapp.main:app", host="0.0.0.0", port=8000, reload=True)
