#!/bin/bash
# prepare output
mkdir /output/${1}

# create and pack environment
conda env create -n env -f /input/environment.yml && conda clean --all --yes
conda pack -n env -o /output/${1}/${1}.tar.gz

# create unpack script
touch /output/${1}/unpack_${1}.sh
echo "#!/bin/bash" >> /output/${1}/unpack_${1}.sh
echo "tar -xvf ${1}.tar.gz" >> /output/${1}/unpack_${1}.sh
echo "rm ${1}.tar.gz" >> /output/${1}/unpack_${1}.sh
echo 'bash -c "bin/activate && conda-unpack"' >> /output/${1}/unpack_${1}.sh
chmod +x /output/${1}/unpack_${1}.sh
