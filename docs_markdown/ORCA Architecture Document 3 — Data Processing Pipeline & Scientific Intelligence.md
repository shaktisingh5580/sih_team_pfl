# ORCA Architecture Document 3 — Data Processing Pipeline & Scientific Intelligence

**Project:** ORCA — Marine EcOsystem Reasoning with Collaborative Agents  
**Problem Statement ID:** 26176  
**Organization:** ISRO / Department of Space  
**Document:** Data Processing Pipeline, Scientific Intelligence, Marine State & Visualization  
**Status:** Planning Phase — Architecture Design  
**Date:** 22 September 2026 (Updated: 26 September 2026)  
**PS Alignment:** This document covers the scientific data foundation — the engine underneath ORCA's agentic investigation loop. The PS requires autonomous data discovery, multi-source correlation, and evidence-grounded decisions. This pipeline makes that possible by turning heterogeneous marine data into trustworthy, aligned scientific information that the agentic brain can reason over.

---

# 0. The Core Technical Identity of ORCA

> **ORCA takes heterogeneous marine data, turns it into clean and aligned scientific information, lets the LLM decide what evidence and analysis are needed, runs deterministic marine computations, builds a Marine State, and then turns the result into an interactive map, charts, explanation and decision.**

That is the strongest technical story — not "ORCA has many agents."

> [!IMPORTANT]
> **Relationship to the Agentic Loop:** This pipeline is the DATA FOUNDATION. The agentic investigation loop (ASK → UNDERSTAND → PLAN → DISCOVER → EXECUTE → CORRELATE → OBSERVE → REPLAN → DECIDE → EXPLAIN) runs ABOVE this foundation. Every agent tool call eventually touches this pipeline to get trustworthy data. The pipeline is essential infrastructure, but the product is the investigation loop.

The judges need to understand:

```text
DATA → PROCESSING → LLM → SCIENTIFIC COMPUTATION → CORRELATION → VISUALIZATION → DECISION
```

before anything else.

---

# 1. The Master Pipeline

```text
USER
  │
  ▼
NATURAL LANGUAGE QUERY
  │
  ▼
LLM: INTENT + CONTEXT
  │
  ▼
DATA REQUIREMENT PLAN
  │
  ▼
┌────────────────────────────┐
│ DATA DISCOVERY & RETRIEVAL │
└────────────────────────────┘
  │
  ┌──────────────┼──────────────┐
  ▼              ▼              ▼
INCOIS         MOSDAC          IMD
Ocean data     Satellite EO    Weather/Hazard
  │              │              │
  └──────────────┼──────────────┘
                 ▼
         SOURCE CONNECTORS
                 │
                 ▼
           RAW DATA STORE
                 │
                 ▼
          DATA VALIDATION
                 │
                 ▼
          NORMALIZATION
                 │
                 ▼
  SPATIAL + TEMPORAL ALIGNMENT
                 │
                 ▼
      DERIVED DATA / FEATURES
                 │
                 ▼
     SCIENTIFIC DATA QUERY
                 │
         ┌───────┼───────┐
         ▼       ▼       ▼
       OCEAN   WEATHER  GEO/RISK
       ENGINE  ENGINE   ENGINE
         └───────┼───────┘
                 ▼
    MULTI-SOURCE CORRELATION
                 │
                 ▼
           MARINE STATE
                 │
                 ▼
       EVIDENCE + DECISION
                 │
         ┌───────┼───────┐
         ▼       ▼       ▼
        CHAT    MAP    CHARTS
                 │
                 ▼
              ALERTS
```

And running across the middle:

```text
PLAN → SELECT → ACT → OBSERVE → VALIDATE → REPLAN
```

---

# 2. The Three Planes

This is the cleanest way to present the architecture.

```text
┌─────────────────────────────────────────────────────────────────┐
│                        DATA PLANE                               │
│                                                                 │
│  Sources → Connectors → Raw → Validation → Normalization       │
│  → Spatial/Temporal Alignment → Derived Data                    │
│  → Scientific Storage → Query API                               │
└────────────────────────────────┬────────────────────────────────┘
                                 │
┌────────────────────────────────▼────────────────────────────────┐
│                    INTELLIGENCE PLANE                            │
│                                                                 │
│  User Query → LLM → Intent → Planner → Agents                  │
│  → Scientific Engines → Marine State → Decision → Evidence      │
└────────────────────────────────┬────────────────────────────────┘
                                 │
┌────────────────────────────────▼────────────────────────────────┐
│                    PRESENTATION PLANE                            │
│                                                                 │
│  Evidence / Results → Visualization Adapter                     │
│  → Chat + Map + Charts + Alerts                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Everything before Marine State** is about getting trustworthy information.
**Everything after Marine State** is about deciding what the information means.

---

# 3. The Most Important Distinction: Data Acquisition ≠ Data Processing

A lot of projects will say:

> "We collect satellite data and feed it to an LLM."

That is not enough. ORCA shows two different pipelines.

## A. Data Acquisition

```text
What data exists?
      ↓
Which dataset is relevant?
      ↓
Which provider?
      ↓
Is it available?
      ↓
What subset is required?
      ↓
How do we retrieve it?
```

## B. Data Processing

```text
What did we retrieve?
      ↓
Is it valid?
      ↓
What does each field mean?
      ↓
Can different sources be compared?
      ↓
Are units compatible?
      ↓
Are locations aligned?
      ↓
Are times aligned?
      ↓
What can be derived?
      ↓
What does the combined state show?
```

Discovery asks: **"What data should ORCA use?"**
Retrieval asks: **"How should ORCA obtain it correctly?"**
Processing asks: **"How should ORCA make it scientifically usable?"**

---

# 4. Data Acquisition: How ORCA Actually Gets the Data

The source layer should not look like a pile of APIs. It should be:

```text
SOURCE REGISTRY
      │
      ▼
DATASET DISCOVERY
      │
      ┌──────────────┼──────────────┐
      ▼              ▼              ▼
   INCOIS          MOSDAC          IMD
      │              │              │
   ERDDAP        APIs/files     Services
      │              │              │
      └──────────────┼──────────────┘
                     ▼
              SOURCE ADAPTER
                     │
                     ▼
                 RETRIEVAL
```

### Why These Sources Matter

**INCOIS** — Official holdings include Argo temperature/salinity profiles, buoys, HF radar currents, ROMS products and PFZ advisories. ERDDAP accepts requests, communicates with underlying source servers, normalizes returned time representation, and provides data in different output formats.

**MOSDAC (ISRO)** — OCM-3 (ocean colour, chlorophyll), SCAT-3 (surface wind vectors), INSAT products. Different users and datasets have different access profiles and latency.

**IMD** — REST API: current weather, forecast, marine bulletins, fishermen warnings, port warnings, sea area bulletins, cyclone tracking, lightning nowcast.

**Copernicus Marine** — Toolbox supports catalogue metadata discovery and subset requests by variables, geographic extent, time and depth, with outputs including NetCDF and Zarr. This is almost exactly the retrieval pattern we want to emulate internally.

### The "Smallest Valid Subset" Principle

```text
User: "Show SST near Gujarat tomorrow morning"

