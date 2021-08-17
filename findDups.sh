#!/bin/bash

cut -d, -f1 lineages.csv |sort | uniq -c | awk '$1 > 1 {print $2;}' | grep -Fwf - lineages.csv | sort -u
