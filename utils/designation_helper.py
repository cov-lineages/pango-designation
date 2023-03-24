"""
Script to help the designation process

Takes arguments:
- parent lineage
- mutations

Does:
- Look up next child of parent lineage
- Generate lineage notes string from lineage, mutations, countries in lineages
- Generate commit message
- Add alias json if necessary
"""

import typer
import pandas as pd
from pango_aliasor.aliasor import Aliasor
import numpy as np

LINEAGE_NOTES = "lineage_notes.txt"
LINEAGES_CSV = "lineages.csv"
METADATA = "~/Downloads/nextstrain_fetch*"
ALIAS_JSON = "pango_designation/alias_key.json"

def extract_level(lineage: str, level: int) -> int:
    """
    Extracts a level from a lineage string
    """
    split = lineage.split(".")
    if len(split) <= level:
        return 0
    return int(lineage.split(".")[level])

def find_next_string(s: str) -> str:
    # Convert the string to a list of characters
    chars = list(s)
    # Find the index of the last character that isn't "Z", "O", "I", or "X"
    i = len(chars) - 1
    while i >= 0 and chars[i] in ("Z", "O", "I", "X"):
        i -= 1
    # If all the characters are "Z", "O", "I", or "X", add another "A" and return
    if i < 0:
        return "A" * (len(chars) + 1)
    # Increment the character at index i, skipping over "O", "I", and "X"
    while True:
        if chars[i] == "Z":
            chars[i] = "A"
            i -= 1
        else:
            chars[i] = chr(ord(chars[i]) + 1)
            if chars[i] not in ("O", "I", "X"):
                break
    # Set all the characters to the right of i to "A"
    for j in range(i+1, len(chars)):
        chars[j] = "A"
    # Return the new string
    return "".join(chars)

def alias_new_child(new_child_unaliased: str, aliasor: Aliasor) -> tuple[str, str]:
    # Try to compress new child
    # If it fails, need to add new alias
    try:
        new_child = aliasor.compress(new_child_unaliased)
        alias = None
    except:
        # Load alias JSON
        import json
        aliases = json.load(open(ALIAS_JSON, "r"))

        # Get list of keys
        keys = list(aliases.keys())

        # Filter out keys that start with X
        keys_without_X = [key for key in keys if not key.startswith("X")]

        # Find length of longest key
        max_len = max([len(key) for key in keys_without_X])

        # Filter to keys that are max_len
        keys_with_max_len = [key for key in keys_without_X if len(key) == max_len]

        # Find alphanumerically largest key
        largest = max(keys_with_max_len)

        alias = find_next_string(largest)

        new_child = alias + ".1"
    
    return (new_child, alias)

def get_lineage_from_parent(parent_lineage: str):
    """
    Get the next child lineage of parent lineage
    """
    # Read in lineages.csv
    # Find last child of parent
    # Return next child
    lineages = pd.read_csv(LINEAGES_CSV, usecols=["lineage"])

    # Get all unique lineages
    unique_lineages = lineages.lineage.unique()

    # Initalize Aliasor
    aliasor = Aliasor(ALIAS_JSON)
    
    # Unalias unique lineages
    unaliased = np.vectorize(aliasor.uncompress)(unique_lineages)

    # Unalias parent lineage
    unaliased_parent = aliasor.uncompress(parent_lineage)

    # Filter to lineages descending from parent lineage
    children=unaliased[np.vectorize(lambda x: x.startswith(unaliased_parent))(unaliased)]

    # Find number of levels of parent lineage
    parent_levels = unaliased_parent.count(".") + 1

    # Find numbers of level below parent lineage
    children_levels = np.vectorize(lambda x: extract_level(x, parent_levels))(children)

    # Find last entry of 1 level below parent lineage
    max_child = max(children_levels)

    # Create compressd child
    new_child_unaliased = f"{unaliased_parent}.{max_child+1}"

    # Alias new child
    (new_child, alias) = alias_new_child(new_child_unaliased, aliasor)
    if alias:
        print(f"New alias: {alias} -> {unaliased_parent}")

    # Return next lineage
    return new_child

# Take optionally a list of strings for mutations
def main(parent_lineage: str, mutations: list[str] = None):
    print(f"Parent: {parent_lineage}")
    print(f"Next child: {get_lineage_from_parent(parent_lineage)}")


if __name__ == "__main__":
    typer.run(main)
