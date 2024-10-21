# About The Global Value Factors Explorer Dataset

This repository presents a reformatted version of the IFVI Global Value Factors Database (GVFD), which converts environmental impacts, such as carbon emissions, into monetary values intended for use in financial analysis. 

The original data source was published by the International Foundation for Valuing Impacts (IFVI) in `XLSM` format in October of 2024 and is intended to provide guidance for organisations wishing to prepare financial accounts that integrate both financial and non-financial line items (this burgenonig field is commonly known as "impact accounting"). 

The (IFVI) Global Value Factor Database is intended for interpretation in conjunction with a set of methodology papers and documentation which are collectively available from their [official website](https://www.ifvi.org). Static versions of those living documents have been included here only for the purpose of data provenance and should neither be regarded as official nor authoritative representations of the IFVI's guidance.

This derivative dataset was assembled in recognition of the fact that expressing companies' impacts financially is part of a much broader societal movement towards placing companies' impacts front and center in how we, as societies, prioritise and define value creation. 

The GVFD was released by the IFVI with the following note:

*"To drive adoption of impact accounting and meet market needs as soon as possible, IFVI is making available four interim environmental methodologies, prior to completing an official methodology oversight process, including the VTPC Review and Due Process."*

This small effort to extend interest in the dataset is made in exactly that same spirit of pragmatism.  

## What are value factors?

"Value factors" convert quantity metrics (like tonnes of carbon dioxide emitted) into monetary terms. For convenience, the GVFD is standardised on the US dollar but is intended for global consideration regardless of the preparers' local currency. 

## What are these files?

The release of the GVFD upon which this derivative dataset is based (V1, October 2024) contains environmental value factors only. 

Purely for the purpose of organising this repository, land use and land conversion were divided into separate files. The GHGs file is unique in that it contains only value factor (GHG emissions, $236/tCO2). 

 The topics as developed by the IFVI - in partnership with the Value Balancing Alliance (VBA) - are:

 | Category                 | Description                                                                                                                              |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| **Air Pollution**         | Impacts from up to 6 possible air pollutants of companies on health, agricultural productivity, and other impacts.                       |
| **Land Use and Conversion**| Impacts on land occupied or converted by a company, covering the loss of ecosystem services in different locations and for different land use types. |
| **Waste**                 | Impacts from the mass of waste generated and disposed of by various methods (such as incineration and waste to landfill), including impacts on leachate, disamenity, climate change, and air pollution. |
| **Water Pollution**       | Impacts from 104 possible corporate water pollutants on human health and eutrophication.                                                 |

---

## Why source data is essential

In order to translate companies' impacts into monetary terms as impact accounting envisions, these value factors need to be paired with the matching datapoints for those same impacts. 

The context here is important. The IFVI and VBA released their Database with the intention of helping account preparers to use these factors in the preparation of "impact accounts". 

The value factors can also be applied externally, however, which is the use-case that this derivative dataset was designed to support ("externally" may mean researchers using public accounts to retrospectively apply these value factors to model what their monetary effects might have been according to the IFVI methodology).

In either case, a second dataset is required to make *this* data useful!

---

## Licensing

This repository contains a derivative work of the Global Value Factors Database (GVFD). Those wishing to use the source data for any downstream applications or commercial purposes should refer directly to the official database and its terms of use, which are available at IFVI.org. The terms provided there, not here, apply to any formal use of the data.

### Versioning

This repository reflects version 1 of the GVFD as released on October 15th. No warranty is offered, nor is any claim made, that this repository reflects the most current or up-to-date version of the GVFD. Users seeking the latest data should refer to the IFVI website for official releases and updates.

This repository strives to mirror the original GVFD release as closely and faithfully as possible. However, applying the database for preparing financial accounts or other official use requires utilizing the database in conjunction with the detailed user documentation, which is not provided in this repository.

### Intended Access

The purpose of this repository (rather) is to assist non-commercial users, such as academics and researchers, in analyzing and understanding the dataset for exploratory use-cases, such as seeking to understand the effects that monetising non-financial impacts would have on the financial performance of publicy-traded companies.

This derivative dataset is non-official and is not endorsed by the IFVI, nor has it been produced or undertaken on their behalf.

---

## Contents

This repository includes:
- **JSON Files**: Structured data representing value factors for various environmental impacts.
- **GeoJSON Files**: Geospatial data to allow for visualizing value factors across geographic regions.
- **Documentation**: Information on how to use and interpret the data.

---
 
## Data Structure

### JSON Files
Each JSON file provides:
- **Value factors** for specific environmental impacts, including emissions, resource use, and waste.
- **Monetary rates** associated with each factor (e.g., cost per tonne of CO2 emissions).
- **Timestamps** and data versioning information where applicable.

### GeoJSON Files
 
 Coming soon

 
## Example Use Cases

- **Visualizing regional CO2 emissions**: Use the GeoJSON files to map emissions per region, alongside the monetary value assigned to these impacts.
- **Incorporating environmental impacts into financial reports**: Use the JSON data to programmatically integrate the value factors into corporate sustainability accounting models.
- **Developing dashboards**: Build interactive visualizations that display environmental impacts and their financial equivalents over time and across regions.

----

## Source Data

### IFVI GVFD V1

The source data for the Global Value Factor Database (in `Source-Data`) was gathered, with consent, from the website of the International Foundation for Valuing Impacts (IFVI), ifvi.org between 21-22 October 2024.

---

## Author (Source Database / GVFD)

The International Foundation for Valuing Impacts (IFVI)

## Author (Repository / Derivative Dataset)

Daniel Rosehill  
(public at danielrosehill dot com)