BAD:  Download entire Arabian Sea SST dataset

GOOD:
  dataset    = SST forecast
  region     = Gujarat marine region
  time       = tomorrow morning
  variables  = SST
  resolution = appropriate regional resolution
        ↓
  retrieve only required subset
```

### Data Requirement — The Bridge Between LLM and Provider

The LLM never calls provider-specific APIs directly. It produces a structured requirement:

```json
{
  "variable": "sea_surface_temperature",
  "region": {"geometry_ref": "G-104", "name": "Gujarat offshore"},
  "time": {
    "type": "forecast_valid",
    "start": "2026-09-23T06:00:00Z",
    "end": "2026-09-23T12:00:00Z"
  },
  "data_type": "forecast",
  "purpose": "safety_assessment",
  "resolution_preference": "regional"
}
```

The Data Discovery & Retrieval service resolves this against the source registry, selects the best dataset, and retrieves only the required subset.

---

# 5. The 10-Step Data Processing Pipeline

This is where ORCA becomes genuinely different from "API → JSON → LLM → frontend."

```text
RAW SOURCE DATA
      │
      ▼
 1. INGESTION
      │
      ▼
 2. STRUCTURAL VALIDATION
      │
      ▼
 3. SCIENTIFIC QUALITY CHECK
      │
      ▼
 4. NORMALIZATION
      │
      ▼
 5. SPATIAL ALIGNMENT
      │
      ▼
 6. TEMPORAL ALIGNMENT
      │
      ▼
 7. MISSING DATA HANDLING
      │
      ▼
 8. CROSS-SOURCE RECONCILIATION
      │
      ▼
 9. DERIVED FEATURES
      │
      ▼
10. MARINE STATE
```

---

## Step 1 — Raw Ingestion

**First principle: Never destroy the original source data.**

Preserved exactly as received:

```text
INCOIS NetCDF
MOSDAC satellite product
IMD forecast response
PFZ advisory
Argo observation
GeoTIFF
CSV
JSON
```

### Ingestion Record Schema

```json
{
  "ingestion_id": "ING-2041",
  "source": "INCOIS",
  "dataset_id": "sst_daily_ard",
  "retrieval_id": "RET-928",
  "format": "NetCDF",
  "raw_payload_ref": "s3://orca-raw/incois/sst/2026-09-21/sst_daily_ard_20260921.nc",
  "raw_checksum": "sha256:a3f9c...",
  "byte_size": 2457600,
  "ingested_at": "2026-09-21T09:15:01Z",
  "immutable": true,
  "metadata": {
    "variables": ["sst", "quality_flag"],
    "dimensions": ["time", "latitude", "longitude"],
    "time_coverage_start": "2026-09-21T00:00:00Z",
    "time_coverage_end": "2026-09-21T23:59:59Z",
    "geospatial_lat_min": 15.0,
    "geospatial_lat_max": 25.0,
    "geospatial_lon_min": 65.0,
    "geospatial_lon_max": 75.0,
    "spatial_resolution_deg": 0.01
  }
}
```

**Key rule:** Raw data is immutable. It matters because later we need to answer: *"Where did this value come from?"*

---

## Step 2 — Structural Validation

Before scientific analysis, ORCA asks:

```text
Does the file parse?               → PASS / FAIL
Are required variables present?    → PASS / MISSING_VARS
Are coordinates present?           → PASS / NO_COORDS
Is time present?                   → PASS / NO_TIME
Are dimensions valid?              → PASS / DIM_MISMATCH
Is the dataset complete?           → COMPLETE / PARTIAL
Is the schema what we expected?    → PASS / SCHEMA_DRIFT
```

### Structural Validation Schema

```json
{
  "validation_id": "SVAL-401",
  "ingestion_id": "ING-2041",
  "status": "PASS",
  "checks": [
    {"check": "file_parse", "status": "PASS"},
    {"check": "required_variables", "status": "PASS",
     "expected": ["sst", "quality_flag"],
     "found": ["sst", "quality_flag"]},
    {"check": "coordinates", "status": "PASS",
     "found": ["latitude", "longitude"]},
    {"check": "time_dimension", "status": "PASS"},
    {"check": "dimensions", "status": "PASS",
     "expected": {"time": 1, "latitude": 1000, "longitude": 1000}},
    {"check": "schema_match", "status": "PASS",
     "expected_schema_version": "incois_sst_v2"}
  ],
  "validated_at": "2026-09-21T09:15:02Z"
}
```

If the expected dataset is `time, latitude, longitude, sst` and the source suddenly changes `sst` to another variable name or removes latitude metadata, ORCA should **not** silently continue. It should produce `DATASET_INVALID` or `DATASET_PARTIAL`. This prevents garbage from reaching the LLM.

---

## Step 3 — Scientific Quality Validation

This is more important than conventional software validation.

Suppose:

```text
SST = 28.2 °C
```

Looks fine. But if:

```text
quality_flag = bad
```

then ORCA cannot treat it like a normal observation.

### Quality States

```text
VALID          → normal scientific use
SUSPECT        → use with warning, reduced weight
MISSING        → acknowledge gap
STALE          → data too old for purpose
INVALID        → reject entirely
UNAVAILABLE    → source could not provide
```

**Questionable records should not simply disappear.** They affect the confidence of the final answer.

### Scientific Quality Check Schema

```json
{
  "quality_id": "QUAL-501",
  "ingestion_id": "ING-2041",
  "variable": "sst",
  "checks": [
    {
      "check": "range_validity",
      "rule": "sst >= -2.0 and sst <= 40.0 degC",
      "status": "PASS",
      "out_of_range_count": 0,
      "total_points": 1000000
    },
    {
      "check": "quality_flags",
      "total": 1000000,
      "valid": 942000,
      "suspect": 38000,
      "bad": 12000,
      "missing": 8000,
      "valid_fraction": 0.942
    },
    {
      "check": "timestamp_freshness",
      "observation_time": "2026-09-21T06:00:00Z",
      "check_time": "2026-09-21T09:15:02Z",
      "age_hours": 3.25,
      "freshness": "FRESH",
      "threshold_hours": 24
    },
    {
      "check": "spatial_coverage",
      "expected_region": "Gujarat offshore",
      "coverage_fraction": 0.94,
      "status": "PASS"
    },
    {
      "check": "processing_level",
      "value": "L3",
      "acceptable": ["L3", "L4"]
    }
  ],
  "overall_quality": "VALID",
  "quality_score": 0.94,
  "quality_at": "2026-09-21T09:15:03Z"
}
```

---

## Step 4 — Normalization

This is one of the most visually powerful things to show in the PPT.

### The Problem

```text
INCOIS SST        → °C        field: "sst"
Copernicus thetao → K         field: "thetao"
NOAA SST          → °C        field: "sst"
Buoy temperature  → °C        field: "temperature"
```

### The Solution — Canonical Representation

```text
CANONICAL VARIABLE: sea_surface_temperature
CANONICAL UNIT:     °C
```

### Normalization Crosswalk Schema

```json
{
  "canonical_variable": "sea_surface_temperature",
  "canonical_unit": "degC",
  "sources": {
    "incois_erddap": {
      "field": "sst",
      "native_unit": "degC",
      "transform": "none"
    },
    "copernicus_marine": {
      "field": "thetao",
      "native_unit": "K",
      "transform": "subtract_273.15"
    },
    "noaa_coastwatch": {
      "field": "sst",
      "native_unit": "degC",
      "transform": "none"
    },
    "buoy_incois": {
      "field": "temperature",
      "native_unit": "degC",
      "transform": "none",
      "note": "surface measurement"
    }
  }
}
```

### Canonical Variables for V1

| Canonical Variable | Unit | Category |
|---|---|---|
| `sea_surface_temperature` | °C | Ocean |
| `chlorophyll_a` | mg/m³ | Ocean |
| `current_speed` | m/s | Ocean |
| `current_direction` | degrees | Ocean |
| `mixed_layer_depth` | m | Ocean |
| `wind_speed` | m/s | Weather |
| `wind_direction` | degrees | Weather |
| `wind_gust` | m/s | Weather |
| `significant_wave_height` | m | Weather |
| `wave_period` | s | Weather |
| `swell_height` | m | Weather |
| `swell_direction` | degrees | Weather |
| `rainfall_rate` | mm/hr | Weather |
| `sea_level_pressure` | hPa | Weather |
| `depth` | m | GIS |
| `distance` | km | GIS |

### Normalized Record Schema

```json
{
  "normalized_id": "NORM-601",
  "ingestion_id": "ING-2041",
  "canonical_variable": "sea_surface_temperature",
  "canonical_unit": "degC",
  "source_field": "sst",
  "source_unit": "degC",
  "transform_applied": "none",
  "data_ref": "s3://orca-normalized/sst/2026-09-21/gujarat_sst.zarr",
  "coordinate_system": "EPSG:4326",
  "time_reference": "UTC",
  "normalized_at": "2026-09-21T09:15:04Z"
}
```

This follows CF (Climate and Forecast) metadata conventions where coordinate semantics such as latitude, longitude and time are explicitly represented through standardized metadata.

---

## Step 5 — Spatial Alignment

Another major hidden complexity.

### The Problem

```text
SST grid:          1 km × 1 km     (raster)
Chlorophyll grid:  4 km × 4 km     (raster)
Buoy:              single point     (point)
Current model:     8 km × 8 km     (raster)
Restricted zone:   polygon          (vector)
Ecol. Sensitive:   polygon          (vector)
```

You cannot just combine those raw datasets.

### The Solution — Common Spatial Reference

```text
         Common spatial reference (EPSG:4326 / WGS84)
                     │
         ┌───────────┼───────────────┐
         │           │               │
    RASTER GRID   POINT DATA    VECTOR GEOMETRY
         │           │               │
    ┌────┼────┐      │           ┌───┼────┐
    │    │    │      │           │   │    │
   SST  CHL  Wave  Buoy/Argo  EEZ  MPA  ESZ  Geofence
  1km   4km  0.5°  point      poly poly  poly
