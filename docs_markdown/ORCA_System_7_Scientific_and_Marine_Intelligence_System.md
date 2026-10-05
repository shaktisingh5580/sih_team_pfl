# ORCA Marine Ecosystem Reasoning with Collaborative Agents
## System 7 — Scientific & Marine Intelligence System

**Problem Statement:** ORCA Marine EcOsystem Reasoning with Collaborative Agents  
**Organization:** ISRO / Department of Space  
**System:** Scientific & Marine Intelligence  
**Document purpose:** Detailed engineering and research specification  
**Scope:** Stakeholder-neutral marine decision intelligence

---

# 1. Executive Definition

ORCA must not be designed as a fishermen-only application.

It is a **general marine decision-intelligence platform** that can support fishermen, marine researchers, coastal authorities, disaster-management agencies, maritime operators, port authorities, environmental agencies, and other marine stakeholders.

The central principle is:

> **Stakeholder role, operational context, spatial region, temporal horizon, constraints, and decision objective determine which scientific analyses are required.**

The Scientific & Marine Intelligence System is the deterministic computational layer between the heterogeneous data foundation and the agentic reasoning layer.

The separation is:

```text
LLM / Agents       = reasoning, planning, interpretation
Scientific Engines = deterministic computation
Data Foundation    = evidence
Decision Layer     = contextual operational judgment
Evidence Layer     = provenance, validation, confidence
```

The LLM must not independently perform scientific calculations that can be implemented deterministically.

---

# 2. Why This System Exists

The ORCA problem involves large volumes of heterogeneous marine information:

- satellite Earth observation
- oceanographic observations
- ocean forecasts
- weather forecasts
- marine advisories
- GIS layers
- historical datasets
- derived scientific products

The challenge is not merely retrieving a value.

A useful marine intelligence system must answer questions such as:

- What is happening?
- Where is it happening?
- When is it happening?
- How unusual is it?
- What other variables are correlated with it?
- What hazards or constraints exist?
- What does the evidence imply?
- What decision is appropriate for this stakeholder and context?
- How confident is the conclusion?
- What evidence supports the conclusion?

Therefore:

```text
Raw Data
   ↓
Marine State
   ↓
Scientific Analysis
   ↓
Contextual Interpretation
   ↓
Decision Intelligence
   ↓
Evidence-Grounded Response
```

---

# 3. Stakeholder-Neutral Architecture

ORCA should not create a separate scientific engine for every user type.

Instead, the same scientific core should support multiple decision classes.

## 3.1 Fisherman

Example:

> Where should I fish tomorrow morning?

Required intelligence:

```text
PFZ
+ SST
+ Chlorophyll
+ Waves
+ Wind
+ Currents
+ Marine warnings
+ Restricted areas
+ Time
→ Fishing operational suitability
```

Important:

PFZ is a potential fishing-zone indicator, not proof that fish are physically present.

---

## 3.2 Marine Researcher

Example:

> Why has productivity decreased in this region?

Required intelligence:

```text
Current chlorophyll
+ Historical chlorophyll
+ Chlorophyll anomaly
+ SST anomaly
+ Currents
+ Wind
+ Fronts / upwelling indicators
→ Ecosystem change analysis
```

The system should distinguish between:

- observation
- derived metric
- scientific indicator
- correlation
- hypothesis/inference

It must not convert correlation into unsupported causation.

---

## 3.3 Coastal Authority

Example:

> Which marine areas currently have operational restrictions or elevated hazards?

Required intelligence:

```text
Marine warnings
+ Cyclone
+ Waves
+ Wind
+ Geofences
+ Restricted areas
+ GIS
→ Spatial operational assessment
```

---

## 3.4 Disaster Management Agency

Example:

> Which coastal regions may be affected by this cyclone?

Required intelligence:

```text
Official cyclone track
+ Forecast position
+ Wind
+ Waves
+ Rain
+ Coastline
+ Spatial overlays
→ Potential impact regions
```

Official warnings remain authoritative.

---

## 3.5 Maritime Operator

Example:

> What is the safest practical route from Port A to Port B tomorrow?

Required intelligence:

```text
Coastline
+ Restricted zones
+ Wind
+ Waves
+ Currents
+ Cyclone
+ Operational constraints
→ Candidate routes
→ Exposure analysis
→ Route ranking
```

The system should not represent a general bathymetry dataset as a certified navigation chart.

---

## 3.6 Port Authority

Example:

> Are marine conditions suitable for planned operations?

Required intelligence:

```text
Wave height
+ Wave period
+ Wind
+ Forecast
+ Marine warnings
+ Operational threshold/policy
→ Operational suitability
```

Thresholds must be configurable to the actual operation rather than hard-coded as universal maritime safety rules.

---

## 3.7 Environmental Agency

Example:

> Is this region experiencing an unusual ecosystem condition?

Required intelligence:

```text
SST anomaly
+ Chlorophyll anomaly
+ Ocean colour
+ Historical baseline
+ HAB indicators
+ Marine heatwave indicators
→ Ecosystem anomaly assessment
```

---

# 4. The Central ORCA Concept: Marine State

The scientific system should construct a machine-readable representation of the marine environment.

This is the **Marine State**.

