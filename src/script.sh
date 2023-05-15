#!/bin/bash
conda env create -n env -f /input/environment.yml && conda clean --all --yes
conda pack -n env -o /output/${1}
