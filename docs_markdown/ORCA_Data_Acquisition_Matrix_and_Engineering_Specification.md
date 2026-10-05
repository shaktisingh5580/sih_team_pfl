# ORCA Marine Ecosystem Reasoning with Collaborative Agents

# Data Acquisition Matrix & Engineering Specification

**Problem Statement:** ORCA --- Marine EcOsystem Reasoning with
Collaborative Agents\
**Problem Statement ID:** 26176\
**Organization:** ISRO / Department of Space\
**Document role:** Engineering continuation of the ORCA Data System /
Data Foundation document\
**Status:** Detailed research and implementation specification\
**Research basis:** Official provider documentation and current
data-access documentation reviewed in September 2026

------------------------------------------------------------------------

# 0. INTRODUCTION --- WHAT IS ALREADY COVERED

The previous Data System specification established the foundation:

-   ORCA needs heterogeneous satellite, oceanographic, meteorological,
    hazard, historical and geospatial data.
-   Primary Indian sources are INCOIS, MOSDAC/ISRO, IMD and
    authoritative Indian GIS.
-   Important secondary/validation sources include Copernicus Marine,
    NOAA CoastWatch and NASA.
-   Argo and BGC-Argo are important in-situ layers.
-   GEBCO provides bathymetry.
-   Raw scientific formats must be preserved.
-   ORCA should use a RAW → NORMALIZED → DERIVED data lifecycle.
-   Scientific arrays should remain in NetCDF/Zarr/GeoTIFF where
    appropriate.
-   PostgreSQL/PostGIS should hold metadata and spatial information.
-   Parquet should be used for large analytical tables.
-   A Data Catalog should describe available datasets.
-   A Data Quality system must track freshness, timestamps, coverage and
    quality flags.
-   A Data Discovery capability should determine which datasets are
    needed for a user task.

This document continues from that point.

The question now is:

> **Exactly how does ORCA acquire, validate, normalize, store, expose
> and select each dataset?**

This document therefore moves from **"what data exists?"** to **"how do
we engineer the complete acquisition system?"**

The current official sources confirm that INCOIS exposes an ERDDAP
service for scientific data and lists Argo, buoys, HF radar, tide
gauges, ROMS and PFZ among its holdings; MOSDAC provides Oceansat-3
products and has a documented access policy; Copernicus Marine provides
a programmatic Toolbox for catalogue discovery, subsetting and
downloads; NOAA CoastWatch provides a portal and ERDDAP access; and
GEBCO provides current 2026 bathymetry downloads and OPeNDAP access.
citeturn1search3turn1search9turn0search6turn0search11turn0search5turn1search0

------------------------------------------------------------------------

# 1. THE CORE DATA ACQUISITION PRINCIPLE

ORCA should not be implemented as:

``` text
Agent
 ↓
Call random API
 ↓
Get data
 ↓
Ask LLM what it means
```

That architecture is fragile.

Instead:

``` text
User task
    ↓
Data requirement planning
    ↓
Data catalog discovery
    ↓
Source selection
    ↓
Connector selection
    ↓
Acquisition
    ↓
Raw preservation
    ↓
Validation
    ↓
Normalization
    ↓
Spatial/temporal alignment
    ↓
Scientific processing
    ↓
Evidence creation
    ↓
Data Query API
    ↓
Agents
```

The acquisition system is therefore a **controlled scientific data
infrastructure**, not merely a collection of API calls.

------------------------------------------------------------------------

# 2. FINAL DATA-SOURCE INVENTORY

## 2.1 Primary Indian sources

  -----------------------------------------------------------------------
  Source                              Primary responsibility
  ----------------------------------- -----------------------------------
  INCOIS                              Ocean observations, forecasts, PFZ,
                                      Argo, buoys, ocean products

  MOSDAC / ISRO                       Indian satellite Earth observation

  IMD                                 Weather, marine forecasts, cyclone
                                      and weather warnings

  Authoritative Indian GIS            Maritime boundaries, coastline,
                                      protected/restricted zones, ports
  -----------------------------------------------------------------------

## 2.2 International scientific sources

  -----------------------------------------------------------------------
  Source                              Primary responsibility
  ----------------------------------- -----------------------------------
  Copernicus Marine                   Ocean forecasts, reanalysis,
                                      observations, biogeochemistry

  NOAA CoastWatch                     Satellite ocean observations and
                                      validation

  NASA Ocean Color / Earthdata        Historical ocean colour and
                                      satellite research data
  -----------------------------------------------------------------------

## 2.3 Physical/geospatial sources

  Source          Primary responsibility
  --------------- ----------------------------
  GEBCO           Global bathymetry
  OpenStreetMap   General geographic context

------------------------------------------------------------------------

# 3. MASTER DATA ACQUISITION MATRIX

