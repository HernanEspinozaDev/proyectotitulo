ARG PYTHON_IMAGE=python:3.12.14-slim-bookworm
ARG PANDOC_IMAGE=pandoc/core:3.6.4
ARG PLANTUML_IMAGE=plantuml/plantuml:1.2026.8

FROM ${PANDOC_IMAGE} AS pandoc
FROM ${PLANTUML_IMAGE} AS plantuml
FROM ${PYTHON_IMAGE} AS informes

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       ca-certificates \
       fonts-liberation \
       graphviz \
       inkscape \
       openjdk-17-jre-headless \
    && rm -rf /var/lib/apt/lists/*

COPY --from=pandoc /usr/local/bin/pandoc /usr/local/bin/pandoc
COPY --from=plantuml /opt/plantuml.jar /opt/plantuml.jar
COPY Informes/requirements.txt /tmp/informes-requirements.txt
RUN python -m pip install --no-cache-dir -r /tmp/informes-requirements.txt \
    && rm /tmp/informes-requirements.txt

ENV PLANTUML_JAR=/opt/plantuml.jar \
    INKSCAPE_BIN=/usr/bin/inkscape \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /workspace
ENTRYPOINT ["python", "Informes/generar.py"]
