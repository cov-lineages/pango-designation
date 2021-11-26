#%%
import pandas as pd
from natsort import natsorted

from pkg_resources import parse_version

from aliasing import Aliasor

#%%
df = pd.read_csv("lineages.csv")

#%%
lineages = df.lineage.unique()

#%%
aliasor = Aliasor("pango_designation/alias_key.json")

#%%
uncompressed_lineages = list(map(aliasor.uncompress, lineages))
#%%
# uncompressed_lineages.sort(key=parse_version)
def lts(lineage):
    items = []
    for item in lineage.split("."):
        item_string = str(item)
        items.append((5-len(item))*"0" + item_string)
    return "".join(items)

uncompressed_lineages.sort(key=lts)
# %%
sorted_lineages = list(map(aliasor.compress, uncompressed_lineages))
# %%
with open("sorted_lineages.txt", "w") as f:
    for lineage in sorted_lineages:
        f.write(lineage + "\n")