import yaml
import time
import pprint
from oaklib import get_adapter

NULL_VALS = ['', 'Not mentioned', 'none mentioned', 'Not mentioned in the text', 
             'Not mentioned in the provided text.', 'No exposures mentioned in the text.', 
             'None', 'N/A', 'No exposures mentioned in the text.', 'None mentioned in the text', 
             'Not mentioned in the text.', 'None relevant', 'None mentioned in the text.', 
             'No gene to molecular activity relationships mentioned in the text.',
             'No genes mentioned', 'No genes mentioned in the text.']
lines = []
chebi_adapter = get_adapter("sqlite:obo:CHEBI")
output_file = "output_2000_0719.yaml"

def tripleprint(dict):
    key = next(iter(dict))
    for i in range(len(dict[key])):
        curr = []
        for value in dict.values():
            curr.append(value[i])
        print(curr)
def forprint(lst):
    for elem in lst:
        print(elem)
def nprint(lst, n):
    for i in range(n):
        print(lst[i])
def sleepprint(lst):
    for elem in lst:
        print(elem)
        time.sleep(0.5)
def enumprint(lst):
    for index, elem in enumerate(lst):
        # print((index + 1), ": ", elem)
        print(str(index + 1) + ":\t" + str(elem))

with open(output_file, "r") as file:
    to_print = False
    # terminators = tuple(["input_text", "  qualifier", "  subject_qualifier", "  object_qualifier"])
    perpetuators = tuple(["  subject:", "  predicate:", "  object:", "    "])
    for line in file:
        line = line.strip("\n")
        # if line.startswith("raw_completion_output"):
        if line.startswith("extracted_object:"):
            to_print = True
        # elif line.startswith("prompt"):
        # elif line.startswith(terminators):
        elif not line.startswith(perpetuators):
            to_print = False
        if to_print:
            lines.append(line)

# lines = list(filter(lambda elem: not(elem.isspace()), lines))
cleaned_lines = [x for x in list(filter(lambda elem: not(elem.isspace()), lines)) if x.strip()]
# forprint(cleaned_lines)
cleaned_lines = [x for x in cleaned_lines if x != "extracted_object: {}"]
# nprint(cleaned_lines, 100)
i = 1
while i < len(cleaned_lines):
    if cleaned_lines[i].startswith("    "):
        cleaned_lines[i-1] += " "
        cleaned_lines[i-1] += cleaned_lines[i][4:]
        del cleaned_lines[i]
    else:
        i += 1
"""for i in range(len(cleaned_lines) - 1):
    if cleaned_lines[i].startswith("raw_completion_output") and cleaned_lines[i+1].startswith("raw_completion_output"):
        cleaned_lines.insert(i+1, "  genes:")
        cleaned_lines.insert(i+2, "  exposures:")
        cleaned_lines.insert(i+3, "  gene_exposures_relationships:")
        i += 4"""
i = 0
while i < len(cleaned_lines):
    if cleaned_lines[i].startswith("extracted_object"):
        # for elem in cleaned_lines[i+1:i+4]:
        for index, elem in enumerate(cleaned_lines[i+1:i+4]):
            if elem.startswith("extracted_object"):
                # next_index = i + 1 + cleaned_lines[i+1:i+4].index("extracted_object")
                next_index = i + 1 + index
                del cleaned_lines[i:next_index]
                i -= 1
    i += 1
# forprint(cleaned_lines)

grouped_lines = [cleaned_lines[n:n+4] for n in range(0, len(cleaned_lines), 4)]
trimmed_dict = {"genes": [], "relationships": [], "exposures": []}
for group in grouped_lines:
    group.pop(0)

for group in grouped_lines:
    # print(group)
    gene = group[0].split(":", 1)[1].strip()
    relation = group[1].split(":", 1)[1].strip()
    exposure = group[2].split(":", 1)[1].strip()
    # print("GENE: \t\t", gene)
    # print("EXPOSURE: \t", exposure)
    # print("RELATION: \t", relation)
    trimmed_dict["genes"].append(gene)
    trimmed_dict["relationships"].append(relation)
    trimmed_dict["exposures"].append(exposure)

for key, value in trimmed_dict.copy().items():
    for i, elem in enumerate(value):
        if elem.lower() in (val.lower() for val in NULL_VALS):
            for key, value in trimmed_dict.items():
                del value[i]

# for key, value in trimmed_dict.items():
#     print(len(value))

# tripleprint(trimmed_dict)
# pprint.pprint(trimmed_dict)
# print(trimmed_dict)

subjects_with_chebi = []
# objects_with_ecto = []
key = next(iter(trimmed_dict))
for i in range(len(trimmed_dict[key])):
    curr = []
    for value in trimmed_dict.values():
        curr.append(value[i])
    subjects_with_chebi.append(curr)
    # objects_with_ecto.append(curr)
subjects_with_chebi = [x for x in subjects_with_chebi if x[0].startswith("CHEBI:")]
# objects_with_ecto = [x for x in objects_with_ecto if x[2].startswith("ECTO:")]

# subjects_with_names = [elem[:] for elem in subjects_with_chebi]
subjects_with_names = []
for elem in subjects_with_chebi:
    curr = elem[:]
    curr[0] = chebi_adapter.label(curr[0])
    subjects_with_names.append(curr)

# enumprint(subjects_with_chebi)
# enumprint(objects_with_ecto)
# enumprint(subjects_with_names)

"""for key, value in trimmed_dict.copy().items():
    for index, elem in enumerate(value):
        if ":" in elem:
            try:
                prefix = elem[:(elem.index(":"))]
                adapter_str = "sqlite:obo:" + str(prefix)
                curr_adapter = get_adapter(adapter_str)
                trimmed_dict[key][index] = curr_adapter.label(elem)
            except:
                continue

tripleprint(trimmed_dict)"""