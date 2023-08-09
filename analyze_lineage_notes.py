#! usr/bin/env python

import pandas as pd

# Will verify file format integrity
#  - Will error if there are too many tab characters
pd.read_csv('lineage_notes.txt', delimiter='\t')