```text
Marine State
│
├── Ocean
│   ├── SST
│   ├── Chlorophyll
│   ├── Currents
│   ├── Waves
│   ├── MLD
│   ├── Temperature
│   ├── Salinity
│   └── Ocean colour
│
├── Atmosphere
│   ├── Wind
│   ├── Rain
│   ├── Lightning
│   └── Cyclone
│
├── Ecosystem
│   ├── Productivity indicators
│   ├── Fronts
│   ├── Upwelling indicators
│   ├── HAB indicators
│   ├── Marine heatwave indicators
│   └── Ecosystem anomalies
│
├── Geography
│   ├── Coastline
│   ├── EEZ
│   ├── MPA
│   ├── Restricted areas
│   ├── Ports
│   └── Bathymetry
│
└── Temporal State
    ├── Current observations
    ├── Forecast
    ├── Historical baseline
    ├── Trend
    └── Anomaly
```

This model is more important than any individual agent.

---

# 5. System Architecture

```text
                         USER
                           │
                           ▼
                    CONVERSATION LAYER
                           │
                           ▼
                     ORCHESTRATOR
                           │
                           ▼
                    TASK / PLAN MODEL
                           │
                           ▼
                 DATA DISCOVERY AGENT
                           │
                           ▼
                 DATA RETRIEVAL AGENT
                           │
                           ▼
             SCIENTIFIC & MARINE INTELLIGENCE
                           │
        ┌──────────────────┼───────────────────┐
        │                  │                   │
        ▼                  ▼                   ▼
      OCEAN             WEATHER            SPATIAL
   INTELLIGENCE       INTELLIGENCE       INTELLIGENCE
        │                  │                   │
        ├──────────────┐   │   ┌──────────────┤
        │              │   │   │              │
        ▼              ▼   ▼   ▼              ▼
   ECOSYSTEM       TEMPORAL ENGINE       GEOSPATIAL
   INTELLIGENCE                         CONSTRAINTS
        │                  │
        └────────────┬─────┘
                     ▼
                 RISK ENGINE
                     │
                     ▼
                ROUTE ENGINE
                     │
                     ▼
             DECISION INTELLIGENCE
                     │
                     ▼
              EVIDENCE VALIDATOR
                     │
                     ▼
             RESPONSE SYNTHESIZER
                     │
                     ▼
                USER + MAP
```

---

# 6. Scientific Intelligence Layers

The system should operate at three major levels.

## Level 1 — Measurement

Directly retrieve or sample data.

Examples:

- SST = 28.4 °C
- chlorophyll = 1.2 mg/m³
- wave height = 1.8 m
- wind speed = 24 km/h
- current speed = 0.7 m/s

No interpretation is performed here.

---

## Level 2 — Analysis

Transform measurements into scientifically meaningful quantities.

Examples:

```text
SST
→ SST anomaly

Chlorophyll
→ chlorophyll anomaly

SST field
→ spatial gradient

SST + chlorophyll gradients
→ potential front

Current vectors
→ current speed and direction

Historical data
→ trend

Current + historical
→ anomaly
```

---

## Level 3 — Decision Intelligence

Combine scientific results with context and constraints.

Example:

```text
Wave conditions
+ Wind
+ Cyclone
+ Marine warning
+ Vessel context
+ Time
→ Operational suitability
```

The LLM explains this result but should not invent the calculation.

---

# 7. Ocean Intelligence Engine

## 7.1 Purpose

The Ocean Intelligence Engine analyzes the physical and biogeochemical state of the ocean.

Primary variables:

- sea surface temperature
- chlorophyll
- ocean colour
- currents
- waves
- mixed layer depth
- temperature profiles
- salinity profiles
- related oceanographic indicators

---

## 7.2 SST Analysis

Operations:

### SST lookup

Inputs:

```text
latitude
longitude
time
dataset
```

Output:

```json
{
  "variable": "sst",
  "value": 28.4,
  "unit": "degC",
  "timestamp": "...",
  "source": "...",
  "evidence_ids": ["..."]
}
```

### Regional SST statistics

Calculate:

- minimum
- maximum
- mean
- median
- standard deviation
- percentile
- spatial coverage

### SST gradient

Calculate:

```text
|∇SST|
```

A strong spatial temperature gradient can indicate an oceanic front.

The result must state:

- method
- grid resolution
- units
- threshold
- input dataset
- confidence

---

# 8. Chlorophyll Intelligence

Chlorophyll-a is a major ocean-colour-derived indicator relevant to biological productivity.

Operations:

```text
lookup
regional statistics
gradient
anomaly
historical comparison
spatial hotspot detection
```

Example:

```text
Current chlorophyll
        ↓
Historical baseline
        ↓
Anomaly
        ↓
Spatial pattern
```

The system should not interpret high chlorophyll as automatically meaning:

> “There are many fish.”

Instead:

> “The region exhibits elevated chlorophyll relative to the selected baseline.”

Further ecological interpretation requires additional evidence.

---

# 9. Ocean Front Detection

Front detection is particularly relevant to ORCA because operational marine advisory systems can use oceanic fronts as part of fisheries intelligence.

A basic implementation can use spatial gradients.

For SST:

```text
SST(x,y)
   ↓
Spatial derivative
   ↓
Gradient magnitude
   ↓
Threshold
   ↓
Potential thermal front
```

For chlorophyll:

```text
Chlorophyll(x,y)
   ↓
Spatial gradient
   ↓
Potential biological boundary
```

A combined method can evaluate:

```text
SST gradient
+
Chlorophyll gradient
+
spatial coherence
+
temporal persistence
```

Important distinction:

```text
Front detected
≠
Fish detected
```

The front is an environmental feature.

---

# 10. Eddy Intelligence

Eddy detection is a V2 capability.

Potential inputs:

- sea-surface height
- sea-surface temperature
- currents
- chlorophyll
- vorticity

Possible methods:

```text
SSH contours
+
velocity field
+
vorticity
+
temperature anomaly
→ Eddy candidate
```