This is the high-level matrix that the implementation team should use
before writing connectors.

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------
  ID        Domain       Dataset           Provider                 Main variables              Type                   Access pattern                 Priority
  --------- ------------ ----------------- ------------------------ --------------------------- ---------------------- ------------------------------ -------------
  IN-01     Ocean        Argo profiles     INCOIS                   Temperature, salinity,      Observation            ERDDAP                         Critical
                                                                    pressure                                                                          

  IN-02     Ocean        Argo gridded      INCOIS                   T/S, errors                 Derived                ERDDAP                         High
                         products                                                                                                                     

  IN-03     Ocean        PFZ               INCOIS                   PFZ locations/advisories    Advisory/derived       Portal/download                Critical

  IN-04     Ocean        Ocean State       INCOIS                   Wind, waves, currents, SST, Forecast               Operational service            Critical
                         Forecast                                   MLD, D20                                                                          

  IN-05     Ocean        Drifting buoys    INCOIS                   Pressure, SST, currents     Observation            Portal/ERDDAP where available  High

  IN-06     Ocean        Moored buoys      INCOIS                   Wind, waves, SST, currents, Observation            Visualization /                High
                                                                    met-ocean                                          source-specific access         

  IN-07     Ocean        HF Radar          INCOIS                   Surface current vectors     Observation            Registered service             High

  IN-08     Ocean        Tide gauges       INCOIS                   Sea level                   Observation            Ocean observation service      High

  IN-09     Ocean        Tsunami buoys     INCOIS                   Sea level                   Hazard observation     Warning service                Critical

  IN-10     Ocean        ROMS              INCOIS                   SST, MLD, D20, currents     Model                  Product/service                High

  MS-01     EO           OCM-3             MOSDAC/ISRO              Ocean colour, derived       Satellite              MOSDAC                         Critical
                                                                    products                                                                          

  MS-02     EO           SCAT-3            MOSDAC/ISRO              Surface wind vectors        Satellite              MOSDAC                         High

  MS-03     EO           SSTM              MOSDAC/ISRO              SST                         Satellite              MOSDAC                         Conditional

  MS-04     EO           INSAT products    MOSDAC/ISRO              Weather/ocean/atmospheric   Satellite              MOSDAC                         High
                                                                    products                                                                          

  IM-01     Weather      Current weather   IMD                      Wind, temp, pressure etc.   Observation            REST API                       High

  IM-02     Weather      Forecast          IMD                      Weather forecast            Forecast               REST API                       Critical

  IM-03     Marine       Marine bulletins  IMD                      Marine conditions           Advisory               REST/API                       Critical

  IM-04     Marine       Fishermen warning IMD                      Warning/advisory            Advisory               REST/API                       Critical

  IM-05     Hazard       Cyclone           IMD                      Track, wind, cone           Forecast/advisory      REST/API                       Critical

  IM-06     Hazard       Lightning         IMD                      Lightning                   Hazard                 REST/API                       High
                                                                    observations/nowcast                                                              

  IM-07     Hazard       Radar             IMD                      Radar imagery               Observation            Service                        High

  GIS-01    GIS          Coastline         Indian authoritative     Geometry                    Static                 File/service                   Critical
                                           source                                                                                                     

  GIS-02    GIS          EEZ               Indian authoritative     Polygon                     Static                 File/service                   Critical
                                           source                                                                                                     

  GIS-03    GIS          Ports/harbours    Authoritative/verified   Point/geometry              Static                 File/service                   High
                                           GIS                                                                                                        

  GIS-04    GIS          Restricted zones  Authoritative source     Polygon                     Static                 File/service                   Critical

  GIS-05    GIS          Protected areas   Authoritative source     Polygon                     Static                 File/service                   High

  GB-01     Bathymetry   GEBCO_2026        GEBCO                    Elevation/depth             Static grid            NetCDF/GeoTIFF/ASCII/OPeNDAP   High

  CM-01     Ocean        Global physics    Copernicus               T/S/current/SSH etc.        Model/reanalysis       Toolbox                        High

  CM-02     Ocean        Waves             Copernicus               Wave variables              Model                  Toolbox                        High

  CM-03     Bio          Biogeochemistry   Copernicus               CHL/O2/nutrients etc.       Model                  Toolbox                        Medium

  NOAA-01   EO           SST               NOAA                     SST                         Satellite              Portal/ERDDAP                  Medium

  NOAA-02   EO           Ocean colour      NOAA                     CHL/Kd490 etc.              Satellite              Portal/ERDDAP                  Medium

  NASA-01   EO           Ocean colour      NASA                     Ocean-colour products       Historical/satellite   Earthdata/Ocean Color          Medium
                         archive                                                                                                                      

  OSM-01    GIS          Geographic        OSM                      Roads/places/facilities     Static                 API/download                   Medium
                         context                                                                                                                      
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------

# 4. INCOIS --- DETAILED ACQUISITION SPECIFICATION

INCOIS should be treated as the primary Indian ocean-data ecosystem.

Its current data holdings explicitly list drifting buoys, moored buoys,
Argo floats, HF radar, tide gauges, tsunami buoys, ROMS, PFZ and other
ocean datasets. The holdings page also exposes information about mode of
reception, availability, formats and accessibility. citeturn1search3

INCOIS also operates an ERDDAP service specifically intended to provide
consistent access to scientific ocean datasets and subsets.
citeturn1search9

------------------------------------------------------------------------

# 5. INCOIS ARGO

## 5.1 Purpose

Argo is one of ORCA's most important in-situ data sources.

Core variables:

``` text
temperature
salinity
pressure
latitude
longitude
time
cycle number
quality flags
```

INCOIS currently lists Argo temperature and salinity profiles from 2000
onward, with public visualization/download facilities for open-ocean
data. citeturn1search3

------------------------------------------------------------------------

## 5.2 Acquisition

Primary route:

``` text
INCOIS ERDDAP
        ↓
Dataset discovery
        ↓
Spatial/time subset
        ↓
Machine-readable retrieval
```

INCOIS ERDDAP is designed specifically to provide consistent subsetting
and download of scientific datasets in common formats.
citeturn1search9

The connector should support:

``` text
time range
latitude range
longitude range
depth/pressure
platform
cycle
variable selection
```

------------------------------------------------------------------------

## 5.3 Storage

Raw:

``` text
raw/incois/argo/
```

Normalized:

``` text
Parquet
```

or a scientific profile representation.

For gridded Argo:

``` text
Zarr / NetCDF
```

Metadata:

``` text
PostgreSQL/PostGIS
```

------------------------------------------------------------------------

## 5.4 Argo canonical record

``` json
{
  "platform_id": "...",
  "cycle_number": 123,
  "latitude": 15.2,
  "longitude": 68.4,
  "observation_time": "...",
  "pressure": 100.0,
  "temperature": 22.4,
  "salinity": 35.7,
  "temperature_qc": "1",
  "salinity_qc": "1",
  "source": "INCOIS",
  "dataset": "ARGO"
}
```

------------------------------------------------------------------------

# 6. BGC-ARGO

BGC-Argo should be represented as an extension of the Argo subsystem.

Potential variables:

``` text
oxygen
chlorophyll fluorescence
backscatter
nitrate
pH
irradiance
```

The exact variables depend on the float and sensor configuration.

ORCA should therefore never assume every Argo float has every BGC
variable.

Schema should use:

``` text
variable availability = dynamic
```

rather than a rigid fixed record.

------------------------------------------------------------------------

# 7. INCOIS PFZ

PFZ is an operationally valuable product.

Acquisition should preserve:

``` text
advisory ID
issue time
valid time if supplied
PFZ geometry/location
reference landmark
distance
direction
source
original advisory
```

PFZ should be classified:

``` text
data_type = advisory
```

and not:

``` text
data_type = direct observation
```

ORCA should use PFZ as an input to a broader decision system.

------------------------------------------------------------------------

# 8. INCOIS OCEAN STATE FORECAST

Current OSF layers include:

-   wind
-   significant wave height
-   wave period
-   swell height
-   swell period
-   surface currents
-   SST
-   mixed-layer depth
-   D20
-   chlorophyll
-   particulate organic carbon
-   particulate inorganic carbon
-   aerosol optical thickness
-   Kd490

The current official OSF interface exposes coastal and regional forecast
selection. citeturn0search18

------------------------------------------------------------------------

## 8.1 Forecast representation

Every forecast value must include:

``` text
model/source
initialization time
valid time
lead time
variable
unit
spatial coordinate/grid
```

Example:

``` json
{
  "variable": "significant_wave_height",
  "value": 1.8,
  "unit": "m",
  "forecast_initialization": "...",
  "forecast_valid_time": "...",
  "source": "INCOIS_OSF"
}
```

------------------------------------------------------------------------

# 9. INCOIS BUOYS

INCOIS lists:

### Drifting buoy

Potential:

``` text
atmospheric pressure
SST
ocean currents
```

with real-time availability and historical records extending from 1991
in the current holdings table.

### Moored buoy

Potential:

``` text
pressure
temperature
humidity
wind
currents
SST
conductivity
waves
rainfall
radiation
irradiance
temperature profiles
salinity profiles
```

The current INCOIS holdings table identifies differing access
restrictions: drifting buoy data has public visualization/download,
while moored buoy data is listed as visualization-only.
citeturn1search3

This distinction must be recorded in the source catalog.

------------------------------------------------------------------------

# 10. INCOIS HF RADAR

