##  Quick Guide: When to Use Which File

### ** Simple Table**

| **Scenario** | **File to Use** | **Why** |
|-------------|----------------|---------|
| **Quick development testing** | `mobilitydcat-ap-shacl.ttl` only | Fast checks: cardinality, datatype, nodeKind |
| **Strict compliance testing** | BOTH files merged | Full validation: everything must be correct |
| **Production data validation** | BOTH files merged | Ensure high-quality data before publishing |
| **Debugging errors** | ONE file at a time | Isolate the problem (basic vs. ranges) |
| **CI/CD pipeline** | BOTH files merged | Automated quality checks |
| **End-user validation tools** | `mobilitydcat-ap-shacl.ttl` only | More forgiving, better UX |
| **Publishing to portal** | BOTH files merged | Strict quality control |

---

##  **The Two Files Explained**

### **File 1: `mobilitydcat-ap-shacl.ttl` (BASIC)**
**Contains:**
-  Cardinality (min/max count)
-  Node kinds (IRI, Literal, BlankNode)
-  Datatypes (xsd:string, xsd:date, etc.)

**Example constraint:**
```turtle
:Agent_Shape_address
  sh:path locn:address ;
  sh:nodeKind sh:BlankNodeOrIRI ;  # ← Must be IRI or blank node
  sh:maxCount 1 .                  # ← At most one
```

**Use when:**
-  Quick testing during development
-  Checking basic structure
-  Creating new data

---

### **File 2: `mobilitydcat-ap-shacl-ranges.ttl` (RANGES)**
**Contains:**
-  Class membership (`sh:class`)
-  Strict typing

**Example constraint:**
```turtle
:Agent_Shape_address_range
  sh:path locn:address ;
  sh:class locn:Address .  # ← Must be locn:Address instance
```

**Use when:**
-  Final quality checks
-  Before publishing data
-  Ensuring strict compliance

---

## **Practical Workflow**

### **Development Phase:**
```
1. Create data
2. Validate with: mobilitydcat-ap-shacl.ttl (basic)
   ↓
    PASS → Continue
    FAIL → Fix structure issues
```

### **Pre-Production Phase:**
```
3. Validate with: BOTH files merged
   ↓
    PASS → Ready to publish!
    FAIL → Fix type/class issues
```

# mobilityDCAT-AP SHACL Import Strategy

## Import Rules

### Development Phase (drafts/)
```turtle
@prefix : <https://w3id.org/mobilitydcat-ap/drafts/1.1.0-draft-0.1#> .

owl:imports <https://mobilitydcat-ap.github.io/mobilityDCAT-AP/drafts/1.1.0-draft-0.1/mobilitydcat-ap_v1.1.0.ttl> ;
owl:imports <https://semiceu.github.io/DCAT-AP/releases/3.0.1/shacl/dcat-ap-SHACL.ttl> ;
```

### Release Phase (releases/)
```turtle
@prefix : <https://w3id.org/mobilitydcat-ap/releases/1.1.0#> .

owl:imports <https://w3id.org/mobilitydcat-ap/releases/1.1.0/mobilitydcat-ap_v1.1.0.ttl> ;
owl:imports <https://semiceu.github.io/DCAT-AP/releases/3.0.1/shacl/dcat-ap-SHACL.ttl> ;
```

## Key Differences

| Aspect | Drafts | Releases |
|--------|--------|----------|
| **Base IRI** | `.../drafts/1.1.0-draft-0.1#` | `.../releases/1.1.0#` |
| **Vocabulary Import** | From `drafts/` | From `releases/` |
| **Status** | Under development | Stable/Published |
| **Shape IRIs** | `drafts/.../1.1.0-draft-0.1#Agent_Shape` | `releases/1.1.0#Agent_Shape` |

## Migration Checklist

When moving from draft to release:
- [ ] Update base prefix IRI
- [ ] Update vocabulary import path
- [ ] Update all shape IRIs
- [ ] Change `owl:versionInfo` from `"1.1.0-draft-0.1"` to `"1.1.0"`
- [ ] Update `adms:status` to `COMPLETED`