"""
Check the lineages designated in lineages.csv against the lineages described in lineage_notes.txt.
If they match, exit with code 0.  If there are discrepancies, exit with code 1.
"""

import csv
import sys


# These lineages don't have directly observed sequences and are defined as the putative
# common ancestor of their sublineages.  Therefore, there are no sequences for them in lineages.csv,
# so it's OK that they are in lineage_notes.txt but not in lineages.csv.
lineages_ignore_not_in_csv = set(["B.1.1.529", "B.1.640", "BA.3.2"])


def load_lineages(lineages_file):
    lineages = set()
    with open(lineages_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            lineage = row['lineage'].strip()
            if lineage:
                lineages.add(lineage)
    return lineages


def load_notes(notes_file):
    notes = set()
    with open(notes_file, 'r') as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            lineage = row['Lineage'].strip()
            # Ignore withdrawn lineages (those starting with '*')
            if lineage and not lineage.startswith('*'):
                notes.add(lineage)
    return notes


def check_lineages_notes(lineages_file, notes_file):
    csv = load_lineages(lineages_file)
    notes = load_notes(notes_file) - lineages_ignore_not_in_csv

    if csv == notes:
        sys.exit(0)
    else:
        csv_not_notes = csv - notes
        notes_not_csv = notes - csv
        if csv_not_notes:
            print("\nError: Lineages in lineages.csv but not in lineage_notes.txt:")
            for lineage in sorted(csv_not_notes):
                print(f"  {lineage}")
        if notes_not_csv:
            print("\nError: Lineages in lineage_notes.txt but not in lineages.csv:")
            for lineage in sorted(notes_not_csv):
                print(f"  {lineage}")
        sys.exit(1)


if __name__ == "__main__":
    check_lineages_notes("lineages.csv", "lineage_notes.txt")
