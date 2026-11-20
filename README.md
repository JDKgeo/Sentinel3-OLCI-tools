# Sentinel3-OLCI-tools
Notebooks: Sentinel-3 OLCI L1B → Rrs (Polymer) → chl-a (OC4Me) + WQSF QC.

## Quickstart
    conda env create -f environment.yml
    conda activate olci-tools
    jupyter lab

Polymer needs ECMWF auxdata — see github.com/hygeos/polymer.

## Data
EUMETSAT Data Store (data.eumetsat.int): OLCI L1B (EFR) + L2 (WFR), coastal scene recommended.

## Key bands
Oa03 442.5 · Oa04 490 · Oa05 510 · Oa06 560 · Oa08 665 · Oa11 708.75 nm

## Notebook
read L1B --> Polymer AC --> OC4Me chl --> WQSF masking --> Plotting
OC4Me: Morel et al. (2007); verify coefficients vs EUMETSAT ATBD.

License: MIT