Candidate output:

```json
{
  "type": "eddy_candidate",
  "center": {"lat": 0, "lon": 0},
  "radius_km": 25,
  "polarity": "cyclonic",
  "confidence": 0.78,
  "method_version": "eddy-v1"
}
```

Do not implement complex eddy classification before the basic scientific pipeline is stable.

---

# 11. Upwelling Intelligence

Upwelling should be treated as an **inferred environmental condition**, not a single directly observed variable.

Possible evidence:

```text
Lower SST
+
elevated chlorophyll
+
favorable wind
+
current structure
+
historical persistence
→ conditions consistent with upwelling
```

Output language should distinguish evidence from inference:

```text
Observed:
SST is below baseline.

Observed:
Chlorophyll is elevated.

Derived:
Wind direction is favorable for coastal upwelling.

Inference:
Conditions are consistent with enhanced upwelling.
```

This is scientifically safer than declaring:

> “Upwelling is occurring.”

unless a validated algorithm supports that statement.

---

# 12. Current Intelligence

Current datasets can provide vector components:

```text
u = east-west component
v = north-south component
```

Derive:

```text
speed = sqrt(u² + v²)
```

and direction using a clearly documented convention.

Operations:

- current speed
- current direction
- vector field
- spatial gradients
- convergence
- divergence
- route exposure

Current direction conventions must be explicitly recorded because oceanographic and meteorological direction conventions can differ.

---

# 13. Vertical Ocean Intelligence

For Argo and related profiles:

```text
Depth
Temperature
Salinity
```

Possible derived products:

- mixed-layer depth
- thermocline indicators
- temperature gradient
- salinity gradient
- vertical structure
- heat-content indicators

Example:

```text
Surface temperature
       ↓
Temperature profile
       ↓
Gradient with depth
       ↓
Thermal structure
```

This is more useful for researchers and ecosystem analysis than for simple fishing queries.

---

# 14. PFZ Intelligence

PFZ must be treated as an existing authoritative operational product when available.

ORCA should **not claim that it invented PFZ**.

The system can:

```text
retrieve PFZ
+
associate PFZ with location
+
compare PFZ with ocean state
+
compare PFZ with weather
+
check hazards
+
check geofences
+
rank operational suitability
```

Example:

```text
PFZ
+
SST
+
Chlorophyll
+
Wind
+
Waves
+
Marine warning
+
Restricted areas
→ Contextual PFZ assessment
```

This is a much stronger contribution than simply displaying the PFZ layer.

---

# 15. Ecosystem Intelligence Engine

Because the problem is explicitly about marine ecosystem reasoning, ORCA should contain an Ecosystem Intelligence capability.

Inputs:

```text
SST
Chlorophyll
Ocean colour
Currents
Fronts
Upwelling indicators
MLD
Historical baseline
HAB indicators
Marine heatwave indicators
PFZ
```

Potential outputs:

```text
ecosystem anomaly
productivity indicator
thermal anomaly
chlorophyll anomaly
possible bloom condition
front persistence
regional ecosystem change
```

The engine should use evidence chains.

Example:

```text
Evidence 1:
Chlorophyll +35% relative to baseline

Evidence 2:
SST -1.2 °C relative to baseline

Evidence 3:
Wind pattern consistent with upwelling

Derived assessment:
Environmental conditions are consistent with enhanced productivity.

Confidence:
Moderate
```

This is preferable to a black-box statement.

---

# 16. Weather & Atmospheric Intelligence Engine

The Weather Engine handles:

- wind
- rain
- waves
- lightning
- cyclone
- marine warnings
- forecast products

---

# 17. Wind Analysis

Operations:

```text
speed
direction
u/v components
regional mean
gradient
forecast trend
historical comparison
```

Possible output:

```json
{
  "variable": "wind_speed",
  "value": 26,
  "unit": "km/h",
  "valid_time": "...",
  "forecast": true,
  "source": "...",
  "confidence": "high"
}
```

---

# 18. Wave Intelligence

Wave analysis should include:

- significant wave height
- wave period
- swell height
- swell period
- wave direction where available
- forecast evolution

Do not create a universal rule such as:

```text
wave > X = unsafe
```

unless the operational context provides a validated threshold.

Instead:

```text
Wave state
+
vessel/operation context
+
official warning
+
forecast uncertainty
→ operational assessment
```

---

# 19. Rain Intelligence

Rain should be classified contextually.

Possible states:

```text
none
light
moderate
heavy
extreme
```

But rain alone should not automatically mean unsafe marine conditions.

It can become relevant when combined with:

- lightning
- cyclone
- visibility
- flooding
- wind
- operational context

---

# 20. Cyclone Intelligence

Cyclone analysis must prioritize authoritative cyclone information.

Operations:

```text
track retrieval
forecast position
distance to region
distance to route
time to closest approach
wind exposure
warning status
forecast evolution
```

Example:

```text
Cyclone forecast track
        ↓
Spatial projection
        ↓
Region / route intersection
        ↓
Distance to closest approach
        ↓
Timing
        ↓
Risk context
```

Official warnings must not be casually overridden by model-derived calculations.

---

# 21. Lightning Intelligence

Operations:

- lightning occurrence
- distance
- spatial density
- recent activity
- trend
- forecast/nowcast where available

Example:

```text
Recent lightning activity
+
distance from operation
+
storm movement
→ lightning exposure
```

---

# 22. Forecast Comparison

Multiple authoritative or high-quality sources can sometimes provide different forecasts.

ORCA should preserve them separately.

