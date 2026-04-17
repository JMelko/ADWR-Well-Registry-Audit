# ADWR Well Registry Audit: Pima County

## Project Objective
To establish a reproducible Data Quality Assurance / Quality Control (QA/QC) workflow for legacy groundwater infrastructure data. This project serves as the foundation for regional spatial analysis of groundwater compliance in the Southwest.

## Data Source
* **Agency:** Arizona Department of Water Resources (ADWR)
* **Dataset:** Wells 55 Registry (Open Data Portal)
* **Scope:** Filtered geographically to Pima County (Tucson AMA region) to manage compute load and establish a regional baseline.

## QA/QC Methodology
Raw tabular data provided by regulatory agencies often contains inconsistencies from legacy drill logs. The following cleaning operations were performed prior to database ingestion:
1. **Spatial Integrity:** Removed records lacking valid Latitude/Longitude coordinates (critical for subsequent GIS routing).
2. **Type Casting Constraints:** Cleaned the `WELL_DEPTH` column, removing non-numeric string characters (e.g., "unknown", "approx") to ensure strict numeric data types for future SQL database insertion.

## Tech Stack
* **Data Manipulation:** Google Sheets
* **Version Control:** Git / GitHub