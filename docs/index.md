# IFVI Value Factors - Derivative Dataset For Analysis

[![Visit Website](https://img.shields.io/badge/Visit%20Website-blue)](https://gvfd-analysis.bydanielrosehill.com/)

This repository is a derivative of the IFVI Global Value Factors Database (GVFD), which converts environmental impacts, such as carbon emissions, into monetary values intended for use in financial analysis. The objective of this repository is to share a version of that database in CSV, JSON and GeoJSON formats to assist those interested in exploring how impact accounting can reshape how we account for value.

The original data source was published by the International Foundation for Valuing Impacts (IFVI) in October of 2024 and is intended to provide guidance for organisations wishing to prepare financial accounts that integrate both financial and non-financial line items. The value factors included in these files are intended to be paired with quantity metrics. The hoped-for result is that companies' financial health will be viewed holistically from a worldview of planetary good.

## Using This Data

The IFVI Data is intended for interpretation in conjunction with a set of methodology papers and documentation which are collectively available from their [official website](https://www.ifvi.org). Static versions of those living documents have been included here only for the purpose of data provenance and should neither be regarded as official nor authoritative representations of the IFVI's guidance.

This derivative dataset was assembled in recognition of the fact that expressing companies' impacts financially is part of a much broader societal movement towards placing companies' impacts front and center in how we, as societies, prioritise and define value creation. 

The GVFD was released by the IFVI with the following note:

*"To drive adoption of impact accounting and meet market needs as soon as possible, IFVI is making available four interim environmental methodologies, prior to completing an official methodology oversight process, including the VTPC Review and Due Process."*
 
 ---

## What are value factors?

"Value factors" convert quantity metrics (like tonnes of carbon dioxide emitted) into monetary terms. For convenience, the GVFD is standardised on the US dollar but is intended for global consideration regardless of the preparers' local currency. 

## What are these files?

The release of the GVFD upon which this derivative dataset is based (V1, October 2024) contains environmental value factors only. 

 The topics as developed by the IFVI - in partnership with the Value Balancing Alliance (VBA) - are:

 | Category                 | Description                                                                                                                              |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| **Air Pollution**         | Impacts from up to 6 possible air pollutants of companies on health, agricultural productivity, and other impacts.                       |
| **Land Use and Conversion**| Impacts on land occupied or converted by a company, covering the loss of ecosystem services in different locations and for different land use types. |
| **Waste**                 | Impacts from the mass of waste generated and disposed of by various methods (such as incineration and waste to landfill), including impacts on leachate, disamenity, climate change, and air pollution. |
| **Water Pollution**       | Impacts from 104 possible corporate water pollutants on human health and eutrophication.                                                 |

---
 
 ## Licensing

The derivative dataset in this repository is subject to the same terms of use of the original database, available as `license.md` at the repository root. 

### Versioning

This repository reflects version 1 of the GVFD as released on October 15th. No warranty is offered, nor is any claim made, that this repository reflects the most current or up-to-date version of the GVFD. Users seeking the latest data should refer to the IFVI website for official releases and updates.

This repository strives to mirror the original GVFD release as closely and faithfully as possible. However, applying the database for preparing financial accounts or other official use requires utilizing the database in conjunction with the detailed user documentation, which is not provided in this repository.

 ---

 ## Data Formatting

 The source data has been reformatted and reshaped to hopefully provide useful material for a few different analytical perspectives. These are listed below:
 
| **Format**                  | **Description**                                                                                                                                                                                               |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **By Methodology**           | This format contains the database in JSON arrays, organized to reflect the parameters in the methodologies.                                                                                                   |
| **By Methodology, By Country** | This format closely mirrors the source database, with the exception of land use and land conversion, which were split into two files to keep the tables separate.                                             |
| **By Territory**             | This folder organizes the data from a geographical perspective, by continent, territory, and US state. US states appear in one methodology. The JSON files aggregate data from various methodology tabs. |

Additional resources are:

- The data in CSV format.
- The metadata folder contains non-data items like notes that appeared on the corresponding tabs of the original Database. The files are named accordingly.

## Data Modifications

No material changes were made to the source data and all the files shared here represent best-effort attempts at reshaping and reformatting the data purely for analytical purposes.

Two sets of non-material changes were made and are noted in the changelog:

- The US dollar sign was stripped throughout to facilitate defining these values as integers in database systems. 
- The names of 12 countries were edited from their sovereign versions into more vernacular equivalents to support more reader-friendly visualistion. As an example, `Bahamas, The` was edited to `Bahamas`. To disambiguate similar names and avoid any confusion, all territories were also mapped onto their ISO-3166 Alpha-2 values.

## Author (Source Database / GVFD)

The International Foundation for Valuing Impacts (IFVI)

## Author (Repository / Derivative Dataset)

Daniel Rosehill  
(public at danielrosehill dot com)