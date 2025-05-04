# mobilityDCAT-AP Validation Files

## Overview

This repository contains validation files for the mobilityDCAT-AP specification. The [SHACL shapes file](mobilitydcat-ap_shacl_shapes.ttl) defines constraints for validating RDF data against the mobilityDCAT-AP requirements.

## Available Shapes and Examples

Each class in the mobilityDCAT-AP specification has corresponding validation shapes and example files:

### Core Components

| Class | Documentation | Shape Definition | Example Files |
|-------|--------------|------------------|--------------|
| **Catalog** | [dcat:Catalog](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-catalogue) | [Catalogue_Shape](mobilitydcat-ap_shacl_shapes.ttl) | [catalogue_shape_examples.ttl](catalogue_shape_examples.ttl) |
| **Catalog Record** | [dcat:CatalogRecord](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-catalogue-record) | [CatalogRecord_Shape](mobilitydcat-ap_shacl_shapes.ttl) | [catalog_record_shape](catalog_record_shape_examples.ttl) |
| **Dataset** | [dcat:Dataset](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-dataset) | [Dataset_Shape](mobilitydcat-ap_shacl_shapes.ttl) | [dataset_shape](dataset_shape_examples.ttl) |
| **Distribution** | [dcat:Distribution](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-distribution) | [Distribution_Shape](mobilitydcat-ap_shacl_shapes.ttl) | [distribution_shape](distribution_shape_examples.ttl) |

### Agents and Contact Information

| Class | Documentation | Shape Definition | Example Files |
|-------|--------------|------------------|--------------|
| **Agent** | [foaf:Agent](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-agent) | [Agent_Shape](mobilitydcat-ap_shacl_shapes.ttl) | [agent_shape_examples.ttl](agent_shape_examples.ttl) |
| **Address** | [locn:Address](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-address-agent) | [Address_Agent_Shape](mobilitydcat-ap_shacl_shapes.ttl) | [address_agent_examples.ttl](address_agent_examples.ttl) |
| **Kind (Contact)** | [vcard:Kind](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-kind) | [Kind_Shape](mobilitydcat-ap_shacl_shapes.ttl) | [kind_shape.ttl](kind_shape.ttl) |

### Metadata and Standards

| Class | Documentation | Shape Definition | Example Files |
|-------|--------------|------------------|--------------|
| **Assessment** | [mobilitydcatap:Assessment](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-assessment) | [Assessment_Shape](mobilitydcat-ap_shacl_shapes.ttl) | [assessment_shape_examples.ttl](assessment_shape_examples.ttl) |
| **Category** | [skos:Concept](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-category) | [Category_Shape](mobilitydcat-ap_shacl_shapes.ttl) | [category_shape_examples.ttl](category_shape_examples.ttl) |
| **Location** | [dct:Location](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-location) | [Location_Shape](mobilitydcat-ap_shacl_shapes.ttl) | [location_shape.ttl](location_shape.ttl) |
| **Mobility Data Standard** | [mobilitydcatap:MobilityDataStandard](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-mobility-data-standard) | [MobilityDataStandard_Shape](mobilitydcat-ap_shacl_shapes.ttl) | [mobility_data_standard_shape.ttl](mobility_data_standard_shape.ttl) |

### Rights and Quality Information

| Class | Documentation | Shape Definition | Example Files |
|-------|--------------|------------------|--------------|
| **License Document** | [dct:LicenseDocument](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-licence-document) | [LicenseDocument_Shape](mobilitydcat-ap_shacl_shapes.ttl) | [license_document_shape.ttl](license_document_shape.ttl) |
| **Quality Annotation** | [dqv:QualityAnnotation](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-quality-annotation) | [QualityAnnotation_Shape](mobilitydcat-ap_shacl_shapes.ttl) | [quality_annotation_shape.ttl](quality_annotation_shape.ttl) |
| **Rights Statement** | [dct:RightsStatement](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-rights-statement) | [RightsStatement_Shape](mobilitydcat-ap_shacl_shapes.ttl) | [rights_statement_shape.ttl](rights_statement_shape.ttl) |

## How to Use These Files

1. **Documentation**: Click on the class name to view the full documentation for each class.
2. **Shape Definition**: This is the SHACL shape that defines the validation rules for the class.
3. **Example Files**: These contain examples of valid and invalid instances of each class.

All shape definitions are contained in the main [SHACL shapes file](mobilitydcat-ap_shacl_shapes.ttl). The example files provide guidance on how to correctly implement each class in your data.

For more information about the mobilityDCAT-AP specification, please visit the [official documentation](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/).















# mobilityDCAT-AP Validation Files