```text
Forecast A
Forecast B
Observation
       ↓
Alignment
       ↓
Difference
       ↓
Agreement / disagreement
```

Example:

```text
INCOIS forecast:
Wave = 1.8 m

Copernicus:
Wave = 2.0 m

Observation:
Wave = 1.9 m
```

This can support a higher-confidence assessment.

If forecasts disagree strongly, confidence should decrease.

---

# 23. Spatial Intelligence Engine

Spatial reasoning is a foundational capability.

Operations:

```text
point-in-polygon
distance
intersection
buffer
nearest feature
spatial join
raster sampling
area statistics
geofence detection
route intersection
```

---

# 24. Point-in-Polygon

Example:

```text
Vessel coordinate
        ↓
Protected-area polygons
        ↓
Point-in-polygon
        ↓
Inside / Outside
```

Use cases:

- MPA membership
- EEZ membership
- restricted zones
- administrative/coastal zones
- operational areas

---

# 25. Distance Calculation

Distance should use an appropriate geodesic calculation for geographic coordinates.

Use cases:

```text
distance to port
distance to PFZ
distance to cyclone
distance to restricted zone
distance to coast
distance between route points
```

---

# 26. Intersection

Example:

```text
Candidate Route
       +
Restricted Zone
       ↓
Geometry intersection
       ↓
Violation = true
```

This should be deterministic.

The LLM should never decide geometric intersection by visual guesswork.

---

# 27. Geofencing

Geofences are **constraints**, not necessarily physical hazards.

Example:

```text
Restricted Area
Protected Area
Military Zone
Port Exclusion Zone
Fishing Restriction
```

Therefore distinguish:

```text
Physical Risk
vs
Compliance / Access Constraint
```

A route can be physically safe but legally prohibited.

---

# 28. Raster Sampling

For satellite or model grids:

```text
Point / polygon
      ↓
Raster / grid
      ↓
Sampling
      ↓
Variable value
```

For polygons, possible statistics include:

- mean
- minimum
- maximum
- percentile
- valid-pixel percentage

Quality and missing-data handling must be recorded.

---

# 29. Temporal Intelligence Engine

Marine intelligence is highly time-dependent.

The engine must understand:

```text
observation_time
forecast_initialization_time
forecast_valid_time
historical_time
analysis_window
```

Do not confuse:

```text
forecast created at 00:00
```

with:

```text
forecast valid at 12:00
```

These are different timestamps.

---

# 30. Forecast Alignment

Example:

User asks:

> What will conditions be at 08:00 tomorrow?

The system should:

```text
Resolve local time
        ↓
Convert to canonical time representation
        ↓
Find forecast valid near requested time
        ↓
Interpolate if appropriate
        ↓
Record interpolation method
```

---

# 31. Historical Comparison

Supported comparisons:

```text
yesterday
7-day baseline
30-day baseline
seasonal baseline
climatology
same month in previous years
```

The baseline must be explicitly named.

Avoid:

> “This is unusually high.”

Prefer:

> “Chlorophyll is 34% above the selected 1993–2016 baseline.”

when the baseline actually supports that statement.

---

# 32. Trend Analysis

Possible methods:

```text
linear trend
rolling average
rolling median
percentage change
rate of change
change-point detection
```

For every result record:

- time window
- sample count
- missing values
- method
- baseline
- confidence

---

# 33. Anomaly Engine

Generic formulation:

```text
Anomaly = Current Value - Expected/Baseline Value
```

Relative anomaly can be:

```text
Relative Anomaly =
(Current - Baseline) / Baseline
```

But the implementation must handle:

- zero baseline
- missing baseline
- seasonal effects
- unit differences
- irregular sampling

---

# 34. Risk Intelligence Engine

Risk must be contextual.

The engine should not simply output an unexplained scalar such as:

```text
Risk = 0.83
```

Instead:

```json
{
  "context": "small_fishing_vessel",
  "hazards": [
    {
      "type": "wave",
      "severity": "moderate",
      "evidence_ids": ["..."]
    },
    {
      "type": "wind",
      "severity": "high",
      "evidence_ids": ["..."]
    }
  ],
  "constraints": [],
  "overall_assessment": "unfavorable",
  "confidence": "high"
}
```

---

# 35. Hazard Components

The V1 risk system should evaluate separately:

```text
wave risk
wind risk
cyclone risk
lightning exposure
rain/storm exposure
```

And separately:

```text
geofence/access constraint
```

---

# 36. Contextual Risk

The same marine state can produce different decisions.

Example:

```text
Wave = 2.0 m
```

For:

```text
small fishing boat
```

the operational assessment may be unfavorable.

For:

```text
large ocean-going vessel
```

the assessment may be different.

Therefore the system must support:

```text
user role
vessel type
operation type
time
route
operational policy
```

---

# 37. Risk vs Confidence

These are different concepts.

```text
Risk
=
How unfavorable / hazardous the situation is.

Confidence
=
How strongly the evidence supports the assessment.
```

Example:

```text
High risk + high confidence
```

is possible.

So is:

```text
High risk + low confidence
```

when data is sparse but available signals are concerning.

---

# 38. Uncertainty

Every important scientific result should be able to represent uncertainty.

Possible fields:

```text
data_quality
forecast_spread
source_agreement
missingness
spatial_resolution
temporal_resolution
algorithm_confidence
```

The final answer should not hide significant uncertainty.

---

# 39. Route & Operations Engine

The Route Engine supports multiple stakeholders.

Examples:

```text
Fishing vessel
Port-to-port vessel
Emergency response
Research vessel
Coastal operation
```

Inputs:

