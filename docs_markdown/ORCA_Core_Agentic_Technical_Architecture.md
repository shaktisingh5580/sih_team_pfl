# ORCA — Core Agentic System Architecture

**How the AI brain actually works — where the LLM sits, what it controls, and what it does NOT control.**

---

## The Core Idea

```
LLM = thinks, plans, interprets, explains
Scientific Engines = calculates (no LLM involved)
Data Foundation = provides evidence (no LLM involved)
```

The LLM never does the math. It decides WHAT math to do, WHICH data to get, and EXPLAINS the result.

---

## Core Technical Architecture

```mermaid
flowchart TD
    User((User))

    User -->|natural language\ntext or voice| NLU

    subgraph LLM_CORE["LLM — The Brain (Planning & Intent)"]
        direction TB
        NLU["NLU Intent Parser\n- What does user want? Where? When?\n- Language detection & complexity tier"]
        Planner["Supervisor Planner\n- What data is needed?\n- Which agents work in what order?"]
        Replan["Dynamic Re-planner\n- Checks if evidence is sufficient\n- Refines plan if data is missing"]

        NLU --> Planner
        Replan --> Planner
    end

    Planner -->|sends tasks to| Supervisor

    subgraph ORCHESTRATOR["Supervisor / Orchestrator"]
        Supervisor["Execution Supervisor\n- Tracks running tasks & execution state\n- Enforces latency, time & budget limits\n- Manages parallel vs sequential tasks"]
    end

    Supervisor -->|assigns work to| AgentLayer

    subgraph AgentLayer["Specialist Agents — each has its own LLM prompt"]
        direction TB
        subgraph EnvironmentalAgents["Marine & Atmospheric Intelligence"]
            OceanAgent["Ocean Agent\n• Analyzes SST, chlorophyll, fronts, upwelling\n• Decides which ocean analyses to run"]
            WeatherAgent["Weather Agent\n• Assesses wind, wave risk & cyclone threat\n• Evaluates official IMD/INCOIS warnings"]
        end
        subgraph SpatialAgents["Geospatial & Data Retrieval Intelligence"]
            DataAgent["Data Agent\n• Identifies and retrieves marine datasets\n• Manages INCOIS / MOSDAC source fallbacks"]
            GeoAgent["Geo Agent\n• Evaluates EEZ, geofences & marine zones\n• Calculates distance to nearest safe port"]
        end
        DecisionAgent["Decision Agent\n• Combines all findings into clear recommendations\n• Evaluates trade-offs & enforces safety boundaries"]
    end

    AgentLayer -->|agents invoke| ToolGateway

    subgraph ToolGateway["Tool Gateway — Deterministic Code, No LLM"]
        direction TB
        ToolCheck["Tool Validator: Checks permissions, schemas, input bounds & rate limits"]
        ToolCheck --> Tools
        
        subgraph Tools["Deterministic Compute Engines"]
            direction TB
            subgraph DataAndOcean["Data & Ocean Compute"]
                T1["Data Retrieval\nDownload INCOIS, MOSDAC, IMD via ERDDAP/REST"]
                T2["Ocean Science Engine\nSST anomaly, chlorophyll gradient, fronts, upwelling"]
            end
            subgraph HazardAndSpatial["Hazard & Spatial Compute"]
                T3["Weather Engine\nWind risk, wave risk, cyclone distance, lightning"]
                T4["Spatial Engine\nPostGIS point-in-polygon, distance, geofence"]
            end
            T5["Risk Engine\nDeterministic hazard scoring & safety rules"]
        end
    end

    Tools -->|structured results| EvidenceCheck

    subgraph EvidenceCheck["Evidence Validator — Code Verification + LLM Guardrails"]
        direction TB
        Check1["Deterministic Code Checks:\n- Data source verification & freshness\n- Physical units & spatial coverage"]
        Check2["LLM Guardrail Checks:\n- Reasoning coherence & safety\n- Claims strictly supported by evidence"]
        Check1 --> PassFail
        Check2 --> PassFail
        PassFail{Sufficient\nEvidence?}
    end

    PassFail -->|No — need more data| Replan
    PassFail -->|Yes — evidence verified| Synthesizer

    Synthesizer["Response Synthesizer (LLM)\n- Explains findings in plain language\n- Cites every source, timestamp & confidence\n- Explicitly highlights uncertainty boundaries\n- Responds in user's preferred regional language"]

    Synthesizer --> Response

    subgraph Response["User Decision Workspace (Output Surfaces)"]
        direction TB
        R1["Chat: Plain language answer with citations"]
        R2["Interactive Map: Auto-selected ocean layers & alerts"]
        R3["Evidence Panel: Source, timestamp & confidence scores"]
        R4["Agent Activity Log: Step-by-step verified execution trace"]
    end

    Response --> User

    subgraph Memory["Memory System — Injected into LLM Prompts"]
        direction TB
        M1["Working Memory: Current investigation state & scratchpad"]
        M2["User Profile: Vessel type, home port, language & preferences"]
        M3["Investigation Memory: Past inquiries & verified fishing spots"]
    end

    Memory -.->|context injection| LLM_CORE
    Memory -.->|context injection| AgentLayer
```