HF radar:

``` text
surface current vectors
```

Use for:

-   coastal current mapping
-   current validation
-   route analysis
-   coastal transport

The current INCOIS holdings page identifies HF Radar current-vector data
as real-time and requiring registered access. citeturn1search3

------------------------------------------------------------------------

# 11. INCOIS TIDE GAUGES

Use:

``` text
sea level
time
station
location
quality
```

Applications:

-   tide context
-   coastal hazard
-   sea-level anomalies
-   validation

------------------------------------------------------------------------

# 12. INCOIS TSUNAMI BUOYS

Treat tsunami information as:

``` text
hazard / authoritative warning
```

not a generic ocean measurement.

The ingestion system must preserve the original warning and timestamp.

------------------------------------------------------------------------

# 13. INCOIS ROMS / MODEL PRODUCTS

Current holdings identify ROMS products including:

``` text
SST
MLD
D20
currents
```

with near-real-time availability. citeturn1search3

Store model metadata separately from observations.

------------------------------------------------------------------------

# 14. MOSDAC / ISRO ACQUISITION

MOSDAC is the principal Indian satellite data portal relevant to ORCA.

EOS-06/Oceansat-3 carries:

``` text
OCM-3
SCAT-3
SSTM
ARGOS
```

MOSDAC documents OCM-3 at 366 m LAC and 1.1 km GAC and SCAT-3 ocean
surface wind-vector modes including 12.5 km and 25 km modes, plus an
experimental 5 km mode. citeturn0search2turn0search3

------------------------------------------------------------------------

# 15. MOSDAC ACCESS POLICY

This must be included in the Data Catalog.

MOSDAC's current access policy distinguishes:

``` text
Registered General Users
Registered Privileged Users
Anonymous Users
```

with different data availability and latency. The current policy states
general users have limited access with a 3-day latency, privileged users
can access all data with NRT access, and anonymous users can access
metadata/image/open data with NRT access. citeturn0search6

Therefore:

> **Do not assume every MOSDAC product is freely accessible in real time
> without registration.**

The connector must know the access profile required for each dataset.

------------------------------------------------------------------------

# 16. OCM-3

OCM-3:

``` text
13 bands
Visible/NIR
LAC ≈ 366 m
GAC ≈ 1.1 km
```

Potential products include ocean-colour and derived products.

MOSDAC's current Oceansat-3 references include documentation for
chlorophyll, aerosol optical depth, inherent optical properties,
fluorescence line height, particulate organic carbon and other derived
products. citeturn0search0turn0search3

For ORCA, prioritize:

``` text
chlorophyll
ocean colour
optical properties
productivity-related products
```

where the operational product is available and documented.

------------------------------------------------------------------------

# 17. SCAT-3

SCAT-3 provides ocean surface wind vectors.

Store:

``` text
wind speed
wind direction
u component
v component where provided
time
location
quality
resolution
```

Use:

-   marine weather
-   fishing conditions
-   air-sea interaction
-   storm analysis
-   model validation

------------------------------------------------------------------------

# 18. SSTM

MOSDAC currently states that Oceansat-3 SSTM developed a technical
problem in its scan mechanism and is not operating at present.
citeturn0search16

Therefore:

``` text
SSTM connector
    ↓
Keep connector capability
    ↓
Do not depend on it for V1 live SST
```

SST fallback chain:

``` text
INCOIS
 ↓
other operational Indian products
 ↓
NOAA
 ↓
Copernicus
 ↓
NASA/research source
```

The exact priority should depend on the variable's operational status
and intended use.

------------------------------------------------------------------------

# 19. IMD ACQUISITION

IMD should be the primary atmospheric and warning source.

The source catalog should distinguish:

``` text
observation
forecast
nowcast
warning
bulletin
cyclone product
```

These are not interchangeable.

------------------------------------------------------------------------

# 20. IMD DATA CONNECTORS

Connector groups:

``` text
imd/
├── weather/
├── forecast/
├── marine/
├── fishermen/
├── cyclone/
├── lightning/
├── radar/
└── warnings/
```

Each should preserve:

``` text
issued_at
valid_from
valid_to
location/region
warning_level
original_text
structured variables
source URL/identifier
```

------------------------------------------------------------------------

# 21. IMD CYCLONE

Cyclone records should contain:

``` text
cyclone ID
storm name if applicable
issue time
current position
forecast positions
wind
pressure where available
cone information
warning category
validity
```

Do not flatten the entire cyclone forecast into one point.

A cyclone is a **time-evolving track**.

------------------------------------------------------------------------

# 22. IMD MARINE WARNINGS

Marine warning data should be treated as authoritative operational
evidence.

Store:

``` text
bulletin ID
issue time
marine area
valid period
hazard
wind
sea state
warning text
source
```

This can later be transformed into spatial polygons and temporal
intervals.

------------------------------------------------------------------------

# 23. GIS ACQUISITION

GIS is different because many layers are slow-changing.

Recommended update pattern:

``` text
Static authoritative GIS
    ↓
Periodic verification
    ↓
Versioned local copy
```

Every layer needs:

``` text
source
version
effective date
geometry CRS
license
authority
last verified
```

------------------------------------------------------------------------

# 24. GEBCO ACQUISITION

GEBCO_2026 is the current global grid.

It provides a 15 arc-second grid, user-defined-area downloads, NetCDF,
GeoTIFF and ASCII, and OPeNDAP access. The global NetCDF file is about 7
GB uncompressed and the TID grid is about 3.5 GB uncompressed.
citeturn1search0turn1search1

For ORCA:

**Do not download the entire global grid for the hackathon.**

Instead:

``` text
Gujarat / Arabian Sea bounding box
        ↓
GEBCO subset
        ↓
regional GeoTIFF/NetCDF
        ↓
local object storage
```

GEBCO's current download system supports user-defined areas.
citeturn1search1

GEBCO also provides OPeNDAP access through CEDA. citeturn1search1

------------------------------------------------------------------------

# 25. GEBCO TID GRID

The Type Identifier Grid is useful because it tells ORCA what kind of
source contributed to each bathymetric cell.

This can be stored as:

``` text
bathymetry.tif
bathymetry_tid.tif
```

or corresponding NetCDF/Zarr arrays.

Do not treat every GEBCO cell as equally measured.

------------------------------------------------------------------------

# 26. COPERNICUS MARINE ACQUISITION

Copernicus Marine now provides an official Toolbox with:

``` text
catalogue discovery
metadata
subset
original-file download
remote dataset access
Python API
CLI
```

The current official documentation describes the Toolbox as the
supported programmatic route for accessing Copernicus Marine data.
citeturn0search11

------------------------------------------------------------------------

# 27. COPERNICUS CATALOGUE-FIRST WORKFLOW

Do not hard-code every Copernicus dataset ID into agents.

Instead:

``` text
ORCA requirement
       ↓
Copernicus catalogue
       ↓
describe metadata
       ↓
find suitable dataset
       ↓
select variables
       ↓
select region/time
       ↓
subset
```

The Toolbox's catalogue API supports programmatic metadata discovery.
citeturn0search17

------------------------------------------------------------------------

