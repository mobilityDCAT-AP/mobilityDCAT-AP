# 📚 mobilityDCAT-AP SHACL Documentation  

## 🔍 Introduction to SHACL  

### 🎯 What is SHACL and Why Use It?  
SHACL (Shapes Constraint Language) is a powerful tool for validating RDF data against predefined rules. It helps to:  

1. **Define** the structure of RDF data. 
2. **Validate** RDF data against specific constraints.  
3. **Ensure** high-quality, well-structured data  .

### 🧩 SHACL: A Real-World Analogy  
<details>  
  <summary>Click to expand</summary>  

  Imagine an online form for collecting contact information:  
  - The email field must contain a valid email  
  - The phone number must follow a correct format  
  - The age must be between 18 and 120  
  - Some fields are required, while others are optional  

  **SHACL does the same for RDF data**, ensuring that:  
  - Required properties exist  
  - Values are in the correct format  
  - Data follows specific rules and patterns

  ### Why It Matters
  Without SHACL, data can be incomplete or inconsistent - like receiving a shipping address with no city or a phone number with letters in it.
  With SHACL, computers can automatically verify data quality before accepting it, leading to:
  * More reliable information
  * Fewer errors in systems
  * Clearer expectations for data providers
  Just like form validation improves data quality in web applications, SHACL enhances data reliability in semantic web applications.

</details>  

### 🤔 Why OWL is Not Enough? 
<details>  
  <summary>Click to expand</summary>  

  While **OWL (Web Ontology Language)** is useful for defining ontologies and inferring knowledge, it has limitations:  

  1. **Open World Assumption (OWA)** – OWL assumes missing information **might** exist, making validation difficult.  
  2. **Limited Constraint Enforcement** – OWL struggles with certain validation tasks, like **ensuring a property appears exactly once**.  
  3. **Designed for Inferencing** – OWL is built for **reasoning**, not strict data validation.  

  ### Different Purposes

- **OWL** is like a detective who makes logical deductions about what must be true
- **SHACL** is like a quality inspector checking if everything meets specific requirements

  ### Real-World Example
  If you need to ensure every person in your database has exactly one email address:
  - OWL can't easily enforce this "exactly one" rule
  - SHACL can directly state: "Each person needs exactly one email property"  
</details>  

### 🌐 Open World vs. Closed World  
<details>  
  <summary>Click to expand</summary>  

  **1️⃣ Open World Assumption (OWA)**  
  - Used in OWL  
  - Assumes missing data **might** exist elsewhere  
  - Great for knowledge representation, but weak for validation  
  - Example: If the database doesn’t state "John has a phone number," OWA assumes we just don’t know yet.  

  **2️⃣ Closed World Assumption (CWA)**  
  - Used in SHACL  
  - Assumes missing data **does not exist**  
  - Ideal for strict validation and ensuring completeness  
  - Example: If "John has a phone number" is missing, CWA assumes he **definitely** has no phone number.  
</details>  

### 💡 Key Takeaway  
<details>  
  <summary>Click to expand</summary>  

  **SHACL fills the gaps left by OWL** by offering strict data validation, ensuring data completeness, and enforcing constraints. Its **closed-world approach** makes it essential for high-quality data management in various applications.  
</details>  

# 🔍 SHACL Basics (Core) and Advanced Features  

<details>
  <summary><strong>Core Features</strong></summary>
  
  - **Shapes**: Define the structure and constraints for RDF nodes (resources or literals).
  - **Validation**: SHACL validates RDF data by checking whether it adheres to the defined shapes.
  - **Simple Constraints**: Includes constraints like required properties, property types, and cardinality (e.g., min/max values).
</details>

<details>
  <summary><strong>Advanced Features</strong></summary>
  
  - **Complex Constraints**: Allows for more advanced validation, such as disjunctions, conjunctions, and custom rules.
  - **Inference**: SHACL can be used alongside inference engines to apply logical rules.
  - **Extensions**: SHACL allows the use of external functions and custom constraints.
</details>

## 📖 Technical Terminology  

### **Basic Terms – Foundation Concepts**  
<details>  
  <summary>Click to expand</summary>  

  **RDF (Resource Description Framework)** – A standard way to structure and share data on the web using subject-predicate-object statements (triples). Example:  
  *"Paris (subject) - is the capital of (predicate) - France (object)."*  

  **IRI (Internationalized Resource Identifier)** – A unique web address (like a URL) used to identify things in RDF. Unlike a URL, it supports different languages and formats. Example:  
  *`http://example.org/dataset/123`*  

  **Ontology** – A structured blueprint that defines concepts and relationships in a specific domain, like a data dictionary. Example:  
  *A medical ontology might define "Patient," "Doctor," and how they relate.*  

  **Literal** – A simple data value such as text, numbers, or dates in RDF. Example:  
  *"Helsinki", 42, or "2023-04-15".*  

  **Node** – Any item in an RDF graph that can have properties, such as a person or a place. Example:  
  *A "Book" node might have properties like "title" and "author".*  

  **Graph** – A collection of RDF triples that connect data, forming a network of relationships. Example:  
  *A social network where users and their connections are linked as nodes.*  

</details>  

### **SHACL-Specific Terms – Key SHACL Concepts**  
<details>  
  <summary>Click to expand</summary>  

  **Constraint** – A rule that data must follow to be considered valid.  

  **Validation** – The process of checking if data follows all defined constraints.  

  **Shape** – A collection of constraints applied to a specific type of data node.  

  **Cardinality** – Rules defining how many times a property must or can appear (minimum and maximum counts).  

  **Property Shape** – Constraints that apply to a **specific property** of a resource.  

  **Node Shape** – Constraints that apply to an **entire resource node**.  

  **Target** – Specifies which nodes in a graph a shape should apply to.  

</details>  

### **Prefix/Namespace – Shorthand Notation for IRIs**  
<details>  
  <summary>Click to expand</summary>  

  **Prefix** – A shorthand notation for IRIs, making RDF data easier to read and manage. Example:  
  *`dcat:` expands to `http://www.w3.org/ns/dcat#`.*  

  **Common prefixes used in SHACL:**  
  - **sh:** SHACL namespace  
  - **dcat:** Data Catalog Vocabulary  
  - **dct:** Dublin Core Terms  
  - **foaf:** Friend of a Friend vocabulary  
  - **rdf:** Resource Description Framework  

</details>  

# 🌱 SHACL Basics (Core Features)  

SHACL Core provides the fundamental constraints and validation mechanisms for RDF data. Here are its key components:  

<details>  
  <summary><strong>1. Node Shapes</strong> - Foundation of SHACL validation</summary>  

  **Node shapes define validation rules for entire nodes (resources).** They serve as the foundation of SHACL and can contain multiple property constraints.  

  ```turtle
  # A shape that validates all dcat:Dataset instances
  :DatasetShape a sh:NodeShape ;
    sh:targetClass dcat:Dataset .
  ```

  ✅ Ensures that all instances of `dcat:Dataset` conform to the specified constraints.  