```

### Spatial Alignment Schema

```json
{
  "spatial_alignment_id": "SA-701",
  "reference_system": "EPSG:4326",
  "query_region": {
    "name": "Gujarat offshore",
    "geometry_ref": "G-104",
    "bbox": [65.0, 18.0, 73.0, 24.0]
  },
  "aligned_layers": [
    {
      "variable": "sea_surface_temperature",
      "source": "INCOIS",
      "native_resolution_km": 1.0,
      "alignment_method": "native_grid",
      "coverage_fraction": 0.94
    },
    {
      "variable": "chlorophyll_a",
      "source": "MOSDAC_OCM3",
      "native_resolution_km": 4.0,
      "alignment_method": "native_grid",
      "coverage_fraction": 0.87
    },
    {
      "variable": "significant_wave_height",
      "source": "INCOIS_OSF",
      "native_resolution_deg": 0.083,
      "alignment_method": "native_grid",
      "coverage_fraction": 1.0
    },
    {
      "type": "point_observation",
      "source": "INCOIS_Buoy",
      "location": {"lat": 20.7, "lon": 71.0},
      "within_region": true
    },
    {
      "type": "vector_boundary",
      "source": "MarineRegions",
      "geometry": "EEZ_India",
      "intersection_method": "ST_Intersects"
    }
  ],
  "aligned_at": "2026-09-21T09:15:05Z"
}
```

A query like *"Show high-chlorophyll areas outside protected zones within 50 km"* becomes a deterministic spatial operation (PostGIS: `ST_Intersects`, `ST_DWithin`), rather than something the LLM tries to reason about from raw text.

---

## Step 6 — Temporal Alignment

Marine data is time-dependent with different temporal semantics.

### The Problem

```text
SST observation:          06:00 UTC
Chlorophyll satellite:    04:30 UTC
Wind forecast:            issued 00:00, valid 06:00
Wave forecast:            issued 03:00, valid 06:00
PFZ advisory:             issued 05:00
Tide prediction:          valid 06:00
```

Those aren't automatically comparable.

### Temporal Metadata Preserved

```text
observation_time          → when the measurement happened
forecast_issue_time       → when the forecast was generated
forecast_valid_time       → when the forecast applies
lead_time                 → gap between issue and valid time
retrieval_time            → when ORCA downloaded it
data_type                 → observation | forecast | advisory | derived | historical | static
```

### Temporal Alignment Schema

```json
{
  "temporal_alignment_id": "TA-801",
  "query_time": {
    "type": "forecast_valid",
    "target": "2026-09-23T06:00:00Z",
    "tolerance_hours": 3
  },
  "aligned_records": [
    {
      "variable": "sea_surface_temperature",
      "data_type": "observation",
      "observation_time": "2026-09-21T06:00:00Z",
      "age_hours": 48,
      "freshness": "ACCEPTABLE",
      "note": "Most recent observation available"
    },
    {
      "variable": "significant_wave_height",
      "data_type": "forecast",
      "forecast_issue_time": "2026-09-22T00:00:00Z",
      "forecast_valid_time": "2026-09-23T06:00:00Z",
      "lead_time_hours": 30,
      "freshness": "FRESH"
    },
    {
      "variable": "wind_speed",
      "data_type": "forecast",
      "forecast_issue_time": "2026-09-22T03:00:00Z",
      "forecast_valid_time": "2026-09-23T06:00:00Z",
      "lead_time_hours": 27,
      "freshness": "FRESH"
    },
    {
      "variable": "marine_warning",
      "data_type": "advisory",
      "issue_time": "2026-09-22T06:00:00Z",
      "valid_until": "2026-09-23T18:00:00Z",
      "freshness": "ACTIVE"
    }
  ],
  "temporal_note": "SST is observation-based (2-day old), weather variables are forecast-based (fresh). This distinction is preserved throughout analysis.",
  "aligned_at": "2026-09-21T09:15:06Z"
}
```

This becomes critical for *"What will conditions be tomorrow morning?"* — ORCA must reason about future valid time, not merely the time the forecast file was downloaded.

---

## Step 7 — Missing Data Handling

### The Problem

```text
SST              ✓ available
Chlorophyll      ✓ available
Wind             ✓ available
Current          ✗ unavailable (source timeout)
Buoy             ✗ unavailable (no nearby buoy)
```

### The Rule

The answer should **not** pretend all five sources exist.

### Missing Data Schema

```json
{
  "coverage_id": "COV-901",
  "workflow_id": "W-100",
  "available": [
    {"variable": "sea_surface_temperature", "source": "INCOIS", "quality": "VALID"},
    {"variable": "chlorophyll_a", "source": "MOSDAC", "quality": "VALID"},
    {"variable": "wind_speed", "source": "IMD", "quality": "VALID"}
  ],
  "unavailable": [
    {
      "variable": "current_speed",
      "reason": "SOURCE_TIMEOUT",
      "attempted_source": "INCOIS_OSF",
      "impact": "Current-based assessments will be absent",
      "fallback_attempted": true,
      "fallback_source": "Copernicus",
      "fallback_status": "ALSO_UNAVAILABLE"
    },
    {
      "variable": "buoy_observation",
      "reason": "NO_NEARBY_STATION",
      "impact": "No in-situ validation available",
      "nearest_station_km": 85
    }
  ],
  "coverage_fraction": 0.6,
  "confidence_impact": "Evidence sufficient with limitations"
}
```

The confidence/limitations layer changes accordingly. This follows the distinction between **uncertainty** in physical information and **confidence** in a specific ORCA conclusion.

---

## Step 8 — Cross-Source Reconciliation

This is where ORCA starts becoming genuinely intelligent.

### The Problem

```text
INCOIS SST     = 28.1 °C
Copernicus SST = 28.0 °C
NOAA SST       = 27.8 °C
Buoy SST       = 28.2 °C
```

ORCA should **not** say *"The correct value is 28.1."*

### The Solution — Examine and Report

```json
{
  "reconciliation_id": "RECON-1001",
  "variable": "sea_surface_temperature",
  "region": "Gujarat offshore",
  "sources": [
    {
      "source": "INCOIS",
      "value": 28.1,
      "type": "satellite_L3",
      "resolution_km": 1.0,
      "observation_time": "2026-09-21T06:00:00Z"
    },
    {
      "source": "Copernicus",
      "value": 28.0,
      "type": "model_L4",
      "resolution_km": 8.0,
      "observation_time": "2026-09-21T00:00:00Z"
    },
    {
      "source": "NOAA",
      "value": 27.8,
      "type": "satellite_L3",
      "resolution_km": 5.0,
      "observation_time": "2026-09-20T18:00:00Z"
    },
    {
      "source": "Buoy",
      "value": 28.2,
      "type": "in_situ",
      "resolution": "point",
      "observation_time": "2026-09-21T06:00:00Z"
    }
  ],
  "analysis": {
    "agreement": "CONSISTENT",
    "range_min": 27.8,
    "range_max": 28.2,
    "spread": 0.4,
    "primary_value": 28.1,
    "primary_source": "INCOIS",
    "primary_reason": "highest resolution, most recent, validated by buoy",
    "buoy_validation": "Buoy supports satellite estimate (delta = 0.1°C)"
  },
  "reconciled_at": "2026-09-21T09:15:07Z"
}
```

That is much stronger than simply saying "we use multiple datasets."

---

## Step 9 — Derived Features

Now ORCA creates information that was not directly downloaded.

```text
SST + historical SST               → SST anomaly
Chlorophyll + historical CHL        → chlorophyll anomaly
SST gradient + CHL gradient         → front indicator
+ currents
Wind + waves + cyclone              → operational risk state
+ lightning + geofence
All environmental variables         → ecosystem state
```

### Derived Feature Schema

```json
{
  "derived_id": "DER-1101",
  "feature": "sst_anomaly",
  "engine": "ocean_engine",
  "method": {
    "name": "regional_mean_anomaly",
    "version": "1.0",
    "description": "Current SST minus climatological monthly mean"
  },
  "inputs": [
    {"evidence_id": "EV-91", "variable": "sea_surface_temperature", "type": "observation"},
    {"evidence_id": "EV-92", "variable": "sst_climatology", "type": "historical"}
  ],
  "outputs": {
    "anomaly_value": 1.1,
    "current_mean": 28.2,
    "baseline_mean": 27.1,
    "unit": "degC",
    "region": "Gujarat offshore",
    "period": "September 2026 vs September climatology"
  },
  "quality": {
    "spatial_coverage": 0.94,
    "baseline_years": 30,
    "confidence": "HIGH"
  },
  "derived_at": "2026-09-21T09:15:08Z"
}
```

### Derived Feature Catalog for V1

| Feature | Inputs | Engine | Category |
|---|---|---|---|
| SST anomaly | SST + climatology | Ocean | Ocean |
| Chlorophyll anomaly | CHL + climatology | Ocean | Ocean |
| Front indicator | SST gradient + CHL gradient + currents | Ocean | Ocean |
| Upwelling indicator | SST + wind + current | Ocean | Ocean |
| MLD analysis | Temperature profile + salinity | Ocean | Ocean |
| Wind risk | Wind speed + gust | Weather | Hazard |
| Wave risk | Wave height + period | Weather | Hazard |
| Cyclone proximity | Cyclone track + user position | Weather | Hazard |
| Lightning proximity | Lightning observations + distance | Weather | Hazard |
| Combined risk state | All hazard variables | Risk | Decision |
| Route exposure | Route geometry + hazard layers | Route | Decision |
| Geofence status | Position + all boundary polygons | Spatial | GIS |
| Ecosystem state | SST + CHL + currents + wind + historical | Ecosystem | Science |
| Productivity indicator | CHL + SST + front + upwelling | Ecosystem | Science |

---

## Step 10 — Marine State

**The central intermediate representation.** Everything before it is about getting trustworthy information. Everything after it is about deciding what the information means.

```text
OBSERVATIONS
+
FORECASTS
+
ADVISORIES
+
HISTORICAL CONTEXT
+
GIS CONSTRAINTS
+
ECOSYSTEM INDICATORS
+
HUMAN ACTIVITY CONTEXT
        ↓
     MARINE STATE
