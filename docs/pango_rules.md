# Rules for the Designation and Naming of Pango Lineages

Version 2, 5th May 2021

In the vast majority of instances it is expected that Pango lineage names and designations will conform to the following rules.  These rules also act as guidelines for the decisions made by the Lineage Designation Committee. 

## SECTION I. Criteria for designation of a new Pango lineage
1.	A set of SARS-CoV-2 genome sequences may be considered for the designation of a new lineage name if it exhibits the following essential characteristics:

    1a.	At the time of designation, the set of sequences is expected to share a single common ancestor and represent a monophyletic or paraphyletic clade in the SARS-CoV-2 phylogeny (see I.1e).
  
    1b.	The clade should be distinguished by at least one unambiguous evolutionary event (single nucleotide change, insertion/deletion, or recombination event). 
  
    1c.	The clade should contain a minimum of 5 sequences with high genome coverage. High coverage means that <5% of nucleotides sites in the whole genome (excluding UTRs) are represented by IUPAC ambiguity codes. 
  
    1d.	The clade must include at least one internal node and therefore cannot be solely composed of a single polytomy. Thus, a lineage is expected to be consistent with a significant amount of onward transmission.
  
    1e.	Due to the large size of the SARS-CoV-2 global phylogeny, a quantitative measure of clade support is no longer required (except for that imposed by I.1b) .
  	
