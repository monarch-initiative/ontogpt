import yaml
from yaml import CLoader as Loader
from oaklib import get_adapter

NULL_VALS = ['', 'Not mentioned', 'none mentioned', 'Not mentioned in the text', 
             'Not mentioned in the provided text.', 'No exposures mentioned in the text.', 
             'None', 'N/A', 'No exposures mentioned in the text.', 'None mentioned in the text', 
             'Not mentioned in the text.', 'None relevant', 'None mentioned in the text.', 
             'No gene to molecular activity relationships mentioned in the text.',
             'No genes mentioned', 'No genes mentioned in the text.', 'NA', '-',
             'None mentioned']
# output_file = "experiments/ibd_literature/output_2000_1122.yaml"

def output_filtered_triples(output_file):
    filtered_data = []

    def filter_dictionary(input_dict, filter_keys):
        filtered_dict = {key: value for key, value in input_dict.items() if key in filter_keys}
        return filtered_dict

    with open(output_file, 'r') as file:
        for doc in yaml.safe_load_all(file):
            try:
                for dict in doc["extracted_object"]["disease_cellular_process_relationships"]:
                    entry = filter_dictionary(dict, ["subject", "predicate", "object"])
                    if (len(entry) == 3 and
                        entry["subject"] not in NULL_VALS and
                        entry["predicate"] not in NULL_VALS and
                        entry["object"] not in NULL_VALS):
                        if (entry["subject"].startswith("MONDO:") and
                            entry["object"].startswith("GO:")):
                            entry["subject"] = get_adapter("sqlite:obo:MONDO").label(entry["subject"])
                            entry["object"] = get_adapter("sqlite:obo:GO").label(entry["object"])
                            if entry["predicate"].startswith("RO:"):
                                entry["predicate"] = get_adapter("sqlite:obo:RO").label(entry["predicate"])
                    filtered_data.append(entry)
            except:
                continue
    
    return filtered_data

"""    for entry in filtered_data:
        if (len(entry) == 3 and
            entry["subject"] not in NULL_VALS and
            entry["predicate"] not in NULL_VALS and
            entry["object"] not in NULL_VALS):
            if (entry["subject"].startswith("MONDO:") and
                entry["object"].startswith("GO:")):
                entry["subject"] = get_adapter("sqlite:obo:MONDO").label(entry["subject"])
                # if entry["predicate"].startswith("RO:"):
                #     entry["predicate"] = get_adapter("sqlite:obo:RO").label(entry["predicate"])
                entry["object"] = get_adapter("sqlite:obo:GO").label(entry["object"])
                if entry["predicate"].startswith("RO:"):
                    entry["predicate"] = get_adapter("sqlite:obo:RO").label(entry["predicate"])
                print(entry)"""