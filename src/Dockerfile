FROM condaforge/mambaforge

RUN conda install -c conda-forge conda-pack

COPY ./script.sh /
RUN chmod +x /script.sh

ENTRYPOINT ["/script.sh"]
CMD ["env.tar.gz"]