```text
origin
destination
departure time
vessel/operation context
coastline
bathymetry
restricted areas
wind
waves
currents
cyclone
hazards
```

---

# 40. Route Generation

V1 approach:

```text
Marine grid
      ↓
Forbidden cells removed
      ↓
Remaining navigable cells
      ↓
Environmental cost assigned
      ↓
A* / Dijkstra
      ↓
Candidate routes
```

Candidate routes can then be ranked.

---

# 41. Route Cost

A conceptual multi-objective cost:

```text
Total Cost =
distance cost
+ time cost
+ environmental exposure
+ wave exposure
+ wind exposure
+ hazard penalty
+ restriction penalty
```

Weights should be configurable.

Do not claim a route is legally or universally “safe” merely because it has the lowest computed cost.

Prefer:

> “Lowest-risk candidate under the configured constraints and available data.”

---

# 42. Current-Aware Routing

Currents can either help or hinder a route.

Conceptually:

```text
Vessel motion
+
Current vector
→ effective movement
```

The route engine should consider current direction relative to the route.

---

# 43. Route Validation

Every candidate route should be checked for:

```text
restricted-zone intersection
coastline intersection
invalid geometry
missing environmental data
hazard exposure
excessive uncertainty
```

Output:

```json
{
  "route_id": "...",
  "distance_km": 420,
  "eta_hours": 18.4,
  "constraint_violations": [],
  "wave_exposure": 0.31,
  "wind_exposure": 0.22,
  "hazard_exposure": 0.14,
  "confidence": "medium"
}
```

---

# 44. Important Bathymetry Limitation

General bathymetry datasets can support:

- depth visualization
- spatial analysis
- route-cost heuristics
- research analysis

But a general bathymetry dataset must not be represented as an official navigation chart or certified navigational safety source.

Navigation-critical decisions require appropriate authoritative navigation information.

---

# 45. Decision Intelligence

The scientific engines produce facts and analyses.

Decision Intelligence combines them with context.

```text
DATA
 ↓
SCIENTIFIC ANALYSIS
 ↓
MARINE STATE
 ↓
USER CONTEXT
 ↓
CONSTRAINTS
 ↓
RISK
 ↓
DECISION
```

Examples:

```text
Where?
→ spatial + ocean + PFZ + route

When?
→ temporal + forecast + weather

Why?
→ historical + anomaly + ecosystem + correlation

What should I do?
→ risk + route + constraints + context

What changed?
→ temporal + anomaly + historical comparison
```

---

# 46. Decision Classes

ORCA should support a generic decision taxonomy.

## WHERE

Examples:

- Where are potential fishing zones?
- Where are high chlorophyll areas?
- Where is the hazard concentrated?
- Which coastal regions are affected?
- Where are suitable operational areas?

## WHEN

Examples:

- When are conditions expected to improve?
- When will cyclone exposure be highest?
- When was the anomaly strongest?

## WHY

Examples:

- Why did productivity decline?
- Why is this region different?
- Why did the risk increase?

## WHAT SHOULD I DO

Examples:

- Which route should I take?
- Should the operation proceed?
- Which area should be avoided?

## WHAT CHANGED

Examples:

- What changed since yesterday?
- How different is this season?
- Did the cyclone track change?

---

# 47. Scientific Engine Contract

Every engine should expose a standardized interface.

```json
{
  "task_id": "task-123",
  "engine": "ocean",
  "operation": "sst_anomaly",
  "inputs": {
    "region": "...",
    "time": "...",
    "baseline": "..."
  },
  "method": {
    "name": "sst_anomaly",
    "version": "1.0"
  },
  "outputs": {},
  "units": {},
  "quality": {},
  "confidence": "high",
  "evidence_ids": ["ev-1", "ev-2"],
  "processing_time": "...",
  "status": "success"
}
```

---

# 48. Evidence-First Computation

Every derived result should reference the data used.

Example:

```text
SST anomaly
   │
   ├── evidence: SST observation
   ├── evidence: historical baseline
   └── method: anomaly-v1
```

Then:

```text
Front detection
   │
   ├── SST evidence
   ├── Chlorophyll evidence
   └── gradient method
```

Then:

```text
Recommendation
   │
   ├── PFZ evidence
   ├── weather evidence
   ├── wave evidence
   ├── geofence evidence
   └── scientific analysis evidence
```

This creates an evidence chain.

---

# 49. Provenance Requirements

Every result should preserve:

```text
source
dataset
variable
timestamp
forecast_valid_time
spatial resolution
temporal resolution
units
quality flags
processing method
algorithm version
evidence IDs
```

The user should be able to ask:

> Why did ORCA say this?

And the system should be able to reconstruct the reasoning chain.

---

# 50. Confidence Model

Confidence should be derived from evidence quality.

Potential factors:

```text
source reliability
data freshness
coverage
missingness
forecast agreement
observation availability
spatial resolution
temporal resolution
algorithm stability
```

Conceptual model:

```text
Confidence
=
f(
source quality,
freshness,
coverage,
agreement,
data quality,
method reliability
)
```

The exact scoring formula should be implemented transparently and versioned.

---

# 51. Scientific Output Must Be Structured

Do not return only natural language from scientific engines.

Bad:

```text
The ocean seems favorable.
```

Good:

```json
{
  "assessment": "elevated_productivity_conditions",
  "indicators": [
    {
      "name": "chlorophyll_anomaly",
      "value": 0.35,
      "unit": "fraction"
    },
    {
      "name": "sst_anomaly",
      "value": -1.2,
      "unit": "degC"
    }
  ],
  "confidence": "moderate",
  "evidence_ids": ["ev1", "ev2"],
  "method_version": "ecosystem-v1"
}
```

