FROM mambaorg/micromamba:0.19.1

COPY --chown=$MAMBA_USER:$MAMBA_USER env.yaml /tmp/env.yaml

RUN micromamba install -y -f /tmp/env.yaml && \
    micromamba clean --all --yes

ARG MAMBA_DOCKERFILE_ACTIVATE=1
ADD ./src/ .
USER root
RUN chmod +x ./migrate_and_run.sh
USER $MAMBA_USER
#CMD  && python main.py

ENTRYPOINT ["/usr/local/bin/_entrypoint.sh", "./migrate_and_run.sh" ]