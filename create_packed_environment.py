import os

def run_docker_command(confpath, envname="env", outpath=None):

    # convert path to absolute path
    confpath = os.path.realpath(confpath)

    # get default path (same as config)
    if outpath is None:
        outpath = os.path.split(confpath)[0]
    else:
        outpath = os.path.realpath(outpath)

    # put together command
    cmd = f"docker run -v {confpath}:/input/environment.yml -v {outpath}:/output conda-builder:alpha {envname}"

    # run
    print(f"Running: {cmd}")
    os.system(cmd)


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) == 1:
        msg = "Utility script to create conda-packed environment via Docker.\n\n"
        msg += "Usage: python /abs-path-to/create_packed_environment.py args\n\n"
        msg += "Here, args are the following positional arguments:\n\n"
        msg += "path-to-config.yaml  - this is the path to conda environment YAML config file.\n"
        msg += "environment-name (optional) - this is the resulting environment name. Defaults to 'env'.\n"
        msg += "output-path (optional) - this is the path where the packed environment is saved. Defaults to the parent folder of 'config.yaml'.\n"
        print(msg)
    else:
        # gather input args
        args = sys.argv[1:]

        # call function
        run_docker_command(*args)
