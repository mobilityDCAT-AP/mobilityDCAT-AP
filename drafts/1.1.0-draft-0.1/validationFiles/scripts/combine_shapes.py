#!/usr/bin/env python3
"""
Combine individual SHACL shape files into a single comprehensive file.
"""

import os
from pathlib import Path
from datetime import date
import json

# Get the script's directory and navigate to project root
SCRIPT_DIR = Path(__file__).parent.resolve()
PROJECT_ROOT = SCRIPT_DIR.parent  # Go up one level from scripts/

# Configuration - now relative to project root
SHAPES_DIR = PROJECT_ROOT / "shapes"
OUTPUT_FILE = PROJECT_ROOT / "mobilitydcat-ap_shacl_shapes.ttl"

# METADATA_TEMPLATE and VOCABULARIES_FOOTER stay the same...
METADATA_TEMPLATE = """@prefix : <https://w3id.org/mobilitydcat-ap#> .
@prefix mobilitydcatap: <https://w3id.org/mobilitydcat-ap#> .
@prefix adms: <http://www.w3.org/ns/adms#> .
@prefix bibo: <http://purl.org/ontology/bibo/> .
@prefix cnt: <http://www.w3.org/2011/content#> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcatap: <http://data.europa.eu/r5r/> .
@prefix dct: <http://purl.org/dc/terms/> .
@prefix dqv: <http://www.w3.org/ns/dqv#> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix org: <http://www.w3.org/ns/org#> .
@prefix locn: <http://www.w3.org/ns/locn#> .
@prefix vcard: <http://www.w3.org/2006/vcard/ns#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix spdx: <http://spdx.org/rdf/terms#> .


<https://w3id.org/mobilitydcat-ap#> a owl:Ontology , adms:Asset ;
  owl:imports <https://raw.githubusercontent.com/SEMICeu/DCAT-AP/master/releases/2.0.1/dcat-ap_2.0.1_shacl_shapes.ttl> ;
  owl:imports <https://raw.githubusercontent.com/SEMICeu/DCAT-AP/master/releases/2.0.1/dcat-ap_2.0.1_shacl_deprecateduris.ttl> ;
  owl:imports <https://raw.githubusercontent.com/SEMICeu/DCAT-AP/master/releases/2.0.1/dcat-ap_2.0.1_shacl_mdr-vocabularies.shape.ttl> ;
  owl:imports <https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/1.1.0/serialisationFiles/mobilitydcat-ap.ttl> ;
  owl:imports <http://www.w3.org/ns/dqv.ttl> ;
  owl:imports <http://inspire.ec.europa.eu/metadata-codelist/SpatialDataServiceCategory/SpatialDataServiceCategory.en.rdf> ;
  owl:imports <http://inspire.ec.europa.eu/metadata-codelist/ConditionsApplyingToAccessAndUse/ConditionsApplyingToAccessAndUse.en.rdf> ;
  owl:imports <http://inspire.ec.europa.eu/metadata-codelist/DegreeOfConformity/DegreeOfConformity.en.rdf> ;
  owl:imports <http://inspire.ec.europa.eu/metadata-codelist/PriorityDataset/PriorityDataset.en.rdf> ;
  owl:imports <http://inspire.ec.europa.eu/metadata-codelist/ProtocolValue/ProtocolValue.en.rdf> ;
  owl:imports <http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess/LimitationsOnPublicAccess.en.rdf> ;
  owl:imports <http://inspire.ec.europa.eu/metadata-codelist/OnLineDescriptionCode/OnLineDescriptionCode.en.rdf> ;
  owl:imports <http://inspire.ec.europa.eu/metadata-codelist/QualityOfServiceCriteria/QualityOfServiceCriteria.en.rdf> ;
  owl:imports <http://inspire.ec.europa.eu/metadata-codelist/ResourceType/ResourceType.en.rdf> ;
  owl:imports <http://inspire.ec.europa.eu/metadata-codelist/ResponsiblePartyRole/ResponsiblePartyRole.en.rdf> ;
  owl:imports <http://inspire.ec.europa.eu/metadata-codelist/SpatialDataServiceType/SpatialDataServiceType.en.rdf> ;
  owl:imports <http://inspire.ec.europa.eu/metadata-codelist/SpatialScope/SpatialScope.en.rdf> ;
  owl:imports <http://inspire.ec.europa.eu/metadata-codelist/TopicCategory/TopicCategory.en.rdf> ;
  owl:versionIRI <http://w3id.org/mobilityDCAT-AP/releases/1.1.0/> ;
  adms:status <http://publications.europa.eu/resource/dataset/dataset-status/COMPLETED> ;
  dcatap:availability dcatap:stable ;
  dct:conformsTo <https://www.w3.org/TR/shacl> ;
  rdfs:isDefinedBy <https://w3id.org/mobilitydcat-ap/releases/1.1.0/> ;
  dct:license <https://creativecommons.org/licenses/by/4.0> ;
  dct:created "2023-08-14"^^xsd:date ;
  dct:issued "2023-08-14"^^xsd:date ;
  dct:modified "{modified_date}"^^xsd:date ;
  dct:dateCopyrighted "2023"^^xsd:gYear ;
  dct:title "The constraints of mobilityDCAT-AP Application Profile for Data Portals in Europe"@en ;
  owl:versionInfo "1.1.0" ;
  dct:description "This document specifies the constraints on properties and classes expressed by mobilityDCAT-AP in SHACL."@en ;
  bibo:editor [
    a foaf:Person ;
    owl:sameAs <https://lina-molinas-comet.name/foaf/#me>;
    owl:sameAs <https://orcid.org/0000-0001-5446-6947> ;
    foaf:name "Lina Molinas Comet"
  ] ;
  bibo:editor [
    a foaf:Person ;
    owl:sameAs <https://github.com/Daham-Mustaf>;
    owl:sameAs <https://orcid.org/0000-0003-1867-4428> ;
    foaf:name "Daham Mustafa"
  ] ;
  dct:creator [ a foaf:Group ;
      foaf:name "NAPCORE SWG 4.4" ;
      foaf:page <https://github.com/mobilityDCAT-AP/mobilityDCAT-AP> ] ;
      dct:publisher <https://napcore.eu/> ;
      dct:rightsHolder <https://napcore.eu/> ;
      dcat:distribution [ a adms:AssetDistribution ;
      dct:format <http://publications.europa.eu/resource/authority/file-type/RDF_TURTLE>,
      <http://www.w3.org/ns/formats/data/Turtle> ;
      dct:title "SHACL (Turtle)"@en ;
      dcat:downloadURL <http://w3id.org/mobilitydcat-ap/releases/1.1.0/serialisationFiles/mobilitydcat-ap.shacl.ttl> ;
      dcat:mediaType "text/turtle"^^dct:IMT
  ] ;
  .

#-------------------------------------------------------------------------
# The shapes in this file complement the DCAT-AP ones to cover all classes
# in mobilityDCAT-AP 1.1.0.
#-------------------------------------------------------------------------

"""

