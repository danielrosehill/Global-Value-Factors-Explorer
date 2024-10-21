# Global Value Factors Explorer

This repository presents a modified version of the IFVI Global Value Factors Database, which converts environmental impacts, such as carbon emissions, into monetary values that can be used in financial analysis. 

The data is provided in **JSON** and **GeoJSON** formats to facilitate easier programmatic intake for use in data analysis and visualization applications and use-cases. 

Note that this is a derivative work and has not been published or produced by or on behalf of the IFVI.

## Licensing

This repository contains a derivative work of the Global Value Factors Database (GVFD). Those wishing to use the source data for any downstream applications or commercial purposes should refer directly to the official database and its terms of use, which are available at IFVI.org. The terms provided there, not here, apply to any formal use of the data.

This repository reflects version 1 of the GVFD as released on October 15th. No warranty is offered, nor is any claim made, that this repository reflects the most current or up-to-date version of the GVFD. Users seeking the latest data should refer to the IFVI website for official releases and updates.

This repository strives to mirror the original GVFD release as closely and faithfully as possible. However, applying the database for preparing financial accounts or other official use requires utilizing the database in conjunction with the detailed user documentation, which is not provided in this repository.

The purpose of this repository (rather) is to assist non-commercial users, such as academics and researchers, in analyzing and understanding the dataset for exploratory use-cases, such as seeking to understand the effects that monetising non-financial impacts would have on the financial performance of publicy-traded companies.

This derivative dataset is non-official and is not endorsed by the IFVI, nor has it been produced or undertaken on their behalf.

## Contents

This repository includes:
- **JSON Files**: Structured data representing value factors for various environmental impacts.
- **GeoJSON Files**: Geospatial data to allow for visualizing value factors across geographic regions.
- **Documentation**: Information on how to use and interpret the data.

## Background

The **IFVI (International Foundation for Valuing Impacts)** developed the Global Value Factors Database (GVFD) to quantify environmental impacts in monetary terms. 

This dataset enables businesses to measure their environmental footprint and integrate it into financial reporting. For example, one of the value factors assigns a rate of **$236 per tonne of CO2 emitted**, translating carbon emissions into a financial value.

This repository provides version one of the original **XLSM format** provided by the IFVI into **JSON** and **GeoJSON** . 

These formats are designed for easier use in programmatic workflows, such as:
- **Data analysis**
- **Visualization** in mapping software or dashboards
- **Financial modeling** that incorporates environmental impacts

## Data Structure

### JSON Files
Each JSON file provides:
- **Value factors** for specific environmental impacts, including emissions, resource use, and waste.
- **Monetary rates** associated with each factor (e.g., cost per tonne of CO2 emissions).
- **Timestamps** and data versioning information where applicable.

### GeoJSON Files
The GeoJSON files contain:
- **Geographical data** that can be used to map value factors to specific regions or countries.
- **Attributes** like regional identifiers and the relevant value factor for the impact being measured.

## How to Use

1. **Download the data**: Clone or download the repository and navigate to the relevant **JSON** or **GeoJSON** files.
2. **Data integration**: The files are formatted for easy integration into analytics platforms, GIS tools, or any codebase that handles JSON or GeoJSON.
3. **Analysis and visualization**: Import the data into tools like **Python (pandas, geopandas)**, **QGIS**, or **D3.js** to analyze or visualize the environmental impacts.

## Example Use Cases

- **Visualizing regional CO2 emissions**: Use the GeoJSON files to map emissions per region, alongside the monetary value assigned to these impacts.
- **Incorporating environmental impacts into financial reports**: Use the JSON data to programmatically integrate the value factors into corporate sustainability accounting models.
- **Developing dashboards**: Build interactive visualizations that display environmental impacts and their financial equivalents over time and across regions.

---

## Author (Source Database / GVFD)

The International Foundation for Valuing Impacts (IFVI)

## Author (Repository / Derivative Dataset)

Daniel Rosehill  
(public at danielrosehill dot com)