# 28. COPERNICUS SUBSETTING

For large data, do not download the entire dataset.

Use:

``` text
dataset_id
variables
minimum longitude
maximum longitude
minimum latitude
maximum latitude
start datetime
end datetime
```

The official Toolbox supports subsetting and can produce NetCDF, Zarr
and CSV for gridded data; sparse datasets can be retrieved in CSV,
Parquet and NetCDF according to the current documentation.
citeturn0search8turn0search14

------------------------------------------------------------------------

# 29. COPERNICUS CREDENTIALS

Copernicus Marine programmatic access requires an account/credentials.

Therefore source registry:

``` json
{
  "provider": "Copernicus Marine",
  "authentication": "required",
  "credential_type": "account",
  "secret_storage": "environment/secret manager"
}
```

Never put credentials into the agent prompt or source code.

------------------------------------------------------------------------

# 30. NOAA COASTWATCH

NOAA CoastWatch provides:

-   data portal
-   downloadable products
-   geographic/temporal subsets
-   ERDDAP
-   NetCDF/HDF processing tools

The current NOAA documentation specifically identifies ERDDAP as a
consistent method for subsetting and downloading gridded Level-3+
environmental datasets. citeturn0search5

The CoastWatch portal supports full-extent or subset downloads, with
NetCDF for mapped/gridded data. citeturn0search15

------------------------------------------------------------------------

# 31. NOAA ERDDAP CONNECTOR

ORCA should reuse the generic ERDDAP connector architecture.

Instead of:

``` text
incois_erddap.py
noaa_erddap.py
another_erddap.py
```

build:

``` text
connectors/
    erddap/
        client.py
        catalog.py
        query.py
        parser.py
```

Then configure:

``` yaml
providers:
  incois:
    erddap_url: ...
  noaa:
    erddap_url: ...
```

This reduces engineering duplication.

------------------------------------------------------------------------

# 32. NASA OCEAN DATA

NASA should primarily support:

``` text
historical
research
validation
ocean colour
long-term trends
```

Do not make NASA the first operational safety source.

The NASA connector should therefore be optimized for:

``` text
historical query
spatial subset
temporal subset
product metadata
scientific validation
```

------------------------------------------------------------------------

# 33. OPENSTREETMAP

Use OSM for:

``` text
general geographic context
roads
places
facilities
harbour context
coastal infrastructure
```

Do not use OSM as the authoritative source for:

``` text
EEZ
navigation warnings
official restricted areas
safety boundaries
```

where authoritative government sources exist.

------------------------------------------------------------------------

# 34. GENERIC CONNECTOR INTERFACE

All connectors should implement a common interface.

Conceptually:

``` python
class DataConnector:

    def discover(self, requirement):
        ...

    def get_metadata(self, dataset_id):
        ...

    def query(self, request):
        ...

    def download(self, request):
        ...

    def validate(self, dataset):
        ...

    def normalize(self, dataset):
        ...
```

The implementation can vary by provider.

The interface should not.

------------------------------------------------------------------------

# 35. DATASET REQUEST OBJECT

Agents should not pass arbitrary provider-specific parameters.

They should create a canonical request.

Example:

``` json
{
  "domain": "ocean",
  "variables": [
    "sst",
    "chlorophyll",
    "wave_height"
  ],
  "region": {
    "type": "bbox",
    "min_lat": 18.0,
    "max_lat": 23.0,
    "min_lon": 68.0,
    "max_lon": 73.0
  },
  "time": {
    "start": "2026-09-16T00:00:00Z",
    "end": "2026-09-17T12:00:00Z"
  },
  "data_type": [
    "forecast",
    "observation"
  ]
}
```

The Data Discovery system translates this into provider-specific
requests.

------------------------------------------------------------------------

# 36. DATASET RESPONSE OBJECT

The connector should return:

``` json
{
  "dataset_id": "incois_osf",
  "source": "INCOIS",
  "status": "success",
  "retrieved_at": "...",
  "data_type": "forecast",
  "coverage": {
    "spatial": "...",
    "temporal": "..."
  },
  "files": [
    {
      "path": "...",
      "format": "netcdf"
    }
  ],
  "metadata": {
    "variables": [],
    "units": {},
    "resolution": {}
  }
}
```

------------------------------------------------------------------------

# 37. INGESTION MANAGER

The ingestion manager orchestrates connectors.

``` text
Ingestion Manager
│
├── schedule acquisition
├── select connector
├── authenticate
├── request data
├── retry failures
├── verify response
├── checksum
├── store raw
├── update catalog
└── emit ingestion event
```

------------------------------------------------------------------------

# 38. RAW DATA NAMING

Use deterministic object paths.

Example:

``` text
raw/
  incois/
    argo/
      2026/
        09/
          15/
            platform_2901234_cycle_123.nc
```

For forecast:

``` text
raw/
  incois/
    osf/
      waves/
        2026/
          09/
            15/
              init_20260915T060000.nc
```

This makes reproducibility easier.

------------------------------------------------------------------------

# 39. CHECKSUMS AND DUPLICATES

Every downloaded file should record:

``` text
SHA-256
size
retrieved_at
source URL
source modification time if available
dataset version
```

If the same content is downloaded again:

``` text
same checksum
    ↓
do not duplicate
```

------------------------------------------------------------------------

# 40. RETRY POLICY

Connectors should support:

``` text
timeout
retry
exponential backoff
maximum retry count
circuit breaker
```

Example:

``` text
attempt 1 → immediate
attempt 2 → 2 sec
attempt 3 → 5 sec
attempt 4 → 15 sec
```

Actual values can be configured.

------------------------------------------------------------------------

# 41. DATA FRESHNESS ENGINE

Every dataset gets:

``` text
observation_age
forecast_age
retrieval_age
```

Example:

``` json
{
  "observation_time": "...",
  "retrieved_at": "...",
  "age_hours": 4.2,
  "freshness_class": "fresh"
}
```

Freshness thresholds must be variable-specific.

Do not use one global rule.

------------------------------------------------------------------------

# 42. SPATIAL ALIGNMENT ENGINE

Sources can have:

``` text
point
line
polygon
raster
grid
trajectory
```

The spatial engine should support:

``` text
point lookup
nearest neighbor
polygon aggregation
raster sampling
spatial intersection
buffer
distance
point-in-polygon
route intersection
```

------------------------------------------------------------------------

# 43. TEMPORAL ALIGNMENT ENGINE

Support:

``` text
observation time
forecast initialization
forecast valid time
interval
trajectory time
advisory validity
```

Important distinction:

``` text
forecast_init_time ≠ forecast_valid_time
```

This must never be lost.

------------------------------------------------------------------------

# 44. SPATIO-TEMPORAL JOIN

Example:

``` text
User location:
20.5 N, 69.7 E

Requested:
2026-09-16 06:00

ORCA:
1. find nearest grid cell
2. find valid forecast timestamp
3. retrieve forecast
4. find nearby observations
5. calculate spatial distance
6. compare observation/model
7. attach uncertainty
```

------------------------------------------------------------------------

# 45. OBSERVATION VS FORECAST

