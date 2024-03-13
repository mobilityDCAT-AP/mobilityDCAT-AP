var respecConfig = {
//	preProcess: [dfn_index],
//    logos: [
//    {
////      src: './images/eu-isa-programme.png',
//      src: "./images/eu-isa2-programme.jpg",
////      url: 'https://ec.europa.eu/isa',
//      url: "https://ec.europa.eu/isa2",
////      alt: "EU ISA Programme",
////      title: "EU ISA Programme",
//      alt: "EU ISA² Programme",
//      title: "EU ISA² Programme",
//      width: 150,
////      height: 42,
//      id: 'logo-eu-isa-programme',
//    }
//    ],
//    includePermalinks: true,
    addSectionLinks: true,
    maxTocLevel: 3,
    doJsonLd: true,
    noRecTrack: false,
    subtitle: "A mobility extension for the DCAT application profile for data portals in Europe",
    logos: [
        {
        src: 'https://mobilitydcat-ap.github.io/respec-style/logos/mobilitydcat-ap.png',
        width: 250,
        height: 140,
        alt: "mobilitydcat-ap logo"
  }
      ],
//    copyrightHolder: "European Union",
//    copyrightURL: "https://europa.eu/",
    copyrightStart: 2023,
    publishDate: "2024-03-13",

    alternateFormats: [
/*
    {
      label: "PDF (TBD)",
      uri: "./geodcat-ap_v2.0.0.pdf",
    },
    {
      label: "DOCX (TBD)",
      uri: "./geodcat-ap_v2.0.0.docx",
    },
    {
      label: "ODT (TBD)",
      uri: "./geodcat-ap_v2.0.0.odt",
    },
*/
    {
      label: "RDF/XML",
      uri: "./mobilitydcat-ap.rdf",
    },
    {
      label: "Turtle",
      uri: "./mobilitydcat-ap.ttl",
    },
    {
      label: "JSON-LD",
      uri: "./mobilitydcat-ap.jsonld",
    },
    {
       label: "SHACL (Turtle)",
       uri: "./mobilitydcat-ap_shacl_shapes.ttl",
    }
    ],
//    implementationReportURI:"https://joinup.ec.europa.eu/document/geodcat-ap-implementations",
    errata:"https://github.com/mobilityDCAT-AP/mobilityDCAT-AP/issues?q=is%3Aissue+label%3Aerrata",
//    specStatus: "unofficial",
    specStatus: "ED",
//    specStatus: "FPWD",
//    specStatus: "WD",
//    specStatus: "LC",
//    specStatus: "PR",
//    specStatus: "RE",
//    crEnd:"2020-10-12",
//    prEnd:"2020-12-23",
    shortName: "mobility-ap",
    canonicalURI: "https://w3id.org/mobilitydcat-ap/drafts/latest/",
//    canonicalURI: "https://semiceu.github.io/GeoDCAT-AP/drafts/2.0.0-draft-0.1/",
//    canonicalURI: "https://semiceu.github.io/GeoDCAT-AP/releases/2.0.0/",
//    canonicalURI: "https://semiceu.github.io/GeoDCAT-AP/releases/",
//    prevRecURI: "https://joinup.ec.europa.eu/release/geodcat-ap/101",
//    prevRecURI: "https://semiceu.github.io/GeoDCAT-AP/releases/1.0.1/",
    prevRecURI: "https://w3id.org/mobilitydcat-ap/releases/1.0.0/",
//    previousPublishDate:  "2016-08-02",
//    previousMaturity:     "final",
//    previousURI:          "https://joinup.ec.europa.eu/release/geodcat-ap/101",
/* MOBILITYDCAT-AP specific - start */
//    thisVersionURI:       "https://semiceu.github.io/GeoDCAT-AP/drafts/latest/",
//    thisVersionURI:       "https://semiceu.github.io/GeoDCAT-AP/drafts/2.0.0-draft-0.1/",
    thisVersionURI:       "https://w3id.org/mobilitydcat-ap/releases/1.0.0/",
//    prevVersionURI:       "https://semiceu.github.io/GeoDCAT-AP/drafts/latest/",
    prevVersionURI:       "https://w3id.org/mobilitydcat-ap/drafts/1.0.0-draft-0.1/",
//    latestVersionURI:     "https://semiceu.github.io/GeoDCAT-AP/releases/2.0.0/",
    latestVersionURI:     "https://w3id.org/mobilitydcat-ap/releases/",
/* MOBILITYDCAT-AP specific - end   */
    edDraftURI:           "https://w3id.org/mobilitydcat-ap/drafts/latest/",
    issueBase:            "https://github.com/mobilityDCAT-AP/mobilityDCAT-AP/issues/",
    github:               "https://github.com/mobilityDCAT-AP/mobilityDCAT-AP",
    editors: [
      {
        name:    "Lina Molinas Comet",
        company: "Fraunhofer Institute for Applied Information Technology FIT",
        orcid:   "0000-0001-5446-6947",
//        companyURL: ""
      },
      {
        name: "Peter Lubrich",
        company: "Federal Highway Research Institute (BASt)",
        orcid: "0000-0002-0023-1234",
//        companyURL: ""
      },
      {
        name: "Mario Scrocca",
        company: "Cefriel",
        orcid: "0000-0002-8235-7331",
//        companyURL: ""
      }

    ],
    authors: [
    {
      name: "NAPCORE Sub-Working Group (SWG) 4.4",
      url: "https://github.com/mobilityDCAT-AP/",
      company: "NAPCORE (National Access Point Coordination Organisation for Europe) Organization",
      companyURL: "https://napcore.eu/"
    },
    ],
    otherLinks: [
    {
      key: "Document status",
      data: [
      {
//        value: "Under development"
        value: "Completed"
      }
      ]
    },
    {
      key: "Document version",
      data: [
      {
//        value: "0.2"
        value: "1.0.1"
      }
      ]
    },
  ],

//    {
//      key: "Reviewed by",
//      data: [
//      {
//        value: "Someone (Some Organization)",
//        href: "https://ec.europa.eu/"
//      },
//      {
//        value: "Someone Else (Some Organization)",
//        href: "https://ec.europa.eu/"
//      },
//      ]
//    },
//    {
//     key: "Approved by",
//      data: [
//      {
//        value: "Someone (Some Organization)",
//        href: "https://ec.europa.eu/"
//      },
//      {
//        value: "Someone Else (Some Organization)",
//        href: "https://ec.europa.eu/"
//      },
//      ]
//    }

//    ],
    wg: "NAPCORE Sub-Working Group (SWG) 4.4",
    wgURI: "https://github.com/mobilityDCAT-AP/",
//    wgURI: "https://joinup.ec.europa.eu/solution/geodcat-ap",
//    wgPublicList: "",
//    wgPatentURI: "",
    inlineCSS: "true",
    lint: "false",
    localBiblio: {
      "ADMS-SKOS":{
        "href":"https://raw.githubusercontent.com/SEMICeu/ADMS-AP/master/purl.org/ADMS_SKOS_v1.00.rdf",
        "title":"Joinup. ADMS Controlled Vocabularies",
        "publisher":"European Commission",
//        "date":"2016"
      },
      "DCAT-AP-DA":{
        "href":"http://data.europa.eu/r5r/availability/",
        "title":"DCAT-AP Distribution Availability Vocabulary",
        "publisher":"European Commission",
      },
      "DCAT-AP-EG":{
        "href":"https://joinup.ec.europa.eu/release/dcat-ap-how-extend-dcat-ap",
        "title":"Joinup. DCAT-AP Implementation Guidelines: How to extend DCAT-AP?",
        "publisher":"European Commission",
      },
      "CiteDCAT-AP": {
        "href": "https://ec-jrc.github.io/datacite-to-dcat-ap/",
        "title": "DataCite to DCAT-AP Mapping",
        "authors": ["Andrea Perego","Timothy Austin"],
        "status": "Working Draft",
        "publisher":"European Commission, Joint Research Centre (JRC)",
        "date": "2019"
      },
      "CNT":{
        "href":"https://www.w3.org/TR/Content-in-RDF/",
        "title":"Representing Content in RDF",
        "date":"2 February 2017",
      },
      "CORE-LOCATION-VOCABULARY":{
        "href":"https://www.w3.org/TR/Content-in-RDF/",
        "title":"ISA Programme Location Core Vocabulary",
        "author":["EU ISA Programme Core Vocabularies Working Group (Location Task Force)"],
        "date":"23 March 2015",
      },
      "LOCN-MAPPING": {
        "href": "https://semiceu.github.io/locn-mapping/",
        "title": "LOCN mappings to vCard and Schema.org",
        "authors": ["Andrea Perego"],
        "status": "Working Draft",
        "publisher":"European Commission, Joint Research Centre (JRC)",
        "date": "2019"
      },
      "CLD-FREQ": {
        "href":"http://dublincore.org/groups/collections/frequency/",
        "title":"Dublin Core Collection Description Frequency Vocabulary",
        "authors":["Dublin Core Collection Description Task Group"],
        "publisher":"Dublin Core Metadata Initiative",
        "date":"9 March 2007"
      },
      "DataCite2RDF": {
        "href":"https://doi.org/10.6084/m9.figshare.2075356",
        "title":"DataCite2RDF: Mapping DataCite Metadata Schema 3.1 Terms to RDF. Version 3.3",
        "authors":["Silvio Peroni","David Shotton","Jan Ashton","Amy Barton","Egbert Gramsbergen","Marie-Christine Jacquemot"],
        "date":"2016"
      },
      "DC2AP": {
        "href":"https://groups.google.com/a/datacite.org/group/dc2map/attach/624ec3cd533a3/DataCite%20Dublin%20Core%20AP%20-%20Draft%201_8.pdf",
        "title":"DataCite Dublin Core Application Profile (DC2AP). Version 1.8",
        "authors":["DataCite Metadata Working Group"],
        "date":"3 February 2016"
      },

      "DCAT-AP-v2.0.1":{
        "href":"https://joinup.ec.europa.eu/collection/semantic-interoperability-community-semic/solution/dcat-application-profile-data-portals-europe/release/201-0",
        "title":"DCAT Application Profile for data portals in Europe. Version 2.0.1.",
        "publisher":"European Commission",
        "date":"08 June 2020"
       },

      "DCAT-AP-v2.1.0-Guideline-Dataservices":{
        "href":"https://github.com/SEMICeu/DCAT-AP/blob/2.1.0-draft/releases/2.1.0/usageguide-dataset-distribution-dataservice.md",
        "title":"DCAT-AP Usage guide on Datasets, Distributions and Data Services",
        "publisher":"European Commission"
       },

      "DCAT-AP-SDO": {
        "href": "https://ec-jrc.github.io/dcat-ap-to-schema-org/",
        "title": "DCAT-AP to Schema.org Mapping",
        "authors": ["Andrea Perego"],
        "status": "Working Draft",
        "publisher":"European Commission, Joint Research Centre (JRC)",
        "date": "2019"
      },
      "DCAT-AP-IG":{
        "href":"https://joinup.ec.europa.eu/solution/dcat-application-profile-implementation-guidelines",
        "title":"Joinup. DCAT application profile implementation guidelines",
        "publisher":"European Commission",
//        "date":"2016"
      },

      "DCAT-AP-HVD": {
        "href":"https://semiceu.github.io/DCAT-AP/releases/2.2.0-hvd/",
        "title":"Usage guidelines of DCAT-AP for High-Value Datasets",
        "publisher":"European Commission",
        "date":"19 June 2023"
      },



    "DC-UG-PM": {
        "href":"https://www.dublincore.org/resources/userguide/publishing_metadata/",
        "title":"Dublin Core™ User Guide: Publishing Metadata",
        "authors":["Stefanie Rühle","Tom Baker","Pete Johnston"],
        "publisher":"Dublin Core Metadata Initiative",
//        "date":"9 March 2007"
      },

      "ELI": {
        "href":"https://eur-lex.europa.eu/eli-register/eu_publications_office.html",
        "title":"European Legislation Identifier (ELI) system",
        "publisher":"EU Publications Office"
      },

      "EPRINTS-AR": {
        "href":"http://purl.org/eprint/accessRights/",
        "title":"Eprints AccessRights Vocabulary Encoding Scheme",
        "date":"14 May 2008"
      },
      "EPSG-RDF":{
        "href":"https://github.com/semiceu/epsg-to-rdf/",
        "title":"Proof of concept for the RDF representation of the OGC EPSG register of coordinate reference systems",
//        "authors":["Andrea Perego"],
        "publisher":"European Commission",
//        "date":"2015"
       },
      "EU-OD-DIR": {
        "href":"http://data.europa.eu/eli/dir/2019/1024/oj",
        "title":"Directive (EU) 2019/1024 of the European Parliament and of the Council of 20 June 2019 on open data and the re-use of public sector information",
        "publisher":"OJ L 172",
        "date":"20 June 2019"
      },
      "EU-EIP-CMC": {
        "href":"https://www.its-platform.eu/achievement/monitoring-harmonisation-of-naps/",
        "title":"Information about the Coordinated Metadata Catalogue (CMC) by EU EIP",
        "publisher":"EU EIP Consortium"
      },
      "EU-EIP-QP": {
        "href":"https://www.its-platform.eu/achievement/quality-of-european-its-services-and-their-data/",
        "title":"Information about the Quality Frameworks by EU EIP",
        "publisher":"EU EIP Consortium"
      },
      "EC-ITS-Directive": {
        "href":"https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32010L0040",
        "title":"Directive 2010/40/EU of the European Parliament and of the Council of 7 July 2010 on the framework for the deployment of Intelligent Transport Systems in the field of road transport and for interfaces with other modes of transport Text with EEA relevance",
        "publisher":"European Commission"
      },
      "EC-MMTIS-DR": {
        "href":"https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX%3A32017R1926",
        "title":"Commission Delegated Regulation (EU) 2017/1926 of 31 May 2017 supplementing Directive 2010/40/EU of the European Parliament and of the Council with regard to the provision of EU-wide multimodal travel information services (Text with EEA relevance.)",
        "publisher":"European Commission"
      },
      "EU-TEN-T": {
        "href":"https://transport.ec.europa.eu/transport-themes/infrastructure-and-investment/trans-european-transport-network-ten-t_en",
        "title":"Information about Trans-European Transport Network (TEN-T)",
        "publisher":"European Commission"
      },
      "EU-REPO-AR": {
        "href":"https://wiki.surfnet.nl/display/standards/info-eu-repo#info-eu-repo-AccessRights",
        "title":"EU-Repo: Access Rights",
        "date":"17 April 2018"
      },
      "FAIR" : {
        "title":"The FAIR Guiding Principles for scientific data management and stewardship",
        "authors":["Mark D. Wilkinson"],
        "etAl": true,
        "status":"Scientific Data, vol. 3, Article nr. 160018",
        "publisher":"Nature",
        "href":"https://doi.org/10.1038/sdata.2016.18"
      },
      "FRAPO": {
        "href":"http://purl.org/cerif/frapo",
        "title":"FRAPO, the Funding, Research Administration and Projects Ontology",
        "authors":["David Shotton"],
        "publisher":"SPAR Ontologies",
        "status":"Namespace Document",
        "date":"4 September 2017"
      },
      "FRBR": {
        "href":"http://purl.org/vocab/frbr/core#",
        "title":"Expression of Core FRBR Concepts in RDF",
        "authors":["Ian Davis","Richard Newman"],
        "publisher":"Vocab.org",
        "status":"Namespace Document",
        "date":"2005"
      },

      "GEODCAT-AP-v2.0.0":{
        "href":"https://semiceu.github.io/GeoDCAT-AP/releases/",
        "title":"GeoDCAT-AP - Version 2.0.0",
        "publisher":"European Commission",
        "date":"23 December 2020"
      },

      "GeoDCAT-ACV":{
        "href":"https://joinup.ec.europa.eu/node/148245/",
        "title":"Joinup. GeoDCAT-AP: Alignment of controlled vocabularies",
//        "authors":["Andrea Perego"],
        "publisher":"European Commission",
//        "date":"2015"
       },
      "GeoDCAT-XSLT":{
        "href":"https://github.com/semiceu/iso-19139-to-dcat-ap/",
        "title":"Reference XSLT-based implementation of GeoDCAT-AP",
//        "authors":["Andrea Perego"],
        "publisher":"European Commission",
//        "date":"2015"
       },
      "GEOHASH":{
        "href":"http://en.wikipedia.org/wiki/Geohash",
        "title":"Geohash",
        "publisher":"Wikipedia"
       },
      "GEOHASH-36":{
        "href":"http://en.wikipedia.org/wiki/Geohash-36",
        "title":"Geohash-36",
        "publisher":"Wikipedia"
       },
      "GEOJSON":{
        "href":"http://geojson.org/geojson-spec.html",
        "title":"The GeoJSON Format Specification",
        "authors":["Howard Butler","Martin Daly","Allan Doyle","Sean Gillies","Tim Schaub","Christopher Schmidt"],
        "date":"16 June 2008"
      },
      "GEONAMES":{
        "href":"http://geonames.org/",
        "title":"Geonames"
       },
      "iiWAS17-JRC": {
        "href": "https://doi.org/10.1145/3151759.3151810",
        "title": "The JRC multidisciplinary research data infrastructure",
        "authors": ["Anders Friis-Christensen"],
        "etAl": true,
        "publisher":"19th International Conference on Information Integration and Web-based Applications & Services (iiWAS'17). Salzburg, Austria, 4-6 Dec 2017 ",
        "date": "2017"
      },
      "INSPIRE-CAU": {
        "href":"http://inspire.ec.europa.eu/metadata-codelist/ConditionsApplyingToAccessAndUse",
        "title":"INSPIRE Registry: Conditions applying to access and use",
        "publisher":"European Commission"
      },
      "INSPIRE-DC": {
        "href":"https://inspire.ec.europa.eu/reports/ImplementingRules/metadata/MD_IR_and_DC_state%20of%20progress.pdf",
        "title":"State of progress in the development of guidelines to express elements of the INSPIRE metadata implementing rules using ISO 15836 (Dublin core)",
//        "authors":["European Commission"],
        "publisher":"European Commission",
        "date":"6 May 2008"
      },
      "INSPIRE-DCAT": {
        "href":"https://ies-svn.jrc.ec.europa.eu/projects/metadata/wiki/Alignment_of_INSPIRE_metadata_with_DCAT-AP",
        "title":"Alignment of INSPIRE metadata with DCAT-AP",
//        "authors":["European Commission"],
        "publisher":"European Commission",
        "date":"2014"
      },
      "INSPIRE-DIR": {
        "href":"http://data.europa.eu/eli/dir/2007/2/oj",
        "title":"DIRECTIVE 2007/2/EC OF THE EUROPEAN PARLIAMENT AND OF THE COUNCIL of 14 March 2007 establishing an Infrastructure for Spatial Information in the European Community (INSPIRE)",
        "publisher":"OJ L 108",
        "date":"25 April 2007"
      },
      "INSPIRE-GLOSSARY": {
        "href":"http://inspire.ec.europa.eu/glossary",
        "title":"INSPIRE Glossary",
        "publisher":"European Commission"
      },
      "INSPIRE-SDSS-REG": {
        "href":"http://data.europa.eu/eli/reg/2010/1089",
        "title":"Commission Regulation (EU) No 1089/2010 of 23 November 2010 implementing Directive 2007/2/EC of the European Parliament and of the Council as regards interoperability of spatial data sets and services",
        "publisher":"OJ L 323",
        "date":"8 December 2010"
      },
      "INSPIRE-LPA": {
        "href":"http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess",
        "title":"INSPIRE Registry: Limitations on public access",
        "publisher":"European Commission"
      },
      "INSPIRE-MD-REG": {
        "href":"http://data.europa.eu/eli/reg/2008/1205",
        "title":"Commission Regulation (EC) No 1205/2008 of 3 December 2008 implementing Directive 2007/2/EC of the European Parliament and of the Council as regards metadata",
        "publisher":"OJ L 326",
        "date":"4 December 2008"
      },
      "INSPIRE-MT": {
        "href":"http://inspire.ec.europa.eu/media-types",
        "title":"INSPIRE Media Type Register",
//        "authors":["European Commission"],
        "publisher":"European Commission",
        "date":"7 November 2011"
      },
      "INSPIRE-PV": {
        "href":"https://inspire.ec.europa.eu/metadata-codelist/ProtocolValue",
        "title":"INSPIRE Registry: Protocol values",
        "publisher":"European Commission"
      },
      "INSPIRE-DS": {
        "href":"https://inspire.ec.europa.eu/documents/Network_Services/TechnicalGuidance_DiscoveryServices_v3.1.pdf",
        "title":"Technical Guidance for the implementation of INSPIRE Discovery Services. Version 3.1",
//        "authors":["European Commission"],
        "publisher":"European Commission",
        "date":"7 November 2011"
      },
      "INSPIRE-DoC": {
        "href":"http://inspire.ec.europa.eu/metadata-codelist/DegreeOfConformity",
        "title":"INSPIRE Registry: Degrees of conformity",
        "publisher":"European Commission"
      },
      "INSPIRE-MF": {
        "href":"http://inspire.ec.europa.eu/metadata-codelist/MaintenanceFrequency",
        "title":"INSPIRE Registry: Maintenance Frequency",
        "publisher":"European Commission"
      },
      "INSPIRE-RPR": {
        "href":"http://inspire.ec.europa.eu/metadata-codelist/ResponsiblePartyRole",
        "title":"INSPIRE Registry: Responsible party roles",
        "publisher":"European Commission"
      },
      "INSPIRE-SDSC": {
        "href":"http://inspire.ec.europa.eu/metadata-codelist/SpatialDataServiceCategory",
        "title":"INSPIRE Registry: Classification of spatial data services",
        "publisher":"European Commission"
      },
      "INSPIRE-SRT": {
        "href":"http://inspire.ec.europa.eu/metadata-codelist/SpatialRepresentationType",
        "title":"INSPIRE Registry: Spatial Representation Types",
        "publisher":"European Commission"
      },
      "INSPIRE-THEMES": {
        "href":"http://inspire.ec.europa.eu/theme",
        "title":"INSPIRE Registry: INSPIRE themes",
        "publisher":"European Commission"
      },
      "INSPIRE-TC": {
        "href":"http://inspire.ec.europa.eu/metadata-codelist/TopicCategory",
        "title":"INSPIRE Registry: Topic categories in accordance with EN ISO 19115",
        "publisher":"European Commission"
      },
      "INSPIRE-SDST": {
        "href":"http://inspire.ec.europa.eu/metadata-codelist/SpatialDataServiceType",
        "title":"INSPIRE Registry: Spatial data service types",
        "publisher":"European Commission"
      },
      "INSPIRE-RPR": {
        "href":"http://inspire.ec.europa.eu/metadata-codelist/ResponsiblePartyRole",
        "title":"INSPIRE Registry: Responsible party roles",
        "publisher":"European Commission"
      },
      "INSPIRE-RT": {
        "href":"http://inspire.ec.europa.eu/metadata-codelist/ResourceType",
        "title":"INSPIRE Registry: Resource types",
        "publisher":"European Commission"
      },
      "OGC-EPSG": {
        "href":"http://www.opengis.net/def/crs/EPSG/",
        "title":"EPSG CRS Register",
        "publisher":"OGC"
      },
      "ISO-8061": {
        "authors": [
            "ISO/TC 154"
        ],
        "href": "https://www.iso.org/standard/40874.html",
        "title": "Data elements and interchange formats -- Information interchange -- Representation of dates and times",
        "publisher": "ISO",
        "status": "International Standard",
        "date": "2004",
        "isoNumber": "ISO 8061:2004"
      },
      "JRC-DP": {
        "href": "https://doi.org/10.2788/607378",
        "title": "JRC Data Policy",
        "authors": ["Catherine Doldirina"],
        "etAl": true,
        "publisher":"Publications Office of the European Union",
        "date": "2015"
      },
      "KML": {
        "href": "http://www.opengeospatial.org/standards/kml",
        "title": "OGC KML 2.3",
        "authors": ["David Burggraf"],
        "publisher":"OGC",
//        "status":"OGC® Implementation Standard",
        "date": "4 August 2015"
      },
      "LD-BOOK": {
        "href":"http://linkeddatabook.com/",
        "title":"Linked Data: Evolving the Web into a Global Data Space",
        "authors":["Tom Heath","Christian Bizer"],
        "publisher":"Morgan & Claypool",
        "date":"2011"
      },
      "LINK-PROP":{
        "href":"https://github.com/OSGeo/Cat-Interop/blob/master/LinkPropertyLookupTable.csv",
        "title":"Link properties",
        "publisher":"OSGeo"
      },

      "NAPCORE":{
        "href":"https://napcore.eu/",
        "title":"Website of the NAPCORE project",
        "publisher":"NAPCORE Consortium"
      },

      "NAPCORE-Metadata-preparatory-activities":{
        "href":"https://napcore.eu/providing-a-baseline-for-a-new-metadata-scheme-for-european-naps/",
        "title":"Documentation about preparatory activities for mobilityDCAT-AP",
        "publisher":"NAPCORE Consortium"
      },

      "NAPCORE-Metadata-Working-Group":{
        "href":"https://napcore.eu/metadata/",
        "title":"Information about the NAPCORE Sub-Working Group on Metadata",
        "publisher":"NAPCORE Consortium"
      },

      "NAPCORE-NAPs":{
        "href":"https://napcore.eu/description-naps/",
        "title":"NAPCORE information about National Access Points (NAPs)",
        "publisher":"NAPCORE Consortium"
      },

      "NAPCORE-NB":{
        "href":"https://napcore.eu/national-bodies/",
        "title":"NAPCORE information about National Bodies (NAPs)",
        "publisher":"NAPCORE Consortium"
      },

      "NUTS-CODES":{
        "href":"http://nuts.geovocab.org/",
        "title":"EU NUTS classification as Linked Data",
        "publisher":"NUTS-RDF project"
      },

      "EUV-AR":{
        "href":"https://publications.europa.eu/en/web/eu-vocabularies/at-dataset/-/resource/dataset/access-right",
        "title":"Named Authority List: Access rights",
        "publisher":"Publications Office of the European Union"
       },
      "EUV-CB":{
        "href":"https://publications.europa.eu/en/web/eu-vocabularies/at-dataset/-/resource/dataset/corporate-body",
        "title":"Named Authority List: Corporate bodies",
        "publisher":"Publications Office of the European Union"
       },
      "EUV-CONT":{
        "href":"https://publications.europa.eu/en/web/eu-vocabularies/at-dataset/-/resource/dataset/continent",
        "title":"Named Authority List: Continents",
        "publisher":"Publications Office of the European Union"
       },
      "EUV-COUNTRIES":{
        "href":"https://publications.europa.eu/en/web/eu-vocabularies/at-dataset/-/resource/dataset/country",
        "title":"Named Authority List: Countries",
        "publisher":"Publications Office of the European Union"
       },
      "EUV-DS":{
        "href":"https://publications.europa.eu/en/web/eu-vocabularies/at-dataset/-/resource/dataset/dataset-status",
        "title":"Named Authority List: Dataset statuses",
        "publisher":"Publications Office of the European Union"
       },
      "EUV-DT":{
        "href":"https://publications.europa.eu/en/web/eu-vocabularies/at-dataset/-/resource/dataset/distribution-type",
        "title":"Named Authority List: Distribution types",
        "publisher":"Publications Office of the European Union"
       },
      "EUV-EUROVOC":{
        "href":"https://publications.europa.eu/en/web/eu-vocabularies/th-dataset/-/resource/dataset/eurovoc",
        "title":"EuroVoc",
        "publisher":"Publications Office of the European Union"
       },
      "EUV-FREQ":{
        "href":"https://publications.europa.eu/en/web/eu-vocabularies/at-dataset/-/resource/dataset/frequency",
        "title":"Named Authority List: Frequencies",
        "publisher":"Publications Office of the European Union"
       },
      "EUV-FT":{
        "href":"https://publications.europa.eu/en/web/eu-vocabularies/at-dataset/-/resource/dataset/file-type",
        "title":"Named Authority List: File types",
        "publisher":"Publications Office of the European Union"
       },
      "EUV-LANG":{
        "href":"https://publications.europa.eu/en/web/eu-vocabularies/at-dataset/-/resource/dataset/language",
        "title":"Named Authority List: Languages",
        "publisher":"Publications Office of the European Union"
       },
      "EUV-LICENCES":{
        "href":"https://publications.europa.eu/en/web/eu-vocabularies/at-dataset/-/resource/dataset/licence",
        "title":"Named Authority List: Licences",
        "publisher":"Publications Office of the European Union"
       },
      "EUV-PLACES":{
        "href":"https://publications.europa.eu/en/web/eu-vocabularies/at-dataset/-/resource/dataset/place",
        "title":"Named Authority List: Places",
        "publisher":"Publications Office of the European Union"
       },
      "EUV-ROLES":{
        "href":"https://publications.europa.eu/en/web/eu-vocabularies/at-dataset/-/resource/dataset/role",
        "title":"Named Authority List: Roles",
        "publisher":"Publications Office of the European Union"
       },
      "EUV-THEMES-TRANSPORT":{
        "href":"https://op.europa.eu/en/web/eu-vocabularies/concept/-/resource?uri=http://publications.europa.eu/resource/authority/data-theme/TRAN",
        "title":"Named Authority List: Data Themes - Label: Transport ",
        "publisher":"Publications Office of the European Union"
       },
       "EUV-THEMES":{
        "href":"https://publications.europa.eu/en/web/eu-vocabularies/at-dataset/-/resource/dataset/data-theme",
        "title":"Named Authority List: Data Themes",
        "publisher":"Publications Office of the European Union"
       },
      "NEOGEO": {
        "href": "http://geovocab.org/doc/neogeo/",
        "title": "NeoGeo Vocabulary Specification - Madrid Edition",
        "authors": ["Juan Martín Salas","Andreas Harth"],
        "publisher":"GeoVocab.org",
        "date": "25 February 2012"
      },

      "Web-Annotation-Data-Model": {
        "href": "https://www.w3.org/TR/annotation-model/",
        "title": "Web Annotation Data Model",
        "publisher":"W3C",
        "date": "23 February 2017"
      },
      "OpenSearch": {
         "authors": [
           "DeWitt Clinton"
         ],
         "href":"https://github.com/dewitt/opensearch/blob/master/opensearch-1-1-draft-6.md",
         "title":"OpenSearch 1.1 Draft 6",
         "date":"17 April 2018",
         "publisher":"OpenSearch"
      },
      "SCHEMA-ORG":{
        "href":"http://schema.org/",
        "title":"Schema.org"
      },
      "SEMVER":{
        "href":"https://semver.org/",
        "title":"Semantic Versioning Specification (SemVer)"
      },
      "SCoRO": {
        "href":"http://purl.org/spar/scoro#",
        "title":"Scholarly Contributions and Roles Ontology (SCoRO)",
        "authors":["David Shotton","Silvio Peroni"],
        "publisher":"SPAR Ontologies",
        "status":"Namespace Document",
        "date":"2017"
      },
      "SDMX":{
        "href":"https://sdmx.org/",
        "title":"Statistical Data and Metadata eXchange (SDMX)",
        "publisher":"SDMX"
      },
      "SDSVoc16-27": {
        "href": "https://www.w3.org/2016/11/sdsvoc/SDSVoc16_paper_27",
        "title": "Using DCAT-AP for research data",
        "authors": ["Andrea Perego"],
        "etAl": true,
        "publisher":"Smart Descriptions & Smarter Vocabularies (SDSVoc). Amsterdam, 30 Nov - 1 Dec 2016",
        "date": "2016"
      },
      "SPDX":{
        "href":"http://spdx.org/rdf/terms#",
        "title":"SPDX 2.2",
        "publisher":"SPDX"
      },
      "ISA":{
        "href":"https://ec.europa.eu/isa/",
        "title":"Interoperability Solutions for European Public Administrations (ISA)",
        "publisher":"European Commission"
       },
      "ISA2":{
        "href":"https://ec.europa.eu/isa2/",
        "title":"Interoperability solutions for public administrations, businesses and citizens (ISA²)",
        "publisher":"European Commission"
       },
      "SEMIC":{
        "href":"https://ec.europa.eu/isa2/actions/improving-semantic-interoperability-european-egovernment-systems_en",
        "title":"Interoperability solutions for public administrations, businesses and citizens (ISA²). Improving semantic interoperability in European eGovernment systems",
        "publisher":"European Commission"
       },
       "DCAT-AP-guideline-spatial":{
        "href":"https://joinup.ec.europa.eu/release/how-should-dctspatial-and-dctlocation-be-used",
        "title":"How should dct:spatial and dct:Location be used?",
        "publisher":"European Commission"
       },
      "DXWG":{
        "href":"https://www.w3.org/2017/dxwg/",
        "title":"Dataset Exchange Working Group (DXWG)",
        "publisher":"W3C"
       },
      "GLD":{
        "href":"https://www.w3.org/2011/gld/",
        "title":"Government Linked Data (GLD) Working Group",
        "publisher":"W3C"
       },
      "VOCAB-DCAT-QA": {
        "title":"Data Catalog Vocabulary (DCAT) - Version 2. Section 13.1",
        "href":"https://www.w3.org/TR/vocab-dcat-2/#qualified-attribution",
        "publisher":"W3C"
      },
      "DataCite-Types": {
        "href":"https://schema.datacite.org/meta/kernel-3/doc/DataCite-MetadataKernel_v3.1.pdf",
        "title":"DataCite Metadata Schema for the Publication and Citation of Research Data, version 3.1. Appendix 1, table 5",
        "publisher":"DataCite"
      },
      "CLDR": {
        "href":"http://unicode.org/cldr/trac/browser/trunk/common/bcp47/transform_mt.xml",
        "title":"CLDR - Unicode Common Locale Data Repository. BCP47, transform_mt.xml",
        "publisher":"UNICODE Consortium"
      },
      "CONNEG": {
        "href":"http://httpd.apache.org/docs/current/content-negotiation.html",
        "title":"Apache Web Server: content negotiation",
        "publisher":"Apache Foundation"
      },
      "ODRS": {
        "authors": ["Leigh Dodds"],
        "href":"http://schema.theodi.org/odrs",
        "title":"Open Data Rights Statement Vocabulary",
        "date":"29 July 2013",
        "publisher":"ODI"
      },

      "MAST-ADS": {
        "href":"http://archive.stsci.edu/pub_dsn.html",
        "title":"Referencing Data Sets in Astronomical Literature",
        "publisher":"Mikulski Archive for Space Telescopes (MAST)"
      },
      "DOI": {
        "href":"http://www.doi.org/",
        "title":"Digital Object Identifier",
        "publisher":"DOI"
      },
      "EZID": {
        "href":"http://n2t.net/ezid",
        "title":"EZID"
      },
      "W3ID": {
        "href":"https://w3id.org/",
        "title":"Permanent Identifiers for the Web",
        "publisher":"W3C Permanent Identifier Community Group"
      },
      "DataCite-RIS": {
        "href":"http://purl.org/spar/datacite/ResourceIdentifierScheme",
        "title":"DataCite Resource Identifier Scheme"
      },
      "ADMS": {
        "href":"https://joinup.ec.europa.eu/solution/asset-description-metadata-schema-adms",
        "title":"Joinup. Asset Description Metadata Schema (ADMS)",
        "publisher":"European Commission"
      },


      "CORE-ORGANIZATION-ONTOLOGY": {
        "href":"https://www.w3.org/TR/vocab-org/",
        "title":"Core organization ontology",
        "date":"16 January 2014"
      },
      "WEB-ANOTATION-ONTOLOGY": {
        "href":"https://www.w3.org/TR/annotation-vocab/",
        "title":"Web Annotation Ontology",
        "date":"23 February 2017",
      }

    }
  };
