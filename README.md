# SARS-CoV-2 Sequences
I could not find a good and easy to use source for SARS-CoV-2 protein sequences, so I make mine available. It is a CSV file resulting from a preprocessing of the data made available [here](https://www.ncbi.nlm.nih.gov/datasets/coronavirus/genomes/). The sources of the data are RefSeq and GenBank.

## Download
You can download the gzipped file [here]()

## Get the raw data
Protein sequences are downloaded from [here](https://www.ncbi.nlm.nih.gov/datasets/coronavirus/genomes/)
- Click *Dataset* of "Severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2)
- Make sure that *only* "Protein sequences (FASTA)* is selected
- Choose an arbitrary file name
- Click *Download*

Once downloaded, extract the contents of the zip-file to the `data/` directory. The resulting directory structure should look like this:

```
data
+-- ncbi_dataset
    +-- data
        +-- data_report.jsonl
        +-- dataset_catalog.json
        +-- protein.faa
        +-- virus_dataset.md
```

## Install
Setup up a biopython environment using conda:

```bash
conda create -n biopython python=3.7.6
```

activate the environment:

```bash
conda activate biopython
```

## Preprocess
Once the raw data is downloaded and the conda environment is ready, just run:

```bash
python preprocess.py
```

This will create the file `data/annotated_seqs.csv.gz`.