</details>  

<details>  
  <summary><strong>2. Property Shapes</strong> - Constraints for specific properties</summary>  

  **Property shapes define constraints for specific properties of a node.**  

  ```turtle
  # Property shape defining constraints for a title
  :DatasetShape sh:property [
    sh:path dct:title ;  # This applies to the title property
  ] .
  ```

  ✅ Each property shape uses `sh:path` to specify which property it applies to.  
</details>  

<details>  
  <summary><strong>3. Cardinality Constraints</strong> - Control how many times a property appears</summary>  

  **Cardinality constraints specify required and allowed occurrences of a property.**  

  ```turtle
  # Title must appear exactly once
  sh:property [
    sh:path dct:title ;
    sh:minCount 1 ;
    sh:maxCount 1 ;
  ] .
  ```

  ✅ Use `sh:minCount` to require a property, `sh:maxCount` to limit occurrences, or both for an exact count.  
</details>  

<details>  
  <summary><strong>4. Value Type Constraints</strong> - What kind of values are allowed</summary>  

  **Define the expected data type for property values.**  

  ```turtle
  # Title must be a literal string
  sh:property [
    sh:path dct:title ;
    sh:nodeKind sh:Literal ;
  ] .
  ```

  ✅ Use `sh:nodeKind` for literals/IRIs, `sh:datatype` for data types, or `sh:class` for specific class instances.  
</details>  

<details>  
  <summary><strong>5. Value Range Constraints</strong> - Numeric and date boundaries</summary>  

  **Ensure numeric or date values fall within a valid range.**  

  ```turtle
  # Rating must be between 1 and 5
  sh:property [
    sh:path :rating ;
    sh:minInclusive 1 ;
    sh:maxInclusive 5 ;
  ] .
  ```

  ✅ Use `sh:minInclusive` / `sh:maxInclusive` (inclusive) or `sh:minExclusive` / `sh:maxExclusive` (exclusive).  
</details>  

<details>  
  <summary><strong>6. String Constraints</strong> - Format controls for text values</summary>  

  **Control the format and length of text values.**  

  ```turtle
  # Email must match a valid pattern
  sh:property [
    sh:path foaf:mbox ;
    sh:pattern "^mailto:[\\w.%+-]+@[\\w.-]+\\.[a-zA-Z]{2,}$" ;
  ] .
  ```

  ✅ Use `sh:pattern` for regex validation, `sh:minLength` / `sh:maxLength` for length control.  
</details>  

<details>  
  <summary><strong>7. Logical Constraints</strong> - Combine using AND, OR, NOT operations</summary>  

  **Combine multiple constraints using logical operations.**  

  ```turtle
  # Must have either title OR name
  sh:or (
    [ sh:path dct:title ; sh:minCount 1 ]
    [ sh:path foaf:name ; sh:minCount 1 ]
  ) .
  ```

  ✅ Use `sh:and`, `sh:or`, and `sh:not` to enforce logical relationships between constraints.  
</details>  

<details>  
  <summary><strong>8. Shape References</strong> - Reuse shapes for modular validation</summary>  

  **Reuse existing shapes by referencing them within other shapes.**  

  ```turtle
  # Contact information must conform to PersonShape
  sh:property [
    sh:path dcat:contactPoint ;
    sh:node :PersonShape ;
  ] .
  ```

  ✅ Enables modular and reusable validation.  
</details>  

<details>  
  <summary><strong>9. Targeting Rules</strong> - Which nodes to validate</summary>  

  **Define which nodes should be validated by a shape.**  

  ```turtle
  :DatasetShape a sh:NodeShape ;
    # Three ways to target nodes
    sh:targetClass dcat:Dataset ;        # All datasets
    sh:targetNode :dataset123 ;          # Specific dataset
    sh:targetSubjectsOf dct:publisher ;  # Anything with a publisher
  ```

  ✅ Use `sh:targetClass`, `sh:targetNode`, or `sh:targetSubjectsOf`.  
</details>  

<details>  
  <summary><strong>10. Result Properties</strong> - Custom error messages</summary>  

  **Improve validation output with custom messages.**  

  ```turtle
  sh:property [
    sh:path dct:title ;
    sh:minCount 1 ;
    sh:message "Each dataset requires a title" ;
  ] .
  ```

  ✅ Use `sh:message` to provide user-friendly error descriptions.  
</details>  

### **Additional Features You Might Need**  

<details>  
  <summary><strong>11. Inverse Property Constraints</strong> - Checking relationships in reverse</summary>  

  **Ensure relationships exist in the opposite direction.**  

  ```turtle
  sh:property [
    sh:path [ sh:inversePath dct:creator ] ;
    sh:minCount 1 ;
  ] .
  ```

  ✅ Ensures that every author is referenced by at least one dataset.  
</details>  

<details>  
  <summary><strong>12. Closed Shapes</strong> - Restricting extra properties</summary>  

  **Prevent data from containing undefined properties.**  

  ```turtle
  :DatasetShape a sh:NodeShape ;
    sh:closed true ;
    sh:ignoredProperties ( rdf:type ) .
  ```

  ✅ Only allows predefined properties, improving data consistency.  
</details>  

<details>  
  <summary><strong>13. Deactivated Shapes</strong> - Temporarily disable validation rules</summary>  

  **Turn off specific shapes without deleting them.**  

  ```turtle
  :DatasetShape sh:deactivated true .
  ```

  ✅ Useful for debugging or incremental development.  
</details>  

<details>  
  <summary><strong>14. SHACL Functions & Expressions</strong> - Advanced validation logic</summary>  

  **Define custom functions for validation.**  

  ```turtle
  :MyFunction a sh:SPARQLFunction ;
    sh:parameter [
      sh:path :input ;
      sh:datatype xsd:string ;
    ] ;
    sh:returnType xsd:boolean ;
    sh:select """
      SELECT ?input WHERE {
        FILTER(STRLEN(?input) > 3)
      }
    """ .
  ```

  ✅ Enables complex validation beyond built-in SHACL features.  
</details>  

<details>
  <summary><strong>📝 Best Practices</strong></summary>
  
  - SHACL Core is sufficient for many common validation scenarios and is widely supported.
  - SHACL Advanced features provide more flexibility but may have limited support in some tools.
  - When using advanced features, consider compatibility with your chosen SHACL engine.
  - Combining multiple features can create powerful validation rules but may also increase complexity.
  - Always test your shapes thoroughly, especially when using advanced features, to ensure they behave as expected.
  - It's often best to start with SHACL Core and only use advanced features when necessary for your specific use case.
