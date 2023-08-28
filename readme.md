This repository creates a tsv file in which all old protein sequences from sgd genomes are listed (`all_previous_seqs.tsv`).
By old protein sequence we mean sequences of proteins that existed in previous releases of SGD, but have currently changed.

The columns of the output file contain:
1. Gene id
2. Sequence
3. Date when that sequence was introduced (extracted from the release date)

## Run as github action

The code can be ran as a github action, and it will update the file. Instructions to run locally are provided below.

## Run locally

### Install dependencies

To install the dependencies, we used poetry (see [poetry installation instructions](https://python-poetry.org/docs/)).

In the source directory run:

```
poetry install
```

This should create a folder `.venv` with the python virtual environment. To activate the virtual environment, then run:

```
poetry shell
```

Now when you call `python`, it will be the one from the `.venv`.

### Run the script

```bash
# activate virtual environment
poetry shell

# Run the script (see the comments)
bash run.sh
```