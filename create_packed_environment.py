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

    # gather input args
    args = sys.argv[1:]

    # call function
    run_docker_command(*args)