2.	A new non-recombinant lineage designation is expected to also represent one or more events of epidemiological significance

    2a.	A non-exhaustive list of possible events are as follows:
  	(i) The clade may represent inferred movement of the virus into a new country or region (founder event
  	(ii) The clade may distinguish successive epidemic waves in the same location.
  	(iii) The clade may be observed to be growing rapidly and/or strongly increasing in frequency compared to other co-circulating lineages.
  	(iv) The clade may be associated with observed or predicted changes in phenotypes including, but not limited to, transmissibility, immunogenicity, or pathogenicity.
  	(v) The clade may indicate a cross-species transmission event.
  	(vi) The clade may carry a set of multiple mutations of particular biological interest or concern. Note that, in most cases, the presence of a single specific mutation, by itself, will not be considered sufficient to warrant a new lineage designation.

    2b.	If a clade becomes the subject of exceptional interest, and a new lineage designation would greatly clarify reference to and discussion of that clade, then a new designation may be considered even if none of the event conditions in I.2a are met. The conditions in section I.1 should still be met.

    2c.	In the event of unforeseen or exceptional circumstances, the Lineage Designation Committee may designate lineages according to criteria other than those in I.2a and I.2b.  Details of these decisions should be recorded and communicated to the Pango Committee. The Pango Committee will use this information to decide if these Rules should be updated correspondingly. 

3.	The essential characteristics in section I.1 are necessary but not sufficient for the designation of a new lineage. Therefore not all phylogenetic clades that meet the conditions in section I.1 will be given a Pango lineage designation.

    3a.	Lineage designation is at the discretion of the Lineage Designation Committee and its interpretation of clade characteristics. The number of available genomes across locations and times may be taken into account when interpreting these designation rules.

    3b.	Recombinant clades can qualify for a lineage designation if they meet the essential characteristics in section I.1, regardless of whether any of the conditions in sections I.2 are met.

    3c.	In most instances it is expected that the number of high quality genomes required to designate a lineage will be greater than the minimum number defined in I.1c.

## SECTION II. Definition of a hierarchical alpha-numeric system for lineage names
Each Pango lineage designated according to the guidelines in Section 1 is given its own unique lineage name. Pango lineage names are based on phylogenetic structure, but are intended to convey only partial, local information about ancestor-descendant relationships. 

1. Syntax

    1a.	Lineage names are constructed from an alphabetical prefix and a numerical suffix. Although lineage names are case-insensitive, the alphabetical prefix is typically capitalised.

    1b.	Any letter in the Latin alphabet , may be used (singly or in combination) within the prefix of standard lineages, except for I, O and X. The letters I and O are omitted to avoid confusion with the numerals 1 and 0.  X is reserved for the names of recombinant lineages (see II.1j). 

    1c.	Each full stop (or period or dot) within the numerical suffix represents “descendant of” and is applied when one ancestor of the lineage can be clearly identified (see II.1g).

    _Example: Lineage B.1.1.7 is the seventh named descendant of lineage B.1.1, which in turn was the first named descendant of lineage B.1._

    1d.	In order to avoid excessively long lineage labels, the numerical suffix has a maximum of three hierarchical levels (primary, secondary and tertiary suffixes). Descendants of lineages with tertiary suffixes are assigned to the next available permitted alphabetical prefix, in alphabetical order. This new prefix acts as an alias for the name of the parental lineage.

    _Example: The first named descendant of lineage B.1.1.1 is not named B.1.1.1.1 but is instead named C.1. The prefix C therefore serves as an alias for B.1.1.1._

    1e.	Details of each alias must be provided in the current [lineage description list](https://github.com/cov-lineages/pango-designation/blob/master/full_alias_key.txt), so that the ancestral relationships of all Pango lineages can be reconstructed unambiguously.  

    1f.	Most lineages are standard lineages. The names of standard lineages must contain both an alphabetical prefix and a numerical suffix. This captures the fact that the prefix of each standard lineage represents a single unambiguous ancestor.

    1g.	Some lineages do not have a single unambiguous parental lineage and are called special case lineages. At present there are two types of special case lineages. The first type comprises lineages A and B. The exact nature of their ancestry is ambiguous because the root of the SARS-CoV-2 phylogeny is not known with certainty. The second type comprises recombinant lineages that, by definition, have more than one parental lineage (see II.1j). A special case lineage name can be used without a numerical suffix.  Descendent lineages of special case lineages acquire numerical suffixes according to the procedure set out in II.1c-II.1e. 

    1h.	After all available single character prefixes are exhausted, assignations continue with two-character prefixes, beginning with the next available letter, and so on.
   
    _Example: Prefix AA is the next available prefix after Z, and BA is the next available prefix after AZ, and AAA is the next available prefix after ZZ._

    1i.	The Lineage Designation Committee determines the next available prefix by reference to the current [lineage description list](https://github.com/cov-lineages/pango-designation/blob/master/full_alias_key.txt). The list must be updated promptly following a new designation.  

    1j.	Recombinant lineages are given alphabetical prefixes beginning with the letter X. With the addition of this condition, recombinant lineages are given the next available prefix according to II.1h.  Incrementation of the prefix for new recombinants is independent of that for new non-recombinants, and determined by reference to the current [lineage description list](https://github.com/cov-lineages/pango-designation/blob/master/full_alias_key.txt) (see II.1i).

    _Example: The first detected recombinant lineage is named XA, followed by XB, XC,…, XAA, XAB, etc._

    1k.	Recombinant lineages are special case lineages and used without a numerical suffix (see II.1g). Non-recombinant descendent lineages of recombinant lineages acquire numerical suffixes, according to II.1c-II.1e. 

    _Example: The first non-recombinant descendant lineage of XA is named XA.1 because it has one unambiguous parental lineage. The usual rules of aliasing also apply, hence XA.1.1.1.1 becomes AJ.1, if AJ is the next available top-level prefix._

    1l.	As recombinant lineage names lack information about their putative parental lineages, this information (which may be uncertain) is added to the [lineage description list](https://github.com/cov-lineages/pango-designation/blob/master/full_alias_key.txt).

## SECTION III. Implementation and revision

1.	Sequences assigned to Pango lineages are aligned relative to the reference sequence, which by convention is that of Wuhan-Hu-1 (GenBank: MN908947.3), and genetic changes are called relative to that reference. Consequently, positional homology is implied.

2.	Lineages are designated only if they descend from the common ancestor of the SARS-CoV-2 pandemic in humans. Pango does not name or classify pre-pandemic viruses recovered from other species. However, if a human pandemic lineage moves into another host species (or thereafter back into humans) then Pango lineages may be designated for each cross-species transmission, in accordance with I.2a.

3.	Retrospective renaming of lineages should be avoided wherever possible.

4.	The Pango nomenclature is dynamic and intended to capture active, ongoing transmission. Therefore each lineage has a status, which is recorded in the [lineage description list](https://github.com/cov-lineages/pango-designation/blob/master/full_alias_key.txt). This status must be one of the categories listed below and represents the current observation state of the lineage:

    `ACTIVE`: last sampled within last 3 months

    `UNOBSERVED`: last sampled seen 3-9 months ago

    `INACTIVE`: not sampled for 9 months

    `WITHDRAWN`: name not in use

    `UNDEFINED`: see III.1g

5.	A lineage name may be withdrawn at the discretion of the Pango Committee. A lineage may be withdrawn for reasons of sample quality, incorrect metadata, clarification, phylogenetic construction errors, or other matters arising.

6.	Once withdrawn, a lineage name cannot be reused and reassigned, and should be permanently marked as having `WITHDRAWN` status in the lineage description list.

7.	If a designated lineage needs to be split into multiple lineages (e.g. through phylogenetic revision following additional sampling) then its descendent lineages are given the next available lineage suffixes of their parent, or the next available aliases, as appropriate following the procedure in Section II. A note of the change must be added to the lineage description list.

8.	Revisions (for whatever reason) may lead to the number of sequences in a designated lineage falling below the number required to designate a new lineage (see I.1.1c). The names of such lineages are retained, and they remain in the lineage description list, regardless of the number of sequences that they contain. If the remaining number of sequences is zero, then the lineage name remains and its lineage status is `UNDEFINED`, not withdrawn.

9.	In the event that a lineage is erroneously designated with a label that is already in use, the more recently designated lineage is re-designated using the next available name according to Section II, and a note is added to the lineage description list.

10.	Should a valid recombination event be overlooked or an invalid recombinant be designated, in neither case should the lineage name be changed, but a note must be added to the lineage description list upon recognition of the misdesignation.

## SECTION IV. Designated sequences

1. The Pango Committee will maintain and distribute a sequence designation list, comprising a list of genomes sequences that have been designated to a Pango lineage.

2. Each designated genome sequence belongs to one, and only one, Pango lineage.

3. Sequences must be of high coverage to be included in the sequence designation list. High High coverage means that <5% of nucleotides sites in the whole genome (excluding UTRs) are represented by IUPAC ambiguity codes.

4. Not all sequences that meet the condition in IV.1c will be necessarily included in the sequence designation list. For example, not all members of lineages that contain large numbers of SARS-CoV-2 genomes will be included.

5. If a genome sequence that is not in the sequence designation list has exactly the same SARS-CoV-2 nucleotide sequence as a member of the sequence designation list, then it can be safely assumed that the lineage of the former is equal to that of the latter.

  