---

## How an Agent Actually Works Internally

Each agent follows the same pattern. Here is what happens inside ONE agent:

```mermaid
flowchart TD
    Task["Supervisor sends a task:\nAnalyze SST near Gujarat"]

    Task --> AgentLLM["Agent's LLM reads the task\nand its prompt"]

    AgentLLM --> Think["LLM thinks:\nI need to run SST lookup,\nthen SST anomaly,\nthen check if there is\na temperature front"]

    Think --> Call1["LLM calls Tool:\nsst_lookup\nregion: Gujarat offshore\ntime: today"]

    Call1 --> Gateway1["Tool Gateway validates\nand runs the code"]
    Gateway1 --> Result1["Result: SST = 28.4 C\nSource: INCOIS\nTime: 6 hours ago"]

    Result1 --> AgentLLM2["LLM reads the result\nand decides next step"]

    AgentLLM2 --> Call2["LLM calls Tool:\nsst_anomaly\nregion: Gujarat offshore\nbaseline: September average"]

    Call2 --> Gateway2["Tool Gateway validates\nand runs the code"]
    Gateway2 --> Result2["Result: Anomaly = +1.1 C\nabove 30-year average"]

    Result2 --> AgentLLM3["LLM reads both results\nand decides: done or more?"]

    AgentLLM3 --> Done{Enough\ninformation?}

    Done -->|Yes| Return["Return structured result\nto Supervisor:\nSST = 28.4 C\nAnomaly = +1.1 C\nNo front detected\nSources: INCOIS, ERDDAP\nConfidence: High"]

    Done -->|No| MoreTools["Call another tool\nand repeat"]
    MoreTools --> AgentLLM2
```

---

## Where LLM is Used vs Where Code Runs

| Step | Who does it | Why |
|---|---|---|
| Understand the user's question | **LLM** | Only AI can understand natural language |
| Create a plan of what to investigate | **LLM** | Requires reasoning about what is needed |
| Pick which agent to use | **LLM** | Requires judgment about which domain matters |
| Pick which tool to call inside an agent | **LLM** | Agent decides what analysis is relevant |
| Actually download data from INCOIS | **Code** | Deterministic API call, no AI needed |
| Calculate SST anomaly | **Code** | Math formula, no AI needed |
| Run PostGIS distance query | **Code** | Database query, no AI needed |
| Calculate wind risk score | **Code** | Fixed rules, no AI needed |
| Check if evidence is fresh and complete | **Code** | Rule-based validation |
| Check if interpretation makes sense | **LLM** | Requires reasoning |
| Decide if more evidence is needed | **LLM** | Requires judgment |
| Write the final answer | **LLM** | Only AI can explain in natural language |
| Translate to regional language | **LLM** | Language generation |

---

## The Key Rule

```
LLM reasons about WHAT to do.
Code does the actual DOING.
LLM explains WHAT happened.
```

The LLM never calculates sea temperature.
The LLM never runs a database query.
The LLM never downloads a file.

The code never understands a question.
The code never writes an explanation.
The code never decides what to investigate next.

---

## Agent Communication — How They Talk

Agents do NOT talk to each other directly. Everything goes through the Supervisor.

```mermaid
flowchart LR
    S["Supervisor\n(LLM)"]
    
    S -->|Task: Get SST data| A1["Data Agent\n(LLM + Tools)"]
    A1 -->|Result: SST data ready| S

    S -->|Task: Analyze ocean state| A2["Ocean Agent\n(LLM + Tools)"]
    A2 -->|Result: SST analysis done| S

    S -->|Task: Check weather| A3["Weather Agent\n(LLM + Tools)"]
    A3 -->|Result: Weather analysis done| S

    S -->|Task: Check location| A4["Geo Agent\n(LLM + Tools)"]
    A4 -->|Result: Location checks done| S

    S -->|Task: Make recommendation| A5["Decision Agent\n(LLM + Tools)"]
    A5 -->|Result: Final recommendation| S

    S -->|All results collected| V["Evidence Validator"]
    V -->|Validated| R["Response Synthesizer\n(LLM writes answer)"]
```

**Why this design:**
- No agent can go rogue — Supervisor controls everything
- No infinite loops — agents cannot call other agents
- Clear responsibility — each agent has one job
- Easy to debug — every step is logged through Supervisor
