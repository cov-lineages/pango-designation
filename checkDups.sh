#!/bin/bash
OUTPUT=$(./findDups.sh)
if [[ "$OUTPUT" ]]; then
    echo "Duplicates found:"
    echo "$OUTPUT"
    exit 1
else
    exit 0
fi