The LLM can then turn this into natural language.

---

# 52. Scientific Engines vs Agents

This distinction is fundamental.

## Scientific Engine

```text
Input
→ deterministic computation
→ structured output
```

## Agent

```text
Goal
→ decide what information is needed
→ select tools
→ execute tasks
→ evaluate results
→ request additional information
→ collaborate
→ produce structured conclusion
```

Therefore:

```text
Agent ≠ Scientific Engine
```

---

# 53. Example Agent Interaction

User:

> “Why is fishing productivity lower near this region than last month?”

Orchestrator creates:

```json
{
  "intent": "ecosystem_change_analysis",
  "region": "...",
  "current_period": "...",
  "comparison_period": "last_month"
}
```

Planner determines required analysis:

```text
chlorophyll
SST
currents
historical baseline
PFZ
front indicators
weather
```

Scientific system executes:

```text
chlorophyll anomaly
SST anomaly
current analysis
front detection
PFZ comparison
```

Evidence validator checks:

```text
freshness
missing data
source conflicts
confidence
```

Response synthesizer produces:

```text
Observed:
chlorophyll decreased.

Observed:
SST increased.

Derived:
front intensity decreased.

Assessment:
the available evidence is consistent with reduced productivity indicators.

Caveat:
this does not prove a single causal mechanism.
```

---

# 54. Engine Registry

A registry should allow agents to discover available scientific operations.

Example:

```json
{
  "engine_id": "ocean",
  "description": "Ocean physical and biogeochemical analysis",
  "operations": [
    "sst_lookup",
    "sst_statistics",
    "sst_anomaly",
    "chlorophyll_lookup",
    "chlorophyll_anomaly",
    "gradient",
    "front_detection",
    "current_analysis",
    "pfz_analysis"
  ]
}
```

Weather:

```json
{
  "engine_id": "weather",
  "operations": [
    "wind_analysis",
    "wave_analysis",
    "rain_analysis",
    "cyclone_proximity",
    "lightning_analysis",
    "forecast_comparison"
  ]
}
```

Spatial:

```json
{
  "engine_id": "spatial",
  "operations": [
    "point_in_polygon",
    "distance",
    "intersection",
    "buffer",
    "nearest_feature",
    "geofence_check",
    "raster_sample"
  ]
}
```

---

# 55. V1 Scientific Capability Set

The first implementation should be practical.

## Ocean

```text
SST lookup
SST statistics
SST anomaly
Chlorophyll lookup
Chlorophyll statistics
Chlorophyll anomaly
SST gradient
Chlorophyll gradient
Basic front detection
Current speed/direction
PFZ context
```

## Weather

```text
Wind
Wave
Rain
Cyclone proximity
Marine warning extraction
Lightning
Basic forecast comparison
```

## Spatial

```text
Point-in-polygon
Distance
Intersection
Nearest port
Geofence
Raster sampling
```

## Temporal

```text
Forecast alignment
Historical baseline
Rolling average
Anomaly
Time-window filtering
Trend
```

## Ecosystem

```text
Productivity indicators
Ecosystem anomaly
Basic front context
PFZ-ocean relationship
```

## Risk

```text
Wave assessment
Wind assessment
Cyclone assessment
Lightning exposure
Geofence/access constraint
Combined operational suitability
```

## Route

```text
Candidate route generation
Geofence avoidance
Distance
ETA
Environmental exposure
A*/Dijkstra routing
Route ranking
```

---

# 56. V2 Scientific Capability Set

After V1 is stable:

```text
advanced eddy detection
upwelling detection
front persistence
current convergence/divergence
vertical ocean structure
marine heatwave analysis
HAB intelligence
advanced BGC analysis
species-specific models
advanced route optimization
uncertainty propagation
multi-model ensemble analysis
```

Do not implement these merely to increase the feature count.

Each must answer a real decision need.

---

# 57. Recommended Implementation Order

## Phase 1 — Scientific Data Interface

Implement:

```text
dataset readers
unit normalization
coordinate normalization
time normalization
quality flags
```

---

## Phase 2 — Core Mathematical Operations

Implement:

```text
statistics
gradient
anomaly
distance
intersection
point-in-polygon
time filtering
interpolation
```

---

## Phase 3 — Ocean Engine

Implement:

```text
SST
chlorophyll
currents
PFZ
front detection
```

---

## Phase 4 — Weather Engine

Implement:

```text
wind
waves
rain
cyclone
lightning
warnings
```

---

## Phase 5 — Spatial Engine

Implement:

```text
GIS
geofencing
spatial joins
raster sampling
```

---

## Phase 6 — Temporal Engine

Implement:

```text
forecast alignment
historical baseline
anomaly
trend
```

---

## Phase 7 — Ecosystem Engine

Combine:

```text
SST
chlorophyll
currents
fronts
historical data
PFZ
```

---

## Phase 8 — Risk Engine

Combine scientific outputs with operational context.

---

## Phase 9 — Route Engine

Build:

```text
grid
constraints
cost function
A*
route validation
ranking
```

---

## Phase 10 — Agent Integration

Only after the scientific layer works independently.

Agents should call scientific operations rather than reproduce them.

---

# 58. Testing Strategy

Every engine must have deterministic tests.

## Ocean tests

```text
known SST grid
→ expected gradient

known baseline
→ expected anomaly

known current vectors
→ expected speed/direction
```

## Spatial tests

```text
point inside polygon
point outside polygon
route crossing polygon
nearest feature
```

## Temporal tests