VOCABULARIES_FOOTER = """
#-------------------------------------------------------------------------
# Concepts from controlled vocabularies defined and used in mobilityDCAT-AP.
#-------------------------------------------------------------------------
<https://w3id.org/mobilitydcat-ap/application-layer-protocol> a skos:ConceptScheme ;
  skos:prefLabel "Application layer protocol"@en ;
.
<https://w3id.org/mobilitydcat-ap/communication-method> a skos:ConceptScheme ;
  skos:prefLabel "Communication method"@en ;
.
<https://w3id.org/mobilitydcat-ap/conditions-for-access-and-usage> a skos:ConceptScheme ;
  skos:prefLabel "Conditions for access and usage"@en ;
.
<https://w3id.org/mobilitydcat-ap/mobility-theme> a skos:ConceptScheme ;
  skos:prefLabel "Mobility Theme"@en ;
.
<https://w3id.org/mobilitydcat-ap/mobility-data-standard> a skos:ConceptScheme ;
  skos:prefLabel "Mobility Data Standard"@en ;
.
<https://w3id.org/mobilitydcat-ap/georeferencing-method> a skos:ConceptScheme ;
  skos:prefLabel "Georeferencing Method"@en ;
.
<https://w3id.org/mobilitydcat-ap/grammar> a skos:ConceptScheme ;
  skos:prefLabel "Grammar"@en ;
.
<https://w3id.org/mobilitydcat-ap/network-coverage> a skos:ConceptScheme ;
  skos:prefLabel "Network coverage"@en ;
.
<https://w3id.org/mobilitydcat-ap/intended-information-service> a skos:ConceptScheme ;
  skos:prefLabel "Intended Information Service"@en ;
 .
<https://w3id.org/mobilitydcat-ap/transport-mode> a skos:ConceptScheme ;
  skos:prefLabel "Transport mode"@en ;
.
<https://w3id.org/mobilitydcat-ap/update-frequency> a skos:ConceptScheme ;
  skos:prefLabel "Update frequency"@en ;
.
#-------------------------------------------------------------------------
# Concepts from additional controlled vocabularies used in mobilityDCAT-AP.
#-------------------------------------------------------------------------
<http://publications.europa.eu/resource/authority/data-theme> a skos:ConceptScheme ;
  skos:prefLabel "Data Themes"@en ;
.
<http://publications.europa.eu/resource/authority/data-theme> a skos:ConceptScheme ;
  skos:prefLabel "Dataset Theme Vocabulary"@en ;
.
<http://publications.europa.eu/resource/authority/access-right> a skos:ConceptScheme ;
  skos:prefLabel "Access right"@en ;
.
<http://publications.europa.eu/resource/authority/frequency> a skos:ConceptScheme ;
  skos:prefLabel "Frequency"@en ;
.
<http://www.opengis.net/def/crs/EPSG/0/> a skos:ConceptScheme ;
  skos:prefLabel "OGC EPSG Coordinate Reference Systems Register"@en ;
.
<http://publications.europa.eu/resource/authority/file-type> a skos:ConceptScheme ;
  skos:prefLabel "File Type"@en ;
.
<http://publications.europa.eu/resource/authority/language> a skos:ConceptScheme ;
  skos:prefLabel "Language"@en ;
.
<http://publications.europa.eu/resource/authority/corporate-body> a skos:ConceptScheme ;
  skos:prefLabel "Corporate body"@en ;
.
<http://publications.europa.eu/resource/authority/continent> a skos:ConceptScheme ;
  skos:prefLabel "Continents"@en ;
.
<http://publications.europa.eu/resource/authority/country> a skos:ConceptScheme ;
  skos:prefLabel "Countries"@en ;
.
<http://publications.europa.eu/resource/authority/place> a skos:ConceptScheme ;
  skos:prefLabel "Places"@en ;
.
<http://sws.geonames.org/> a skos:ConceptScheme ;
  skos:prefLabel "GeoNames"@en ;
.
<http://nuts.geovocab.org/> a skos:ConceptScheme;
  skos:prefLabel "NUTS (Nomenclature of Territorial Units for Statistics)"@en ;
.
<http://purl.org/adms/publishertype/> a skos:ConceptScheme ;
  skos:prefLabel "ADMS publisher type"@en ;
.
<https://eur-lex.europa.eu/eli-register/eu_publications_office.html> a skos:ConceptScheme ;
  skos:prefLabel "European Legislation Identifier (ELI)"@en ;
.
"""

