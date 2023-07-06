import yaml
from src.ontogpt.io.csv_wrapper import write_obj_as_csv
import time
import pprint

lines = []

output_file = "long_output.yaml"#"output.yaml"

with open(output_file, "r") as file:
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
# copy_cleaned_lines = cleaned_lines[:]
for i in range(len(cleaned_lines) - 1):
    if cleaned_lines[i].startswith("raw_completion_output") and cleaned_lines[i+1].startswith("raw_completion_output"):
        cleaned_lines.insert(i+1, "  genes:")
        cleaned_lines.insert(i+2, "  exposures:")
        cleaned_lines.insert(i+3, "  gene_exposures_relationships:")
        i += 4
grouped_lines = [cleaned_lines[n:n+4] for n in range(0, len(cleaned_lines), 4)]
trimmed_dict = {}
trimmed_dict["genes"] = []
trimmed_dict["exposures"] = []
trimmed_dict["relationships"] = []
for group in grouped_lines:
    group.pop(0)
for group in grouped_lines:
    gene, exposure, relation = None, None, None
    # try:
    gene = group[0].split(":", 1)[1].strip()
    exposure = group[1].split(":", 1)[1].strip()
    relation = group[2].split(":", 1)[1].strip()
    # print("GENE: \t\t", gene)
    # print("EXPOSURE: \t", exposure)
    # print("RELATION: \t", relation)
    trimmed_dict["genes"].append(gene)
    trimmed_dict["exposures"].append(exposure)
    trimmed_dict["relationships"].append(relation)
    # except IndexError:
    #     continue

# pprint.pprint(trimmed_dict)
# print(trimmed_dict)