```

### Marine State Schema

```json
{
  "marine_state_id": "MS-1201",
  "workflow_id": "W-100",
  "region": {
    "name": "Gujarat offshore",
    "geometry_ref": "G-104",
    "bbox": [65.0, 18.0, 73.0, 24.0]
  },
  "reference_time": "2026-09-23T06:00:00Z",
  "time_type": "forecast_valid",

  "ocean": {
    "sst": {"value": 28.2, "unit": "degC", "type": "observation", "evidence_id": "EV-91"},
    "sst_anomaly": {"value": 1.1, "unit": "degC", "evidence_id": "EV-93"},
    "chlorophyll": {"value": 0.8, "unit": "mg/m3", "type": "observation", "evidence_id": "EV-94"},
    "chlorophyll_anomaly": {"value": -0.31, "unit": "fraction", "evidence_id": "EV-95"},
    "current_speed": null,
    "current_note": "Unavailable (source timeout)"
  },

  "atmosphere": {
    "wind_speed": {"value": 8.2, "unit": "m/s", "type": "forecast", "evidence_id": "EV-96"},
    "wind_direction": {"value": 245, "unit": "degrees"},
    "wave_height": {"value": 2.1, "unit": "m", "type": "forecast", "evidence_id": "EV-97"},
    "swell_height": {"value": 1.5, "unit": "m", "type": "forecast"},
    "lightning_proximity": null,
    "cyclone_active": false,
    "marine_warning": {
      "active": true,
      "source": "IMD",
      "severity": "MODERATE",
      "valid_until": "2026-09-23T18:00:00Z",
      "evidence_id": "EV-98"
    }
  },

  "ecosystem": {
    "productivity_state": "BELOW_BASELINE",
    "front_detected": false,
    "upwelling_indicator": "WEAK",
    "hab_indicator": "NONE",
    "pfz_available": true,
    "pfz_count": 2,
    "pfz_evidence_id": "EV-99"
  },

  "geography": {
    "eez_status": "WITHIN_INDIA",
    "mpa_nearby": false,
    "restricted_zones_nearby": true,
    "restricted_zone_count": 1,
    "nearest_port": {"name": "Veraval", "distance_km": 42},
    "bathymetry_range": {"min_m": 15, "max_m": 200}
  },

  "temporal": {
    "query_refers_to": "future",
    "lead_time_hours": 30,
    "data_freshness": {
      "ocean": "ACCEPTABLE",
      "weather": "FRESH",
      "advisory": "ACTIVE"
    }
  },

  "coverage": {
    "available_variables": 8,
    "unavailable_variables": 1,
    "coverage_fraction": 0.89,
    "limitations": [
      "No current observation available",
      "No nearby buoy for in-situ validation"
    ]
  },

  "evidence_ids": ["EV-91", "EV-93", "EV-94", "EV-95", "EV-96", "EV-97", "EV-98", "EV-99"],
  "constructed_at": "2026-09-21T09:15:10Z"
}
```

The same Marine State can serve fishermen, researchers, authorities, disaster-management teams and maritime operators — the **Decision layer** on top adapts the interpretation to the user's context.

---

# 6. The Critical Boundary: LLM vs Scientific Engine

This is the single most important technical statement in the presentation:

```text
LLM                          SCIENTIFIC ENGINE
│                             │
reasoning / planning          deterministic math
│                             │
▼                             ▼
"I need SST anomaly,          (28.4 - 27.1) = 1.3
 chlorophyll anomaly,         ST_DWithin(point, zone, 50km)
 wind and baseline"           route_distance(A, B)
