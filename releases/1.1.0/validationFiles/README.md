# mobilityDCAT-AP SHACL

MobilityDCAT uses the [SHACL Shapes Constraint Language](https://www.w3.org/TR/shacl/) to encode the constraints to which datasets must adhere in order to be MobilityDCAT-compliant. 
This folder contains the [SHACL shapes file](mobilitydcat-ap_shacl_shapes.ttl) as well as some `*_examples.ttl`-files that illustrate what both valid and invalid data look like.

## Running an automated validation (Docker)

The `.docker` folder contains the necessary resources to build an image containing a basic validation setup using [pySHACL](https://github.com/RDFLib/pySHACL). 

Building the validation image:
```bash
docker build -f ./.docker/shacl-validation.Dockerfile -t mobilitydcat-shacl-validator .
```

Running a validation. This example validates the Belgian NAP catalog dataset.
```bash
docker run mobilitydcat-shacl-validator "https://transportdata.be/catalog.ttl" > shacl_validation_report.ttl
```

