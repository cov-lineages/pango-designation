#! usr/bin/env python

import pandas as pd

df = pd.read_csv("lineages.csv",header=0)

df.drop_duplicates(inplace=True)

df.to_csv("lineages.csv",index=False)