def generate_statistics(shape_files):
    """Generate statistics about shapes and save to JSON."""
    
    stats = {
        "generation_date": date.today().isoformat(),
        "total_shapes": len(shape_files),
        "shapes": []
    }
    
    for shape_file in shape_files:
        with open(shape_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Count properties
        mandatory_props = content.count("sh:minCount 1")
        properties = content.count("sh:property [")
        
        # Extract shape name
        shape_name = shape_file.stem.replace('_shape', '').replace('_', ' ').title()
        
        shape_info = {
            "file_name": shape_file.name,
            "shape_name": shape_name,
            "total_properties": properties,
            "mandatory_properties": mandatory_props,
            "file_size_bytes": shape_file.stat().st_size
        }
        
        stats["shapes"].append(shape_info)
    
    # Save to JSON
    # Save to JSON in shapes/ directory
    stats_file = SHAPES_DIR / "shapes_statistics.json"
    with open(stats_file, 'w', encoding='utf-8') as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)
    
    print(f"\nStatistics saved to '{stats_file}'")
    return stats

def extract_shape_content(file_path):
    """Extract shape content from a file, removing prefix declarations."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove prefix declarations (lines starting with @prefix)
    lines = content.split('\n')
    shape_lines = []
    in_shape = False
    
    for line in lines:
        stripped = line.strip()
        # Skip empty lines at the start
        if not stripped and not in_shape:
            continue
        # Skip prefix declarations
        if stripped.startswith('@prefix'):
            continue
        # Start collecting after prefixes
        in_shape = True
        shape_lines.append(line)
    
    return '\n'.join(shape_lines).strip()


def combine_shapes():
    """Combine all shape files into one comprehensive file."""
    
    # DEBUG: Print all paths
    print("=" * 60)
    print("DEBUG INFORMATION:")
    print("=" * 60)
    print(f"Script file: {Path(__file__)}")
    print(f"Script directory: {SCRIPT_DIR}")
    print(f"Project root: {PROJECT_ROOT}")
    print(f"Shapes directory: {SHAPES_DIR}")
    print(f"Output file: {OUTPUT_FILE}")
    print(f"Shapes dir exists? {SHAPES_DIR.exists()}")
    print(f"Current working directory: {Path.cwd()}")
    print("=" * 60)
    print()
    
    if not SHAPES_DIR.exists():
        print(f"Error: Directory '{SHAPES_DIR}' does not exist!")
        print(f"\nContents of PROJECT_ROOT ({PROJECT_ROOT}):")
        if PROJECT_ROOT.exists():
            for item in PROJECT_ROOT.iterdir():
                print(f"  - {item.name}{'/' if item.is_dir() else ''}")
        return False
    
    # Get all .ttl files from shapes directory
    shape_files = sorted(SHAPES_DIR.glob("*_shape.ttl"))
    
    if not shape_files:
        print(f"Error: No shape files found in '{SHAPES_DIR}'!")
        return False
    # Generate statistics
    stats = generate_statistics(shape_files)
    
    print(f"Found {len(shape_files)} shape files:")
    for f in shape_files:
        print(f"  - {f.name}")
    
    # Start building the combined file
    today = date.today().isoformat()
    combined_content = METADATA_TEMPLATE.format(modified_date=today)
    
    # Add each shape
    for shape_file in shape_files:
        print(f"Processing {shape_file.name}...")
        shape_content = extract_shape_content(shape_file)
        combined_content += f"\n{shape_content}\n"
    
    # Add vocabularies footer
    combined_content += VOCABULARIES_FOOTER
    
    # Write to output file
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(combined_content)
    
    print(f"\n✓ Successfully combined {len(shape_files)} shapes into '{OUTPUT_FILE}'")
    return True


if __name__ == "__main__":
    success = combine_shapes()
    exit(0 if success else 1)