```text
forecast valid-time matching
missing timestamp
interpolation
historical baseline
```

## Risk tests

```text
high wind
high wave
cyclone proximity
geofence violation
combined conditions
```

## Route tests

```text
blocked cell
restricted polygon
shortest route
environmental penalty
```

---

# 59. Synthetic / Mock Data Mode

Because some operational data sources may be inaccessible during development or demos, every engine should support mock datasets.

Example:

```text
mock_sst.nc
mock_chlorophyll.nc
mock_currents.nc
mock_wave.nc
mock_wind.nc
mock_cyclone.json
mock_restricted_zones.geojson
```

The same scientific code should run against:

```text
REAL DATA
or
MOCK DATA
```

without changing its scientific logic.

This is critical for hackathon reliability.

---

# 60. Caching

Not every scientific operation needs a fresh download.

Cache:

```text
recent forecasts
recent satellite products
static GIS
historical baselines
derived grids
```

Cache metadata should include:

```text
dataset
time
region
source
created_at
expires_at
```

Do not serve stale data as live data.

---

# 61. Computational Storage

Scientific data should retain appropriate formats.

Prefer:

```text
NetCDF / Zarr
→ multidimensional scientific arrays

GeoTIFF
→ raster products

Parquet
→ large analytical tables

PostgreSQL/PostGIS
→ metadata, vector geometry, spatial queries

Object storage
→ raw files and large products
```

Do not force every scientific dataset into JSON.

JSON should primarily represent:

```text
metadata
requests
structured results
evidence
agent state
```

---

# 62. API Layer

The Scientific Intelligence System should expose a stable internal API.

Example:

```text
POST /scientific/ocean/sst
POST /scientific/ocean/anomaly
POST /scientific/ocean/front
POST /scientific/ocean/current
POST /scientific/weather/wave
POST /scientific/weather/wind
POST /scientific/weather/cyclone
POST /scientific/spatial/distance
POST /scientific/spatial/geofence
POST /scientific/temporal/anomaly
POST /scientific/risk/assess
POST /scientific/route/optimize
POST /scientific/ecosystem/analyze
```

Exact public exposure is not required; these can be internal service endpoints.

---

# 63. Generic Scientific Request

```json
{
  "task_id": "task-001",
  "operation": "sst_anomaly",
  "region": {
    "type": "polygon",
    "coordinates": []
  },
  "time": {
    "start": "...",
    "end": "..."
  },
  "baseline": {
    "type": "historical",
    "start": "...",
    "end": "..."
  },
  "options": {
    "spatial_resolution": "..."
  }
}
```

---

# 64. Generic Scientific Response

```json
{
  "task_id": "task-001",
  "status": "success",
  "result": {
    "value": -1.2,
    "unit": "degC"
  },
  "quality": {
    "missing_fraction": 0.03,
    "coverage": 0.97
  },
  "confidence": "high",
  "evidence_ids": [
    "ev-001",
    "ev-002"
  ],
  "method": {
    "name": "sst_anomaly",
    "version": "1.0"
  }
}
```

---

# 65. Failure Handling

Scientific engines must explicitly return failure states.

Examples:

```text
NO_DATA
PARTIAL_DATA
STALE_DATA
INVALID_REGION
INVALID_TIME
SOURCE_UNAVAILABLE
CONFLICTING_SOURCES
INSUFFICIENT_RESOLUTION
CALCULATION_ERROR
```

Never silently replace missing scientific data with invented values.

---

# 66. Source Conflict Handling

Example:

```text
Source A:
Wave = 1.4 m

Source B:
Wave = 2.4 m
```

The system should not arbitrarily select one.

Instead:

```text
identify source priority
compare forecast valid times
compare resolutions
check observations
record disagreement
adjust confidence
```

For official warnings:

```text
Authoritative advisory
→ highest operational priority
```

Derived calculations should not casually override it.

---

# 67. Explainability

A final response should be traceable.

Example:

```text
Recommendation
     ↓
Decision factors
     ↓
Scientific analyses
     ↓
Raw/normalized evidence
     ↓
Source
```

The UI can expose:

```text
Why this recommendation?
```

with:

- source
- timestamp
- variable
- value
- calculation
- confidence

---

# 68. Map Integration

Scientific output must be visualizable.

Required map layers can include:

```text
SST
Chlorophyll
PFZ
Waves
Wind
Currents
Cyclone
Lightning
Restricted zones
MPA
EEZ
Bathymetry
Risk
Routes
Ecosystem anomalies
```

The scientific system should return geometries or raster references that the visualization layer can consume.

---

# 69. Charts

Useful scientific visualizations:

```text
SST time series
chlorophyll time series
anomaly chart
wind forecast
wave forecast
cyclone track
current vectors
vertical profiles
regional comparisons
route exposure profile
```

The chart layer should consume structured scientific results rather than perform calculations itself.

---

# 70. Alert Support

Alerts should not depend entirely on a user asking a question.

Scientific conditions can trigger:

```text
cyclone proximity
lightning increase
extreme waves
marine warning
large ecosystem anomaly
geofence entry
route hazard change
```

The alert system should use the same validated scientific outputs.

---

# 71. Security and Safety Boundaries

Safety-critical outputs should use:

```text
authoritative advisories
+
validated forecast products
+
observations
+
derived analysis
```

The LLM should never invent:

- marine warnings
- cyclone positions
- safety thresholds
- restricted zones
- navigational permissions

When evidence is insufficient:

```text
insufficient evidence
```

is a valid output.

---

# 72. LLM Boundary

The LLM is responsible for:

