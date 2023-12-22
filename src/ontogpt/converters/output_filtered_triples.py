import yaml
from yaml import CLoader as Loader
from oaklib import get_adapter

NULL_VALS = [
    "",
    "Not mentioned",
    "none mentioned",
    "Not mentioned in the text",
    "Not mentioned in the provided text.",
    "No exposures mentioned in the text.",
    "None",
    "N/A",
    "No exposures mentioned in the text.",
    "None mentioned in the text",
    "Not mentioned in the text.",
    "None relevant",
    "None mentioned in the text.",
    "No gene to molecular activity relationships mentioned in the text.",
    "No genes mentioned",
    "No genes mentioned in the text.",
    "NA",
    "-",
    "None mentioned",
]
# output_file = "experiments/ibd_literature/output_2000_1122.yaml"


def output_filtered_triples(input_file, subject_prefix, object_prefix, pred_prefix):
    filtered_data = []

    def filter_dictionary(input_dict, filter_keys):
        filtered_dict = {key: value for key, value in input_dict.items() if key in filter_keys}
        return filtered_dict

    # TODO:
    # 1. This does not handle situations where the subject or object or predicate is a list of values
    # 2. This does not handle situations where any of the above are None (as in, not specified)
    # 3. This does not handle situations where the input triples may be missing s, p, or o
    # 4. This does not allow us to not label s, p, or o
    # 5. This makes the assumption that the adapter is the same as the prefix
    with open(input_file, "r") as file:
        for doc in yaml.safe_load_all(file):
            try:
                for dict in doc["extracted_object"]["disease_cellular_process_relationships"]:
                    entry = filter_dictionary(dict, ["subject", "predicate", "object"])
                    if (
                        len(entry) == 3
                        and entry["subject"] not in NULL_VALS
                        and entry["predicate"] not in NULL_VALS
                        and entry["object"] not in NULL_VALS
                    ):
                        if entry["subject"].startswith(f"{subject_prefix}:") and entry[
                            "object"
                        ].startswith(f"{object_prefix}:"):
                            entry["subject"] = get_adapter(f"sqlite:obo:{subject_prefix}").label(
                                entry["subject"]
                            )
                            entry["object"] = get_adapter(f"sqlite:obo:{object_prefix}").label(
                                entry["object"]
                            )
                            if entry["predicate"].startswith(f"{pred_prefix}:"):
                                entry["predicate"] = get_adapter(f"sqlite:obo:{pred_prefix}").label(
                                    entry["predicate"]
                                )
                            filtered_data.append(entry)
            except:
                continue

    return filtered_data
