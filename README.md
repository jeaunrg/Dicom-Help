# DICOM HELP
A beginner's guide to understand the contents of DICOM files, enabling them to read, modify, and create them in compliance with DICOM standards.

## Intro
From my perspective, DICOM visualization tools are not easily understandable for humans, and tools for creating various types of DICOMs deserve straightforward explanations. I've spent too much time trying to grasp the metadata structure of DICOM files, so I hope this brief guide can assist you in understanding their workings more quickly.
Certainly, here is the translation while maintaining the formatting:

The examples you will see have been implemented using pydicom.

## Tools for Understanding DICOMs
Use the script `pretty_dcmdump.py` to see the structure of a dicom. Here is a sample:
```CS (0040, a491) CompletionFlag                                  COMPLETE
CS (0040, a493) VerificationFlag                                UNVERIFIED
CS (0040, a496) PreliminaryFlag                                 FINAL
SQ (0040, a504) ContentTemplateSequence(1)
CS (0008, 0105)         MappingResource                                 DCMR
UI (0008, 0118)         MappingResourceUID                              1.2.840.10008.8.1.1
CS (0040, db00)         TemplateIdentifier                              1500
SQ (0040, a730) ContentSequence(5)
1.1 -----------    1
CS (0040, a010)         RelationshipType                                HAS CONCEPT MOD
CS (0040, a040)         ValueType                                       CODE
SQ (0040, a043)         ConceptNameCodeSequence(1)
SH (0008, 0100)                 CodeValue                                       113011
SH (0008, 0102)                 CodingSchemeDesignator                          DCM
LO (0008, 0104)                 CodeMeaning                                     Document Title Modifier
SQ (0040, a168)         ConceptCodeSequence(1)
SH (0008, 0100)                 CodeValue                                       CHESTCT0304
SH (0008, 0102)                 CodingSchemeDesignator                          99SHSAIRC
LO (0008, 0104)                 CodeMeaning                                     AI-Rad CT Cardio
1.2 -----------    2
CS (0040, a010)         RelationshipType                                HAS CONCEPT MOD
CS (0040, a040)         ValueType                                       CODE
SQ (0040, a043)         ConceptNameCodeSequence(1)
SH (0008, 0100)                 CodeValue                                       121049
SH (0008, 0102)                 CodingSchemeDesignator                          DCM
LO (0008, 0104)                 CodeMeaning                                     Language of Content Item and Descendants
SQ (0040, a168)         ConceptCodeSequence(1)
SH (0008, 0100)                 CodeValue                                       eng
SH (0008, 0102)                 CodingSchemeDesignator                          RFC5646
LO (0008, 0104)                 CodeMeaning                                     English
SQ (0040, a730)         ContentSequence(1)```
```
### NEMA (DICOM Standards)
[https://dicom.nema.org/medical/dicom/current/output/chtml/part16/ps3.16.html](https://dicom.nema.org/medical/dicom/current/output/chtml/part16/ps3.16.html)
### Element Structures
- A DICOM object is referred to as a 'Dataset.' A Dataset is an object containing **Sequences** (which are simply lists of sub-Datasets) and 'Elements.' In the previous example, lines ending with "Sequence(n)" represent Sequences of n datasets, while the other lines are Elements.

- An **Element** has multiple attributes (as seen in the previous example):
  * Value representation, *e.g., LO*
  * Tag, *e.g., (0008, 0104)*
  * Description, *e.g., CodeMeaning*
  * Value, *e.g., English*

- A **Dataset** is typically more of a conceptual entity, and it is composed of these Elements:
  * RelationshipType, *describing the relationship with its parent Dataset, e.g., "HAS CONCEPT MOD"*
  * ValueType, *describing the type of value represented, e.g., "CODE"*
  * ConceptNameCodeSequence, *describing the name of the concept, e.g., (121049, DCM, Language of Content Item and Descendants)*
### Table Structures
### INNOLITICS (DICOM type browser)
[https://dicom.innolitics.com/ciods](https://dicom.innolitics.com/ciods)
# DCMTK
Dicom toolkit to generate, modify or validate your dicoms

## Different Types of DICOMs
### Base DICOM
### Secondary Capture
#### Multiframe
#### Image Compression
JPEG2000Lossless, JPEG2000, JPEGLSLossless, RLELossless
### Structured Report
According to NEMA TID 1501 standards
#### Qualitative Primitive
#### Measurement Primitive
#### Location Primitive
#### Location Primitive
### GSPS
### Encapsulated PDF