```text
natural language understanding
intent extraction
context interpretation
task planning
tool selection
multi-turn reasoning
evidence synthesis
explanation
language generation
```

The LLM should NOT be responsible for:

```text
gradient calculations
distance calculations
polygon intersection
route search
anomaly calculation
forecast interpolation
risk arithmetic
scientific classification
```

Those belong to deterministic systems.

---

# 73. Core Separation

This should be treated as a fundamental ORCA engineering rule:

```text
┌──────────────────────────────┐
│             LLM              │
│ reasoning + interpretation   │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│       SCIENTIFIC ENGINES     │
│ deterministic computation    │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│             DATA             │
│ observations + forecasts +   │
│ advisories + GIS + history   │
└──────────────────────────────┘
```

---

# 74. Anti-Patterns to Avoid

## Anti-pattern 1 — Fisherman-first architecture

Bad:

```text
Fishing App
+ Research Mode
+ Disaster Mode
+ Shipping Mode
```

Better:

```text
Marine Intelligence Core
→ Contextual decision modes
```

---

## Anti-pattern 2 — Agent for every noun

Bad:

```text
SST Agent
Chlorophyll Agent
Wind Agent
Wave Agent
PFZ Agent
```

Better:

```text
Ocean Intelligence Engine
Weather Intelligence Engine
```

with deterministic operations.

---

## Anti-pattern 3 — LLM mathematics

Bad:

```text
LLM calculates route distance
LLM estimates cyclone distance
LLM detects a front from numbers
```

Better:

```text
LLM calls scientific tool
→ tool calculates
→ LLM interprets
```

---

## Anti-pattern 4 — Black-box risk score

Bad:

```text
Risk = 87%
```

without explanation.

Better:

```text
Wind: high
Wave: moderate
Cyclone: low
Lightning: elevated
Geofence: clear

Overall operational assessment:
Unfavorable

Confidence:
High
```

---

## Anti-pattern 5 — Treating inference as observation

Bad:

```text
High chlorophyll = fish abundance
```

Better:

```text
High chlorophyll
→ elevated productivity indicator
→ potentially favorable ecological conditions
```

---

## Anti-pattern 6 — Treating bathymetry as a navigation chart

Never do this.

General bathymetry can support analysis but is not automatically certified navigation information.

---

# 75. Recommended ORCA Scientific Architecture

The final architecture should be:

```text
                         ORCA
                           │
                           ▼
                     USER CONTEXT
                 role + location + time
                 objective + constraints
                           │
                           ▼
                     ORCHESTRATOR
                           │
                           ▼
                    TASK PLANNER
                           │
                           ▼
                DATA DISCOVERY / RETRIEVAL
                           │
                           ▼
                ┌─────────────────────────┐
                │ MARINE STATE BUILDER    │
                └────────────┬────────────┘
                             │
          ┌──────────────────┼───────────────────┐
          ▼                  ▼                   ▼
      OCEAN              WEATHER              SPATIAL
   INTELLIGENCE        INTELLIGENCE         INTELLIGENCE
          │                  │                   │
          └───────────┬──────┴───────┬──────────┘
                      ▼              ▼
                TEMPORAL        ECOSYSTEM
                INTELLIGENCE    INTELLIGENCE
                      │              │
                      └──────┬───────┘
                             ▼
                        RISK ENGINE
                             │
                             ▼
                       ROUTE ENGINE
                             │
                             ▼
                    DECISION INTELLIGENCE
                             │
                             ▼
                     EVIDENCE VALIDATOR
                             │
                             ▼
                    RESPONSE SYNTHESIZER
                             │
                ┌────────────┼────────────┐
                ▼            ▼            ▼
              CHAT         MAP         CHARTS
                             │
                             ▼
                           ALERTS
```

---

# 76. Final Design Philosophy

ORCA should think of the marine environment as a continuously changing state.

The user provides:

```text
WHO AM I?
WHAT DO I WANT TO KNOW?
WHERE?
WHEN?
WHAT ARE MY CONSTRAINTS?
```

The system determines:

```text
WHAT DATA IS REQUIRED?
WHAT SCIENTIFIC ANALYSIS IS REQUIRED?
WHAT CONSTRAINTS APPLY?
WHAT EVIDENCE SUPPORTS THE RESULT?
WHAT DECISION CAN BE JUSTIFIED?
```

Therefore the fundamental ORCA pipeline is:

```text
Stakeholder
    ↓
Intent
    ↓
Context
    ↓
Required information
    ↓
Data discovery
    ↓
Data retrieval
    ↓
Marine state
    ↓
Scientific analysis
    ↓
Risk / constraints
    ↓
Decision
    ↓
Evidence validation
    ↓
Explanation
```

---

# 77. One-Sentence System Definition

> **ORCA's Scientific & Marine Intelligence System is a deterministic, evidence-grounded computational layer that transforms heterogeneous oceanographic, meteorological, Earth-observation, ecosystem, temporal, and geospatial data into a machine-readable marine state and contextual scientific analyses that can support different marine stakeholders and operational decisions.**

---

# 78. Engineering Rule to Lock

The most important architectural rule for the entire project is:

> **Do not build scientific intelligence around a particular stakeholder. Build a reusable marine intelligence core, and let stakeholder context determine how that intelligence is applied.**

Thus:

```text
Fisherman
Researcher
Authority
Disaster Manager
Maritime Operator
Port Operator
Environmental Agency
        │
        ▼
   SAME MARINE
 INTELLIGENCE CORE
        │
        ▼
 DIFFERENT DECISIONS
```

This makes ORCA a genuine **marine decision-intelligence platform**, rather than a fishing application with additional features.
