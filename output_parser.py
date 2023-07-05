import yaml
from src.ontogpt.io.csv_wrapper import write_obj_as_csv
import time
import pprint

lines = []

with open("output.yaml", "r") as file:
    to_print = False
    for line in file:
        line = line.strip("\n")
        if line.startswith("raw_completion_output"):
            # next(file)
            to_print = True
        elif line.startswith("prompt"):
            to_print = False
        if to_print:
            lines.append(line)
            # print(line)

# print(len(lines))
lines = list(filter(lambda elem: not(elem.isspace()), lines))
cleaned_lines = [x for x in lines if x.strip()]
grouped_lines = [cleaned_lines[n:n+4] for n in range(0, len(cleaned_lines), 4)]
trimmed_dict = {}
trimmed_dict["genes"] = []
trimmed_dict["exposures"] = []
trimmed_dict["relationships"] = []
for group in grouped_lines:
    group.pop(0)
for group in grouped_lines:
    gene = group[0].split(":", 1)[1].strip()
    exposure = group[1].split(":", 1)[1].strip()
    relation = group[2].split(":", 1)[1].strip()
    # print("GENE: \t\t", gene)
    # print("EXPOSURE: \t", exposure)
    # print("RELATION: \t", relation)
    trimmed_dict["genes"].append(gene)
    trimmed_dict["exposures"].append(exposure)
    trimmed_dict["relationships"].append(relation)

pprint.pprint(trimmed_dict)
# print(trimmed_dict)