```

### What the LLM Does (6 Operations)

```text
1. UNDERSTAND    → "What is the user asking?"
2. CONTEXTUALIZE → "Where? When? For whom? What constraints?"
3. PLAN          → "What evidence is necessary?"
4. SELECT        → "Which capabilities/tools should execute?"
5. OBSERVE       → "Are results sufficient or contradictory?"
6. SYNTHESIZE    → "What does the evidence mean to this user?"
```

And sometimes:

```text
OBSERVE → insufficient evidence → REPLAN → request additional evidence
```

### What the LLM Should NOT Receive

```text
BAD:
  NetCDF → convert entire file to JSON → put JSON in LLM context

GOOD:
  NetCDF / Zarr → Scientific Engine → Structured Result
```

The LLM receives compact structured results:

```json
{
  "variable": "sea_surface_temperature",
  "region": "Gujarat offshore",
  "mean": 28.2,
  "min": 27.7,
  "max": 28.8,
  "anomaly": 1.1,
  "unit": "degC",
  "valid_time": "2026-09-23T06:00:00Z",
  "evidence_ids": ["EV-91", "EV-93"]
}
```

Not 500MB of raw NetCDF.

---

# 7. Four Data Representations

The same dataset should NOT be passed through the whole system in the same representation.

```text
┌──────────────────────────────────────────────────────────┐
│            RAW SCIENTIFIC REPRESENTATION                  │
│  NetCDF, Zarr, GeoTIFF, HDF, GRIB, CSV, JSON            │
│  → Storage: S3/MinIO object storage                      │
│  → Purpose: Immutable source archive                     │
└──────────────────────┬───────────────────────────────────┘
                       ▼
┌──────────────────────────────────────────────────────────┐
│            ANALYTICAL REPRESENTATION                      │
│  xarray arrays, Parquet tables, PostGIS geometries       │
│  → Storage: Zarr chunks, Parquet files, PostGIS tables   │
│  → Purpose: Scientific computation and querying          │
└──────────────────────┬───────────────────────────────────┘
                       ▼
┌──────────────────────────────────────────────────────────┐
│         VISUALIZATION REPRESENTATION                      │
│  COG/raster tiles, GeoJSON/vector tiles,                 │
│  structured time series, vector fields, route geometries │
│  → Storage: Tile server, GeoJSON API, MVT               │
│  → Purpose: Browser rendering                            │
└──────────────────────┬───────────────────────────────────┘
                       ▼
┌──────────────────────────────────────────────────────────┐
│              LLM REPRESENTATION                           │
│  Compact structured evidence: metrics, findings,         │
│  methods, uncertainty, provenance references              │
│  → Transport: JSON in agent context                      │
│  → Purpose: Reasoning and synthesis                      │
└──────────────────────────────────────────────────────────┘
```

### Example: SST Flows Through All Four

```text
SST NetCDF (raw)
    ↓
xarray + validated SST array (analytical)
    ↓
SST anomaly calculated (analytical)
    ↓
┌──────────────────────────────────────────────┐
│ Two parallel outputs from same derived data: │
│                                              │
│ COG / color-mapped raster tiles              │
│     ↓                                        │
│ Browser map visualization                    │
│                                              │
│ Structured scientific result                 │
│     ↓                                        │
│ LLM → natural-language explanation           │
└──────────────────────────────────────────────┘
```

That is far more technically credible than: `API → JSON → LLM → frontend`

---

# 8. Scientific Data Storage Architecture

Not just "Database: PostgreSQL." Show the real architecture:

```text
DATA STORAGE
  │
  ┌──────────────────┼─────────────────┼───────────────┐
  ▼                  ▼                 ▼               ▼
OBJECT STORAGE    POSTGRES+POSTGIS   PARQUET         REDIS
S3 / MinIO        Metadata + GIS     Analytics       Cache
  │                  │                 │               │
NetCDF            workflows          history          hot cache
Zarr              variables          features         temp state
GeoTIFF           evidence           vessel data      in-flight dedup
HDF               tables             observations     short-lived
GRIB              geometries         time-series      rate/coord state
  │               geofences                │
  │               ports/harbours           │
  │               source registry          │
  │               dataset catalog          │