</details>
<details>
  <summary><strong>🛠️ Practical Debugging Tips</strong></summary>

  - **Use Detailed Error Messages**: Always include the `sh:message` property in your shapes. This helps you provide human-readable error messages that make it easier to identify what went wrong during validation.
  
  - **Test Incrementally**: Start with basic constraints and build up gradually. This allows you to pinpoint where validation breaks down, rather than debugging a complex set of rules all at once.
  
  - **Check Targeting Rules**: Double-check that your targeting rules are applied correctly. If a shape doesn’t seem to validate as expected, ensure it’s being applied to the correct nodes by verifying `sh:targetClass`, `sh:targetNode`, or `sh:targetSubjectsOf`.
  
  - **Use Debugging Tools**: Some SHACL validation engines offer debugging features that give you detailed logs and trace information about why a validation failed. This can save a lot of time when tracking down issues.
  
  - **Verify Cardinality Constraints**: If data validation fails due to missing or extra values, revisit your `sh:minCount` and `sh:maxCount` constraints. Sometimes, a simple miscount can cause validation errors.
  
  - **Validate with Small Data Sets**: Before applying your shapes to large datasets, test them with a small, known dataset. This allows you to easily verify that the constraints are working as expected without being overwhelmed by too much data.
  
  - **Validate Multiple Times**: If a shape works in one context but not another, try running the validation multiple times. Often, issues arise from data that isn't fully integrated into the graph, and re-validation can highlight the missing pieces.
  
  - **Use Online Validators**: Use SHACL validators like the SHACL Playground to quickly test shapes and get real-time feedback. This helps isolate issues and provides immediate feedback as you refine your constraints.

</details>


# 📚 SHACL Shape Prefixes

<details>
  <summary><strong>Prefix Table</strong> - Common namespaces used in SHACL shapes</summary>
  
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
</details>

<details>
  <summary><strong>Notes on Prefixes</strong></summary>
  
  - The `:` prefix and `mobilitydcatap` prefix both refer to the same IRI (`http://w3id.org/mobilitydcat-ap#`). This is for convenience, allowing both a shorthand (`:`) and a more descriptive prefix for the same namespace.
  - These prefixes cover a wide range of vocabularies and standards used in semantic web technologies, including:
    - DCAT (Data Catalog Vocabulary)
    - Dublin Core Terms
    - FOAF (Friend of a Friend)
    - SKOS (Simple Knowledge Organization System)
    - OWL (Web Ontology Language)
    - SHACL (Shapes Constraint Language)
    - XML Schema
  - Some prefixes are specific to certain domains or applications, such as `bibo` for bibliographic ontology and `vcard` for contact information.
</details>

<details>
  <summary><strong>Usage Example</strong></summary>
  
  When working with SHACL shapes or RDF data using these vocabularies, you can use these prefixes to shorten IRIs. For example, instead of writing:
  
  ```turtle
  <http://w3id.org/mobilitydcat-ap#someProperty> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#ObjectProperty> .
  ```
  
  You can write:
  
  ```turtle
  mobilitydcatap:someProperty rdf:type owl:ObjectProperty .
  ```
</details>

# ⚠️ Watch Out for Namespaces!

<details>
  <summary><strong>The Problem: HTTP vs HTTPS</strong> - A critical issue that causes silent failures</summary>
  
  When working with SHACL shapes, one tiny difference can break everything:
  
  ```
  http://w3id.org/example#  ≠  https://w3id.org/example#
  ```
  
  Even though these look almost identical, they're completely different to computers. It's like sending mail to "123 Main St" versus "123 Main Ave" - they'll never reach the same place!
</details>

<details>
  <summary><strong>Why Validation Silently Fails</strong></summary>
  
  When your shape uses `http://` but your data uses `https://`:
  - The validator looks for resources at the http:// address
  - It doesn't find anything (because everything is at the https:// address)
  - No validation happens
  - The result appears "valid" (but was never actually checked!)
</details>

<details>
  <summary><strong>Simple Fix</strong></summary>
  
  Make sure both your shapes and data use exactly the same prefix:
  - Either both use `http://`
  - Or both use `https://`
  
  This small detail can save hours of troubleshooting!
</details>

<details>
  <summary><strong>📝 Notes</strong></summary>

  - SHACL Core is sufficient for many common validation scenarios and is widely supported.
  - SHACL Advanced features provide more flexibility but may have limited support in some tools.
  - When using advanced features, consider compatibility with your chosen SHACL engine.
  - Combining multiple features can create powerful validation rules but may also increase complexity.
  - Always test your shapes thoroughly, especially when using advanced features, to ensure they behave as expected.

  Remember, while SHACL Advanced offers powerful capabilities, it's often best to start with SHACL Core and only use advanced features when necessary for your specific use case.
</details>


# 🛠️ SHACL Playgrounds and APIs

