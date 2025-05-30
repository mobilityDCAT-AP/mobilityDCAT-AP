# mobilityDCAT-AP Validation Files

## Overview

This repository contains validation files for the mobilityDCAT-AP specification. The [SHACL shapes file](mobilitydcat-ap_shacl_shapes.ttl) defines constraints for validating RDF data against the mobilityDCAT-AP requirements.

## ⚠️ SHACL Validation Requirements

**Important**: The SHACL shapes require additional ontology models to be loaded for proper validation. Most SHACL validators do not perform automatic reasoning, which means class hierarchies (like `foaf:Organization` being a subclass of `foaf:Agent`) must be explicitly provided.

### Required Ontologies

Before validating your data, ensure you have these ontology files loaded:

| Ontology | Purpose | Download Link |
|----------|---------|---------------|
| **FOAF** | Friend of a Friend vocabulary | [foaf.rdf](http://xmlns.com/foaf/spec/20140114.rdf) |
| **Organization Ontology** | Organizational structures | [org.ttl](https://www.w3.org/ns/org.ttl) |
| **DCAT** | Data Catalog Vocabulary | [dcat.ttl](https://www.w3.org/ns/dcat.ttl) |
| **Dublin Core Terms** | Metadata elements | [dcterms.ttl](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl) |
| **SKOS** | Knowledge organization systems | [skos.ttl](https://www.w3.org/2009/08/skos-reference/skos.ttl) |
| **vCard** | Contact information | [vcard.ttl](https://www.w3.org/2006/vcard/ns.ttl) |
| **LOCN** | Location vocabulary | [locn.ttl](https://www.w3.org/ns/locn.ttl) |
| **DQV** | Data Quality Vocabulary | [dqv.ttl](https://www.w3.org/ns/dqv.ttl) |
| **DCAT-AP 2.0.1** | DCAT Application Profile | [dcat-ap.ttl](https://raw.githubusercontent.com/SEMICeu/DCAT-AP/master/releases/2.0.1/dcat-ap_2.0.1.ttl) |
| **mobilityDCAT-AP Core** | Main vocabulary | [mobilitydcat-ap.ttl](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/1.1.0/serialisationFiles/mobilitydcat-ap.ttl) |

### Validation Commands

**With pyshacl (supports reasoning):**

First, install pyshacl:
```bash
# Install pyshacl
pip install pyshacl

# Or with conda
conda install -c conda-forge pyshacl
```

Then download required ontologies and validate:
```bash
# Download required ontologies first
wget https://www.w3.org/ns/dcat.ttl
wget http://xmlns.com/foaf/spec/20140114.rdf
wget https://www.w3.org/ns/org.ttl
wget https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl
wget https://www.w3.org/2009/08/skos-reference/skos.ttl
wget https://www.w3.org/2006/vcard/ns.ttl
wget https://www.w3.org/ns/locn.ttl
wget https://www.w3.org/ns/dqv.ttl
wget https://raw.githubusercontent.com/SEMICeu/DCAT-AP/master/releases/2.0.1/dcat-ap_2.0.1.ttl
wget https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/1.1.0/serialisationFiles/mobilitydcat-ap.ttl

# Validate with reasoning enabled
pyshacl -s mobilitydcat-ap_shacl_shapes.ttl \
        -e dcat.ttl \
        -e foaf.rdf \
        -e org.ttl \
        -e dublin_core_terms.ttl \
        -e skos.ttl \
        -e vcard.ttl \
        -e locn.ttl \
        -e dqv.ttl \
        -e dcat-ap_2.0.1.ttl \
        -e mobilitydcat-ap.ttl \
        -i rdfs \
        your-data.ttl
```

**With Apache Jena:**
```bash
# Merge all required graphs
riot --validate your-data.ttl mobilitydcat-ap_shacl_shapes.ttl dcat.ttl foaf.rdf
```

### Validator Compatibility

| Validator | Reasoning Support | Notes |
|-----------|-------------------|-------|
| **pyshacl** | ✅ With `-i rdfs` flag | Recommended approach |
| **Apache Jena** | ❌ Manual ontology loading | Requires merging graphs |
| **TopBraid** | ✅ Configurable | Commercial tool |
| **SHACL Playground** | ❌ Manual setup | Include ontologies in data |

> **💡 Tip**: Always specify which SHACL validator you used when reporting validation results, as different validators may behave differently.

## Available Shapes and Examples

Each class in the mobilityDCAT-AP specification has corresponding validation shapes and example files:

### Core Components

| Class | Documentation | Shape Definition | Example Files |
|-------|--------------|------------------|--------------|
| **Catalog** | [dcat:Catalog](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-catalogue) | [Catalogue_Shape](mobilitydcat-ap_shacl_shapes.ttl) | [catalogue_shape](catalogue_shape_examples.ttl) |
| **Catalog Record** | [dcat:CatalogRecord](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-catalogue-record) | [CatalogRecord_Shape](mobilitydcat-ap_shacl_shapes.ttl) | [catalog_record_shape](catalog_record_shape_examples.ttl) |
| **Dataset** | [dcat:Dataset](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-dataset) | [Dataset_Shape](mobilitydcat-ap_shacl_shapes.ttl) | [dataset_shape](dataset_shape_examples.ttl) |
| **Distribution** | [dcat:Distribution](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-distribution) | [Distribution_Shape](mobilitydcat-ap_shacl_shapes.ttl) | [distribution_shape](distribution_shape_examples.ttl) |

### Agents and Contact Information

| Class | Documentation | Shape Definition | Example Files |
|-------|--------------|------------------|--------------|
| **Agent** | [foaf:Agent](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-agent) | [Agent_Shape](mobilitydcat-ap_shacl_shapes.ttl) | [agent_shape](agent_shape_examples.ttl) |
| **Address** | [locn:Address](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-address-agent) | [Address_Agent_Shape](mobilitydcat-ap_shacl_shapes.ttl) | [address_agent](address_agent_examples.ttl) |
| **Kind (Contact)** | [vcard:Kind](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-kind) | [Kind_Shape](mobilitydcat-ap_shacl_shapes.ttl) | [kind_shape](kind_shape_examples.ttl) |

### Metadata and Standards

| Class | Documentation | Shape Definition | Example Files |
|-------|--------------|------------------|--------------|
| **Assessment** | [mobilitydcatap:Assessment](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-assessment) | [Assessment_Shape](mobilitydcat-ap_shacl_shapes.ttl) | [assessment_shape](assessment_shape_examples.ttl) |
| **Category** | [skos:Concept](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-category) | [Category_Shape](mobilitydcat-ap_shacl_shapes.ttl) | [category_shape](category_shape_examples.ttl) |
| **Location** | [dct:Location](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-location) | [Location_Shape](mobilitydcat-ap_shacl_shapes.ttl) | [location_shape](location_shape_examples.ttl) |
| **Mobility Data Standard** | [mobilitydcatap:MobilityDataStandard](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-mobility-data-standard) | [MobilityDataStandard_Shape](mobilitydcat-ap_shacl_shapes.ttl) | [mobility_data_standard](mobility_data_standard_shape_examples.ttl) |

### Rights and Quality Information

| Class | Documentation | Shape Definition | Example Files |
|-------|--------------|------------------|--------------|
| **License Document** | [dct:LicenseDocument](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-licence-document) | [LicenseDocument_Shape](mobilitydcat-ap_shacl_shapes.ttl) | [license_document_shape](license_document_shape_examples.ttl) |
| **Quality Annotation** | [dqv:QualityAnnotation](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-quality-annotation) | [QualityAnnotation_Shape](mobilitydcat-ap_shacl_shapes.ttl) | [quality_annotation_shape](quality_annotation_shape_examples.ttl) |
| **Rights Statement** | [dct:RightsStatement](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-rights-statement) | [RightsStatement_Shape](mobilitydcat-ap_shacl_shapes.ttl) | [rights_statement_shape](rights_statement_shape_examples.ttl) |

## How to Use These Files

1. **Documentation**: Click on the class name to view the full documentation for each class.
2. **Shape Definition**: This is the SHACL shape that defines the validation rules for the class.
3. **Example Files**: These contain examples of valid and invalid instances of each class.

All shape definitions are contained in the main [SHACL shapes file](mobilitydcat-ap_shacl_shapes.ttl). The example files provide guidance on how to correctly implement each class in your data.

## Common Validation Issues

### Class Inheritance Problems
If you see errors like `"foaf:Organization not recognized as foaf:Agent"`, ensure you have loaded the FOAF ontology that defines the class hierarchy.

### Missing Controlled Vocabularies
Some properties require values from controlled vocabularies. Ensure your data uses the correct URI patterns as defined in the SHACL shapes.

## Future Improvements

We are working with Peter to develop a comprehensive Docker-based validation tool with built-in reasoning support to eliminate the need for manual ontology management.

For more information about the mobilityDCAT-AP specification, please visit the [official documentation](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/).