Canonical schema:

``` text
data_type:
  observation
  forecast
  advisory
  derived
  historical
  static
```

Forecast:

``` text
forecast_initialization_time
forecast_valid_time
lead_time
```

Observation:

``` text
observation_time
```

Advisory:

``` text
issued_time
valid_from
valid_to
```

Derived:

``` text
input_evidence_ids
processing_method
processing_version
```

------------------------------------------------------------------------

# 46. PROVENANCE

Every derived result should preserve its inputs.

Example:

``` json
{
  "derived_product": "fishing_suitability",
  "method_version": "1.0",
  "inputs": [
    "EV-001",
    "EV-002",
    "EV-003",
    "EV-004"
  ],
  "generated_at": "...",
  "software_version": "..."
}
```

This allows ORCA to answer:

> "Why did you recommend this location?"

------------------------------------------------------------------------

# 47. EVIDENCE OBJECT

Canonical evidence:

``` json
{
  "evidence_id": "EV-001",
  "source": "INCOIS",
  "dataset": "OSF",
  "variable": "wave_height",
  "value": 1.8,
  "unit": "m",
  "data_type": "forecast",
  "forecast_initialization": "...",
  "forecast_valid_time": "...",
  "location": {
    "lat": 20.4,
    "lon": 69.8
  },
  "quality": "valid",
  "retrieved_at": "..."
}
```

------------------------------------------------------------------------

# 48. DATA SOURCE PRIORITY

Priority must be variable-specific.

Example:

## Cyclone warning

``` text
IMD authoritative warning
        ↓
Do not override with generic model
```

## PFZ

``` text
INCOIS PFZ
        ↓
Use as primary advisory
```

## SST

``` text
Operational Indian source
        ↓
Copernicus / NOAA / NASA validation/fallback
```

## Bathymetry

``` text
GEBCO scientific context
        ↓
authoritative navigation data where required
```

------------------------------------------------------------------------

# 49. FALLBACK MATRIX

  -------------------------------------------------------------------------------
  Variable          Primary              Fallback               Important
                                                                restriction
  ----------------- -------------------- ---------------------- -----------------
  PFZ               INCOIS               None                   Do not invent PFZ

  Cyclone warning   IMD                  Official contextual    Do not override
                                         sources                

  Fishermen warning IMD                  INCOIS context         Preserve warning

  Tsunami           INCOIS               None                   Authoritative
                                                                warning

  SST               INCOIS/operational   Copernicus/NOAA/NASA   Check latency
                    source                                      

  Chlorophyll       INCOIS/MOSDAC        NASA/NOAA/Copernicus   Resolution
                                                                differs

  Wind              IMD/MOSDAC           NOAA/Copernicus        Compare
                                                                timestamps

  Waves             INCOIS               Copernicus             Forecast metadata

  Currents          INCOIS               Copernicus             Resolution
                                                                matters

  Argo T/S          INCOIS Argo          Global Argo/Copernicus Observation
                                                                sparse

  Bathymetry        GEBCO                authoritative charts   Not a navigation
                                         where available        chart

  General map       OSM                  other map sources      Not safety
                                                                authority
  -------------------------------------------------------------------------------

------------------------------------------------------------------------

# 50. DATA AVAILABILITY SERVICE

Before retrieval, ORCA should ask:

``` text
Does the source have the required variable?
Does it cover the region?
Does it cover the requested time?
Is it fresh enough?
Is access currently available?
```

Example:

``` json
{
  "dataset": "argo",
  "region": "Arabian Sea",
  "time": "2026-09-16",
  "available": true,
  "latest_profile_age_hours": 31,
  "spatial_density": "sparse"
}
```

This prevents hallucinated availability.

------------------------------------------------------------------------

# 51. DATA CATALOG SCHEMA

Recommended table:

``` text
dataset_registry
----------------
dataset_id
provider
dataset_name
description
domain
variables
data_type
spatial_coverage
temporal_coverage
spatial_resolution
temporal_resolution
update_frequency
access_method
endpoint
format
authentication
license
primary_for
fallback_sources
quality_notes
status
last_verified
```

------------------------------------------------------------------------

# 52. VARIABLE REGISTRY

Separate dataset registry from variable registry.

``` text
variable_registry
-----------------
variable_id
canonical_name
aliases
unit
domain
description
valid_range
aggregation_method
preferred_sources
fallback_sources
```

Example:

``` json
{
  "variable_id": "sst",
  "canonical_name": "sea_surface_temperature",
  "aliases": [
    "SST",
    "sea_surface_temp"
  ],
  "unit": "degC",
  "domain": "ocean"
}
```

------------------------------------------------------------------------

# 53. UNIT NORMALIZATION

External providers may use different units.

ORCA should define canonical units.

Examples:

``` text
temperature → °C
salinity → PSU / provider-defined practical salinity convention
wave height → m
wind speed → m/s
pressure → Pa or hPa according to canonical convention
distance → km
depth → m
time → UTC ISO 8601
```

Do not silently convert without recording the transformation.

------------------------------------------------------------------------

# 54. COORDINATE REFERENCE SYSTEM

Canonical spatial standard:

``` text
WGS84
EPSG:4326
```

unless a scientific raster requires a native projection.

Store:

``` text
native_crs
canonical_crs
transformation_method
```

------------------------------------------------------------------------

# 55. TEMPORAL STANDARD

Use:

``` text
UTC
ISO 8601
```

internally.

Example:

``` text
2026-09-16T06:00:00Z
```

The UI can convert to local Indian time.

------------------------------------------------------------------------

# 56. DATA QUALITY STATES

Recommended:

``` text
VALID
SUSPECT
MISSING
STALE
INVALID
UNAVAILABLE
```

Do not simply discard questionable records.

------------------------------------------------------------------------

# 57. SOURCE CONFLICT ENGINE

Example:

``` text
INCOIS SST = 28.1
NOAA SST   = 27.8
Copernicus = 28.0
Buoy       = 28.2
```

The engine should consider:

``` text
time difference
distance
resolution
observation vs forecast
quality flags
provider methodology
```

Then report:

``` text
agreement
disagreement
confidence
```

rather than arbitrarily selecting one.

------------------------------------------------------------------------

# 58. CACHING

Use caching at multiple levels.

## Metadata cache

Long-lived.

``` text
dataset metadata
source catalog
variable registry
```

## Forecast cache

Shorter.

``` text
latest forecast cycle
```

## Satellite cache

Product-dependent.

## Warning cache

Very short-lived and refresh aggressively.

Never cache a safety warning indefinitely.

------------------------------------------------------------------------

# 59. SCHEDULING

Acquisition schedules should be dataset-specific.

Example:

``` text
IMD warnings
→ frequent polling

Forecasts
→ after forecast cycle

Satellite
→ after product availability

Argo
→ periodic refresh

GEBCO
→ version/update based

Static GIS
→ periodic verification
```

Do not use one universal cron schedule.

------------------------------------------------------------------------

# 60. DATA RETENTION

Recommended:

``` text
RAW
Long-term / according to storage budget

NORMALIZED
Long-term for important operational data

DERIVED
Versioned and reproducible

TEMPORARY CACHE
Short retention
```

