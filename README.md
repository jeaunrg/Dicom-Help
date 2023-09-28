# DICOM HELP
A beginner's guide to understand the contents of DICOM files, enabling them to read, modify, and create them in compliance with DICOM standards.

## Intro
From my perspective, DICOM visualization tools are not easily understandable for humans, and tools for creating various types of DICOMs deserve straightforward explanations. I've spent too much time trying to grasp the metadata structure of DICOM files, so I hope this brief guide can assist you in understanding their workings more quickly.
Certainly, here is the translation while maintaining the formatting:

The examples you will see have been implemented using pydicom.
(
## Tools for Understanding DICOMs
### NEMA (DICOM Standards)
[https://dicom.nema.org/medical/dicom/current/output/chtml/part16/ps3.16.html](https://dicom.nema.org/medical/dicom/current/output/chtml/part16/ps3.16.html)
### Element Structures
- A DICOM is referred to as a 'Dataset' in pydicom. A Dataset is an object containing 'Elements' and 'Sequences,' which are simply lists of sub-Datasets.
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



