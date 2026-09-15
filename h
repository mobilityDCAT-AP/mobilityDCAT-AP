[1mdiff --git a/drafts/latest/mobilitydcat-ap.jsonld b/drafts/latest/mobilitydcat-ap.jsonld[m
[1mindex 95ccacb..8a723ed 100644[m
[1m--- a/drafts/latest/mobilitydcat-ap.jsonld[m
[1m+++ b/drafts/latest/mobilitydcat-ap.jsonld[m
[36m@@ -3141,7 +3141,7 @@[m
   }, {[m
     "@id" : "https://www.w3.org/TR/vocab-org/#org:Organization"[m
   }, {[m
[31m-    "@id" : "https://www.w3.org/ns/org#Organization"[m
[32m+[m[32m    "@id" : "http://www.w3.org/ns/org#Organization"[m
   } ],[m
   "http://www.w3.org/2003/06/sw-vocab-status/ns#term_status" : [ {[m
     "@value" : "stable"[m
[1mdiff --git a/drafts/latest/mobilitydcat-ap.rdf b/drafts/latest/mobilitydcat-ap.rdf[m
[1mindex 5a99a9f..d5e80d0 100644[m
[1m--- a/drafts/latest/mobilitydcat-ap.rdf[m
[1m+++ b/drafts/latest/mobilitydcat-ap.rdf[m
[36m@@ -3534,7 +3534,7 @@[m
     This specification does not impose any additional requirements to properties for this entity.</rdfs:comment>[m
         <rdfs:seeAlso rdf:resource="https://semiceu.github.io/GeoDCAT-AP/releases/3.0.0/#Organisation"/>[m
         <rdfs:seeAlso rdf:resource="https://www.w3.org/TR/vocab-org/#org:Organization"/>[m
[31m-        <rdfs:seeAlso rdf:resource="https://www.w3.org/ns/org#Organization"/>[m
[32m+[m[32m        <rdfs:seeAlso rdf:resource="http://www.w3.org/ns/org#Organization"/>[m
         <vs:term_status>stable</vs:term_status>[m
     </rdf:Description>[m
     <rdf:Description rdf:about="http://www.w3.org/ns/org#memberOf">[m
[1mdiff --git a/drafts/latest/mobilitydcat-ap.ttl b/drafts/latest/mobilitydcat-ap.ttl[m
[1mindex 8ddea7b..1df824b 100644[m
[1m--- a/drafts/latest/mobilitydcat-ap.ttl[m
[1m+++ b/drafts/latest/mobilitydcat-ap.ttl[m
[36m@@ -522,7 +522,7 @@[m [mdct:MediaTypeOrExtent rdf:type owl:Class ;[m
                 <https://semiceu.github.io/GeoDCAT-AP/releases/3.0.0/#MediaTypeorExtent> ,[m
                 <https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/3.0.0/#distribution-format> .[m
 [m
[31m-### https://www.w3.org/ns/org#Organization[m
[32m+[m[32m### http://www.w3.org/ns/org#Organization[m
 org:Organization rdf:type owl:Class ;[m
     rdfs:comment """Represents a collection of people organized together into a community or other social, commercial or political structure. The group has some common purpose or reason for existence which goes beyond the set of people belonging to it and can act as an Agent. Organizations are often decomposable into hierarchical structures.[m
     See Organization in The Organization Ontology.[m
[36m@@ -530,7 +530,7 @@[m [morg:Organization rdf:type owl:Class ;[m
     This specification does not impose any additional requirements to properties for this entity."""@en ;[m
     vs:term_status "stable" ;[m
     adms:status <http://publications.europa.eu/resource/dataset/concept-status/CURRENT> ;[m
[31m-    rdfs:seeAlso <https://www.w3.org/ns/org#Organization> ,[m
[32m+[m[32m    rdfs:seeAlso <http://www.w3.org/ns/org#Organization> ,[m
                 <https://semiceu.github.io/GeoDCAT-AP/releases/3.0.0/#Organisation> ,[m
                 <https://www.w3.org/TR/vocab-org/#org:Organization> .[m
 [m
[1mdiff --git a/drafts/latest/tables/class-organisation.html b/drafts/latest/tables/class-organisation.html[m
[1mindex 7b9bdd2..35bea6b 100644[m
[1m--- a/drafts/latest/tables/class-organisation.html[m
[1m+++ b/drafts/latest/tables/class-organisation.html[m
[36m@@ -9,7 +9,7 @@[m
 <tr>[m
 <th>URI</th>[m
 <td>[m
[31m-<p><a href="https://www.w3.org/ns/org#Organization"><code>org:Organization</code></a></p>[m
[32m+[m[32m<p><a href="http://www.w3.org/ns/org#Organization"><code>org:Organization</code></a></p>[m
 </td></tr>[m
 <tr>[m
 <th>References</th>[m
[1mdiff --git a/drafts/latest/tables/namespaces.html b/drafts/latest/tables/namespaces.html[m
[1mindex da657d1..e96cf4f 100644[m
[1m--- a/drafts/latest/tables/namespaces.html[m
[1m+++ b/drafts/latest/tables/namespaces.html[m
[36m@@ -65,12 +65,12 @@[m
 <tr>[m
 <tr>[m
 <td><code>oa</code></td>[m
[31m-<td><code>https://www.w3.org/ns/oa#</code></td>[m
[32m+[m[32m<td><code>http://www.w3.org/ns/oa#</code></td>[m
 <td>[[WEB-ANNOTATION-ONTOLOGY]]</td>[m
 </tr>[m
 <tr>[m
 <td><code>org</code></td>[m
[31m-<td><code>https://www.w3.org/ns/org#</code></td>[m
[32m+[m[32m<td><code>http://www.w3.org/ns/org#</code></td>[m
 <td>[[CORE-ORGANIZATION-ONTOLOGY]]</td>[m
 </tr>[m
 <tr>[m
