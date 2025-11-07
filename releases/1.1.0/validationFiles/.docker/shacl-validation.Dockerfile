# Use an official Python base image
FROM python:3.10-slim

WORKDIR /app

# Install dependencies: wget, pyshacl
RUN apt-get update && \
    apt-get install -y wget raptor2-utils && \
    pip install --no-cache-dir pyshacl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Download mobilityDCAT-AP ontology
RUN wget https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/1.1.0/serialisationFiles/mobilitydcat-ap.ttl

# Download external ontologies
RUN mkdir external_ontologies
WORKDIR /app/external_ontologies

# List as per mobilitydcat https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#controlled-vocabularies-to-be-used
RUN wget http://publications.europa.eu/resource/authority/data-theme -O data-theme.xml && \
    wget http://publications.europa.eu/resource/authority/access-right -O access-right.rdf && \
    wget http://publications.europa.eu/resource/authority/frequency -O frequency.rdf && \
    wget http://publications.europa.eu/resource/authority/file-type -O file-type.rdf && \
    wget http://publications.europa.eu/resource/authority/language -O language.rdf && \
    wget http://publications.europa.eu/resource/authority/licence -O license.rdf && \
    wget http://publications.europa.eu/resource/authority/corporate-body -O corporate-body.rdf && \
    wget http://publications.europa.eu/resource/authority/continent -O continent.rdf && \
    wget http://publications.europa.eu/resource/authority/country -O country.rdf && \
    wget http://publications.europa.eu/resource/authority/place -O place.xml && \
    wget http://publications.europa.eu/resource/authority/nuts -O nuts.xml && \
    wget https://w3id.org/mobilitydcat-ap/application-layer-protocol && \
    wget https://w3id.org/mobilitydcat-ap/communication-method && \
    wget https://w3id.org/mobilitydcat-ap/conditions-for-access-and-usage && \
    wget https://w3id.org/mobilitydcat-ap/mobility-theme && \
    wget https://w3id.org/mobilitydcat-ap/mobility-data-standard && \
    wget https://w3id.org/mobilitydcat-ap/georeferencing-method && \
    wget https://w3id.org/mobilitydcat-ap/grammar && \
    wget https://w3id.org/mobilitydcat-ap/network-coverage && \
    wget https://w3id.org/mobilitydcat-ap/intended-information-service && \
    wget https://w3id.org/mobilitydcat-ap/transport-mode && \
    wget https://w3id.org/mobilitydcat-ap/update-frequency

WORKDIR /app

# Download shacl file
COPY mobilitydcat-ap_shacl_shapes.ttl .

COPY ./.docker/entrypoint.sh .
RUN chmod +x entrypoint.sh

ENTRYPOINT [ "/app/entrypoint.sh" ]