<details>
  <summary><strong>SHACL Playgrounds</strong></summary>
  
  SHACL playgrounds are online tools that allow you to experiment with SHACL shapes and validate RDF data without needing to set up a local environment.
  
  1. **TopBraid SHACL Playground** [Try it ↗](https://shacl.org/playground/)
     - Features: Allows testing SHACL shapes against data graphs, provides detailed violation reports.
  2. **RDFShape** [Try it ↗](https://rdfshape.weso.es/shaclValidate)
     - Features: Supports SHACL and ShEx validation, data conversion, and visualization.
  3. **SHACL Play** [Try it ↗](https://shacl-play.sparna.fr/play/)
     - Features: Offers a user-friendly interface for SHACL validation and shape creation.
  4. **Zazuko SHACL Playground** [Try it ↗](https://shacl-playground.zazuko.com/)
     - Features: Simple interface for SHACL validation, good for quick tests.

</details>

<details>
  <summary><strong>💻 ☕ Java APIs for SHACL</strong></summary>
  
  1. **Apache Jena SHACL** [Learn more ↗](https://jena.apache.org/documentation/shacl/)
     - Features: Part of the Apache Jena framework, offers comprehensive SHACL support.
  2. **TopBraid SHACL API** [GitHub ↗](https://github.com/TopQuadrant/shacl)
     - Features: The reference implementation of SHACL, very complete and well-maintained.
  3. **RDF4J SHACL** [Documentation ↗](https://rdf4j.org/documentation/programming/shacl/)
     - Features: SHACL support as part of the RDF4J framework.

</details>

<details>
  <summary><strong>🐍 Python APIs for SHACL</strong></summary>
  
  1. **pySHACL** [GitHub ↗](https://github.com/RDFLib/pySHACL)
     - Features: A Python implementation of SHACL, built on top of RDFLib.
  2. **Pyshacl** [PyPI ↗](https://pypi.org/project/pyshacl/)
     - Features: SHACL validator for Python, available via pip.

</details>

<details>
  <summary><strong>📝 Notes</strong></summary>
  
  - When choosing a tool or API, consider factors such as:
    - Ease of use and integration with your existing workflow
    - Performance, especially for large datasets
    - Compliance with the latest SHACL specification
    - Community support and documentation
  - For production use, it's often best to use a well-established library like Apache Jena (Java) or pySHACL (Python).
  - Online playgrounds are great for quick tests and learning, but for sensitive data or large-scale validation, a local implementation is usually more appropriate.
  - Some of these tools may have additional features beyond basic SHACL validation, such as inference support or integration with other semantic web technologies.

</details>

### 📚 Common Errors in SHACL Validation

<details>
  <summary><strong>⚠️ Common Errors in SHACL Validation</strong></summary>

  While working with SHACL, users often encounter common mistakes that can lead to validation failures or unexpected results. Below are some typical errors and how to resolve them:

  ## 1. Mismatched Prefixes for IRIs
  - **Error**: Using `http://` vs `https://` can lead to silent validation failures.
  - **Solution**: Ensure consistency between your SHACL shapes and data. Both should use either `http://` or `https://` for the same prefix.
  - **Example**:
    ```sh
    http://example.com/shape#someProperty ≠ https://example.com/shape#someProperty
    ```

  ## 2. Incorrect Cardinality Constraints
  - **Error**: Failing to specify or enforce the correct cardinality can lead to incorrect validation results.
  - **Solution**: Double-check that cardinality constraints (`minCount`, `maxCount`) are properly defined and match your expectations.
  - **Example**: 
    ```turtle
    sh:minCount 1 ; sh:maxCount 1 ;
    ```

  ## 3. Missing or Incorrect Data Types
  - **Error**: Not defining the correct data type for properties, such as using a literal when a resource is expected, or vice versa.
  - **Solution**: Ensure the data type is consistent with the property’s constraints. Use `xsd:string`, `xsd:int`, etc., for literals.
  - **Example**:
    ```turtle
    sh:datatype xsd:string ;  # Correct for text-based properties
    ```

  ## 4. Missing Required Properties
  - **Error**: Forgetting to include required properties in instances, which results in validation failures.
  - **Solution**: Review your shape definitions and ensure required properties are included in your data. If the property is optional, make sure it’s handled accordingly.
  - **Example**: 
    ```turtle
    locn:postCode 12345 ;  # Missing required property
    ```

  ## 5. Incorrect Use of `sh:and` and `sh:or`
  - **Error**: Misusing logical operators like `sh:and` or `sh:or` can lead to invalid shapes or incorrect validation logic.
  - **Solution**: Carefully review the use of logical operators in your shapes. Make sure you understand how they work with other constraints.
  - **Example**:
    ```turtle
    sh:and (sh:minCount 1 sh:maxCount 1) ;  # Correct usage of sh:and
    ```

  ## 6. Invalid Data Format
  - **Error**: Providing data in an unsupported or incorrect format.
  - **Solution**: Check your data's format against the expected SHACL input format (e.g., RDF, Turtle, or JSON-LD) and make sure it matches the shape definitions.
  - **Example**: Using a wrong RDF format or incorrect syntax can prevent the validation process.

  ## 7. Over-Complicating Shapes
  - **Error**: Defining overly complex or redundant validation rules can increase the risk of errors.
  - **Solution**: Start simple, with core constraints, and only introduce advanced features as necessary. Keep shapes as simple and understandable as possible.

  ## 8. Validation Engine Incompatibility
  - **Error**: Some SHACL engines may not support certain advanced SHACL features.
  - **Solution**: Ensure compatibility between your shapes and the SHACL validation engine you are using. Test your shapes with multiple tools if necessary.
  
</details>



# 🛠️ SHACL Playground Guide for mobilityDCAT-AP

## 🌐 Accessing SHACL Playground
Go to [Try it ↗](https://shacl.org/playground/)

<details>
  <summary><strong>📚 Using mobilityDCAT-AP Resources</strong></summary>
  
  ### 📐 Shapes Graph
  
  Load mobilityDCAT-AP SHACL shapes: [GitHub ↗](https://github.com/mobilityDCAT-AP/mobilityDCAT-AP/blob/gh-pages/releases/1.1.0/validationFiles/mobilitydcat-ap_shacl_shapes.ttl)
  
  ### 📊 Data Graph
  
  Find example data graphs here: [GitHub ↗](https://github.com/mobilityDCAT-AP/mobilityDCAT-AP/tree/gh-pages/releases/1.1.0/validationFiles)
  
  ## ✅ Validation
  
  The playground automatically validates the data against the shapes.
  
</details>
<details>
  <summary><strong>📜 :Address_Agent_Shape</strong></summary>
  
  The [`:Address_Agent_Shape`↗](https://github.com/mobilityDCAT-AP/mobilityDCAT-AP/blob/2f66a609310874cf8ac7ff8fc2d54470a6915020/releases/1.1.0/validationFiles/mobilitydcat-ap_shacl_shapes.ttl#L87C2-L87C21) is a SHACL node shape that defines the structure and constraints for the [`locn:Address`↗](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-address-agent) class. This shape ensures that instances of address information for agents have the necessary properties and conform to specified rules.

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

  ## 🧪 Examples
  For practical examples showing both valid and invalid instances of the Address (Agent) shape, refer to our [`:Address_Agent_Shape`↗](https://github.com/mobilityDCAT-AP/mobilityDCAT-AP/blob/gh-pages/releases/1.1.0/validationFiles/address_agent_shape.ttl).

  This file contains:
  - ✅ Valid examples that pass all validation constraints
  - ❌ Invalid examples that demonstrate common mistakes
  - 💡 Annotations explaining why certain examples fail validation
</details>

<details>
  <summary><strong>📜 :Agent_Shape</strong></summary>

  The [`:Agent_Shape`](https://github.com/mobilityDCAT-AP/mobilityDCAT-AP/blob/2f66a609310874cf8ac7ff8fc2d54470a6915020/releases/1.1.0/validationFiles/mobilitydcat-ap_shacl_shapes.ttl#L142) is a SHACL node shape that defines the structure and constraints for the [`foaf:Agent`](https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/index.html#properties-for-agent) class. This shape ensures that agent information has the necessary properties and conforms to specified rules.

  ## 📊 Shape Details
  - **Type**: `sh:NodeShape`
  - **Target Class**: `foaf:Agent`
  - **Name**: "Agent" (in English)

  ## 📝 Properties

  ### Mandatory Property
  1. **Name** 📋
     - **Path**: `foaf:name`
     - **Cardinality**: 1..n (Mandatory, multiple values allowed)
     - **Value Type**: Literal
     - **Description**: The name of the agent. This property can be repeated for different versions of the name (e.g., in different languages).
     - **Message**: "Each Agent must have at least one name property."
     - **Severity**: Violation

  ### Recommended Property
  2. **Type** 🏷️
     - **Path**: `dct:type`
     - **Cardinality**: 0..1 (Recommended, maximum 1)
     - **Type**: `skos:Concept`
     - **Description**: Refers to the type of agent (e.g., person, organization). A controlled vocabulary is used.
     - **Message**: "Agent type must be a skos:Concept and can appear at most once."
     - **Severity**: Violation

  ### Optional Properties
  3. **Address** 📍
     - **Path**: `locn:address`
     - **Cardinality**: 0..n (Optional, multiple values allowed)
     - **Type**: `locn:Address`
     - **Description**: Specifies the postal address of the agent. May be used if applicable.
     - **Message**: "Address must be a blank node or IRI and must be an instance of locn:Address."
     - **Severity**: Violation

  4. **Affiliation** 🏢
     - **Path**: `org:memberOf`
     - **Cardinality**: 0..n (Optional, multiple values allowed)
     - **Type**: `org:Organization`
     - **Description**: If the agent is a person, this property specifies their organizational affiliation.
     - **Message**: "Affiliation must be an instance of org:Organization."
     - **Severity**: Violation

  5. **Email** 📧
     - **Path**: `foaf:mbox`
     - **Cardinality**: 0..n (Optional, multiple values allowed)
     - **Value Type**: IRI
     - **Description**: Specifies the email address of the agent using the `mailto:` scheme.
     - **Message**: "Email must be an IRI using the mailto: scheme."
     - **Severity**: Violation

  6. **First Name** 👤
     - **Path**: `foaf:firstName`
     - **Cardinality**: 0..1 (Optional, maximum 1)
     - **Value Type**: Literal
     - **Description**: Specifies the first name of the agent if the agent is a person.
     - **Message**: "First name must be a literal and can appear at most once."
     - **Severity**: Violation

  7. **Phone** ☎️
     - **Path**: `foaf:phone`
     - **Cardinality**: 0..n (Optional, multiple values allowed)
     - **Value Type**: IRI
     - **Description**: Provides the phone number of the agent using the `tel:` URI scheme.
     - **Message**: "Phone must be an IRI using the tel: scheme."
     - **Severity**: Violation

  8. **Surname** 👥
     - **Path**: `foaf:surname`
     - **Cardinality**: 0..1 (Optional, maximum 1)
     - **Value Type**: Literal
     - **Description**: Specifies the surname of the agent if the agent is a person.
     - **Message**: "Surname must be a literal and can appear at most once."
     - **Severity**: Violation

  9. **Work Place Homepage URL** 🌐
     - **Path**: `foaf:workplaceHomepage`
     - **Cardinality**: 0..1 (Optional, maximum 1)
     - **Type**: `rdfs:Resource`
     - **Description**: Specifies the workplace homepage URL of the agent.
     - **Message**: "Workplace homepage must be an rdfs:Resource and can appear at most once."
     - **Severity**: Violation

  ## ⚠️ Constraints
  - All properties have a severity level of "Violation" if constraints are not met.
  - The name property is mandatory (must appear at least once).
  - Type, first name, surname, and workplace homepage are limited to a maximum of one value.
  - Email must be an IRI (mailto: scheme).
  - Phone must be an IRI (tel: scheme).
  - Address must be either a blank node or an IRI.

  ## 🧪 Examples
  For practical examples showing both valid and invalid instances of the Agent shape, refer to our [example validation file](https://github.com/mobilityDCAT-AP/mobilityDCAT-AP/blob/gh-pages/releases/1.1.0/validationFiles/agent_examples.ttl).

</details>
<details>
  <summary><strong>📜 :Assessment_Shape</strong></summary>

  The `:Assessment_Shape` is a SHACL node shape that defines the structure and constraints for the `mobilitydcatap:Assessment` class. This shape ensures that assessment information has the necessary properties and conforms to specified rules.

  ## 📊 Shape Details
  - **Type**: `sh:NodeShape`
  - **Target Class**: `mobilitydcatap:Assessment`
  - **Name**: "Assessment"

  ## 📝 Properties
  1. **Assessment Date** 📅
     - **Path**: `dct:issued`
     - **Cardinality**: Maximum 1 (Optional)
     - **Data Type**: Either `xsd:date` OR `xsd:dateTime`
     - **Description**: This property MAY be used to describe the date of the latest assessment procedure.
     - **Severity**: Violation

  2. **Assessment Result** 📊
     - **Path**: `oa:hasBody`
     - **Cardinality**: Maximum 1 (Optional)
     - **Type**: `rdfs:Resource`
     - **Description**: This property MAY be used to describe the result of the latest assessment procedure, in the form of a URL linking to further details or results. Alternatively, textual information MAY be provided using the Embedded Textual Body construction of the Web Annotation Data Model [Web-Annotation-Data-Model], which allows specifying text formats and languages relevant for multilingual purposes.
     - **Severity**: Violation

  ## ⚠️ Constraints
  - Both properties have a severity level of "Violation" if constraints are not met.
  - Both properties are limited to a maximum of one value.
  - Both properties are optional.
  - **Assessment date** must be either a date or datetime value.
  - **Assessment result** must be a resource (typically a URL or embedded text).

  ## 📌 Notes
  - The assessment result can be provided either as:
    - A URL linking to detailed results.
    - Embedded textual information with language specifications.
  - Date values must conform to either:
    - XML Schema date format (`YYYY-MM-DD`).
    - XML Schema dateTime format (`YYYY-MM-DDThh:mm:ss`).

</details>
 
<details>
  <summary><strong>📜 :Catalogue_Shape <span>🔑</span></strong></summary>

  The `:Catalogue_Shape` is a SHACL node shape that defines the structure and constraints for the `dcat:Catalog` class. This shape ensures that catalogue information has the necessary properties and conforms to specified rules.

  ## 📊 Shape Details
  - **Type**: `sh:NodeShape`
  - **Target Class**: `dcat:Catalog`
  - **Name**: "Catalogue" (in English)

  ## 📝 Properties
  1. **Primary Identifier** 🔑
     - **Path**: `dct:identifier`
     - **Cardinality**: Maximum 1 (Optional)
     - **Value Type**: Literal
     - **Name**: "identifier"
     - **Description**: This property MAY contain an identifier for the mobility data portal. It allows a unique identification of the individual portal and is used for referencing, e.g., when exchanging metadata between mobility data portals. This property SHOULD be populated by the URI used within the RDF statement (via `rdf:about`). This property is analogous to an addition by [GEODCAT-AP-v2.0.0].
     - **Severity**: Violation

  2. **Other Identifier** 🏷️
     - **Path**: `adms:identifier`
     - **Cardinality**: Maximum 1 (Optional)
     - **Type**: `adms:Identifier`
     - **Name**: "other identifier"
     - **Description**: This property MAY be used as an additional identifier, besides `dct:identifier`. It MAY be referring to a dedicated, EU-wide identifier system of NAPS or other portals to be introduced in the future.
     - **Severity**: Violation

  ## ⚠️ Constraints
  - Both properties have a severity level of "Violation" if constraints are not met.
  - Both properties are limited to a maximum of one value.
  - **Primary identifier** must be a literal value.
  - **Other identifier** must be of type `adms:Identifier`.

</details>

<details>
  <summary><strong>📜 :CatalogRecord_Shape <span>⏰</span></strong></summary>

  The `:CatalogRecord_Shape` is a SHACL node shape that defines the structure and constraints for the `dcat:CatalogRecord` class. This shape ensures that catalogue record information has the necessary properties and conforms to specified rules.

  ## 📊 Shape Details
  - **Type**: `sh:NodeShape`
  - **Target Class**: `dcat:CatalogRecord`
  - **Name**: "Catalogue Record"

  ## 📝 Properties
  1. **Creation Date** ⏰
     - **Path**: `dct:created`
     - **Cardinality**: Exactly 1 (Mandatory)
     - **Data Type**: Either `xsd:date` OR `xsd:dateTime`
     - **Name**: "creation date"
     - **Description**: This property contains the date stamp (date and time) when the metadata entry was created for the first time. It SHOULD be generated by the system whenever a platform user enters the metadata entry.
     - **Severity**: Violation

  2. **Publisher** 👥
     - **Path**: `dct:publisher`
     - **Cardinality**: Maximum 1 (Optional)
     - **Type**: `foaf:Agent`
     - **Name**: "publisher"
     - **Description**: This property refers to an entity (an organisation or a person) that is responsible for the creation and maintenance of the metadata entry on the data platform. This entity is the direct contact for the data platform operators or data-searching users, who have questions or issues about the metadata entry. This information can be natively created by a data platform, then corresponding to the entity that is registered to the data platform and has the role of a metadata creator. It should include, as a minimum, the name and email address of the entity. This property is analogue to an addition by [GEODCAT-AP-v2.0.0].
     - **Severity**: Violation

  ## ⚠️ Constraints
  - Both properties have a severity level of "Violation" if constraints are not met.
  - **Creation date**:
    - Must be present (minimum count: 1)
    - Must appear exactly once (maximum count: 1)
    - Must be either a date or datetime value
  - **Publisher**:
    - Optional (no minimum count)
    - Maximum one publisher allowed
    - Must be of type `foaf:Agent`

  ## 🔧 Usage
  When creating or validating a Catalogue Record:
  - ⏰ Must include exactly one creation date:
    - Use either date (YYYY-MM-DD) or DateTime (YYYY-MM-DDThh:mm:ss) format
    - Should be system-generated
</details>


<details>
  <summary><strong>📜 Dataset Shape Documentation</strong></summary>

  ## 📋 Overview
  The `Dataset_Shape` is a SHACL node shape that defines the structure and constraints for the `dcat:Dataset` class. This shape ensures that dataset information has the necessary properties and conforms to specified rules.

  ## 📊 Shape Details
  - **Type**: `sh:NodeShape`
  - **Target Class**: `dcat:Dataset`
  - **Name**: "Dataset" (in English)

  ## 📝 Properties

  1. **Mobility Theme** 🚦 (Mandatory)
     - **Path**: `mobilitydcatap:mobilityTheme`
     - **Pattern**: Must match "https://w3id.org/mobilitydcat-ap/mobility-theme"
     - **Minimum Count**: 1
     - **Name**: "mobility theme"
     - **Description**: Refers to mobility-related theme of content. Requires hierarchical categorization with mandatory first level and optional second level.
     - **Severity**: Violation

  2. **Georeferencing Method** 🗺️ (Recommended)
     - **Path**: `mobilitydcatap:georeferencingMethod`
     - **Pattern**: Must match "https://w3id.org/mobilitydcat-ap/georeferencing-method"
     - **Name**: "georeferencing method"
     - **Description**: Should specify the georeferencing method used in the dataset.
     - **Severity**: Violation

  3. **Network Coverage** 🌐 (Recommended)
     - **Path**: `mobilitydcatap:networkCoverage`
     - **Pattern**: Must match "https://w3id.org/mobilitydcat-ap/network-coverage"
     - **Name**: "network coverage"
     - **Description**: Describes covered transport network parts, particularly for road traffic.
     - **Severity**: Violation

  4. **Reference System** 📍 (Recommended)
     - **Path**: `dct:conformsTo`
     - **Pattern**: Must match "http://www.opengis.net/def/crs/EPSG/0/"
     - **Name**: "reference system"
     - **Description**: Should specify spatial reference system using EPSG URIs.
     - **Severity**: Violation

  5. **Rights Holder** 👤 (Recommended)
     - **Path**: `dct:rightsHolder`
     - **Type**: `foaf:Agent`
     - **Name**: "rights holder"
     - **Description**: Entity legally owning or holding data rights.
     - **Severity**: Violation

  6. **Transport Mode** 🚗 (Recommended)
     - **Path**: `mobilitydcatap:transportMode`
     - **Pattern**: Must match "https://w3id.org/mobilitydcat-ap/transport-mode"
     - **Name**: "transport mode"
     - **Description**: Describes covered transport modes (multiple possible).
     - **Severity**: Violation

  7. **Applicable Legislation** ⚖️ (Optional)
     - **Path**: `dcatap:applicableLegislation`
     - **Type**: `skos:Concept`
     - **Name**: "applicable legislation"
     - **Description**: References relevant legal frameworks.
     - **Severity**: Violation

  8. **Assessment Result** 📊 (Optional)
     - **Path**: `mobilitydcatap:assessmentResult`
     - **Type**: `mobilitydcatap:Assessment`
     - **Maximum Count**: 1
     - **Name**: "assessment result"
     - **Description**: References assessment process results.
     - **Severity**: Violation

  9. **Intended Information Service** ℹ️ (Optional)
     - **Path**: `mobilitydcatap:intendedInformationService`
     - **Pattern**: Must match "https://w3id.org/mobilitydcat-ap/intended-information-service"
     - **Name**: "intended information service"
     - **Description**: Describes predefined information services the data supports.
     - **Severity**: Violation

  10. **Quality Description** ✅ (Optional)
      - **Path**: `dqv:hasQualityAnnotation`
      - **Type**: `dqv:QualityAnnotation`
      - **Name**: "quality description"
      - **Description**: Describes quality aspects of the content.
      - **Severity**: Violation

  ## ⚠️ Constraints
  - All properties have violation severity
  - **Mobility Theme** is mandatory (minimum 1)
  - **Assessment Result** limited to maximum 1
  - All other properties are either recommended or optional

</details>
<details>
  <summary><strong>📜 Distribution Shape Documentation</strong></summary>

  ## 📋 Overview
  The `:Distribution_Shape` is a SHACL node shape that defines the structure and constraints for the `dcat:Distribution` class. This shape ensures that distribution information has the necessary properties and conforms to specified rules.

  ## 📊 Shape Details
  - **Type**: `sh:NodeShape`
  - **Target Class**: `dcat:Distribution`
  - **Name**: "Distribution"

  ## 📝 Properties

  ### 1. **Mobility Data Standard** 📊 (Mandatory)
     - **Path**: `mobilitydcatap:mobilityDataStandard`
     - **Type**: `mobilitydcatap:MobilityDataStandard`
     - **Pattern**: Must match "https://w3id.org/mobilitydcat-ap/mobility-data-standard"
     - **Cardinality**: Exactly 1 (Mandatory)
     - **Name**: "mobility data standard"
     - **Description**: Describes the mobility data standard used for content delivery (e.g., DATEX II).
     - **Severity**: Violation

  ### 2. **Application Layer Protocol** 🔄 (Recommended)
     - **Path**: `mobilitydcatap:applicationLayerProtocol`
     - **Pattern**: Must match "https://w3id.org/mobilitydcat-ap/application-layer-protocol"
     - **Maximum Count**: 1
     - **Name**: "application layer protocol"
     - **Description**: Describes the transmitting channel of the distribution.
     - **Severity**: Violation

  ### 3. **Character Encoding** 📝 (Optional)
     - **Path**: `cnt:characterEncoding`
     - **Type**: `sh:Literal`
     - **Maximum Count**: 1
     - **Name**: "character encoding"
     - **Description**: Specifies the technical encoding format via character set standard.
     - **Severity**: Violation

  ### 4. **Communication Method** 🔁 (Optional)
     - **Path**: `mobilitydcatap:communicationMethod`
     - **Pattern**: Must match "https://w3id.org/mobilitydcat-ap/communication-method"
     - **Maximum Count**: 1
     - **Name**: "communication method"
     - **Description**: Indicates push or pull mode for data services.
     - **Severity**: Violation

  ### 5. **Data Format Notes** 📋 (Optional)
     - **Path**: `mobilitydcatap:dataFormatNotes`
     - **Type**: `sh:Literal`
     - **Maximum Count**: 1
     - **Name**: "data format notes"
     - **Description**: Additional textual information about content format.
     - **Severity**: Violation

  ### 6. **Grammar** 📖 (Optional)
     - **Path**: `mobilitydcatap:grammar`
     - **Pattern**: Must match "https://w3id.org/mobilitydcat-ap/grammar"
     - **Maximum Count**: 1
     - **Name**: "grammar"
     - **Description**: Describes technical data grammar format as sub-property of `dct:conformsTo`.
     - **Severity**: Violation

  ### 7. **Sample** 🔍 (Optional)
     - **Path**: `adms:sample`
     - **Type**: `rdfs:Resource`
     - **Name**: "sample"
     - **Description**: References a sample distribution of the dataset.
     - **Severity**: Violation

  ### 8. **Temporal Coverage** ⏱️ (Optional)
     - **Path**: `dct:temporal`
     - **Type**: `dct:PeriodOfTime`
     - **Maximum Count**: 1
     - **Name**: "temporal coverage"
     - **Description**: Specifies time interval for data service delivery.
     - **Severity**: Violation

  ## ⚠️ Constraints
  - All properties have violation severity.
  - **Mobility Data Standard**:
    - Mandatory (exactly one required)
    - Must follow specific URI pattern.
  - Other properties:
    - Most have maximum count of 1.
    - Must follow specified patterns where applicable.

</details>
<details>
  <summary><strong>📜 Kind Shape Documentation</strong></summary>

  ## 📋 Overview
  The `:Kind_Shape` is a SHACL node shape that defines the structure and constraints for the `vcard:Kind` class. This shape ensures that contact information has the necessary properties and conforms to specified rules.

  ## 📊 Shape Details
  - **Type**: `sh:NodeShape`
  - **Target Class**: `vcard:Kind`
  - **Name**: "Kind" (in English)

  ## 📝 Properties

  ### 1. **Email** 📧 (Mandatory)
     - **Path**: `vcard:hasEmail`
     - **Minimum Count**: 1
     - **Value Type**: IRI
     - **Pattern**: Must start with "mailto:" (case-insensitive)
     - **Name**: "email"
     - **Description**: Contains email address using mailto: URI scheme [RFC6068].
     - **Severity**: Violation
     - **Message**: "Email must be a valid mailto: URI"

  ### 2. **Name** 👤 (Mandatory)
     - **Path**: `vcard:fn`
     - **Value Type**: Literal
     - **Minimum Count**: 1
     - **Name**: "name"
     - **Description**: Contains name of the Kind. Can be repeated for different languages.
     - **Severity**: Violation

  ### 3. **URL** 🌐 (Recommended)
     - **Path**: `vcard:hasURL`
     - **Maximum Count**: 1
     - **Name**: "URL"
     - **Description**: Points to a Web site of the Kind.
     - **Severity**: Violation

  ### 4. **Address** 📫 (Optional)
     - **Path**: `vcard:hasAddress`
     - **Type**: `vcard:Address`
     - **Maximum Count**: 1
     - **Name**: "address"
     - **Description**: Specifies the postal address of the Kind.
     - **Severity**: Violation

  ### 5. **Affiliation** 🏢 (Optional)
     - **Path**: `vcard:organization-name`
     - **Value Type**: Literal
     - **Maximum Count**: 1
     - **Name**: "affiliation"
     - **Description**: Specifies the affiliation. Can be repeated for different languages.
     - **Severity**: Violation

  ### 6. **Phone** ☎️ (Optional)
     - **Path**: `vcard:hasTelephone`
     - **Maximum Count**: 1
     - **Name**: "phone"
     - **Description**: Provides phone number using tel: URI scheme [RFC3966].
     - **Severity**: Violation

  ## ⚠️ Constraints
  - All properties have violation severity.
  - **Mandatory properties**:
    - Email (must have at least one).
    - Name (must have at least one).
  - **Maximum one instance** for:
    - URL
    - Address
    - Affiliation
    - Phone
  - Email must follow mailto: URI scheme.
  - Phone must follow tel: URI scheme.

</details>
<details>
  <summary><strong>📜 License Document Shape Documentation</strong></summary>

  ## 📋 Overview
  The `:LicenseDocument_Shape` is a SHACL node shape that defines the structure and constraints for the `dct:LicenseDocument` class. This shape ensures that license information has the necessary properties and conforms to specified rules.

  ## 📊 Shape Details
  - **Type**: `sh:NodeShape`
  - **Target Class**: `dct:LicenseDocument`
  - **Name**: "License Document" (in English)

  ## 📝 Properties

  ### 1. **Standard License** 📄 (Recommended)
     - **Path**: `dct:identifier`
     - **Pattern**: Must match "http://publications.europa.eu/resource/authority/access-right"
     - **Maximum Count**: 1
     - **Name**: "standard licence"
     - **Description**: Used to link to a concrete standard license.
     - **Severity**: Violation

  ### 2. **License Text** 📝 (Optional)
     - **Path**: `rdfs:label`
     - **Value Type**: Literal
     - **Maximum Count**: 1
     - **Name**: "licence text"
     - **Description**: Contains the full text of a License Document as free text. Can be used when no standard license is available. Supports multiple language versions.
     - **Severity**: Violation

  ## ⚠️ Constraints
  - All properties have violation severity.
  - **Both properties** are limited to a maximum of one instance.
  - Standard License must follow the specified URI pattern.
  - License Text must be a literal value.

</details>
<details>
  <summary><strong>📜 Location Shape Documentation</strong></summary>

  ## 📋 Overview
  The `:Location_Shape` is a SHACL node shape that defines the structure and constraints for the `dct:Location` class. This shape ensures that location information has the necessary properties and conforms to specified rules.

  ## 📊 Shape Details
  - **Type**: `sh:NodeShape`
  - **Target Class**: `dct:Location`
  - **Name**: "Location" (in English)

  ## 📝 Properties

  ### 1. **Gazetteer** 🗺️ (Recommended)
     - **Path**: `skos:inScheme`
     - **Type**: `skos:ConceptScheme`
     - **Maximum Count**: 1
     - **Name**: "gazetteer"
     - **Description**: Specifies the gazetteer to which the Location belongs.
     - **Severity**: Violation

  ### 2. **Geographic Identifier** 📍 (Recommended)
     - **Path**: `dct:identifier`
     - **Value Type**: Either Literal OR IRI
     - **Name**: "geographic identifier"
     - **Description**: Contains the geographic identifier for the Location, e.g., the URI or other unique identifier in the context of the relevant gazetteer.
     - **Severity**: Violation

  ### 3. **Geographic Name** 🏷️ (Optional)
     - **Path**: `skos:prefLabel`
     - **Value Type**: Literal
     - **Name**: "geographic name"
     - **Description**: Contains a preferred label of the Location. Can be repeated for different language versions.
     - **Severity**: Violation

  ## ⚠️ Constraints
  - All properties have violation severity.
  - **Gazetteer** is limited to a maximum of one instance.
  - **Geographic Identifier** must be either a Literal or IRI.
  - **Geographic Name** must be a literal value.

</details>
<details>
  <summary><strong>📜 Mobility Data Standard Shape Documentation</strong></summary>

  ## 📋 Overview
  The `:MobilityDataStandard_Shape` is a SHACL node shape that defines the structure and constraints for the `mobilitydcatap:mobilityDataStandard` class. This shape ensures that mobility data standard information has the necessary properties and conforms to specified rules.

  ## 📊 Shape Details
  - **Type**: `sh:NodeShape`
  - **Target Class**: `mobilitydcatap:mobilityDataStandard`
  - **Name**: "Mobility Data Standard" (in English)

  ## 📝 Properties

  ### 1. **Version Number** 🔢 (Optional)
     - **Path**: `owl:versionInfo`
     - **Value Type**: Literal
     - **Maximum Count**: 1
     - **Name**: "version"
     - **Description**: Describes the version of the mobility data standard used in the content (e.g., "3.2" for DATEX II v3.2). Should use concise version identifiers without redundant prefixes.
     - **Severity**: Violation

  ### 2. **Schema Reference** 📋 (Optional)
     - **Path**: `mobilitydcatap:schema`
     - **Type**: `rdfs:Resource`
     - **Maximum Count**: 1
     - **Name**: "schema"
     - **Description**: References the schema of the mobility data standard. Can point to:
       - Portal-internal schema catalogue
       - Individual publisher-provided schema
       - External schema catalogue (e.g., DATEX II profile)
     - **Sub-property**: dct:conformsTo
     - **Severity**: Violation

  ## ⚠️ Constraints
  - All properties have violation severity.
  - Both properties are limited to a maximum of one instance.
  - **Version** must be a literal value.
  - **Schema** must be a resource reference.

</details>
<details>
  <summary><strong>📜 Quality Annotation Shape Documentation</strong></summary>

  ## 📋 Overview
  The `:QualityAnnotation_Shape` is a SHACL node shape that defines the structure and constraints for the `dqv:QualityAnnotation` class. This shape ensures that quality annotation information has the necessary properties and conforms to specified rules.

  ## 📊 Shape Details
  - **Type**: `sh:NodeShape`
  - **Target Class**: `dqv:QualityAnnotation`
  - **Name**: "Quality Annotation" (in English)

  ## 📝 Properties

  ### 1. **Quality Annotation Resource** ✅ (Optional)
     - **Path**: `oa:hasBody`
     - **Value Type**: Literal
     - **Maximum Count**: 1
     - **Name**: "quality annotation resource"
     - **Description**: Describes quality aspects through either:
       - URL linking to detailed information
       - Embedded textual information with language specifications
     - Supports Web Annotation Data Model format.
     - **Severity**: Violation

  ### 2. **Quality Annotation Target** 🎯 (Optional)
     - **Path**: `oa:hasTarget`
     - **Type**: `dcat:Dataset`
     - **Maximum Count**: 1
     - **Name**: "quality annotation target"
     - **Description**: References the target dataset being described. Acts as inverse property of "dqv:hasQualityAnnotation" for Dataset class.
     - **Severity**: Violation

  ## ⚠️ Constraints
  - All properties have violation severity.
  - Both properties are limited to a maximum of one instance.
  - **Quality Annotation Resource** must be a literal value.
  - **Quality Annotation Target** must reference a Dataset.

</details>
<details>
  <summary><strong>📜 Rights Statement Shape Documentation</strong></summary>

  ## 📋 Overview
  The `RightsStatement_Shape` is a SHACL node shape that defines the structure and constraints for the `dct:RightsStatement` class. This shape ensures that rights statement information has the necessary properties and conforms to specified rules.

  ## 📊 Shape Details
  - **Type**: `sh:NodeShape`
  - **Target Class**: `dct:RightsStatement`
  - **Name**: "Rights Statement" (in English)

  ## 📝 Properties

  ### 1. **Conditions for Access and Usage** 🔒 (Mandatory)
     - **Path**: `dct:type`
     - **Pattern**: Must match "https://w3id.org/mobilitydcat-ap/conditions-for-access-and-usage"
     - **Cardinality**: Exactly 1 (Mandatory)
     - **Name**: "conditions for access and usage"
     - **Description**: Indicates whether:
       - Free and unrestricted use is possible
       - Contract must be concluded
       - License must be agreed upon
     - **Severity**: Violation

  ### 2. **Additional Information for Access and Usage** ℹ️ (Recommended)
     - **Path**: `rdfs:label`
     - **Value Type**: Literal
     - **Name**: "additional information for access and usage"
     - **Description**: Provides supplementary textual information about:
       - Access conditions
       - Usage requirements
       - Licensing details
     - Supports multiple language versions
     - **Severity**: Violation

  ## ⚠️ Constraints
  - Both properties have violation severity.
  - **Conditions for Access and Usage**:
    - Mandatory (exactly one required)
    - Must follow a specific URI pattern.
  - **Additional Information**:
    - Must be a literal value.
    - Can have multiple language versions.

</details>

