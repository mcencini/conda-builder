# Conda-builder
Docker image for the creation of portable Linux Conda environment built using [conda-pack](https://conda.github.io/conda-pack/).

## Prerequisites
This tool requires a local installation of [Docker](https://www.docker.com/) and [Python 3](https://www.python.org/).

## Installation

First, download or clone the repository:

```bash
git clone git@github.com:mcencini/conda-builder.git
```

Navigate to the repository main folder and enter the `src` folder to build the docker image:

```bash
cd /path/to/repo/src
docker build -t conda-builder:alpha .
```

## Usage

We provide a `create_packed_environment.py` Python script to run the docker command. Usage is:

```
python /path/to/folder/create_packed_environment.py args
```

Here, `args` represents the following positional arguments:

```
path-to-config.yaml  - this is the path to conda environment YAML config file.
environment-name (optional) - this is the resulting environment name. Defaults to "env".
output-path (optional) - this is the path where the packed environment is saved. Defaults to the parent folder of "config.yaml"
```

For example, creation of a Pytorch environment using the provided configuration example can be done as:

```
python /abs-path-to/create_packed_environment.py /abs-path-to/examples/torch_environment.yaml "pytorch-cpu"
```

This will create a `pytorch-cpu` folder containing a `pytorch-cpu.tar.gz` archive and a `unpack_pytorch-cpu.sh` shell script. In general, the script will create an `environment-name`folder containing a `environment-name.tar.gz` archive and a `unpack_environment-name.sh` script.

To relocate the environment in the target machine, copy the newly created folder in the desired location and run the following commands:

```
cd /abs-path-on-target-machine/environment-name
./unpack_environment-name.sh
```

This will untar the environment, clean the prefixes and create a shortcut to the activation script in the environment parent folder. Specifically, the path on target machine will appear as:

```
├── /abs-path-on-target-machine/
├── environment-name/ 
└── activate-environment-name
```

That's it! Now, the environment can be activated when desired by running:

```
source /abs-path-on-target-machine/activate-environment-name
```

Some caveats:

- Currently, we do not provide a shortcut to the deactivation script. Environment can be deactivated by running `source /abs-path-on-target-machine/environment-name/bin/deactivate`.
- Activation does not work with `csh` shell due to limitations in Conda `activate` script.
