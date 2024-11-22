
# 📚 mobilityDCAT-AP SHACL Documentation

# 🔍 Introduction to SHACL

## 🎯 What is SHACL and Why Use It?

SHACL (Shapes Constraint Language) is a language for validating RDF graphs against a set of conditions. It is used to:

1. Define the structure of RDF data
2. Validate RDF data against predefined shapes
3. Data quality assurance

## 🔄 Why OWL is Not Enough

While OWL (Web Ontology Language) is powerful for defining ontologies and inferring new knowledge, it has limitations:

1. OWL operates under the Open World Assumption, making it challenging to validate data completeness
2. OWL lacks built-in support for certain validation tasks, like cardinality checks on properties
3. OWL is designed for inferencing, not for data validation

SHACL complements OWL by providing a robust framework specifically for data validation and integrity constraints.

## 🌐 Open World vs. Closed World
For a detailed technical explanation of these concepts, see: [Open World vs. Closed World Assumptions in Knowledge Representation](https://www.sciencedirect.com/topics/computer-science/open-world-assumption)

1. **Open World Assumption (OWA)**:
   - Used in OWL
   - Assumes that what is not explicitly stated might be true
   - Good for knowledge representation and inferencing
   - Challenging for data validation

2. **Closed World Assumption (CWA)**:
   - Used in SHACL
   - Assumes that what is not explicitly stated is false
   - Better suited for data validation and constraint checking
   - Allows for more stringent data quality control

SHACL's use of CWA makes it more appropriate for scenarios where you need to ensure data completeness and adherence to a specific structure.

## 💡 Key Takeaway

SHACL provides a standardized, powerful way to validate RDF data, filling gaps left by OWL and other Semantic Web technologies. Its closed-world approach makes it particularly useful for ensuring data quality and completeness in various applications, from data integration.


# 🔍 SHACL Basics (Core) and Advanced Features

## 🌱 SHACL Basics (Core Features)

SHACL Core provides the fundamental constraints and validation mechanisms. Here are the key components, for more detail see: [Core Constraint Components](https://www.w3.org/TR/shacl/#core-components)

1. **Node Shapes**
   - Define constraints that apply to nodes in the data graph.
   - Example: `sh:NodeShape` to define a shape for a specific class of nodes.

2. **Property Shapes**
   - Define constraints on properties and their values.
   - Example: `sh:PropertyShape` to define constraints on a specific property.

3. **Cardinality Constraints**
   - Control the number of values a property can have.
   - Examples: `sh:minCount`, `sh:maxCount`

4. **Value Type Constraints**
   - Specify the allowed types for property values.
   - Examples: `sh:datatype`, `sh:class`, `sh:nodeKind`

5. **Value Range Constraints**
   - Define allowed ranges for numeric and date values.
   - Examples: `sh:minInclusive`, `sh:maxExclusive`

6. **String Constraints**
   - Constrain string values using patterns or length.
   - Examples: `sh:pattern`, `sh:minLength`, `sh:maxLength`

7. **Logical Constraints**
   - Combine constraints using logical operators.
   - Examples: `sh:and`, `sh:or`, `sh:not`

8. **Shape References**
   - Reference other shapes within a shape definition.
   - Example: `sh:node` to reference another shape

9. **Targeting Rules**
   - Specify which nodes in the data graph a shape applies to.
   - Examples: `sh:targetClass`, `sh:targetNode`

10. **Result Properties**
    - Customize validation result messages.
    - Example: `sh:message` for custom violation messages

## 📝 Notes

- SHACL Core is sufficient for many common validation scenarios and is widely supported.
- SHACL Advanced features provide more flexibility but may have limited support in some tools.
- When using advanced features, consider compatibility with your chosen SHACL engine.
- Combining multiple features can create powerful validation rules but may also increase complexity.
- Always test your shapes thoroughly, especially when using advanced features, to ensure they behave as expected.

Remember, while SHACL Advanced offers powerful capabilities, it's often best to start with SHACL Core and only use advanced features when necessary for your specific use case.


# 📚 SHACL Shape Prefixes

This document lists the prefixes used in the SHACL shapes for the [mobilityDCAT-AP](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html) Application Profile.

| Prefix | IRI |
|--------|-----|
| : | `http://w3id.org/mobilitydcat-ap#` |
| mobilitydcatap | `http://w3id.org/mobilitydcat-ap#` |
| adms | `http://www.w3.org/ns/adms#` |
| bibo | `http://purl.org/ontology/bibo/` |
| cnt | `http://www.w3.org/2011/content#` |
| dcat | `http://www.w3.org/ns/dcat#` |
| dcatap | `http://data.europa.eu/r5r/` |
| dct | `http://purl.org/dc/terms/` |
| dqv | `http://www.w3.org/ns/dqv#` |
| foaf | `http://xmlns.com/foaf/0.1/` |
| org | `http://www.w3.org/ns/org#` |
| locn | `http://www.w3.org/ns/locn#` |
| vcard | `http://www.w3.org/2006/vcard/ns#` |
| owl | `http://www.w3.org/2002/07/owl#` |
| rdf | `http://www.w3.org/1999/02/22-rdf-syntax-ns#` |
| oa | `http://www.w3.org/ns/oa#` |
| skos | `http://www.w3.org/2004/02/skos/core#` |
| rdfs | `http://www.w3.org/2000/01/rdf-schema#` |
| sh | `http://www.w3.org/ns/shacl#` |
| xsd | `http://www.w3.org/2001/XMLSchema#` |

## 📝 Notes

- The `:` prefix and `mobilitydcatap` prefix both refer to the same IRI (`http://w3id.org/mobilitydcat-ap#`). This is likely for convenience, allowing both a shorthand (`:`) and a more descriptive prefix for the same namespace.
- These prefixes cover a wide range of vocabularies and standards used in semantic web technologies, including:
  - DCAT (Data Catalog Vocabulary)
  - Dublin Core Terms
  - FOAF (Friend of a Friend)
  - SKOS (Simple Knowledge Organization System)
  - OWL (Web Ontology Language)
  - SHACL (Shapes Constraint Language)
  - XML Schema
- Some prefixes are specific to certain domains or applications, such as `bibo` for bibliographic ontology and `vcard` for contact information.

## 🔧 Usage

When working with SHACL shapes or RDF data using these vocabularies, you can use these prefixes to shorten IRIs. For example, instead of writing:

```turtle
<http://w3id.org/mobilitydcat-ap#someProperty> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#ObjectProperty> .
```

You can write:

```turtle
mobilitydcatap:someProperty rdf:type owl:ObjectProperty .
```

This makes the data more readable and easier to manage.

# 🛠️ SHACL Playgrounds and APIs
Here's the reformatted version with cleaner links:

## 🎮 SHACL Playgrounds
SHACL playgrounds are online tools that allow you to experiment with SHACL shapes and validate RDF data without needing to set up a local environment.
1. **TopBraid SHACL Playground** [Try it ↗](https://shacl.org/playground/)
   - Features: Allows testing SHACL shapes against data graphs, provides detailed violation reports.
2. **RDFShape** [Try it ↗](https://rdfshape.weso.es/shaclValidate)
   - Features: Supports SHACL and ShEx validation, data conversion, and visualization.
3. **SHACL Play** [Try it ↗](https://shacl-play.sparna.fr/play/)
   - Features: Offers a user-friendly interface for SHACL validation and shape creation.
4. **Zazuko SHACL Playground** [Try it ↗](https://shacl-playground.zazuko.com/)
   - Features: Simple interface for SHACL validation, good for quick tests.

## 💻 Java APIs for SHACL
1. **Apache Jena SHACL** [Learn more ↗](https://jena.apache.org/documentation/shacl/)
   - Features: Part of the Apache Jena framework, offers comprehensive SHACL support.
2. **TopBraid SHACL API** [GitHub ↗](https://github.com/TopQuadrant/shacl)
   - Features: The reference implementation of SHACL, very complete and well-maintained.
3. **RDF4J SHACL** [Documentation ↗](https://rdf4j.org/documentation/programming/shacl/)
   - Features: SHACL support as part of the RDF4J framework.

## 🐍 Python APIs for SHACL
1. **pySHACL** [GitHub ↗](https://github.com/RDFLib/pySHACL)
   - Features: A Python implementation of SHACL, built on top of RDFLib.
2. **Pyshacl** [PyPI ↗](https://pypi.org/project/pyshacl/)
   - Features: SHACL validator for Python, available via pip.

## 📝 Notes

- When choosing a tool or API, consider factors such as:
  - Ease of use and integration with your existing workflow
  - Performance, especially for large datasets
  - Compliance with the latest SHACL specification
  - Community support and documentation

- For production use, it's often best to use a well-established library like Apache Jena (Java) or pySHACL (Python).

- Online playgrounds are great for quick tests and learning, but for sensitive data or large-scale validation, a local implementation is usually more appropriate.

- Some of these tools may have additional features beyond basic SHACL validation, such as inference support or integration with other semantic web technologies.



# 🛠️ SHACL Playground Guide for mobilityDCAT-AP

## 🌐 Accessing SHACL Playground

1. Go to [https://shacl.org/playground/](https://shacl.org/playground/)

## 📚 Using mobilityDCAT-AP Resources

### 📐 Shapes Graph

Load mobilityDCAT-AP SHACL shapes:

[https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/mobilitydcat-ap_shacl_shapes.ttl](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/mobilitydcat-ap_shacl_shapes.ttl)

### 📊 Data Graph

Find example data graphs here:

[https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#examples](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#examples)

## ✅ Validation

The playground automatically validates the data against the shapes.

---

# mobilityDCAT-AP SHACL Shapes:

# 📜 :Address_Agent_Shape
The `:Address_Agent_Shape` is a SHACL node shape that defines the structure and constraints for the `locn:Address` class. This shape ensures that instances of address information for agents have the necessary properties and conform to specified rules.

## 📊 Shape Details
- **Type**: `sh:NodeShape`
- **Target Class**: `locn:Address`
- **Name**: "Address (Agent)" (in English)

## 📝 Properties
### 1. Administrative Area 🏛️
- **Path**: `locn:adminUnitL2`
- **Cardinality**: Maximum 1 (Recommended)
- **Type**: Literal
- **Name**: "administrative area"
- **Description**: The administrative area of an Address of the Agent. Depending on the country, this corresponds to a province, a county, a region, or a state.
- **Severity**: Violation

### 2. City 🌆
- **Path**: `locn:postName`
- **Cardinality**: Maximum 1 (Recommended)
- **Type**: Literal
- **Name**: "city"
- **Description**: The city of an Address of the Agent.
- **Severity**: Violation

### 3. Country 🌍
- **Path**: `locn:adminUnitL1`
- **Cardinality**: Maximum 1 (Recommended)
- **Type**: Literal
- **Name**: "country"
- **Description**: The country of an Address of the Agent.
- **Severity**: Violation

### 4. Postal Code 📮
- **Path**: `locn:postCode`
- **Cardinality**: Maximum 1 (Recommended)
- **Type**: Literal
- **Name**: "postal code"
- **Description**: The postal code of an Address of the Agent.
- **Severity**: Violation

### 5. Street Address 🏠
- **Path**: `locn:thoroughfare`
- **Cardinality**: Maximum 1 (Recommended)
- **Type**: Literal
- **Name**: "street address"
- **Description**: In mobilityDCAT-AP, this is a recommended property to be used for Address (Agent)
- **Severity**: Violation

## ⚠️ Constraints
- All properties have a severity level of "Violation" if constraints are not met
- Each property is limited to a maximum of one value
- All values must be literals
- All properties are recommended (not mandatory)

# 📜 :Agent_Shape Documentation
The `:Agent_Shape` is a SHACL node shape that defines the structure and constraints for the `foaf:Agent` class. This shape ensures that agent information has the necessary properties and conforms to specified rules.

## 📊 Shape Details
- **Type**: `sh:NodeShape`
- **Target Class**: `foaf:Agent`
- **Name**: "Agent" (in English)

## 📝 Properties
### 1. Address 📍
- **Path**: `locn:address`
- **Type**: `locn:Address`
- **Value Type**: Literal
- **Name**: "address"
- **Description**: This property MAY be used to specify the postal address of the Agent. This property is analogue to an addition by [GEODCAT-AP-v2.0.0].
- **Severity**: Violation

### 2. Affiliation 🏢
- **Path**: `org:memberOf`
- **Type**: `org:Organization`
- **Name**: "affiliation"
- **Description**: If the agent is of type person, this property SHOULD be used to specify the affiliation of the Agent, see § 7. Agent Types, Agent Roles and Contact Information. This property is analogue to an addition by [GEODCAT-AP-v2.0.0].
- **Severity**: Violation

### 3. Email 📧
- **Path**: `foaf:mbox`
- **Value Type**: IRI
- **Name**: "email"
- **Description**: This property SHOULD be used to provide the email address of the Agent, specified using fully qualified mailto: URI scheme [RFC6068]. The email SHOULD be used to establish a communication channel to the agent.
- **Severity**: Violation

### 4. First Name 👤
- **Path**: `foaf:firstName`
- **Cardinality**: Maximum 1
- **Data Type**: `sh:Literal`
- **Name**: "first name"
- **Description**: If the agent is of type person, this property SHOULD be used to specify the first name of the Agent, see section § 7. Agent Types, Agent Roles and Contact Information.
- **Severity**: Violation

### 5. Phone ☎️
- **Path**: `foaf:phone`
- **Value Type**: Literal
- **Name**: "phone"
- **Description**: This property MAY be used to provide the phone number of the Agent, specified using fully qualified tel: URI scheme [RFC3966]. This property is analogue to an addition by [GEODCAT-AP-v2.0.0].
- **Severity**: Violation

### 6. Surname 👥
- **Path**: `foaf:surname`
- **Cardinality**: Maximum 1
- **Data Type**: `xsd:string`
- **Name**: "surname"
- **Description**: If the agent is of type person, this property SHOULD be used to specify the surname of the Agent, see section 7.
- **Severity**: Violation

### 7. work place Homepage URL 🌐
- **Path**: `foaf:workplaceHomepage`
- **Cardinality**: Maximum 1
- **Type**: `rdfs:Resource`
- **Name**: "work place Homepage URL"
- **Description**: If the agent is of type person, this property SHOULD be used to specify the surname of the Agent, see section 7.
- **Severity**: Violation

## ⚠️ Constraints
- All properties have a severity level of "Violation" if constraints are not met
- First name, surname, and URL are limited to a maximum of one value
- Email must be an IRI (mailto: scheme)
- Phone numbers should use the tel: URI scheme
- All properties are optional but recommended when applicable

# 📜 :Assessment_Shape
The `:Assessment_Shape` is a SHACL node shape that defines the structure and constraints for the `mobilitydcatap:Assessment` class. This shape ensures that assessment information has the necessary properties and conforms to specified rules.

## 📊 Shape Details
- **Type**: `sh:NodeShape`
- **Target Class**: `mobilitydcatap:Assessment`
- **Name**: "Assessment"

## 📝 Properties
### 1. Assessment Date 📅
- **Path**: `dct:issued`
- **Cardinality**: Maximum 1 (Optional)
- **Data Type**: Either `xsd:date` OR `xsd:dateTime`
- **Name**: "assessment date"
- **Description**: This property MAY be used to describe the date of the latest assessment procedure.
- **Severity**: Violation

### 2. Assessment Result 📊
- **Path**: `oa:hasBody`
- **Cardinality**: Maximum 1 (Optional)
- **Type**: `rdfs:Resource`
- **Name**: "assessment result"
- **Description**: This property MAY be used to describe the result of the latest assessment procedure, in form of a URL linking to further details or results. Alternatively, textual information MAY be provided using the Embedded Textual Body construction of the Web Annotation Data Model [Web-Annotation-Data-Model], which allows to specify text formats and languages which might be relevant for multilingual purposes.
- **Severity**: Violation

## ⚠️ Constraints
- Both properties have a severity level of "Violation" if constraints are not met
- Both properties are limited to a maximum of one value
-  Both properties are optional
- Assessment date must be either a date or datetime value
- Assessment result must be a resource (typically a URL or embedded text)

## 📌 Notes
- The assessment result can be provided either as:
  - A URL linking to detailed results
  - Embedded textual information with language specifications
- Date values must conform to either:
  - XML Schema date format (YYYY-MM-DD)
  - XML Schema dateTime format (YYYY-MM-DDThh:mm:ss)
 
# 📜 :Catalogue_Shape 
The `:Catalogue_Shape
` is a SHACL node shape that defines the structure and constraints for the `dcat:Catalog` class. This shape ensures that catalogue information has the necessary properties and conforms to specified rules.

## 📊 Shape Details
- **Type**: `sh:NodeShape`
- **Target Class**: `dcat:Catalog`
- **Name**: "Catalogue" (in English)

## 📝 Properties
### 1. Primary Identifier 🔑
- **Path**: `dct:identifier`
- **Cardinality**: Maximum 1 (Optional)
- **Value Type**: Literal
- **Name**: "identifier"
- **Description**: This property MAY contain an identifier for the mobility data portal. Allows a unique identification of the individual portal and is used for referencing, e.g., when exchanging metadata between mobility data portals. This property SHOULD populated by the URI used within the RDF statement (via rdf:about). This property is analogue to an addition by [GEODCAT-AP-v2.0.0].
- **Severity**: Violation

### 2. Other Identifier 🏷️
- **Path**: `adms:identifier`
- **Cardinality**: Maximum 1 (Optional)
- **Type**: `adms:Identifier`
- **Name**: "other identifier"
- **Description**: This property MAY be used as an additional identifier, besides dct:identifier. It MAY be referring to a dedicated, EU-wide identificator system of NAPS or other portals, to be introduced in the future.
- **Severity**: Violation

## ⚠️ Constraints
- Both properties have a severity level of "Violation" if constraints are not met
- Both properties are limited to a maximum of one value
- Primary identifier must be a literal value
- Other identifier must be of type `adms:Identifier`

# 📜 :CatalogRecord_Shape
The `:CatalogRecord_Shape
` is a SHACL node shape that defines the structure and constraints for the `dcat:CatalogRecord` class. This shape ensures that catalogue record information has the necessary properties and conforms to specified rules.

## 📊 Shape Details
- **Type**: `sh:NodeShape`
- **Target Class**: `dcat:CatalogRecord`
- **Name**: "Catalogue Record" 

## 📝 Properties
### 1. Creation Date ⏰
- **Path**: `dct:created`
- **Cardinality**: Exactly 1 (Mandatory)
- **Data Type**: Either `xsd:date` OR `xsd:dateTime`
- **Name**: "creation date"
- **Description**: This property contains the date stamp (date and time) when the metadata entry was created for the first time. It SHOULD be generated by the system, whenever a platform user enters the metadata entry.
- **Severity**: Violation

### 2. Publisher 👥
- **Path**: `dct:publisher`
- **Cardinality**: Maximum 1 (Optional)
- **Type**: `foaf:Agent`
- **Name**: "publisher"
- **Description**: This property refers to an entity (an organisation or a person), which is responsible for creation and maintenance of the metadata entry on the data platform. This entity is the direct contact for the data platform operators or data-searching users, who have questions or issues about the metadata entry. This information can be natively created by a data platform, then corresponding to the entity that is registered to the data platform and has the role of a metadata creator. This information can be also harvested from other portals. It should include, as a minimum, the name and email address of the entity. The information might be identical to the property "Publisher" of the corresponding dataset. This property is analogue to an addition by [GEODCAT-AP-v2.0.0].
- **Severity**: Violation

## ⚠️ Constraints
- Both properties have a severity level of "Violation" if constraints are not met
- Creation date:
  - Must be present (minimum count: 1)
  - Must appear exactly once (maximum count: 1)
  - Must be either a date or datetime value
- Publisher:
  - Optional (no minimum count)
  - Maximum one publisher allowed
  - Must be of type `foaf:Agent`

## 🔧 Usage
When creating or validating a Catalogue Record:
1. ⏰ Must include exactly one creation date:
   - Use either date (YYYY-MM-DD) or
   - DateTime (YYYY-MM-DDThh:mm:ss) format
   - Should be system-generated

# 📜 :Category_Shape
The `:Category_Shape
` is a SHACL node shape that defines the structure and constraints for the `skos:Concept` class. This shape ensures that category information has the necessary properties and conforms to specified rules.

## 📊 Shape Details
- **Type**: `sh:NodeShape`
- **Target Class**: `skos:Concept`
- **Name**: "Category" (in English)

## 📝 Properties
### 1. Category Scheme 🗂️
- **Path**: `skos:inScheme`
- **Cardinality**: Maximum 1 (Optional)
- **Type**: `skos:ConceptScheme`
- **Name**: "category scheme"
- **Description**: This property MAY be used to specify the Category Scheme to which the Category belongs. This property is analogue to an addition by [GEODCAT-AP-v2.0.0].
- **Severity**: Violation

## ⚠️ Constraints
- The property has a severity level of "Violation" if constraints are not met
- Category scheme is limited to a maximum of one value
- Must be of type `skos:ConceptScheme`

## 🔧 Usage
When creating or validating a Category:
1. 🗂️ Optionally include one category scheme:
   - Specifies the broader classification system
   - Links the category to its parent scheme

# 📜 Dataset Shape Documentation
## 📋 Overview
The `Dataset_Shape` is a SHACL node shape that defines the structure and constraints for the `dcat:Dataset` class. This shape ensures that dataset information has the necessary properties and conforms to specified rules.

## 📊 Shape Details
- **Type**: `sh:NodeShape`
- **Target Class**: `dcat:Dataset`
- **Name**: "Dataset" (in English)

## 📝 Properties

### 1. Mobility Theme 🚦 (Mandatory)
- **Path**: `mobilitydcatap:mobilityTheme`
- **Pattern**: Must match "https://w3id.org/mobilitydcat-ap/mobility-theme"
- **Minimum Count**: 1
- **Name**: "mobility theme"
- **Description**: Refers to mobility-related theme of content. Requires hierarchical categorization with mandatory first level and optional second level.
- **Severity**: Violation

### 2. Georeferencing Method 🗺️ (Recommended)
- **Path**: `mobilitydcatap:georeferencingMethod`
- **Pattern**: Must match "https://w3id.org/mobilitydcat-ap/georeferencing-method"
- **Name**: "georeferencing method"
- **Description**: Should specify the georeferencing method used in the dataset.
- **Severity**: Violation

### 3. Network Coverage 🌐 (Recommended)
- **Path**: `mobilitydcatap:networkCoverage`
- **Pattern**: Must match "https://w3id.org/mobilitydcat-ap/network-coverage"
- **Name**: "network coverage"
- **Description**: Describes covered transport network parts, particularly for road traffic.
- **Severity**: Violation

### 4. Reference System 📍 (Recommended)
- **Path**: `dct:conformsTo`
- **Pattern**: Must match "http://www.opengis.net/def/crs/EPSG/0/"
- **Name**: "reference system"
- **Description**: Should specify spatial reference system using EPSG URIs.
- **Severity**: Violation

### 5. Rights Holder 👤 (Recommended)
- **Path**: `dct:rightsHolder`
- **Type**: `foaf:Agent`
- **Name**: "rights holder"
- **Description**: Entity legally owning or holding data rights.
- **Severity**: Violation

### 6. Transport Mode 🚗 (Recommended)
- **Path**: `mobilitydcatap:transportMode`
- **Pattern**: Must match "https://w3id.org/mobilitydcat-ap/transport-mode"
- **Name**: "transport mode"
- **Description**: Describes covered transport modes (multiple possible).
- **Severity**: Violation

### 7. Applicable Legislation ⚖️ (Optional)
- **Path**: `dcatap:applicableLegislation`
- **Type**: `skos:Concept`
- **Name**: "applicable legislation"
- **Description**: References relevant legal frameworks.
- **Severity**: Violation

### 8. Assessment Result 📊 (Optional)
- **Path**: `mobilitydcatap:assessmentResult`
- **Type**: `mobilitydcatap:Assessment`
- **Maximum Count**: 1
- **Name**: "assessment result"
- **Description**: References assessment process results.
- **Severity**: Violation

### 9. Intended Information Service ℹ️ (Optional)
- **Path**: `mobilitydcatap:intentedInformationService`
- **Pattern**: Must match "https://w3id.org/mobilitydcat-ap/intended-information-service"
- **Name**: "intended information service"
- **Description**: Describes predefined information services the data supports.
- **Severity**: Violation

### 10. Quality Description ✅ (Optional)
- **Path**: `dqv:hasQualityAnnotation`
- **Type**: `dqv:QualityAnnotation`
- **Name**: "quality description"
- **Description**: Describes quality aspects of the content.
- **Severity**: Violation

## ⚠️ Constraints
- All properties have violation severity
- Mobility Theme is mandatory (minimum 1)
- Assessment Result limited to maximum 1
- All other properties are either recommended or optional

# 📜  :Distribution_Shape
The ` :Distribution_Shape
` is a SHACL node shape that defines the structure and constraints for the `dcat:Distribution` class. This shape ensures that distribution information has the necessary properties and conforms to specified rules.

## 📊 Shape Details
- **Type**: `sh:NodeShape`
- **Target Class**: `dcat:Distribution`
- **Name**: "Distribution"

## 📝 Properties

### 1. Mobility Data Standard 📊 (Mandatory)
- **Path**: `mobilitydcatap:mobilityDataStandard`
- **Type**: `mobilitydcatap:MobilityDataStandard`
- **Pattern**: Must match "https://w3id.org/mobilitydcat-ap/mobility-data-standard"
- **Cardinality**: Exactly 1 (Mandatory)
- **Name**: "mobility data standard"
- **Description**: Describes the mobility data standard used for content delivery (e.g., DATEX II).
- **Severity**: Violation

### 2. Application Layer Protocol 🔄 (Recommended)
- **Path**: `mobilitydcatap:applicationLayerProtocol`
- **Pattern**: Must match "https://w3id.org/mobilitydcat-ap/application-layer-protocol"
- **Maximum Count**: 1
- **Name**: "application layer protocol"
- **Description**: Describes the transmitting channel of the distribution.
- **Severity**: Violation

### 3. Character Encoding 📝 (Optional)
- **Path**: `cnt:characterEncoding`
- **Type**: `sh:Literal`
- **Maximum Count**: 1
- **Name**: "character encoding"
- **Description**: Specifies the technical encoding format via character set standard.
- **Severity**: Violation

### 4. Communication Method 🔁 (Optional)
- **Path**: `mobilitydcatap:communicationMethod`
- **Pattern**: Must match "https://w3id.org/mobilitydcat-ap/communication-method"
- **Maximum Count**: 1
- **Name**: "communication method"
- **Description**: Indicates push or pull mode for data services.
- **Severity**: Violation

### 5. Data Format Notes 📋 (Optional)
- **Path**: `mobilitydcatap:dataFormatNotes`
- **Type**: `sh:Literal`
- **Maximum Count**: 1
- **Name**: "data format notes"
- **Description**: Additional textual information about content format.
- **Severity**: Violation

### 6. Grammar 📖 (Optional)
- **Path**: `mobilitydcatap:grammar`
- **Pattern**: Must match "https://w3id.org/mobilitydcat-ap/grammar"
- **Maximum Count**: 1
- **Name**: "grammar"
- **Description**: Describes technical data grammar format as sub-property of dct:conformsTo.
- **Severity**: Violation

### 7. Sample 🔍 (Optional)
- **Path**: `adms:sample`
- **Type**: `rdfs:Resource`
- **Name**: "sample"
- **Description**: References a sample distribution of the dataset.
- **Severity**: Violation

### 8. Temporal Coverage ⏱️ (Optional)
- **Path**: `dct:temporal`
- **Type**: `dct:PeriodOfTime`
- **Maximum Count**: 1
- **Name**: "temporal coverage"
- **Description**: Specifies time interval for data service delivery.
- **Severity**: Violation

## ⚠️ Constraints
- All properties have violation severity
- Mobility Data Standard:
  - Mandatory (exactly one required)
  - Must follow specific URI pattern
- Other properties:
  - Most have maximum count of 1
  - Must follow specified patterns where applicable

# 📜 :Kind_Shape

The `:Kind_Shape` is a SHACL node shape that defines the structure and constraints for the `vcard:Kind` class. This shape ensures that contact information has the necessary properties and conforms to specified rules.

## 📊 Shape Details
- **Type**: `sh:NodeShape`
- **Target Class**: `vcard:Kind`
- **Name**: "Kind" (in English)

## 📝 Properties

### 1. Email 📧 (Mandatory)
- **Path**: `vcard:hasEmail`
- **Minimum Count**: 1
- **Value Type**: IRI
- **Pattern**: Must start with "mailto:" (case-insensitive)
- **Name**: "email"
- **Description**: Contains email address using mailto: URI scheme [RFC6068].
- **Severity**: Violation
- **Message**: "Email must be a valid mailto: URI"

### 2. Name 👤 (Mandatory)
- **Path**: `vcard:fn`
- **Value Type**: Literal
- **Minimum Count**: 1
- **Name**: "name"
- **Description**: Contains name of the Kind. Can be repeated for different languages.
- **Severity**: Violation

### 3. URL 🌐 (Recommended)
- **Path**: `vcard:hasURL`
- **Maximum Count**: 1
- **Name**: "URL"
- **Description**: Points to a Web site of the Kind.
- **Severity**: Violation

### 4. Address 📫 (Optional)
- **Path**: `vcard:hasAddress`
- **Type**: `vcard:Address`
- **Maximum Count**: 1
- **Name**: "address"
- **Description**: Specifies the postal address of the Kind.
- **Severity**: Violation

### 5. Affiliation 🏢 (Optional)
- **Path**: `vcard:organization-name`
- **Value Type**: Literal
- **Maximum Count**: 1
- **Name**: "affiliation"
- **Description**: Specifies the affiliation. Can be repeated for different languages.
- **Severity**: Violation

### 6. Phone ☎️ (Optional)
- **Path**: `vcard:hasTelephone`
- **Maximum Count**: 1
- **Name**: "phone"
- **Description**: Provides phone number using tel: URI scheme [RFC3966].
- **Severity**: Violation

## ⚠️ Constraints
- All properties have violation severity
- Mandatory properties:
  - Email (must have at least one)
  - Name (must have at least one)
- Maximum one instance for:
  - URL
  - Address
  - Affiliation
  - Phone
- Email must follow mailto: URI scheme
- Phone must follow tel: URI scheme

# 📜 :LicenseDocument_Shape
The `:LicenseDocument_Shape` is a SHACL node shape that defines the structure and constraints for the `dct:LicenseDocument` class. This shape ensures that license information has the necessary properties and conforms to specified rules.

## 📊 Shape Details
- **Type**: `sh:NodeShape`
- **Target Class**: `dct:LicenseDocument`
- **Name**: "License Document" (in English)

## 📝 Properties

### 1. Standard License 📄 (Recommended)
- **Path**: `dct:identifier`
- **Pattern**: Must match "http://publications.europa.eu/resource/authority/access-right"
- **Maximum Count**: 1
- **Name**: "standard licence"
- **Description**: Used to link to a concrete standard license.
- **Severity**: Violation

### 2. License Text 📝 (Optional)
- **Path**: `rdfs:label`
- **Value Type**: Literal
- **Maximum Count**: 1
- **Name**: "licence text"
- **Description**: Contains the full text of a License Document as free text. Can be used when no standard license is available. Supports multiple language versions.
- **Severity**: Violation

## ⚠️ Constraints
- All properties have violation severity
- Both properties limited to maximum of one instance
- Standard License must follow specified URI pattern
- License Text must be a literal value

# 📜 :Location_Shape
The `:Location_Shape` is a SHACL node shape that defines the structure and constraints for the `dct:Location` class. This shape ensures that location information has the necessary properties and conforms to specified rules.

## 📊 Shape Details
- **Type**: `sh:NodeShape`
- **Target Class**: `dct:Location`
- **Name**: "Location" (in English)

## 📝 Properties

### 1. Gazetteer 🗺️ (Recommended)
- **Path**: `skos:inScheme`
- **Type**: `skos:ConceptScheme`
- **Maximum Count**: 1
- **Name**: "gazetteer"
- **Description**: Specifies the gazetteer to which the Location belongs.
- **Severity**: Violation

### 2. Geographic Identifier 📍 (Recommended)
- **Path**: `dct:identifier`
- **Value Type**: Either Literal OR IRI
- **Name**: "geographic identifier"
- **Description**: Contains the geographic identifier for the Location, e.g., the URI or other unique identifier in the context of the relevant gazetteer.
- **Severity**: Violation

### 3. Geographic Name 🏷️ (Optional)
- **Path**: `skos:prefLabel`
- **Value Type**: Literal
- **Name**: "geographic name"
- **Description**: Contains a preferred label of the Location. Can be repeated for different language versions.
- **Severity**: Violation

## ⚠️ Constraints
- All properties have violation severity
- Gazetteer is limited to maximum of one instance
- Geographic Identifier must be either a Literal or IRI
- Geographic Name must be a literal value

# 📜  :MobilityDataStandard_Shape
The ` :MobilityDataStandard_Shape` is a SHACL node shape that defines the structure and constraints for the `mobilitydcatap:mobilityDataStandard` class. This shape ensures that mobility data standard information has the necessary properties and conforms to specified rules.

## 📊 Shape Details
- **Type**: `sh:NodeShape`
- **Target Class**: `mobilitydcatap:mobilityDataStandard`
- **Name**: "Mobility Data Standard" (in English)

## 📝 Properties

### 1. Version Number 🔢 (Optional)
- **Path**: `owl:versionInfo`
- **Value Type**: Literal
- **Maximum Count**: 1
- **Name**: "version"
- **Description**: Describes the version of the mobility data standard used in the content (e.g., "3.2" for DATEX II v3.2). Should use concise version identifiers without redundant prefixes.
- **Severity**: Violation

### 2. Schema Reference 📋 (Optional)
- **Path**: `mobilitydcatap:schema`
- **Type**: `rdfs:Resource`
- **Maximum Count**: 1
- **Name**: "schema"
- **Description**: References the schema of the mobility data standard. Can point to:
  - Portal-internal schema catalogue
  - Individual publisher-provided schema
  - External schema catalogue (e.g., DATEX II profile)
- Sub-property of dct:conformsTo
- **Severity**: Violation

## ⚠️ Constraints
- All properties have violation severity
- Both properties limited to maximum of one instance
- Version must be a literal value
- Schema must be a resource reference

# 📜 :QualityAnnotation_Shape
The `:QualityAnnotation_Shape` is a SHACL node shape that defines the structure and constraints for the `dqv:QualityAnnotation` class. This shape ensures that quality annotation information has the necessary properties and conforms to specified rules.

## 📊 Shape Details
- **Type**: `sh:NodeShape`
- **Target Class**: `dqv:QualityAnnotation`
- **Name**: "Quality Annotation" (in English)

## 📝 Properties

### 1. Quality Annotation Resource ✅ (Optional)
- **Path**: `oa:hasBody`
- **Value Type**: Literal
- **Maximum Count**: 1
- **Name**: "quality annotation resource"
- **Description**: Describes quality aspects through either:
  - URL linking to detailed information
  - Embedded textual information with language specifications
- Supports Web Annotation Data Model format
- **Severity**: Violation

### 2. Quality Annotation Target 🎯 (Optional)
- **Path**: `oa:hasTarget`
- **Type**: `dcat:Dataset`
- **Maximum Count**: 1
- **Name**: "quality annotation target"
- **Description**: References the target dataset being described. Acts as inverse property of "dqv:hasQualityAnnotation" for Dataset class.
- **Severity**: Violation

## ⚠️ Constraints
- All properties have violation severity
- Both properties limited to maximum of one instance
- Quality Annotation Resource must be a literal value
- Quality Annotation Target must reference a Dataset

# 📜 Rights Statement Shape Documentation
## 📋 Overview
The `RightsStatement_Shape` is a SHACL node shape that defines the structure and constraints for the `dct:RightsStatement` class. This shape ensures that rights statement information has the necessary properties and conforms to specified rules.

## 📊 Shape Details
- **Type**: `sh:NodeShape`
- **Target Class**: `dct:RightsStatement`
- **Name**: "Rights Statement" (in English)

## 📝 Properties

### 1. Conditions for Access and Usage 🔒 (Mandatory)
- **Path**: `dct:type`
- **Pattern**: Must match "https://w3id.org/mobilitydcat-ap/conditions-for-access-and-usage"
- **Cardinality**: Exactly 1 (Mandatory)
- **Name**: "conditions for access and usage"
- **Description**: Indicates whether:
  - Free and unrestricted use is possible
  - Contract must be concluded
  - License must be agreed upon
- **Severity**: Violation

### 2. Additional Information ℹ️ (Recommended)
- **Path**: `rdfs:label`
- **Value Type**: Literal
- **Name**: "Additional information for access and usage"
- **Description**: Provides supplementary textual information about:
  - Access conditions
  - Usage requirements
  - Licensing details
- Supports multiple language versions
- **Severity**: Violation

## ⚠️ Constraints
- Both properties have violation severity
- Conditions for Access and Usage:
  - Mandatory (exactly one required)
  - Must follow specific URI pattern
- Additional Information:
  - Must be literal value
  - Can have multiple language versions
