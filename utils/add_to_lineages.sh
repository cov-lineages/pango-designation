#!/bin/bash

# This script takes a lineage (e.g., XBB.1.5.34) as an argument and performs the following tasks:
# 1. Select the first field from TSV files in ~/Downloads/nextstrain_fetch*.
# 2. Remove the 'hCoV-19/' prefix from the selected field.
# 3. Remove everything after the first '|' character.
# 4. Append the provided lineage to the end of each line.
# 5. Skip the first line (header) and append the result to lineages.csv.
# 6. Run the deduplicate_keeping_last.py Python script.
# 7. Remove all files matching the ~/Downloads/nextstrain_fetch* pattern.

usage() {
  echo "Usage: $0 <lineage> [--keep-first]"
  echo "Example: $0 XBB.1.5.34"
}

lineage=$1

if [ -z "$lineage" ]; then
  echo "Error: Please provide a lineage as an argument."
  usage
  exit 1
fi

tsv-select -f1 ~/Downloads/nextstrain_fetch* \
  | sed 's/hCoV-19\///g' \
  | sed 's/|.*//g' \
  | sed "s/\$/,${lineage}/" \
  | tail -n +2 \
  >>lineages.csv

if [ "$2" != "--keep-first" ]; then
  python deduplicate_keeping_last.py
else
  echo "Keeping first"
  python deduplicate_keeping_first.py
fi

rm ~/Downloads/nextstrain_fetch*