The [SHACL shapes graph](mobilitydcat-ap_shacl_shapes.ttl) contains constraints for a Data Graph expressed as RDF. This file defines shapes that ensure instances of specific classes have the necessary properties and conform to specified rules.

## Shape Definitions and Example Files

Each shape has corresponding example files to demonstrate valid and invalid instances:
- **Address_Agent_Shape**: Defines constraints for the [locn:Address](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-address-agent) class.
  - Shape definition: [Address_Agent_Shape in mobilitydcat-ap_shacl_shapes.ttl](https://github.com/mobilityDCAT-AP/mobilityDCAT-AP/blob/285311b9c92546c04edefcedfc7a4a663eaa8edf/releases/1.1.0/validationFiles/mobilitydcat-ap_shacl_shapes.ttl#L88)
  - Examples: [address_agent_examples.ttl](https://github.com/mobilityDCAT-AP/mobilityDCAT-AP/blob/285311b9c92546c04edefcedfc7a4a663eaa8edf/releases/1.1.0/validationFiles/address_agent_examples.ttl)


- The [Address_Agent_Shape](https://github.com/mobilityDCAT-AP/mobilityDCAT-AP/blob/285311b9c92546c04edefcedfc7a4a663eaa8edf/releases/1.1.0/validationFiles/mobilitydcat-ap_shacl_shapes.ttl#L88) is a SHACL node shape that defines the structure and constraints for the [locn:Address](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-address-agent) class. See [examples](https://github.com/mobilityDCAT-AP/mobilityDCAT-AP/blob/285311b9c92546c04edefcedfc7a4a663eaa8edf/releases/1.1.0/validationFiles/address_agent_examples.ttl) for validation.

- The [Agent_Shape](https://github.com/mobilityDCAT-AP/mobilityDCAT-AP/blob/e0981eb1ea7e7b3691a5104e59161f342db65c90/releases/1.1.0/validationFiles/mobilitydcat-ap_shacl_shapes.ttl#L142) is a SHACL node shape that defines the structure and constraints for the [foaf:Agent](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-agent) class. See [examples](https://github.com/mobilityDCAT-AP/mobilityDCAT-AP/blob/gh-pages/releases/1.1.0/validationFiles/agent_shape_examples.ttl) for validation.

- The [Assessment_Shape](https://github.com/mobilityDCAT-AP/mobilityDCAT-AP/blob/e0981eb1ea7e7b3691a5104e59161f342db65c90/releases/1.1.0/validationFiles/mobilitydcat-ap_shacl_shapes.ttl#L233) is a SHACL node shape that defines the structure and constraints for the [mobilitydcatap:Assessment](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-assessment) class. See [example](https://github.com/mobilityDCAT-AP/mobilityDCAT-AP/blob/gh-pages/releases/1.1.0/validationFiles/assessment_shape_examples.ttl) for validation.

- The [Catalogue_Shape](mobilitydcat-ap_shacl_shapes.ttl) is a SHACL node shape that defines the structure and constraints for the [dcat:Catalog](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-catalogue) class.
- The [CatalogRecord_Shape](catalog_record_shape.ttl) is a SHACL node shape that defines the structure and constraints for the [dcat:CatalogRecord](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-catalogue-record) class. 
- The [Category_Shape](category_shape.ttl) is a SHACL node shape that defines the structure and constraints for the [skos:Concept](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-category) class.
- The [Dataset_Shape](dataset_shape.ttl) is a SHACL node shape that defines the structure and constraints for the [dcat:Dataset](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-dataset) class. 
- The [Distribution_Shape](distribution_shape.ttl) is a SHACL node shape that defines the structure and constraints for the [dcat:Distribution](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-distribution) class. 
- The [Kind_Shape](kind_shape.ttl) is a SHACL node shape that defines the structure and constraints for the [vcard:Kind](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-kind) class.
- The [LicenseDocument_Shape](license_document_shape.ttl) is a SHACL node shape that defines the structure and constraints for the [dct:LicenseDocument](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-licence-document) class. 
- The [Location_Shape](location_shape.ttl) is a SHACL node shape that defines the structure and constraints for the [dct:Location](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-location) class. 
- The [MobilityDataStandard_Shape](mobility_data_standard_shape.ttl) is a SHACL node shape that defines the structure and constraints for the [mobilitydcatap:MobilityDataStandard](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-mobility-data-standard) class. 
- The [QualityAnnotation_Shape](quality_annotation_shape.ttl) is a SHACL node shape that defines the structure and constraints for the [dqv:QualityAnnotation](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-quality-annotation) class.
- The [RightsStatement_Shape](rights_statement_shape.ttl) is a SHACL node shape that defines the structure and constraints for the [dct:RightsStatement](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-rights-statement) class. 