```

### Technology Justification

| Storage | Technology | Why |
|---|---|---|
| Scientific arrays | **xarray** | Labelled multidimensional arrays, Dask-backed chunked processing for larger-than-memory datasets, Zarr and NetCDF workflows |
| Columnar analytics | **Parquet** | Column-oriented format for efficient analytical storage and retrieval |
| Spatial queries | **PostGIS** | Spatial indexing, `ST_Intersects`, `ST_DWithin`, index-aware predicates |
| Raster delivery | **Cloud Optimized GeoTIFF** | Tiling, reduced-resolution overviews, HTTP range requests — retrieve only needed portions |
| Map rendering | **MapLibre GL JS** | Interactive vector-tile maps in the browser |
| Heavy layers | **deck.gl** | High-performance visualization of large datasets through composable layers |

---

# 9. Data Catalog / Dataset Registry

Between source discovery and storage:

```text
DATA CATALOG
      │
      ┌──────────────┼──────────────┐
      ▼              ▼              ▼
  dataset          variable        source
  metadata         metadata        metadata
```

### Dataset Registry Entry Schema

```json
{
  "dataset_id": "incois_sst_daily",
  "provider": "INCOIS",
  "variables": ["sea_surface_temperature", "quality_flag"],
  "spatial_coverage": {
    "region": "Indian Ocean",
    "bbox": [30.0, -30.0, 120.0, 30.0]
  },
  "temporal_coverage": {
    "start": "2010-01-01",
    "end": "present",
    "update_frequency": "daily"
  },
  "spatial_resolution_km": 1.0,
  "temporal_resolution": "daily",
  "format": "NetCDF",
  "access_method": "ERDDAP",
  "data_type": "observation",
  "processing_level": "L3",
  "trust_class": "AUTHORITATIVE",
  "role": "primary",
  "fallback": "copernicus_sst",
  "authentication": "none",
  "rate_limit": "10/min",
  "quality_info": "CF-compliant quality flags",
  "license": "open",
  "version": "v2",
  "last_verified": "2026-09-15"
}
```

For Earth-observation assets, STAC provides a standardized way to describe and discover spatiotemporal geospatial assets. ORCA doesn't need full STAC infrastructure for the hackathon, but STAC-like dataset metadata is a very strong architectural concept.

---

# 10. Visualization Architecture

Visualization should NOT be an afterthought.

```text
SCIENTIFIC RESULT
      │
      ▼
VISUALIZATION ADAPTER
      │
      ┌─────────┼──────────────┐
      ▼         ▼              ▼
     MAP      CHARTS     SUMMARY CARDS
      │         │              │
      ▼         ▼              ▼
   Layers    Time-series      KPIs
   Raster    Anomaly          Findings
   Vector    Comparison       Evidence
   Route     Forecast         Limitations
```

The scientific engine should not tell the browser how to calculate anything. It returns: geometry, raster reference, time series, vectors, structured metrics. The browser renders.

### Map Layer Types for ORCA

| Type | Examples | Format |
|---|---|---|
| **Raster** | SST, chlorophyll, wave height, rain, bathymetry, risk surface | COG tiles / TileJSON |
| **Vector** | Currents, wind, routes, vessel activity | GeoJSON / MVT |
| **Points** | Buoys, Argo profiles, ports, harbours, lightning events | GeoJSON |
| **Polygons** | EEZ, MPA, restricted zones, geofences, hazard zones | GeoJSON / MVT |
| **Lines** | Cyclone track, recommended route, historical trajectory | GeoJSON |

### Visualizations Are Generated From the Question

```text
"Where are the high-chlorophyll regions with suitable SST?"
→ Map: High CHL + SST suitability + PFZ
→ Chart: Chlorophyll vs SST
→ Evidence: Satellite timestamp, SST source, CHL source, PFZ advisory

"Why has productivity decreased?"
→ Map: Productivity anomaly
→ Chart: Current vs historical chlorophyll
→ Chart: SST anomaly
→ Chart: Wind/current comparison
→ Explanation: Structured evidence

"Show the safest route."
→ Map: Route A, Route B, hazard zones, restricted zones
→ Chart: Route exposure comparison
→ Summary: Distance, ETA, wave exposure, wind exposure, hazards
```

The map is conversationally controlled — the user's question determines which layers appear, not a static layer list.

---

# 11. Complete End-to-End Execution Trace

**Query:** *"Find suitable fishing areas near Gujarat tomorrow morning, but avoid hazardous zones."*

### Stage 1 — LLM Understands

```json
{
  "intent": "fishing_suitability_with_constraints",
  "decision_type": "WHERE",
  "region": "Gujarat offshore",
  "time": "tomorrow morning (2026-09-23T06:00:00Z)",
  "objective": "fishing suitability",
  "constraints": ["avoid hazards", "avoid restricted zones"],
  "user_context": {"role": "fisherman", "language": "gu", "vessel": "mechanized"}
}
```

### Stage 2 — Planner Creates Data Requirements

```text
Need: PFZ, SST, chlorophyll, wind, waves, currents,
      cyclone/lightning, restricted zones, marine warnings
```

### Stage 3 — Data Discovery

```text
PFZ             → INCOIS PFZ Advisory
SST             → INCOIS (primary) / Copernicus (fallback)
Chlorophyll     → MOSDAC OCM-3 / INCOIS
Wind            → IMD forecast
Waves           → INCOIS OSF
Currents        → INCOIS / Copernicus
Cyclone         → IMD tracking
Lightning       → IMD nowcast
GIS boundaries  → MarineRegions / ProtectedSeas
Marine warnings → IMD
```

### Stage 4 — Retrieval (smallest valid subset)

```text
Region   = Gujarat offshore (bbox: 65-73E, 18-24N)
Time     = 2026-09-23T06:00:00Z
Variables = SST, CHL, wind, waves, currents only
```

### Stage 5 — Data Processing Pipeline

```text
1. Ingest        → raw files stored immutably
2. Validate      → structural checks pass
3. Quality       → quality flags checked, coverage assessed
4. Normalize     → all units → canonical (°C, m/s, m, km)
5. Spatial align  → all layers referenced to common EPSG:4326
6. Temporal align → observation vs forecast times preserved
7. Missing data   → current observation unavailable, noted
8. Reconcile     → SST sources agree within 0.4°C
9. Derive        → SST anomaly, CHL anomaly, risk indicators
```

### Stage 6 — Scientific Engines

```text
Ocean Engine    → SST anomaly (+1.1°C), CHL anomaly (-31%)
Weather Engine  → Wind risk (MODERATE), wave risk (MODERATE)
Spatial Engine  → 1 restricted zone nearby, within EEZ
Risk Engine     → Combined risk: MODERATE
Ecosystem Engine → Productivity: BELOW_BASELINE, no front detected
```

### Stage 7 — Marine State Constructed

Full structured Marine State (see schema in Step 10 above)

### Stage 8 — Evidence Gate

```text
✓ Source availability:   8/9 variables available
✓ Freshness:             weather FRESH, ocean ACCEPTABLE
✗ Conflict:              none detected
✓ Official warnings:     IMD marine warning ACTIVE (MODERATE)
✗ Missing evidence:      current observation absent
→ Confidence:            SUFFICIENT WITH LIMITATIONS
```

### Stage 9 — LLM Synthesis

LLM receives compact Marine State + evidence and produces:

```text
"ગુજરાત દરિયાકિનારે 2 PFZ વિસ્તારો ઉપલબ્ધ છે...

