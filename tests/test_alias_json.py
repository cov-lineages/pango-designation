#! /usr/bin/env python3
import json
import re

SKIP_VALID_ALIAS = {
    "A",
    "B",
}

SKIP_UNIQUE_VALUE_FOR_KEYS = {
    "A",
    "B",
    "XD",
    "XE",
    "XF",
    "XG",
    "XH",
    "XJ",
    "XK",
    "XL",
    "XM",
    "XM",
    "XN",
    "XP",
    "XQ",
    "XR",
    "XT",
    "XU",
    "XV",
    "XW",
    "XY",
    "XZ",
    "XAA",
    "XAB",
    "XAC",
    "XAD",
    "XAD",
    "XAE",
    "XAE",
    "XAF",
    "XAG",
    "XAH",
    "XAH",
    "XAK",
    "XAL",
    "XAP",
    "XAP",
    "XAQ",
    "XAR",
    "XAY",
    "XBA",
    "XBK",
    "XBP",
    "XBQ",
    "XBR",
    "XBS",
    "XCA",
}

def are_keys_valid(json_data):
    is_valid = True
    for key in json_data.keys():
        if not all(char.isupper() for char in key):
            print(f"Key '{key}' is not in uppercase.")
            is_valid = False
        if 'O' in key or 'I' in key:
            print(f"Key '{key}' contains illegal characters ('O' or 'I').")
            is_valid = False
    return is_valid


def are_values_valid_pango_lineages(json_data):
    is_valid = True  # Initialize to True
    
    # Regex pattern for Pango lineage
    pango_lineage_pattern = re.compile(r'^([A-Z]+)(\.[1-9]\d*\.[1-9]\d*\.[1-9]\d*)+$')
    valid_keys = json_data.keys()
    
    for key, value in json_data.items():
        # Skip the check if the value is a list
        if isinstance(value, list):
            continue
        
        if key in SKIP_VALID_ALIAS:
            continue
        
        # Check if the value matches the Pango lineage format
        match = pango_lineage_pattern.match(value)
        if not match:
            print(f"Value '{value}' for key '{key}' is not a valid Pango lineage.")
            is_valid = False
            continue
        
        # Check if the value starts with a key that's in valid_keys
        starting_key = match.group(1)
        if starting_key not in valid_keys:
            print(f"Value '{value}' for key '{key}' does not start with a valid key.")
            is_valid = False
    
    return is_valid


def dict_raise_on_duplicates(ordered_pairs):
    d = {}
    duplicate_keys = {}
    for k, v in ordered_pairs:
        if k in d:
            duplicate_keys.setdefault(k, []).append(d[k])
            duplicate_keys[k].append(v)
        else:
            d[k] = v
    if duplicate_keys != {}:
        raise ValueError(f"Duplicate keys found: `{duplicate_keys}`")
    return d


def test_json(json_str):
    is_valid = True
    try:
        # Parse JSON string to dictionary
        json_data = json.loads(json_str)
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
        return False

    # Test if keys are unique
    try:
        json.loads(json_str, object_pairs_hook=dict_raise_on_duplicates)
    except ValueError as e:
        print(e)
        is_valid = False

    # Initialize empty set for checking unique keys and values
    values_set = set()

    # Loop through each key-value pair
    for key, value in json_data.items():
        # Check if value is unique (converting lists to tuple for hashability)VAE
        value_as_tuple = tuple(value) if isinstance(value, list) else value
        if value_as_tuple in values_set:
            if key in SKIP_UNIQUE_VALUE_FOR_KEYS:
                continue
            is_valid = False
            all_keys = [k for k, v in json_data.items() if v == value]
            print(
                f"Duplicate value found: value `{value}` with keys `{all_keys}`"
            )
        else:
            values_set.add(value_as_tuple)
    
    # Check if keys are legal:
    # - no O,I
    # - capital letters only
    is_valid &= are_keys_valid(json_data)
    is_valid &= are_values_valid_pango_lineages(json_data)


    return is_valid


if __name__ == "__main__":
    with open("pango_designation/alias_key.json", "r") as f:
        json_str = f.read()
        is_valid = test_json(json_str)
        if is_valid is False:
            exit(1)
