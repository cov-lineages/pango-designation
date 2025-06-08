# Pango designation

The latest maintained Pango-lineage designations.

## Suggesting a new lineage
Novel lineages or lineage refinements can be suggested by filing an issue with the respective sequence names, as found on GISAID, and any supporting information such as a phylogenetic tree for the putative lineage. 

Full details on how to suggest a new lineage can be found in the [Pango lineage designation guide](https://web.archive.org/web/20240116214048/https://www.pango.network/how-does-the-system-work/how-to-suggest-a-new-lineage/).

Nomenclature rules can be found in the [Pango statement of nomenclature rules](pango_rules.html).

## Resources available on this repository

As detailed on the former pango.network website, we host the lineage description list (LDL) and sequence designation list (SDL) in this repository. 
### Lineage description list: [lineage_notes.txt](https://github.com/cov-lineages/pango-designation/blob/master/lineage_notes.txt)
### Sequence designation list: [lineages.csv](https://github.com/cov-lineages/pango-designation/blob/master/lineages.csv)
### Alias record: [alias_key.json](https://github.com/cov-lineages/pango-designation/blob/master/pango_designation/alias_key.json)

### Other
The lineage_constellations directory contains the mutations associated with each of the AY lineages. These are the mutations that were acquried along the phylogenetic path leading to the common ancestor of the lineage and remain conserved in the lineage (defined here as being in >70% of sequences designated to the lineage). This path is identified using the UShER phylogenetic tree. These constellations are different from those in [constellations](https://github.com/cov-lineages/constellations) as they attempt to capture all of the associated mutations, not only the defining mutations for a lineage. These constellations are provided for reference and are not used by scorpio currently. However, they should be compatible with scorpio if researchers are interested in exploring them. Sites in the intermediate category drop in and out in the Delta clade so may be associated with the lineage but may be prone to artefacts.

## Developer docs

It is recommended to clone this repo using `--filter=blob:none` for a blobless clone unless you want to download and put 15GB on your hard drive. The `lineages.csv` file is quite large and since git stores the state of each file at each commit, that creates a large repo. Git is good at downloading past blobs when necessary, so you shouldn't be impacted in your day to day work by doing this partial clone. Learn more about partial clone here: https://github.blog/2020-12-21-get-up-to-speed-with-partial-clone-and-shallow-clone/

Recommended commands to clone:

```bash
git clone git clone --filter=blob:none git+https://github.com/cov-lineages/pango-designation.git
gh repo clone cov-lineages/pango-designation -- --filter=blob:none
```