Area A: Higher chlorophyll, favorable SST, PFZ indication
  But: Elevated wave conditions (2.1m), IMD moderate advisory active.

Area B: Lower productivity, but lower hazard exposure.

Limitation: Current observation was not available.
Based on: INCOIS PFZ advisory, MOSDAC chlorophyll, IMD forecast."
```

### Stage 10 — Visualization Generated From Question

```text
MAP
├── PFZ markers (INCOIS)
├── Chlorophyll heatmap (MOSDAC)
├── SST overlay (INCOIS)
├── Hazard zones (IMD warning)
├── Restricted zones (MarineRegions)
├── Candidate fishing areas (derived)
└── Decision overlay (green/yellow/red)

CHARTS
├── SST current vs baseline
├── Chlorophyll current vs baseline
└── Wave forecast for tomorrow

EVIDENCE PANEL
├── INCOIS PFZ — Fresh
├── MOSDAC CHL — Recent observation
├── IMD Wind — Forecast valid 06:00
├── INCOIS Wave — Forecast
└── Limitation: No current observation
```

---

# 12. What the PPT Main Technical Slide Should Show

```text
              ORCA TECHNICAL APPROACH

              USER
                │
                ▼
┌─────────────────────────────────────────────┐
│       LLM CONTEXT + PLANNING LAYER          │
│  Intent • Context • Data Requirements       │
│  Tool Selection • Replanning • Synthesis     │
└──────────────────────┬──────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────┐
│         MARINE DATA DISCOVERY               │
│  Dataset Registry • Semantic Mapping        │
│  Source Selection • Subset Retrieval         │
└──────────────────────┬──────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────┐
│       DATA PROCESSING PIPELINE              │
│  Ingest → Validate → Normalize → Align     │
│  Spatial/Temporal → Quality → Derived Data  │
└──────────────────────┬──────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────┐
│       SCIENTIFIC INTELLIGENCE               │
│  Ocean • Weather • Ecosystem • GIS • Risk   │
│  Deterministic Scientific Computation       │
└──────────────────────┬──────────────────────┘
                       │
                       ▼
              MARINE STATE
                       │
                       ▼
           EVIDENCE + DECISION
                       │
           ┌───────────┼───────────┐
           ▼           ▼           ▼
         CHAT         MAP        CHARTS


DATA STORAGE ─────────────────────────────────
S3/MinIO         PostgreSQL/PostGIS    Parquet       Redis
Scientific       Metadata + GIS       Analytics     Cache/State
NetCDF/Zarr      Evidence/Geometry     Historical    Dedup
GeoTIFF/HDF      Dataset Registry     Features      Query cache


INDIAN + GLOBAL SOURCES ──────────────────────
INCOIS │ MOSDAC │ IMD │ Copernicus │ NOAA │ GEBCO │ GIS
```

---

# 13. What Should NOT Dominate the PPT

Push these into internal engineering documentation only:

```text
✗ WAF / CDN / Edge
✗ IAM / RBAC details
✗ Kubernetes / multi-region
✗ Service mesh
✗ Zero trust details
✗ Red-team scenarios
✗ Complex enterprise deployment diagrams
✗ Huge agent registries
✗ 20+ component diagrams
```

Keep only visible runtime controls:

```text
✓ Validation
✓ Timeouts
✓ API limits
✓ Fallbacks
✓ Basic tool controls
✓ Failure handling
```

---

# 14. The ORCA Story for the Judges

> Marine data is fragmented across satellites, ocean observations, weather forecasts, advisories and GIS datasets. ORCA first discovers the datasets required for the user's question and retrieves only the relevant spatio-temporal subset. The data is then validated, normalized and aligned across space and time before deterministic scientific engines calculate anomalies, correlations, hazards and routes. These results are consolidated into a machine-readable Marine State. The LLM does not replace the scientific computation; it plans the investigation, selects the required capabilities, interprets validated evidence, detects when additional evidence is needed, and explains the final result. The same structured results drive the conversational response, dynamic marine map, scientific charts and alerts.

That is the core technical identity of ORCA. And it is much stronger than presenting ORCA primarily as a multi-agent chatbot.

---

# 15. Summary Principles

```text
1. DATA PIPELINE IS THE CENTER OF GRAVITY
   Not the LLM. Not the agents. The scientific data pipeline.

2. RAW → VALIDATED → NORMALIZED → ALIGNED → DERIVED → MARINE STATE
   Every step has a concrete schema and purpose.

3. FOUR REPRESENTATIONS, NOT ONE
   Raw scientific → Analytical → Visualization → LLM
   The same data flows through different forms for different consumers.

4. LLM PLANS, ENGINES CALCULATE
   The LLM never computes SST anomaly. The Ocean Engine does.

5. RETRIEVE ONLY WHAT IS NEEDED
   Smallest valid spatio-temporal subset, not entire global datasets.

6. MISSING DATA IS EXPLICIT
   Never pretend all sources exist. State limitations.

7. CROSS-SOURCE RECONCILIATION, NOT BLIND SELECTION
   Report agreement/disagreement, don't silently pick one value.

8. MARINE STATE IS THE CENTRAL ABSTRACTION
   Everything before it = getting trustworthy data.
   Everything after it = deciding what it means.

9. THE MAP IS DRIVEN BY THE QUESTION
   Not a static layer dashboard — visualization adapts to the query.

10. THE STORY IS SCIENTIFIC DATA ENGINEERING
    Not "AI agents thinking" — real data processing that
    turns heterogeneous marine observations into decisions.
```

---

# 16. PS Fulfillment Verification - Data Pipeline Document

```text
V PS-6  Autonomous data discovery and retrieval
        -> Section 4 (Data Acquisition): catalog -> semantic mapping -> source selection
        -> Data Requirement Plan bridges LLM intent to provider APIs

V PS-7  Spatial-temporal reasoning (data layer)
        -> Steps 5-6 (Spatial + Temporal Alignment): all layers aligned to EPSG:4326
        -> Temporal semantics preserved: observation_time != forecast_valid_time

V PS-8  Evidence-grounded decision (data layer)
        -> Step 1 (Raw Ingestion): immutable source data with checksum
        -> Steps 2-3 (Validation + Quality): every value has quality state
        -> Step 8 (Reconciliation): cross-source agreement tracked
        -> Step 10 (Marine State): unified evidence-linked snapshot

V PS-5  Multi-source correlation
        -> Step 4 (Normalization): canonical variables + unit crosswalk
        -> Step 8 (Reconciliation): INCOIS vs Copernicus vs NOAA vs Buoy
        -> Step 9 (Derived Features): SST anomaly, CHL anomaly, front detection

V PS-9  Explainable visualization (data layer)
        -> Section 7 (Four Representations): Raw -> Analytical -> Visualization -> LLM
        -> Section 10 (Visualization Architecture): map driven by the question

V PS-3  Autonomous planning (data layer)
        -> Step 7 (Missing Data): gaps tracked and reported to planner
        -> Planner can REPLAN based on data availability/gaps
```

### How the Data Pipeline Serves the Hero Investigation Loop

```text
Hero Loop Step              Data Pipeline Contribution