For the hackathon:

Keep:

-   current data
-   selected historical window
-   raw examples
-   all derived outputs used in demonstrations

------------------------------------------------------------------------

# 61. DATA QUERY API

Agents should never directly know provider-specific URLs.

Expose ORCA APIs.

Example:

``` text
GET /api/ocean/sst
GET /api/ocean/chlorophyll
GET /api/ocean/waves
GET /api/ocean/currents
GET /api/ocean/argo
GET /api/weather/wind
GET /api/weather/rainfall
GET /api/hazard/cyclone
GET /api/hazard/lightning
GET /api/marine/warnings
GET /api/pfz
GET /api/gis/geofences
GET /api/gis/ports
GET /api/bathymetry
```

------------------------------------------------------------------------

# 62. Query API REQUEST EXAMPLE

``` json
{
  "region": {
    "type": "bbox",
    "bbox": [
      68.0,
      18.0,
      73.0,
      23.0
    ]
  },
  "time": {
    "start": "2026-09-16T00:00:00Z",
    "end": "2026-09-16T12:00:00Z"
  },
  "variables": [
    "sst",
    "chlorophyll",
    "wave_height",
    "wind"
  ]
}
```

------------------------------------------------------------------------

# 63. DATA DISCOVERY AGENT

The agent should reason at the semantic level.

User:

> "Find a safe productive fishing zone tomorrow morning."

Planner creates:

``` text
Need:
PFZ
SST
chlorophyll
waves
wind
currents
marine warning
cyclone
lightning
geofences
```

Data Discovery:

``` text
PFZ → INCOIS
SST → INCOIS
chlorophyll → INCOIS/MOSDAC
waves → INCOIS
wind → IMD/MOSDAC
cyclone → IMD
lightning → IMD
geofence → GIS
```

Then Retrieval executes.

------------------------------------------------------------------------

# 64. DATA DISCOVERY IS NOT DATA RETRIEVAL

Keep these separate.

### Discovery

Answers:

> Which datasets should we use?

### Retrieval

Answers:

> How do we obtain those datasets?

### Processing

Answers:

> How do we convert them into usable information?

This separation makes the system easier to test.

------------------------------------------------------------------------

# 65. DATA DISCOVERY ALGORITHM

Conceptually:

``` text
INPUT:
user task

1. classify task
2. extract location
3. extract time
4. extract user role
5. determine decision type
6. identify required variables
7. search catalog
8. rank datasets
9. check availability
10. select primary/fallback
11. generate retrieval plan
```

Output:

``` json
{
  "task": "...",
  "datasets": [
    {
      "dataset_id": "incois_osf",
      "variables": ["wave_height", "current"],
      "priority": 1
    }
  ]
}
```

------------------------------------------------------------------------

# 66. SOURCE RANKING

Dataset selection should score:

``` text
authority
freshness
spatial relevance
temporal relevance
resolution
availability
quality
coverage
```

Conceptually:

``` text
score =
authority
+ freshness
+ relevance
+ quality
+ coverage
```

The exact formula should be deterministic and configurable.

------------------------------------------------------------------------

# 67. SCIENTIFIC PROCESSING LAYER

The data system should expose reusable calculations.

## Ocean engine

``` text
SST anomaly
chlorophyll anomaly
gradient
front detection
MLD
D20
current statistics
```

## Weather engine

``` text
wind exposure
wave exposure
rainfall
lightning proximity
cyclone proximity
```

## Spatial engine

``` text
point-in-polygon
distance
intersection
geofence
nearest port
```

## Temporal engine

``` text
historical comparison
forecast matching
rolling averages
anomaly windows
```

------------------------------------------------------------------------

# 68. DERIVED PRODUCT VERSIONING

Every derived dataset needs:

``` text
method
method_version
software_version
input_dataset_versions
generated_at
parameters
```

Example:

``` json
{
  "product": "sst_anomaly",
  "method_version": "1.0",
  "baseline": "2015-2025_monthly",
  "input": "incois_sst",
  "generated_at": "..."
}
```

------------------------------------------------------------------------

# 69. HISTORICAL BASELINE ENGINE

For a question like:

> "Why did chlorophyll decrease?"

ORCA needs:

``` text
current value
7-day average
30-day average
seasonal average
historical climatology
```

A baseline should specify:

``` text
baseline period
spatial grid
temporal aggregation
missing-data handling
```

Do not call a single previous day the "historical baseline."

------------------------------------------------------------------------

# 70. ALERT DATA PIPELINE

Warnings should have a separate fast path.

``` text
IMD / INCOIS
       ↓
Alert ingestion
       ↓
Deduplication
       ↓
Spatial indexing
       ↓
Temporal indexing
       ↓
Affected-user calculation
       ↓
Notification
```

Chat should not be required for alerts.

------------------------------------------------------------------------

# 71. GEOSPATIAL ALERT MATCHING

Example:

``` text
Cyclone polygon/track
        +
User location
        +
User route
        ↓
Spatial intersection
        ↓
Affected?
```

This is deterministic geospatial computation.

------------------------------------------------------------------------

# 72. ROUTE DATA PIPELINE

Route planning needs:

``` text
start
destination
geofences
coastline
depth context
current
wind
waves
hazards
```

The route engine produces:

``` text
candidate routes
distance
ETA
hazard exposure
weather exposure
geofence violations
```

The LLM explains the result.

------------------------------------------------------------------------

# 73. SAFETY RULE

ORCA should distinguish:

``` text
scientific information
operational recommendation
authoritative warning
navigation authority
```

A model-derived recommendation must never be presented as an official
safety clearance.

------------------------------------------------------------------------

# 74. LOGGING AND OBSERVABILITY

Every acquisition should generate a trace:

``` text
request_id
source
dataset
query
started_at
completed_at
status
bytes
checksum
records
errors
```

Every agent task should be able to trace:

``` text
answer
 ↓
derived result
 ↓
evidence
 ↓
dataset
 ↓
raw file
 ↓
source
```

------------------------------------------------------------------------

# 75. FAILURE MODES

The system must explicitly handle:

### Source unavailable

``` text
primary unavailable
→ fallback
```

### No coverage

``` text
source exists
but region unavailable
→ report unavailable
```

### Stale data

``` text
data exists
but too old
→ mark stale
```

### Conflicting data

``` text
sources disagree
→ preserve both
→ calculate confidence
```

### Missing variable

``` text
required variable unavailable
→ identify incomplete decision
```

### Authentication failure

``` text
credential unavailable
→ fallback / degraded mode
```

------------------------------------------------------------------------

# 76. DEGRADED MODE

ORCA should still operate when some sources are unavailable.

Example:

``` text
INCOIS unavailable
       ↓
Copernicus + NOAA available
       ↓
scientific analysis possible
       ↓
but Indian operational advisory unavailable
       ↓
response explicitly states limitation
```

For a safety-critical warning, however:

``` text
authoritative warning source unavailable
       ↓
do not fabricate equivalent warning
```

------------------------------------------------------------------------

# 77. DATA SECURITY

Credentials should be stored in:

