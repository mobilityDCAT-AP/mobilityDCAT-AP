# Use Python 3.11 slim image
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    wget \
    curl \
    raptor2-utils \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages
RUN pip install --no-cache-dir pyshacl rdflib

# Download mobilityDCAT-AP ontology
RUN wget -q --timeout=30 --tries=3 \
    https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/1.1.0/serialisationFiles/mobilitydcat-ap.ttl \
    || curl -L -o mobilitydcat-ap.ttl \
    https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/1.1.0/serialisationFiles/mobilitydcat-ap.ttl

# Create directory for external ontologies
RUN mkdir -p external_ontologies
WORKDIR /app/external_ontologies

# Download core ontologies with retry and fallback
RUN wget -q --timeout=30 --tries=3 https://www.w3.org/ns/dcat.ttl -O dcat.ttl || \
    curl -L -o dcat.ttl https://www.w3.org/ns/dcat.ttl || \
    echo "Warning: Could not download dcat.ttl"

RUN wget -q --timeout=30 --tries=3 http://xmlns.com/foaf/spec/20140114.rdf -O foaf.rdf || \
    curl -L -o foaf.rdf http://xmlns.com/foaf/spec/20140114.rdf || \
    echo "Warning: Could not download foaf.rdf"

RUN wget -q --timeout=30 --tries=3 https://www.w3.org/ns/org.ttl -O org.ttl || \
    curl -L -o org.ttl https://www.w3.org/ns/org.ttl || \
    echo "Warning: Could not download org.ttl"

RUN wget -q --timeout=30 --tries=3 https://www.w3.org/2009/08/skos-reference/skos.ttl -O skos.ttl || \
    curl -L -o skos.ttl https://www.w3.org/2009/08/skos-reference/skos.ttl || \
    echo "Warning: Could not download skos.ttl"

RUN wget -q --timeout=30 --tries=3 https://www.w3.org/2006/vcard/ns.ttl -O vcard.ttl || \
    curl -L -o vcard.ttl https://www.w3.org/2006/vcard/ns.ttl || \
    echo "Warning: Could not download vcard.ttl"

RUN wget -q --timeout=30 --tries=3 https://www.w3.org/ns/locn.ttl -O locn.ttl || \
    curl -L -o locn.ttl https://www.w3.org/ns/locn.ttl || \
    echo "Warning: Could not download locn.ttl"

RUN wget -q --timeout=30 --tries=3 https://www.w3.org/ns/dqv.ttl -O dqv.ttl || \
    curl -L -o dqv.ttl https://www.w3.org/ns/dqv.ttl || \
    echo "Warning: Could not download dqv.ttl"

# Download EU Authority Tables (optional, continue on failure)
RUN wget -q --timeout=30 --tries=2 http://publications.europa.eu/resource/authority/data-theme -O data-theme.xml || true
RUN wget -q --timeout=30 --tries=2 http://publications.europa.eu/resource/authority/access-right -O access-right.rdf || true
RUN wget -q --timeout=30 --tries=2 http://publications.europa.eu/resource/authority/frequency -O frequency.rdf || true
RUN wget -q --timeout=30 --tries=2 http://publications.europa.eu/resource/authority/file-type -O file-type.rdf || true
RUN wget -q --timeout=30 --tries=2 http://publications.europa.eu/resource/authority/language -O language.rdf || true
RUN wget -q --timeout=30 --tries=2 http://publications.europa.eu/resource/authority/corporate-body -O corporate-body.rdf || true
RUN wget -q --timeout=30 --tries=2 http://publications.europa.eu/resource/authority/continent -O continent.rdf || true
RUN wget -q --timeout=30 --tries=2 http://publications.europa.eu/resource/authority/country -O country.rdf || true

# Download MobilityDCAT-AP controlled vocabularies (optional)
RUN wget -q --timeout=30 --tries=2 https://w3id.org/mobilitydcat-ap/application-layer-protocol -O application-layer-protocol.ttl || true
RUN wget -q --timeout=30 --tries=2 https://w3id.org/mobilitydcat-ap/communication-method -O communication-method.ttl || true
RUN wget -q --timeout=30 --tries=2 https://w3id.org/mobilitydcat-ap/mobility-theme -O mobility-theme.ttl || true
RUN wget -q --timeout=30 --tries=2 https://w3id.org/mobilitydcat-ap/mobility-data-standard -O mobility-data-standard.ttl || true
RUN wget -q --timeout=30 --tries=2 https://w3id.org/mobilitydcat-ap/georeferencing-method -O georeferencing-method.ttl || true
RUN wget -q --timeout=30 --tries=2 https://w3id.org/mobilitydcat-ap/grammar -O grammar.ttl || true
RUN wget -q --timeout=30 --tries=2 https://w3id.org/mobilitydcat-ap/network-coverage -O network-coverage.ttl || true
RUN wget -q --timeout=30 --tries=2 https://w3id.org/mobilitydcat-ap/transport-mode -O transport-mode.ttl || true

WORKDIR /app

# Copy SHACL shapes file
COPY mobilitydcat-ap_shacl_shapes.ttl .

# Copy entrypoint script
COPY .docker/entrypoint.sh .
RUN chmod +x entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]