DISCOVER DATA            ->  Source Registry + Dataset Catalog + Semantic Crosswalk
RETRIEVE                 ->  Source Connectors + Smallest Valid Subset
CORRELATE                ->  Normalization + Spatial/Temporal Alignment + Reconciliation
OBSERVE STATE            ->  Marine State (unified snapshot with coverage + gaps)
VALIDATE                 ->  Evidence Chain (retrieval witness -> quality -> provenance)
EXPLAIN                  ->  Four Representations (Raw -> Analytical -> Viz -> LLM)
VISUALIZE                ->  Tile server + GeoJSON + Charts from derived data
```

> **The data pipeline is the engine. The investigation loop is the product.**

---

# 17. Companion Reference: Data Acquisition Matrix

> For detailed connector specifications, dataset IDs, access patterns, and provider-specific engineering, refer to:
> ORCA_Data_Acquisition_Matrix_and_Engineering_Specification.md (64KB, 94 sections)

That document contains:
- Complete source inventory with 30+ dataset IDs (IN-01 through OSM-01)
- Detailed INCOIS ERDDAP, MOSDAC, IMD, Copernicus, NOAA, GEBCO connector specs
- Generic ERDDAP connector architecture (reusable across providers)
- Dataset request/response object schemas
- Ingestion manager workflow
- Raw data naming conventions
- Checksum and deduplication
- Data security rules

---

# 18. Variable-Specific Fallback Matrix

> Not all variables have fallbacks. PFZ has NONE. Cyclone warnings have NONE. SST has four.

```text
Variable          Primary              Fallback               Restriction
-----------       --------             --------               -----------
PFZ               INCOIS               NONE                   Do NOT invent PFZ
Cyclone warning   IMD                  Official sources only  Do NOT override
Fishermen warning IMD                  INCOIS context         Preserve warning text
Tsunami           INCOIS               NONE                   Authoritative only
SST               INCOIS/operational   Copernicus/NOAA/NASA   Check latency
Chlorophyll       INCOIS/MOSDAC        NASA/NOAA/Copernicus   Resolution differs
Wind              IMD/MOSDAC           NOAA/Copernicus        Compare timestamps
Waves             INCOIS               Copernicus             Forecast metadata
Currents          INCOIS               Copernicus             Resolution matters
Argo T/S          INCOIS Argo          Global Argo/Copernicus Observation sparse
Bathymetry        GEBCO                auth. charts           Not a nav chart
General map       OSM                  other map sources      Not safety authority
```

### Critical Fallback Rules

```text
1. authoritative warning source unavailable -> do NOT fabricate equivalent warning
2. PFZ unavailable -> say "PFZ data currently unavailable" (do not substitute)
3. SST unavailable from primary -> use fallback but REPORT the substitution
4. Never silently substitute a source
```

---

# 19. MOSDAC Access Constraints (Engineering Reality)

> MOSDAC access is NOT freely available in real-time for all users.

```text
Registered General Users:    limited access, 3-day latency
Registered Privileged Users: all data, NRT access
Anonymous Users:             metadata/image/open data only, NRT access
```

### SSTM Status

Oceansat-3 SSTM has developed a technical problem in its scan mechanism and is NOT operating as of September 2026.

```text
SSTM connector -> Keep capability -> Do NOT depend on it for V1 live SST

SST fallback chain:
  INCOIS -> other Indian operational -> NOAA -> Copernicus -> NASA
```

---

# 20. Evidence-Fused Marine State (Replaces "4D-Var" Language)

> ORCA does NOT perform numerical ocean data assimilation. Do not claim "4D-Var."

### What ORCA Actually Does

```text
observations / forecast products / advisories
              |
              v
ORCA harmonization and evidence fusion
              |
              v
EVIDENCE-FUSED MARINE STATE
(also: Decision-Ready Marine State)
```

### Correct Terminology

DO NOT say: "ORCA performs 4D-Var ocean assimilation"
DO say: "ORCA constructs an Evidence-Fused Marine State from heterogeneous sources"

### Marine State Structure

```text
MARINE STATE
+-- Ocean
|   +-- SST, Chlorophyll, Currents, Sea Level, Salinity, Fronts
+-- Atmosphere / Weather
|   +-- Wind, Waves, Swell, Rain, Lightning, Warnings
+-- Ecosystem
|   +-- Productivity, PFZ, Bloom Indicators
+-- Geography
|   +-- EEZ, MPA, Restricted Zones, Ports, Bathymetry
+-- Human Activity
|   +-- Maritime Activity Context
+-- Temporal
    +-- Current, Forecast, Historical, Trend/Event State
```

### 4D-Capable Terminology

```text
X = longitude
Y = latitude
Z = depth (where available)
T = time

Most V1 products are surface: X * Y * T
Say "4D-Capable Marine State" not "4D Marine State"
(depth data available for Argo profiles, bathymetry, MLD/D20)
```

---

# 21. State Versioning and Delta Tracking

> Avoid recomputing the full state when only part changed.

### Versioned Snapshots

```text
MS-100  06:00 UTC
MS-101  09:00 UTC  (parent: MS-100)
MS-102  12:00 UTC  (parent: MS-101)
```

### State Delta

```text
STATE A
   +
NEW EVIDENCE
   |
   v
STATE DELTA
   |
   v
STATE B
```

Example delta:

```json
{
  "parent_state": "MS-100",
  "new_state": "MS-101",
  "changed": {
    "wave_height": {"old": 1.2, "new": 2.1},
    "marine_warning": {"old": false, "new": true}
  }
}
```

This enables:
- "What changed?" -> show delta
- "Has risk increased?" -> compare states
- "Why did the alert trigger?" -> show the specific change

### 4D Query Operations

```text
STATE_NOW                              - current marine state
STATE_AT(location, time)               - state at point in space-time
STATE_TIMESERIES(region, var, t1, t2)  - variable over time in region
STATE_DEPTH_PROFILE(location, depths)  - vertical profile at location
STATE_DIFF(region, t1, t2)             - what changed between times
STATE_FORECAST(region, valid_time)     - predicted future state
STATE_ALONG_ROUTE(route, time_window)  - conditions along travel path
```

STATE_ALONG_ROUTE is critical for route optimization because conditions vary along both space and travel time.

---

# 22. Enhanced Source Conflict Engine

> When sources disagree, don't arbitrarily pick one. Report the disagreement.

```text
INCOIS SST = 28.1 C
NOAA SST   = 27.8 C
Copernicus = 28.0 C
Buoy       = 28.2 C
```

### Conflict Resolution Considerations

```text
time difference       - are observations from the same time?
distance              - are they at the same location?
resolution            - 1km vs 25km grid
observation vs forecast - different semantic types
quality flags         - any flagged as suspect?
provider methodology  - different algorithms/sensors
```

### Output

```text
agreement:   sources within 0.3 C -> HIGH AGREEMENT
disagreement: sources differ by > 1.0 C -> FLAG
confidence:  weighted by freshness, resolution, type
```

DO NOT: silently select one source
DO: report agreement level and selected value with reasoning
