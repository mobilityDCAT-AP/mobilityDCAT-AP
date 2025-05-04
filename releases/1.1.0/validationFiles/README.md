# mobilityDCAT-AP Validation Files

## Overview

This repository contains validation files for the mobilityDCAT-AP specification. The [SHACL shapes file](mobilitydcat-ap_shacl_shapes.ttl) defines constraints for validating RDF data against the mobilityDCAT-AP requirements.

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

For more information about the mobilityDCAT-AP specification, please visit the [official documentation](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/).

