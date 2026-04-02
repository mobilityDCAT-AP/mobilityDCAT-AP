# ⚠️ DEPRECATED

This folder is deprecated as of mobilityDCAT-AP v3.0.0.

The SHACL validation files have been moved to:
 `../shaclShapes/`

## New files:
- `../shaclShapes/mobilitydcat-ap-shacl.ttl` — Basic validation (cardinality, nodeKind, patterns)
- `../shaclShapes/mobilitydcat-ap-shacl-ranges.ttl` — Range constraints (sh:class)

## Why deprecated?
The individual per-class files in this folder were replaced by two consolidated 
files that extend DCAT-AP 3.0.1 SHACL shapes via owl:imports.

The files in this folder will be removed in a future release.



# mobilityDCAT-AP Validation files

The [SHACL shapes file](mobilitydcat-ap_shacl_shapes.ttl) contains constraints for a Data Graph expressed as RDF. 

The following shape files ensure that an instances of a specific class has the necessary properties and conforms to specified rules.

- The [Address_Agent_Shape](address_agent_shape.ttl) is a SHACL node shape that defines the structure and constraints for the [locn:Address](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-address-agent) class. 
- The [Agent_Shape](agent_shape.ttl) is a SHACL node shape that defines the structure and constraints for the [foaf:Agent](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-agent) class. 
- The [Assessment_Shape](assessment_shape.ttl) is a SHACL node shape that defines the structure and constraints for the [mobilitydcatap:Assessment](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-assessment) class.
- The [Catalogue_Shape](catalogue_shape.ttl) is a SHACL node shape that defines the structure and constraints for the [dcat:Catalog](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-catalogue) class.
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