``` text
environment variables
secret manager
deployment secret store
```

Never:

``` text
LLM prompt
Git repository
frontend JavaScript
database plaintext
```

------------------------------------------------------------------------

# 78. API SECURITY

Internal APIs should support:

``` text
authentication
authorization
rate limits
request validation
logging
```

The public frontend should not receive provider credentials.

------------------------------------------------------------------------

# 79. HACKATHON-SCALE IMPLEMENTATION

Do not implement every source immediately.

## Phase 1

Build:

``` text
INCOIS Argo
INCOIS OSF
INCOIS PFZ
IMD marine/cyclone
GIS
GEBCO regional subset
```

## Phase 2

Add:

``` text
MOSDAC OCM
MOSDAC SCAT
INSAT
```

## Phase 3

Add:

``` text
Copernicus
NOAA
NASA
```

## Phase 4

Add:

``` text
BGC-Argo
HF Radar
tide gauges
advanced ecosystem products
```

------------------------------------------------------------------------

# 80. FIRST WORKING VERTICAL SLICE

The first complete demonstration should work like this:

``` text
User:
"Kal subah Gujarat ke paas fishing ke liye
safe aur productive area batao."

             ↓

Planner

             ↓

Data Discovery

             ↓

INCOIS PFZ
INCOIS SST
INCOIS chlorophyll
INCOIS waves
INCOIS currents
IMD wind
IMD fishermen warning
IMD cyclone
GIS restricted zones

             ↓

Data Retrieval

             ↓

Validation

             ↓

Spatial/Temporal Alignment

             ↓

Ocean Engine
Weather Engine
Spatial Engine

             ↓

Risk Engine

             ↓

Evidence Validator

             ↓

Recommendation

             ↓

Map + explanation + evidence
```

This single workflow demonstrates almost the entire PS.

------------------------------------------------------------------------

# 81. RECOMMENDED V1 STORAGE

``` text
MinIO
│
├── raw/
│   ├── incois/
│   ├── imd/
│   ├── mosdac/
│   ├── copernicus/
│   ├── noaa/
│   ├── nasa/
│   └── gebco/
│
├── normalized/
│
└── derived/
```

PostgreSQL/PostGIS:

``` text
datasets
variables
sources
observations
geometries
warnings
pfz
ports
geofences
evidence
derived_products
ingestion_runs
```

------------------------------------------------------------------------

# 82. RECOMMENDED TECHNOLOGY STACK

## Acquisition

``` text
Python
httpx / requests
xarray
pandas
netCDF4
h5py
rasterio
geopandas
```

## Scientific

``` text
xarray
numpy
scipy
pandas
```

## Geospatial

``` text
GeoPandas
Shapely
PostGIS
Rasterio
pyproj
```

## Storage

``` text
MinIO
PostgreSQL
PostGIS
Zarr
NetCDF
Parquet
```

## API

``` text
FastAPI
```

## Scheduling

For the hackathon:

``` text
APScheduler
or
simple scheduled workers
```

Do not introduce Airflow unless the workflow genuinely requires it.

------------------------------------------------------------------------

# 83. GENERIC DATA PIPELINE CODE STRUCTURE

``` text
orca_data/
│
├── catalog/
│   ├── datasets.py
│   ├── variables.py
│   └── sources.py
│
├── connectors/
│   ├── base.py
│   ├── erddap.py
│   ├── incois.py
│   ├── imd.py
│   ├── mosdac.py
│   ├── copernicus.py
│   ├── noaa.py
│   ├── nasa.py
│   └── gebco.py
│
├── ingestion/
│   ├── manager.py
│   ├── scheduler.py
│   ├── retry.py
│   └── checksum.py
│
├── validation/
│   ├── schema.py
│   ├── quality.py
│   ├── spatial.py
│   └── temporal.py
│
├── normalization/
│   ├── ocean.py
│   ├── weather.py
│   ├── satellite.py
│   └── gis.py
│
├── alignment/
│   ├── spatial.py
│   └── temporal.py
│
├── derived/
│   ├── anomaly.py
│   ├── ocean.py
│   ├── risk.py
│   └── geospatial.py
│
├── evidence/
│   ├── provenance.py
│   └── evidence.py
│
└── api/
    ├── ocean.py
    ├── weather.py
    ├── hazards.py
    └── geospatial.py
```

------------------------------------------------------------------------

# 84. DATA ACQUISITION TESTING

Each connector should have:

## Unit tests

``` text
query construction
parser
unit conversion
metadata
```

## Integration tests

``` text
live provider request
authentication
download
subset
```

## Data-quality tests

``` text
coordinate range
time
units
missing values
```

## Regression tests

Save a small known dataset and verify that new code produces the
expected normalized output.

------------------------------------------------------------------------

# 85. GOLDEN DATASETS

For the hackathon, maintain small frozen examples:

``` text
golden/
├── argo/
├── osf/
├── pfz/
├── imd/
├── mosdac/
└── gebco/
```

These allow the team to work even if an external service temporarily
fails.

------------------------------------------------------------------------

# 86. MOCK MODE

The application should have:

``` text
LIVE MODE
MOCK MODE
```

### LIVE

Uses real sources.

### MOCK

Uses cached/frozen data.

This is extremely valuable during a hackathon presentation because an
external API outage should not destroy the demo.

------------------------------------------------------------------------

# 87. DATA LINEAGE GRAPH

The system should conceptually maintain:

``` text
SOURCE
  ↓
DATASET
  ↓
OBSERVATION
  ↓
DERIVED PRODUCT
  ↓
EVIDENCE
  ↓
DECISION
  ↓
RECOMMENDATION
```

Example:

``` text
INCOIS OSF
    ↓
Wave forecast
    ↓
Wave exposure calculation
    ↓
Risk evidence
    ↓
Route risk
    ↓
Recommendation
```

------------------------------------------------------------------------

# 88. WHAT SHOULD THE DATA DISCOVERY AGENT NEVER DO?

It should not:

-   invent a dataset
-   invent an API
-   assume availability
-   ignore freshness
-   ignore source authority
-   silently substitute a source
-   discard quality flags
-   treat a forecast as an observation
-   treat PFZ as guaranteed fish presence
-   treat GEBCO as a navigation chart
-   override official warnings
-   fabricate missing values

------------------------------------------------------------------------

# 89. WHAT SHOULD THE DATA SYSTEM GUARANTEE?

For every piece of information delivered to an agent:

``` text
WHERE did it come from?
WHEN was it observed?
WHEN was it forecast?
HOW fresh is it?
WHAT is its unit?
WHAT is its spatial resolution?
WHAT is its temporal resolution?
WHAT quality flags exist?
WHAT processing was applied?
WHAT source produced it?
CAN the result be traced back?
```

If the system cannot answer these questions, the data should not be
treated as high-confidence evidence.

------------------------------------------------------------------------

# 90. FINAL DATA PIPELINE

The complete architecture is:

``` text
                     EXTERNAL DATA SOURCES
                              │
       ┌──────────────────────┼──────────────────────┐
       │                      │                      │
     INCOIS                 IMD                 MOSDAC/ISRO
       │                      │                      │
       │                      │                      │
       └──────────────────────┼──────────────────────┘
                              │
                 COPERNICUS / NOAA / NASA
                              │
                    GIS / GEBCO / OSM
                              │
                              ▼
                       SOURCE CATALOG
                              │
                              ▼
                    DATA DISCOVERY ENGINE
                              │
                              ▼
                     DATA REQUIREMENT
                              │
                              ▼
                       CONNECTOR ROUTER
                              │
                              ▼
                       INGESTION MANAGER
                              │
                     ┌────────┴────────┐
                     ▼                 ▼
                  RAW STORE        METADATA STORE
                     │                 │
                     ▼                 ▼
                 VALIDATION        DATA CATALOG
                     │
                     ▼
                NORMALIZATION
                     │
                     ▼
          SPATIAL + TEMPORAL ALIGNMENT
                     │
                     ▼
              DERIVED DATA ENGINES
                     │
         ┌───────────┼───────────┐
         ▼           ▼           ▼
       OCEAN       WEATHER      GIS
       ENGINE      ENGINE      ENGINE
         │           │           │
         └───────────┼───────────┘
                     ▼
                 RISK ENGINE
                     │
                 ROUTE ENGINE
                     │
                     ▼
              EVIDENCE STORE
                     │
                     ▼
              DATA QUERY API
                     │
                     ▼
               AGENTIC SYSTEM
                     │
                     ▼
             DECISION + EXPLANATION
```

------------------------------------------------------------------------

# 91. FINAL ENGINEERING RULES

## Rule 1

**Sources remain sources.**

Do not pretend ORCA owns the scientific measurements.

## Rule 2

**Raw data is immutable.**

Never overwrite provider data.

## Rule 3

**Metadata is first-class data.**

A value without time, location, unit and provenance is incomplete.

## Rule 4

**Observation, forecast, advisory and derived data are different
semantic objects.**

Never merge them blindly.

## Rule 5

**The LLM does not calculate scientific truth.**

Deterministic scientific engines do.

## Rule 6

**Official warnings have operational authority.**

The system should contextualize them, not contradict them casually.

## Rule 7

**Every recommendation must be traceable to evidence.**

## Rule 8

**Fallbacks are explicit.**

Never silently substitute a source.

## Rule 9

**Spatial and temporal alignment must be recorded.**

Interpolation is a scientific operation, not invisible preprocessing.

## Rule 10

**The data system must work in degraded/mock mode.**

A hackathon demo should not depend on perfect internet/API availability.

------------------------------------------------------------------------

# 92. FINAL IMPLEMENTATION ORDER

The actual engineering team should now work in this order:

``` text
STEP 1
Build Source Registry

        ↓

STEP 2
Build generic HTTP + ERDDAP connector

        ↓

STEP 3
Connect INCOIS Argo

        ↓

STEP 4
Connect INCOIS OSF

        ↓

STEP 5
Connect INCOIS PFZ

        ↓

STEP 6
Connect IMD marine/cyclone

        ↓

STEP 7
Load coastline/EEZ/geofences

        ↓

STEP 8
Load regional GEBCO

        ↓

STEP 9
Build RAW storage

        ↓

STEP 10
Build normalization

        ↓

STEP 11
Build spatial/temporal alignment

        ↓

STEP 12
Build evidence/provenance

        ↓

STEP 13
Build Data Query API

        ↓

STEP 14
Connect Ocean/Weather/Spatial engines

        ↓

STEP 15
Only then connect agents
```

This order is intentional.

**Do not start by building agents.**

First make sure ORCA can reliably answer:

``` text
"What data do we have?"
"Where did it come from?"
"Can I retrieve it?"
"Is it fresh?"
"Is it valid?"
"What does it mean?"
"Can I trace it?"
```

Only then should the agentic layer be allowed to reason over it.

------------------------------------------------------------------------

# 93. RESEARCHED OFFICIAL ACCESS REFERENCES

## INCOIS

-   Data Holdings:\
    https://incois.gov.in/site/dataholdings.jsp

-   INCOIS ERDDAP:\
    https://erddap.incois.gov.in/erddap/

-   Ocean State Forecast:\
    https://www.incois.gov.in/oceanservices/osfforecast.jsp

-   Ocean Observation Network:\
    https://incois.gov.in/OON/index.jsp

INCOIS confirms the availability and access characteristics of Argo,
buoys, HF radar, tide gauges, ROMS and PFZ datasets in its current
holdings. citeturn1search3turn1search7

## MOSDAC / ISRO

-   MOSDAC:\
    https://mosdac.gov.in/

-   Oceansat-3:\
    https://mosdac.gov.in/oceansat-3

-   Oceansat-3 Payloads:\
    https://mosdac.gov.in/oceansat-3-payloads

-   Oceansat-3 References:\
    https://www.mosdac.gov.in/oceansat-3-references

-   Data Access Policy:\
    https://www.mosdac.gov.in/data-access-policy

MOSDAC documents the current Oceansat-3 payload configuration and its
access profiles. citeturn0search2turn0search3turn0search6

## IMD

-   API portal:\
    https://api.imd.gov.in/

-   API reference:\
    https://api.imd.gov.in/public/api_reference.html

-   Main weather/marine service:\
    https://mausam.imd.gov.in/

## Copernicus Marine

-   Data Store:\
    https://data.marine.copernicus.eu/

-   Marine portal:\
    https://marine.copernicus.eu/

-   Toolbox documentation:\
    https://help.marine.copernicus.eu/

The current Toolbox supports metadata discovery, subsetting,
original-file retrieval and remote programmatic access.
citeturn0search11turn0search17turn0search8

## NOAA CoastWatch

-   Main portal:\
    https://coastwatch.noaa.gov/

-   Data access tools:\
    https://coastwatch.noaa.gov/cwn/data-access-tools.html

NOAA documents both its data portal and ERDDAP-based programmatic/subset
access. citeturn0search5turn0search7

## NASA Ocean Color

-   Ocean Color:\
    https://oceancolor.gsfc.nasa.gov/

-   Ocean Data:\
    https://oceandata.sci.gsfc.nasa.gov/

## GEBCO

-   GEBCO 2026:\
    https://www.gebco.net/data-products-gridded-bathymetry-data/gebco2026-grid

-   Gridded bathymetry:\
    https://www.gebco.net/data-products/gridded-bathymetry-data

GEBCO_2026 is the current 15-arc-second global grid and supports global
files, user-defined-area downloads and OPeNDAP.
citeturn1search0turn1search1

------------------------------------------------------------------------

# 94. FINAL DECISION

The previous document answered:

> **What data should ORCA have?**

This document answers:

> **How should ORCA acquire and engineer that data?**

The next layer after this should be the **actual implementation of the
first connectors**, beginning with:

``` text
INCOIS ERDDAP
      ↓
Argo
      ↓
OSF
      ↓
PFZ
```

Then:

``` text
IMD
      ↓
Marine + cyclone
```

Then:

``` text
GIS + GEBCO
```

Once those are working, ORCA will have a genuine data foundation rather
than a conceptual list of sources.
