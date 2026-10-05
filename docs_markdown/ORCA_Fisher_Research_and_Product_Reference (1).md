# ORCA — Fisher-Facing Product Research & Field Validation Reference

**Project:** ORCA — Marine EcOsystem Reasoning with Collaborative Agents  
**Focus of this document:** Fisher-facing product only  
**Primary geography for first field validation:** Dholai / Bilimora / Navsari, Gujarat  
**Broader scope:** Marine fishing communities across India  
**Research window emphasized:** October 2024 – October 2026, with a small number of older sources retained where they are still useful for product design or provide a long-running baseline.  
**Purpose:** Research reference for product design, fisherman survey, field interviews, PFZ use, navigation, safety, language, phone usability, connectivity, and feature planning.

---

## 1. Why this document was made

ORCA should not be designed as a collection of features decided in advance. The fisherman-facing product needs to start from the way fishing is actually done in India:

- how a trip is planned,
- how a fishing area is chosen,
- how a boat travels,
- how weather and sea conditions are checked,
- how fishing information is received,
- how PFZ information is understood,
- how a fisherman uses a phone on a moving boat,
- what happens when mobile internet is not available,
- how warnings reach the boat,
- how the fisherman returns to the harbour,
- and what information is useful after the trip.

The central question for ORCA is therefore not:

> **“What information can we show?”**

It is:

> **“What information does a fisherman need at a particular moment, and how can we make that information easy to understand and act on?”**

This document combines the research, product conclusions, field-survey questions, Dholai-specific information, PFZ findings, navigation findings, phone-usability findings, connectivity findings, safety findings, and feature ideas discussed during the ORCA work.

---

# 2. Research method and limits

This is a practical product research document, not a formal systematic literature review.

For the recent research work, a broad search was carried out across government sources, Indian research journals, fisheries institutions, university publications, marine-safety sources, app documentation, and recent field studies. More than 100 search-result candidates were screened, with the strongest and most directly useful sources selected for closer reading and inclusion here.

The most important sources were prioritized in this order:

1. Government and government-science sources such as INCOIS, ISRO, IMD-related material, Department of Fisheries, Fishery Survey of India, DG Shipping and CMFRI.
2. Peer-reviewed Indian fisheries and marine studies.
3. Recent studies that directly tested digital tools with fishermen or fish farmers.
4. Current descriptions of deployed applications such as SAMUDRA, Fisher Friend, FISH, and Nabhmitra-related systems.
5. Local studies around Dholai, Bilimora and Navsari.

### Important limitation

The evidence is geographically and operationally diverse. A study in Kerala, Odisha, Andhra Pradesh or the Sundarbans should not automatically be treated as proof that every fisherman in Gujarat behaves in exactly the same way.

Use the broader research to form hypotheses, then use the Dholai field survey to verify them locally.

---

# 3. The main conclusion

## India does not mainly have a shortage of marine information

India already has many sources of information:

- Potential Fishing Zone (PFZ) advisories,
- ocean-state forecasts,
- wind and wave information,
- tides,
- currents,
- sea-surface temperature,
- chlorophyll,
- cyclone and high-wave warnings,
- marine heat-wave information,
- fishing-vessel communication systems,
- navigation systems,
- geofencing,
- government schemes,
- market information,
- and fisheries databases.

INCOIS provides PFZ and ocean-state services, and SAMUDRA exposes PFZ, tides, marine heat waves, currents, winds, waves, swell and other warnings. The national VCSS plan also combines satellite communication with safety alerts, no-fishing-zone information, IMBL geofencing and Nabhmitra integration. The National Fisheries Digital Platform covers registration, schemes, credit, insurance, training, marketing and other fisheries functions. [R01][R02][R03][R04]

Therefore, ORCA should not try to win by saying:

> “We put weather, PFZ and GPS in one application.”

That is not enough because important parts of that already exist.

### Better problem statement for ORCA

> **Information is available, but the fisherman still has to collect it, understand it, compare it, decide what matters, and turn it into an action.**

ORCA should solve that last part.

---

# 4. The central product idea

## ORCA should feel like a trip companion, not a data portal

For the fisherman, the product should answer a small set of simple questions:

1. **Can I go?**
2. **Where should I go?**
3. **What will the sea be like during the trip?**
4. **What should I avoid?**
5. **How do I get there?**
6. **How do I return?**
7. **Why is ORCA telling me this?**

The complex work should happen in the background.

### The simple front end

> **ASK → UNDERSTAND → DECIDE → ACT**

### The complex back end

> collect information → check freshness → compare sources → calculate → check restrictions → evaluate evidence → recommend → explain

This separation is one of the strongest product ideas for ORCA.

---

# 5. What research tells us about the fisherman and the phone

## 5.1 Digital skill is not the same as owning a smartphone

A recent 2026 study on digital information systems for small-scale fisheries in the Sundarbans found that information is still spread across basic phones, radio, television, local communication and smartphones. It also reported limits around digital adoption, local information and language. This supports the idea that an application cannot assume that every fisherman is a comfortable smartphone user.

A 2026 Indian study of fish farmers in Andhra Pradesh found **usability** to be the strongest constraint dimension for digital/social-media information use, with an RBQ of 70.05. The largest individual constraint was the **lack of content in the user's preferred local language**, with an RBQ of 84.50. [R05]

This is strong evidence for designing ORCA around:

- local language,
- clear wording,
- large controls,
- simple screens,
- voice input,
- audio output,
- and very little typing.

## 5.2 Small screens and reading burden matter

A long-running Fisher Friend field study in Tamil Nadu, republished in 2025, identified practical phone problems such as:

- small screen size,
- too many scrolls,
- slow scrolling,
- small font size,
- and limited time available to use the device.

The same study reported preference for GPS integration, voice-enabled messages, water-resistant equipment, stronger batteries and simpler interaction. [R06]

Even though the original field study is older, these findings remain useful because the physical conditions of using a phone on a boat have not disappeared.

## 5.3 The newest INCOIS app research gives an even stronger lesson

The 2026 FISH app paper is especially important for ORCA. INCOIS originally considered a more detailed data-collection flow, but after consultations it simplified the app. The paper explicitly says simpler interaction was prioritized because overly complex processes could discourage fishermen from using the app. The application was localized into English, Hindi, Gujarati, Marathi, Kannada, Malayalam, Tamil, Telugu, Odia and Bengali and was designed to work offline because fishers frequently operate outside mobile-network coverage. [R07]

This is direct evidence from an Indian marine-service deployment:

> **More functionality does not automatically mean a better fisherman application.**

---

# 6. The biggest product lesson: complexity should stay inside ORCA

A fisherman should not have to understand:

- satellite products,
- SST,
- chlorophyll,
- ocean current models,
- several weather models,
- data-source differences,
- map layers,
- geospatial files,
- model confidence numbers,
- or which government organization provides which dataset.

Those things can exist in the system, but they should normally be hidden from the main interface.

### The fisherman should see

- **GO**
- **WAIT**
- **CAUTION**
- **RETURN**
- **GO TO PFZ**
- **OPEN MAP**
- **ASK ORCA**
- **HELP**

### The system should handle

- multiple data sources,
- source checks,
- time alignment,
- spatial alignment,
- route checks,
- hazard checks,
- PFZ evaluation,
- uncertainty,
- freshness,
- and explanations.

This is the simplest way to express the central design rule:

> **Complexity belongs inside ORCA, not in the fisherman's hands.**

---

# 7. What the fisherman actually needs during a trip

The fishing trip can be understood in five stages.

## Stage 1 — Before leaving

Questions:

- Is it a good time to leave?
- What is the weather?
- What are the waves like?
- Is there any official warning?
- Is there a useful PFZ nearby?
- How far away is it?
- Will conditions change later in the trip?
- Is there a restricted area on the way?

## Stage 2 — Travelling to the fishing area

Questions:

- Which direction?
- How far?
- How long will it take?
- Is the planned route crossing a danger/restricted zone?
- Are conditions getting worse?

## Stage 3 — Fishing

Questions:

- Is the fishing area still worth considering?
- Did the PFZ information become old?
- Are there hazards nearby?
- Have sea conditions changed?
- Should the fisherman stay, move, or return?

## Stage 4 — Return

Questions:

- Which direction is the harbour?
- How far is it?
- How long will it take?
- Will weather get worse before arrival?
- Is there a safer or more practical return route?

## Stage 5 — After the trip

Questions:

- Was the trip successful?
- What was actually caught?
- Was the PFZ useful?
- What happened compared with the forecast?
- Can the fisherman save this ground for later?

The product should follow this trip, rather than forcing the fisherman to think in terms of software modules.

---

# 8. Navigation research and what ORCA should do about it

## 8.1 Navigation is not only “GPS”

There are several different navigation problems:

### Finding a fishing area

The fisherman may combine:

- personal experience,
- traditional fishing grounds,
- previous successful locations,
- other fishermen,
- PFZ information,
- GPS,
- mobile maps,
- landmarks,
- or a boat navigation system.

### Reaching the fishing area

The direct shortest route is not always the best operational route.

The route can be affected by:

- weather,
- waves,
- current,
- restricted zones,
- international maritime boundaries,
- fishing areas,
- and vessel capabilities.

### Returning home

Returning is a separate need and should have a dedicated action:

> **RETURN TO HARBOUR**

### Navigating when visibility is poor

Ask fishermen what happens during:

- night,
- heavy rain,
- fog,
- reduced shore visibility,
- rough sea,
- or equipment failure.

## 8.2 Existing navigation systems already cover parts of this

ISRO documents a MapmyIndia/NavIC message receiver application that works offline, provides PFZ locations and waypoint navigation, displays live location, gives IMBL proximity alerts, and can receive emergency messages from INCOIS. [R08]

Nabhmitra and the national VCSS plan also cover vessel communication, adverse-weather alerts, no-fishing zones and geofencing. [R03][R09]

Therefore ORCA should **not** claim that it invented offline navigation or basic geofencing.

### ORCA should add context

Instead of:

> “PFZ A is here.”

ORCA can answer:

> “PFZ A is closer, but the route has worse sea conditions. PFZ B is farther but is the better option for this trip.”

That is a more meaningful decision problem.

---

# 9. Recommended navigation experience

## Two main route actions

### GO TO FISHING AREA

The user chooses a PFZ or saved fishing ground.

The screen should show:

- direction,
- distance,
- estimated travel time,
- route line,
- active restrictions,
- current hazards,
- and a large map button.

### RETURN TO HARBOUR

This action should always be easy to reach.

Show:

- harbour direction,
- remaining distance,
- estimated time,
- route condition,
- active hazards.

## Compass-style view

A large directional arrow can be more useful than a complicated map when the main question is “which way?”

Example:

> **Keep NE**  
> **042°**  
> **11.4 km**

The map should still be available below or through a single button.

---

# 10. PFZ: why it matters

Potential Fishing Zone (PFZ) advisories are an important existing Indian service. INCOIS explains that PFZ information is generated using satellite-derived sea-surface temperature and chlorophyll information, and that advisories are intended to reduce search time, fuel use and fishing effort. PFZ information is provided in local languages and can include location, depth, distance and direction from recognizable coastal points. Wind direction and speed are included because PFZ features can move. [R10][R11]

A 2025 peer-reviewed study along the southwest coast of India reported a positive relationship between PFZ advisories and daily village fish landings and discussed the usefulness of daily landing observations for PFZ validation and future fisheries forecasting. [R12]

A 2024 study also explored additional environmental signals such as chlorophyll, SST fronts, wind, currents, Ekman transport and eddies to improve PFZ interpretation. [R13]

### Important point

PFZ means a **potential** fishing zone. It does not mean:

> “Fish are guaranteed here.”

ORCA should preserve that distinction.

---

# 11. PFZ should not be just a map dot

A simple PFZ map is already available in existing services.

ORCA can make PFZ more useful by giving a complete trip context.

## PFZ card

Example:

### PFZ 01

**11.4 km from harbour**  
**NE 42°**  
**Fresh advisory**  
**Sea conditions: favourable**  
**Route: clear**  
**Restriction conflict: none**

**[GO TO PFZ]**

### PFZ 02

**17.8 km from harbour**  
**E 87°**  
**Older advisory**  
**Wind increasing later**

**[VIEW]**

ORCA can rank the available choices based on trip needs instead of forcing the fisherman to compare them manually.

---

# 12. PFZ freshness is important

Because the ocean changes, the fisherman needs to know whether the advisory is recent.

Every PFZ card should show:

- issued time,
- time since issue,
- source,
- freshness status,
- and where possible a simple evidence status.

Use simple words such as:

- **Fresh**
- **Getting old**
- **Old**

Avoid fake precision such as:

> “87.6% fish probability.”

The evidence does not justify that kind of number.

---

# 13. PFZ should be combined with distance and travel cost

PFZ research shows value in reducing search effort and fuel use, but the most scientifically attractive PFZ is not automatically the best PFZ for every boat. [R10][R12]

If a fisherman has two options:

**PFZ A**
- stronger PFZ signal,
- 32 km away,
- higher travel time.

**PFZ B**
- slightly weaker signal,
- 12 km away,
- better route conditions.

ORCA can say:

> **“PFZ B is the better option for this trip because it is closer and the route has better conditions.”**

This is a much more useful use of the PFZ service.

---

# 14. Save the fisherman's own fishing grounds

A useful feature should be:

## MY FISHING GROUNDS

The fisherman can save a location using:

- a map tap,
- GPS,
- or voice.

Examples:

> “Good sardine area.”

> “Avoid — rocky area.”

> “Usually good in July.”

The system should separate:

1. **Private fisherman knowledge**
2. **Community-shared information**
3. **Official/scientific information**

Private locations should not automatically become public.

This is important because a fishing ground can have economic value and trust implications.

---

# 15. Weather and sea conditions: show what changes a decision

INCOIS's Ocean State Forecast provides wind, waves, currents, water temperature and other ocean information at forecast intervals, with forecasts extending several days. [R14]

SAMUDRA exposes five-day ocean-state forecasts along with PFZ and marine alerts. [R01]

The fisherman does not need all of the raw numbers on the first screen.

Instead show:

### WIND
Moderate

### WAVES
Low → rising later

### RAIN
Low

### CURRENT
Moderate

### WARNING
None

Then:

### NEXT MAJOR CHANGE

> **Wind expected to increase after 11 AM.**

This converts a forecast into a decision.

---

# 16. Use “NOW” and “NEXT” instead of scientific tables

The main screen should have:

## NOW

What is happening now?

## NEXT 3 HOURS

What changes soon?

## NEXT 6 HOURS

Will the trip still look reasonable?

## TODAY

Overall trip picture.

This is better for action than displaying a long table of hourly weather values.

---

# 17. Official warnings must always be treated differently

Weather forecasts and official safety warnings are not the same thing.

For example:

> “Wind moderate”

is not equivalent to:

> “Official high-wave warning active.”

The official warning should be shown first when it exists.

The system should never say:

> “ORCA says the sea is safe.”

Prefer:

> **“No active official warning found. Current forecast conditions appear favourable based on available data.”**

For an official warning:

> **“Official warning active — avoid or return according to the advisory.”**

This distinction matters for safety and trust.

---

# 18. Alerts need priority, not volume

The fisherman should not receive a continuous stream of low-value notifications.

Use four levels.

## CRITICAL

Examples:

- cyclone warning,
- tsunami warning,
- very high-wave or swell-surge warning,
- emergency vessel message.

## IMPORTANT

Examples:

- restricted zone approaching,
- international boundary approaching,
- major route hazard.

## CAUTION

Examples:

- worsening wind,
- rising waves,
- forecast changing.

## INFORMATION

Examples:

- new PFZ advisory,
- updated market information.

Only the first two categories should normally interrupt the fisherman.

SAMUDRA already gives strong attention to active high-wave, swell-surge, current, tsunami and storm-surge alerts. ORCA's difference should be the connection between the warning and the fisherman's current trip. [R01]

---

# 19. Offline mode should be a main feature, not a backup feature

A fisherman can travel beyond normal mobile coverage.

The 2026 FISH study describes this directly and designs its application around offline use, retaining unsent information until connectivity returns. [R07]

ISRO's MapmyIndia/NavIC fisher application also provides offline operation. [R08]

Therefore ORCA should automatically download a **trip pack** before departure.

## Trip pack

At the harbour or whenever a connection is available, download:

- latest PFZ data,
- latest weather forecast,
- latest official warnings,
- relevant offline map area,
- saved fishing grounds,
- restricted zones,
- harbour information,
- emergency contacts,
- selected language content.

At sea, the app should continue to work with the last synchronized information.

Each important item should show its last update time.

---

# 20. Show “last updated” clearly

Example:

> **Weather:** 06:00 AM  
> **PFZ:** 05:30 AM  
> **Warnings:** 06:02 AM  
> **Map data:** yesterday  

The fisherman should immediately know whether he is looking at fresh information or cached information.

This fits ORCA's evidence and freshness design and is especially important when offline.

---

# 21. Phone use on a fishing boat is a special design problem

The phone may be used:

- under strong sunlight,
- with wet hands,
- on a moving boat,
- while wearing gloves,
- during engine noise,
- while the fisherman is doing another task,
- and sometimes for only a few seconds.

Therefore:

### UI rules

- large controls,
- large type,
- high contrast,
- little text,
- one main action per screen,
- no deep menus,
- no compulsory typing,
- simple map labels,
- voice input,
- audio responses,
- vibration for important alerts,
- strong offline behavior.

The earlier Fisher Friend usability study directly reported problems with small screens, too much scrolling, small fonts and limited time. [R06]

---

# 22. Voice is important, but voice alone is not enough

Voice solves several problems:

- typing difficulty,
- local-language access,
- limited time,
- users who are uncomfortable reading technical text.

But a boat is noisy. Wind, engine noise and multiple people may reduce speech accuracy.

Therefore the best design is:

> **Voice + large buttons + visual confirmation + audio answer**

Example:

Fisherman:

> “Aaje savare Dholai thi javu ke nahi?”

ORCA:

### CAUTION

> “Wind is expected to increase after 11 AM. Conditions are better earlier.”

On screen:

- Wind: Moderate
- Waves: Low
- Warning: None
- PFZ: 2 nearby

Buttons:

**PLAN TRIP**

**WHY?**

**OPEN MAP**

---

# 23. Local language is not an optional extra

The 2026 Andhra Pradesh study identified preferred local language as the largest reported constraint for fish farmers using digital information. [R05]

The current INCOIS FISH app supports multiple Indian coastal languages, including Gujarati, Hindi, Marathi, Kannada, Malayalam, Tamil, Telugu, Odia and Bengali. [R07]

INCOIS also provides PFZ maps and text in local languages. [R11]

Therefore ORCA should treat language as part of the core design.

### First field prototype

For Dholai:

- Gujarati
- Hindi
- English for technical testing

Later:

- Marathi
- Konkani
- Malayalam
- Tamil
- Telugu
- Kannada
- Odia
- Bengali

The spoken language and the written language should be independently configurable.

---

# 24. “Ask ORCA” should be a focused tool, not a general chatbot

The user can ask:

> “Where should I go today?”

> “Wave ketli che?”

> “Maro harbour ketlo door che?”

> “PFZ kya che?”

> “Pachha ketla time ma avi sakay?”

> “Aagal koi danger che?”

ORCA should turn the question into a real task.

Example:

### User

“Tomorrow morning where should I go?”

### System work

1. Understand trip time.
2. Get PFZ options.
3. Get forecast.
4. Check route.
5. Check restricted areas.
6. Check warning status.
7. Compare options.
8. Explain the best available option.

### User sees

> **Best available option: PFZ 02**  
> 12 km NE  
> Conditions favourable until about 10 AM  
> Wind increases later  
> **[GO TO PFZ]**

This is a better use of the language model than making it talk about everything.

---

# 25. Every important decision should have “WHY?”

Trust is important.

If ORCA says:

> **CAUTION**

then the fisherman should be able to tap:

### WHY?

and see:

- wind rising,
- wave forecast rising,
- official warning status,
- data freshness,
- and source names.

Example:

> **Why caution?**
>
> Wind is expected to rise after 11 AM. Wave conditions are also forecast to increase. No cyclone warning is currently active.
>
> **Sources:** IMD forecast, INCOIS ocean-state forecast.

This prevents the system from becoming a black box.

---

# 26. Geofencing and restricted areas

Fishermen need awareness of:

- no-fishing zones,
- international maritime boundaries,
- protected areas,
- port/harbour restrictions,
- and other relevant boundaries.

VCSS and Nabhmitra already support important parts of this capability. [R03][R08]

ORCA should therefore focus on making the information simple and useful in a trip decision.

Example:

> **PFZ 03 looks useful, but the direct route intersects a restricted zone. PFZ 02 is the better available option.**

That is more useful than only displaying the boundary.

---

# 27. Safety should include more than storms

Recent Indian research shows that fishermen face many occupational risks besides cyclones. A 2025 study of small-scale motorized fishers in southern India ranked heat-related stress, musculoskeletal problems, cyclones, heavy rain, insomnia and overexertion among the major hazards. [R15]

A 2026 synthesis of Indian fisherfolk health research also links climate and environmental changes with longer or riskier trips, physical injury and broader economic and health stress. [R16]

For the first ORCA product, the most relevant safety functions are still:

- weather alerts,
- high-wave/swell alerts,
- route hazards,
- restricted-zone alerts,
- return-to-harbour guidance,
- emergency contacts,
- official warning messages.

Health and heat information can be added later.

---

# 28. Return-to-harbour should be a first-class action

This deserves its own feature because returning is not the same as going out.

The fisherman may ask:

> “Can I return before conditions worsen?”

The screen should show:

### RETURN TO HARBOUR

**Distance:** 17.2 km  
**Estimated time:** 58 min  
**Direction:** SW  
**Weather:** worsening after 2 PM  
**Hazard ahead:** none / detected

Then:

**[START RETURN ROUTE]**

This is one of the most useful combinations of navigation + weather + time.

---

# 29. Add “what will change?”

A fisherman rarely needs every forecast variable. The important question is what changes his plan.

ORCA should have a simple section:

## WHAT WILL CHANGE?

Examples:

> Wind expected to increase after 11 AM.

> Waves expected to rise during your return window.

> An official advisory was issued after your last sync.

> The PFZ is now older than the freshness threshold used by the system.

This can be more useful than a chart.

---

# 30. Boat profile

A one-time setup can make ORCA more useful without adding daily work.

### Boat profile

- boat type,
- length,
- engine information,
- typical speed,
- fuel capacity,
- typical operating range,
- number of crew,
- gear/fishing method.

Then the same PFZ can be evaluated differently for different boats.

The goal is not to tell every boat exactly where to fish, but to avoid giving the same recommendation without considering basic trip constraints.

---

# 31. Fuel and effort comparison

This should be optional but useful.

Example:

### PFZ A

Distance: 32 km  
Travel time: high  
Fuel effort: higher  
PFZ evidence: strong

### PFZ B

Distance: 12 km  
Travel time: low  
Fuel effort: lower  
PFZ evidence: good

### ORCA view

> **PFZ B is the better balance for this trip.**

This turns the system into a practical decision tool rather than a scientific display.

---

# 32. Local knowledge should be part of the system

Scientific data should not replace fisher knowledge.

The system should allow the fisherman to record:

- local fishing ground,
- unusual current,
- poor visibility,
- local hazard,
- good catch,
- poor catch,
- gear problem,
- or another useful observation.

This can be done through voice, a simple map tap or a small number of choices.

The important design rule is:

> **Local knowledge should complement official/scientific data, not silently replace it.**

---

# 33. A simple post-trip feedback loop

The fisherman should not fill a long form after returning.

A simple flow could be:

### HOW WAS THE TRIP?

**Good** | **Average** | **Poor**

Then optional:

### CATCH

> Sardine — 40 kg

> Pomfret — 8 kg

The FISH project shows why this type of catch information can matter: georeferenced catch observations can be used to improve future fisheries advice and species-specific forecasting. However, the same project also showed that installation alone does not guarantee active use; training and a clear user benefit matter. [R07]

Therefore ORCA should make post-trip reporting extremely short.

---

# 34. The learning loop for ORCA

The long-term concept can be:

> **Recommendation → real trip → real outcome → feedback → better future advice**

This creates a useful relationship between:

- satellite data,
- ocean conditions,
- PFZ,
- weather,
- route,
- local knowledge,
- and real fishing outcomes.

But the first version should not promise perfect catch prediction.

---

# 35. Historical comparison

Another useful future feature is:

## MY GROUND — THEN VS NOW

Example:

> Sea temperature is higher than your recent seasonal average.

or:

> Your saved fishing ground has had weaker conditions compared with the previous period.

This is useful for understanding changes in fishing patterns.

Recent work on Indian coastal fisheries describes changes in weather, sea temperature, fish distribution, fishing days and livelihoods. [R17][R18]

Historical comparison is therefore more useful than showing only today's number.

---

# 36. Climate and changing fish patterns

Climate and marine-environment change appear repeatedly in Indian fisheries research.

Recent Indian research reports links between:

- changing sea temperature,
- unusual weather,
- cyclones,
- fishing-day losses,
- catch changes,
- and livelihood stress. [R17][R18][R19]

One recent Odisha study also connected declining catch, extreme weather, coastal erosion and rising sea temperature with livelihood pressure and migration. [R20]

This suggests a future ORCA service:

### “What changed in my usual fishing area?”

rather than only:

### “What is the temperature today?”

---

# 37. Pollution and environmental hazards

Fishing problems are not limited to weather.

A 2026 study from coastal Andhra Pradesh examined industrial pollution, environmental degradation and changes in fishing livelihoods. The authors stressed that the study involved only three fishermen and should not be generalized to all communities, but it is useful as an example of how environmental degradation can affect local fishing. [R21]

A 2025 study around Chilika reported that most sampled fishers believed degraded water quality harmed fishing, with some reporting reduced catch and income. [R22]

A future ORCA layer could therefore flag:

- known pollution events,
- unusual environmental conditions,
- harmful algal bloom information where available,
- marine heatwaves,
- and other relevant official/environmental advisories.

This should be added carefully and only when a reliable data source exists.

---

# 38. Economic problems are important, but should not make the app too large

Indian fishing communities face economic pressure from:

- fuel costs,
- uncertain catches,
- fish-price changes,
- equipment costs,
- debt,
- market power differences,
- and post-harvest losses.

Research from Gujarat has also documented pressure created by debt and trader relationships in some fishing communities. [R23]

The government is now expanding the National Fisheries Digital Platform with information about schemes, credit, insurance, training, marketing, e-auctions and other fisheries services. [R04]

### Product decision

Do not put all of that into the main sea screen.

Instead, use a separate:

## SHORE

section later for:

- market information,
- scheme information,
- insurance,
- training,
- cooperative information,
- and other shore-side services.

The central ORCA fishing experience should remain focused on marine decisions.

---

# 39. Fisherwomen and shore users

The fishing economy includes many women who work in processing, marketing and other parts of the value chain.

MSSRF's 2024–25 annual report describes a FisherWomenConnect application intended to support fisherwomen with weather information, market trends and digital marketing support. [R24]

This suggests that a long-term ORCA ecosystem could include a different shore-facing experience rather than forcing the same interface on everyone.

### Fisher mode

Trip, weather, PFZ, route, hazard, return.

### Shore mode

Vessel status, arrival, market, schemes, catch, price, weather, community information.

### Research mode

Data, maps, history, sources, comparisons, analysis.

The three experiences can use the same underlying data foundation while keeping the interfaces separate.

---

# 40. Trust and location privacy

Fishing locations can be economically sensitive.

A fisherman may not want a private fishing ground to be automatically shared.

ORCA should therefore clearly distinguish:

### Private

Only the fisherman sees it.

### Shared with selected people

Boat owner, family, cooperative, etc.

### Community

Only if explicitly contributed.

### Public/scientific

Official/public information.

The system should ask for location permission only when it is needed, and explain why.

Trust is part of product adoption, not just a technical security matter.

---

# 41. The fisherman should not need a complicated registration process

The user should be able to reach the main value quickly.

Possible first setup:

1. Choose language.
2. Choose boat type.
3. Select home harbour.
4. Optional boat profile.
5. Download local trip data.
6. Start.

Avoid a long form before the first useful answer.

For features that need registration or government identity, registration can be added later.

The lesson from recent fisheries app work is that field users need a clear reason to continue using the application. [R07]

---

# 42. One-screen fisherman home design

The central fisherman screen should look more like a cockpit than a dashboard.

Suggested structure:

```text
┌─────────────────────────────────────┐
│ ORCA                         06:10  │
│ Dholai                     ● Synced │
├─────────────────────────────────────┤
│                                     │
│        TODAY AT SEA                 │
│                                     │
│        CAUTION                      │
│        Conditions change later      │
│                                     │
│  Wind       Moderate                │
│  Waves      Low → Rising            │
│  Warning    None                    │
│  PFZ        2 nearby                │
│                                     │
│            [ WHY? ]                 │
├─────────────────────────────────────┤
│        BEST AVAILABLE PFZ           │
│                                     │
│        PFZ 02                       │
│        11.4 km • NE                 │
│        Fresh • Route clear          │
│                                     │
│         [ GO TO PFZ ]               │
├─────────────────────────────────────┤
│        NEXT CHANGE                  │
│        Wind increases after 11 AM   │
├─────────────────────────────────────┤
│ [ MAP ] [ ASK ORCA ] [ ALERTS ]     │
│                         [ HELP ]     │
└─────────────────────────────────────┘
```

The main screen does not show 20 data layers.

It shows the decision and the most important reasons.

---

# 43. Fisher app navigation structure

Keep the bottom navigation to four main items:

## HOME

Trip cockpit.

## MAP

Route, PFZ, hazards, restrictions, harbour.

## ASK ORCA

Voice-first questions.

## ALERTS

Official and contextual warnings.

The user should not need more than that for the first version.

---

# 44. The map should open for a reason

Do not make the fisherman open a generic map and then configure ten layers.

Instead:

### From PFZ

Tap **GO TO PFZ** → map opens directly on that PFZ with route.

### From alert

Tap **VIEW** → map opens on the hazard.

### From return

Tap **RETURN TO HARBOUR** → map opens with return route.

### From saved location

Tap **MY GROUND** → map opens directly there.

This is a simple example of good software design: the map should support the current task.

---

# 45. Map layers

The fisherman does need layers, but they should be hidden behind one button.

### Suggested layers

- PFZ
- Weather
- Waves
- Current
- Restrictions
- Hazards
- Harbour
- My grounds

Default state should show only the layers relevant to the current action.

---

# 46. “SEA NOW” screen

If the fisherman just wants to know current conditions:

# SEA NOW

### WIND
Moderate

### WAVES
Low

### CURRENT
Moderate

### RAIN
Low

### VISIBILITY
Good

### WARNING
None

Then:

### NEXT CHANGE
Wind increasing later.

This is far easier than requiring the user to read several charts.

---

# 47. “TRIP DECISION” is a core ORCA feature

This should be one of the main features in the product specification.

It combines:

- official warnings,
- weather,
- waves,
- currents,
- PFZ,
- restrictions,
- route,
- vessel profile,
- travel time,
- and data freshness.

The result should be one simple trip status:

### FAVOURABLE

or

### CAUTION

or

### AVOID / RETURN

The wording must be carefully tied to available evidence. It should never be presented as an absolute guarantee of safety.

---

# 48. The system should explain the difference between data, evidence and a decision

A useful internal structure is:

### DATA

Example:

Wind = 18 km/h

### EVIDENCE

Forecast says wind increases after 11 AM.

### DECISION SUPPORT

Morning departure appears more favourable than late departure.

The fisherman normally only needs the third one, with the first two available through “WHY?”.

---

# 49. What ORCA can realistically solve

| Problem | Can ORCA help? | Main response |
|---|---|---|
| Too many information sources | Strongly | One trip view |
| Complex marine information | Strongly | Simplify and explain |
| Local-language barrier | Strongly | Local language + voice |
| Typing difficulty | Strongly | Voice + large buttons |
| Small-screen burden | Strongly | Simple cards, progressive detail |
| Poor mobile network | Partly | Offline trip pack |
| PFZ interpretation | Strongly | Rank + explain + route |
| Weather interpretation | Strongly | Convert forecast to actions |
| Route selection | Partly/strongly | Route engine + constraints |
| Restricted zones | Strongly | Geofencing + simple warning |
| Returning to harbour | Strongly | One-tap route |
| Fishing-ground memory | Strongly | Saved private grounds |
| Catch recording | Strongly | Very short post-trip flow |
| Better future PFZ validation | Partly | Catch feedback |
| Fish catch prediction | Partly | Research/future feature |
| Fish price | Possible | Shore module |
| Debt | Not directly | Outside core scope |
| Emergency satellite communication | Integration | Use existing government systems |
| Medical care | Limited | Contacts/first-aid information |
| Poverty | Not directly | Requires broader programs |

---

# 50. What ORCA should NOT promise

Avoid statements such as:

- “ORCA knows exactly where fish are.”
- “ORCA guarantees safe travel.”
- “ORCA replaces the boat's navigation system.”
- “ORCA replaces official warnings.”
- “ORCA predicts the exact catch.”
- “ORCA works everywhere without any connectivity.”
- “The route is certified safe.”

Better wording:

- “Based on available PFZ information.”
- “Based on the latest available forecast.”
- “Official warning status.”
- “Estimated route.”
- “Evidence currently available.”
- “Information last updated at…”

---

# 51. Existing products ORCA must be compared against

## INCOIS PFZ service

Provides PFZ maps and text, local-language dissemination, distance/direction guidance, and related services. [R10][R11]

### ORCA opportunity

Use PFZ as one input and connect it with the fisher's trip.

## SAMUDRA

Provides active alerts, PFZ, tides, marine heat waves, currents, waves, winds and other ocean-state services, with interactive maps and charts. The current public app listing says the app is served in English, while coastal languages are proposed. [R01][R25]

### ORCA opportunity

Simpler fisherman experience, voice-first questions, trip recommendations, route context, freshness, explanation.

## Fisher Friend

Has a broad fisher-facing set of functions including weather, schemes, district news, tracking, contacts, and other fisheries information. MSSRF reports more than 106,000 overall users in 2024–25, and the current Android listing remains active. [R24][R26]

### ORCA opportunity

Do not copy the whole menu. Focus on marine trip decisions.

## FISH by INCOIS

Designed for multilingual, offline, field data collection and catch observations. Recent research explicitly reports the need to keep the fisher-facing workflow simple. [R07]

### ORCA opportunity

Use the same lesson: simpler field operation, clear value, multilingual/offline.

## Nabhmitra / VCSS / NavIC-related fisher systems

Cover important parts of vessel communication, geofencing, emergency alerts, offline navigation and PFZ access. [R03][R08][R09]

### ORCA opportunity

Do not replace them. Connect decision support to the information they already provide.

## National Fisheries Digital Platform

Covers a wide set of fisheries services such as registration, schemes, credit, insurance, training, marketing and traceability. [R04]

### ORCA opportunity

Use a future shore-side connection rather than turning the sea screen into a government portal.

---

# 52. A key product gap: “one screen for the decision”

Existing systems are strong at providing individual services.

The ORCA opportunity is to make a single fisher-facing trip screen that answers:

> **What is the situation for my trip right now?**

This screen should combine:

- warning status,
- sea conditions,
- PFZ options,
- route status,
- restriction status,
- data freshness,
- and the recommended next action.

This is the part that should be tested in the field.

---

# 53. The field survey should test real behavior, not opinions about ORCA

Do not begin with:

> “Would you use our application?”

Do not begin with:

> “Do you think an AI assistant is useful?”

Instead ask:

> “How do you decide where to fish?”

> “How do you check weather?”

> “What do you do when the network is unavailable?”

> “How do you return to the harbour?”

> “What is difficult about using your phone?”

> “What happens when two sources disagree?”

> “What information do you wish you could get more easily?”

The app should be designed from these answers.

---

# 54. Recommended Dholai fisherman survey

## Part A — Background

1. What is your role?
   - fisherman/crew
   - captain
   - boat owner
   - other

2. How many years have you been involved in fishing?

3. What type of fishing do you mainly do?

4. How long is a normal fishing trip?

5. How far from the harbour do you normally travel?

## Part B — Navigation

6. How do you find your fishing area?

7. Do you use GPS?

8. What navigation equipment do you use?

9. Do you use a smartphone while fishing?

10. Which apps do you actually use?

11. How do you save or remember a good fishing location?

12. How do you find the harbour when returning?

13. What happens if visibility becomes poor?

14. Have you ever had difficulty finding the way back?

## Part C — Weather and ocean information

15. What information do you check before leaving?

16. Where do you get it?

17. How many sources do you normally check?

18. What happens when two sources disagree?

19. Which marine information is hardest to understand?

20. What weather warning information do you need while already at sea?

## Part D — PFZ and fishing location

21. How do you decide where to fish?

22. Do you use PFZ information?

23. Where do you receive PFZ information?

24. What is difficult about using PFZ information?

25. How much do distance and fuel affect your decision?

26. How often is the PFZ information useful when you actually reach the area?

## Part E — Phone use

27. What is difficult about using a smartphone on the boat?

28. Is typing difficult?

29. Are maps difficult to understand?

30. Is reading difficult in sunlight?

31. Does water on the screen create problems?

32. Do you prefer voice or typing?

33. Which language do you prefer?

## Part F — Network and power

34. How often do you lose mobile network at sea?

35. What do you do without network?

36. Have you had a phone-battery problem at sea?

37. How do you charge your phone on the boat?

## Part G — Safety

38. What are the biggest dangers you face?

39. Have you received an official warning while at sea?

40. How did you receive it?

41. What would be most useful during a dangerous situation?
   - voice warning
   - map
   - direction to safe/harbour area
   - direct call/help
   - other

## Part H — Open questions

42. What information do you wish you could get before going to sea?

43. What information do you wish you could get while already at sea?

44. What is the one problem you most want technology to solve?

---

# 55. Observe phone skill instead of only asking about it

A very useful field method is to ask the fisherman to show how he normally checks something on his phone.

Record:

- Can open the app independently?
- Can find weather information?
- Can search a location?
- Can read a map?
- Can understand map symbols?
- Can share location?
- Can use voice search?
- Can follow a route?
- Can change language?
- Can find the harbour?

This is more useful than simply asking:

> “Are you comfortable with smartphones?”

---

# 56. The strongest field question

One question from the combined research should be asked to almost every fisherman:

> **“When you need important information at sea, what is hardest: getting the information, understanding the information, or deciding what to do with it?”**

Give three choices:

### GET IT

### UNDERSTAND IT

### ACT ON IT

This directly tests ORCA's main product hypothesis.

---

# 57. Another strong field question

Ask:

> **“When two sources give different weather or fishing information, who do you trust?”**

Then ask why.

Possible answers may include:

- government advisory,
- experienced fisherman,
- weather app,
- harbour,
- another boat,
- personal experience.

This gives you real information about trust and source selection.

---

# 58. Dholai-specific field context

Dholai is a particularly good place for field validation because it is an active fishing harbour and has recent fisheries research.

A 2026 Dholai study covering September 2025 to April 2026 described the harbour as South Gujarat's largest operational fishing harbour and reported approximately 250 registered and actively operating fishing vessels. [R27]

A 2024 socio-economic study covered Bilimora, Dholai, Bhat and Mendar and reported approximately 300 fishing families across those selected villages. [R28]

The Gujarat Marine Fisheries Census 2016 recorded **1,189 active fishermen in Dholai**, 400 people in fish marketing-related activity, and other fishing-linked occupations. This is a historical baseline, not a current count. [R29]

A 2025 study of the Bilimora wholesale fish market reported 22 enrolled traders and an observed daily market volume of about 30 tonnes, with activity concentrated in the early morning. [R30]

These facts make Dholai/Bilimora useful for a mixed field study:

- fishermen,
- boat crews,
- boat owners,
- fish traders,
- fisheries academics,
- and local service providers.

---

# 59. Suggested sample for the first Dholai field study

You do not need hundreds of respondents for an initial product study.

A practical target is:

### 20 respondents — minimum useful first pass

### 30–40 — good for a hackathon field study

### 50+ — strong field evidence if time allows

Try to mix:

- 8–10 boat owners/captains,
- 10–15 experienced fishermen,
- 8–10 crew/younger fishers,
- and a few traders or fisheries-side people for the wider context.

Do not claim this sample represents all fishermen in Gujarat or India.

Call it:

> **Regional field-validation survey at Dholai Fishing Harbour, Navsari**

---

# 60. Secondary stakeholder interviews

The fisherman is the primary user, but the wider research network matters.

## Fisheries professor/researcher

Ask:

> Which marine variables actually matter for fishermen's decisions?

> What are the limitations of PFZ?

> Which information do fishermen commonly misunderstand?

> What would make fisheries information more practical?

## Meteorologist

Ask:

> Which forecast variables are most important for fishing trips?

> How should warning uncertainty be communicated?

## Ocean-data scientist

Ask:

> Which datasets are reliable and accessible?

> How fresh are they?

> What are the known limitations?

## Fisheries officer

Ask:

> What official information already exists?

> Where does the information-delivery gap remain?

## Harbour/port/safety person

Ask:

> What incidents and communication problems are common?

> What information is most important during an emergency?

This gives ORCA evidence from the complete information chain.

---

# 61. Feature priority for the first fisherman prototype

## P0 — Must have

1. **Today / Trip cockpit**
2. **PFZ Scout**
3. **Weather and sea conditions**
4. **Route to PFZ**
5. **Return to Harbour**
6. **Official warnings**
7. **Restricted-zone/geofence awareness**
8. **Voice in Gujarati/Hindi/English**
9. **Offline trip pack**
10. **Why? explanation**
11. **Last updated time**
12. **Simple map**

## P1 — Very useful

1. My Fishing Grounds
2. Boat Profile
3. Trip history
4. Fuel/effort comparison
5. Local hazard report
6. Share trip status
7. Catch feedback
8. Historical comparison
9. Tide information
10. Harbour information

## P2 — Future

1. Species-specific forecasting
2. Fish price optimization
3. Community knowledge network
4. Pollution intelligence
5. Marine heatwave reasoning
6. Advanced catch prediction
7. Insurance/scheme integrations
8. Marketplace
9. Fleet/cooperative analytics

Do not put all P2 features into the SIH prototype.

---

# 62. Recommended fisherman app structure

```text
ORCA FISHER
│
├── HOME
│   ├── Trip Decision
│   ├── Sea Now
│   ├── Best PFZ
│   ├── Next Change
│   └── Last Updated
│
├── MAP
│   ├── My Location
│   ├── PFZ
│   ├── Route
│   ├── Hazards
│   ├── Restrictions
│   ├── Harbour
│   └── My Grounds
│
├── ASK ORCA
│   ├── Voice
│   ├── Text
│   ├── Quick Questions
│   └── Why?
│
└── ALERTS
    ├── Critical
    ├── Important
    ├── Caution
    └── Information
```

---

# 63. One-screen information architecture

The first screen should contain only four information groups.

## 1. TRIP STATUS

Favourable / Caution / Avoid

## 2. CURRENT CONDITIONS

Wind / waves / rain / warning

## 3. BEST AVAILABLE FISHING OPTION

PFZ + distance + direction + freshness

## 4. NEXT CHANGE

What will change during the trip?

Everything else should be one tap away.

---

# 64. Recommended visual design for the fisherman app

The interface should use:

- white background,
- very light blue support areas,
- dark navy/charcoal text,
- one main blue accent,
- red only for critical hazards,
- amber for caution,
- green for favourable conditions.

Avoid:

- neon gradients,
- dark cyberpunk styling,
- glowing effects,
- many decorative icons,
- tiny labels,
- technical dashboards,
- long paragraphs.

### Design character

The application should feel:

- calm,
- clear,
- trustworthy,
- practical,
- easy to learn,
- and usable under pressure.

---

# 65. Do not make it look like Google Maps for the ocean

A map is not the whole product.

The fisherman needs:

> **Direction + destination + distance + hazard + route**

before he needs a sophisticated map.

Therefore a large directional arrow can be more useful than a full map at some moments.

The full map remains available when the fisherman wants it.

---

# 66. The role of “Ask ORCA” on the main screen

Place one large button:

## ASK ORCA

The user should not have to decide whether the question belongs to “weather,” “PFZ,” “navigation,” or “alerts.”

He can simply ask:

> “Should I leave now?”

> “Where is the nearest PFZ?”

> “What is the sea like?”

> “How far is my ground?”

> “Can I return before the wind increases?”

ORCA should work out which information is required.

This is one of the most important differences between a normal information app and the planned system.

---

# 67. Why the language model should not make the scientific decision by itself

For marine decisions, the language model should not invent:

- current values,
- wave values,
- PFZ points,
- restricted zones,
- weather warnings,
- or route safety.

The system should retrieve real data from the proper source, run calculations where needed, check the evidence, and then let the language model explain the result in simple language.

This keeps the user interface simple without making the science unreliable.

---

# 68. Source hierarchy for the fisherman product

A practical source hierarchy should be:

### Safety warnings

Prefer official government/authorized warning sources.

### PFZ

Prefer INCOIS PFZ service.

### Ocean state

Prefer INCOIS ocean-state information and compatible validated sources.

### Weather

Use the appropriate official/validated meteorological forecast source available for the service.

### Geofences

Use authoritative legal/operational boundaries where required.

### Navigation

Use actual device location and appropriate marine/geospatial information, with clear limitations.

### Historical/context data

Use compatible scientific datasets and clearly label dates.

---

# 69. Data freshness rules

For every important data type, the system should store:

- source,
- issue time,
- received time,
- valid time,
- geographical coverage,
- and age.

A simple internal rule can be:

> **Do not silently use old data when the user expects current information.**

If the latest warning cannot be retrieved:

> **“Latest warning status could not be confirmed. Last successful update: 08:20 AM.”**

That is much safer than pretending everything is current.

---

# 70. Connectivity design

## Online

Use live updates.

## Weak network

Use cached information and retry quietly.

## Offline

Use trip pack and saved maps/data.

## Connection returns

Synchronize updates.

The app should clearly show:

> **Offline — using data from 05:30 AM**

rather than silently behaving as if it has live data.

---

# 71. Emergency design

The ORCA emergency screen should be extremely simple.

## EMERGENCY

### CURRENT LOCATION

### NEAREST HARBOUR / SAFE POINT

### CALL

### SOS / EXISTING EMERGENCY LINK

### RETURN ROUTE

ORCA should integrate with existing government communication systems where appropriate rather than claiming to replace them.

The national VCSS project is being rolled out for one lakh marine fishing vessels and is designed around satellite communication, safety alerts, no-fishing zones, IMBL geofencing and Nabhmitra integration. [R03]

---

# 72. Family / shore sharing

A simple future feature:

## SHARE TRIP

> Departed: 05:42 AM  
> Destination: PFZ 02  
> Expected return: 02:20 PM

This can help connect boat, family and shore-side people.

It should be optional and transparent.

---

# 73. Catch and trip feedback should be tiny

After the trip:

### HOW WAS THE TRIP?

Good / Average / Poor

### WAS THE PFZ USEFUL?

Yes / Partly / No / Not used

### OPTIONAL CATCH

Photo / species / rough amount

The Fisher Friend app also demonstrates that broad, practical fisher services can have significant reach, while the FISH study demonstrates that user participation improves when the task is made simple and its benefit is understood. [R24][R07]

---

# 74. What should make ORCA different

The strongest difference is not “more features.”

It is the following chain:

### Existing systems

**provide information**

### ORCA

**understands the fisher's question → gets the needed information → checks it → compares it → explains it → gives one practical next step**

That is the product identity.

---

# 75. What should be different on the researcher app

The user has already decided that researchers should get a separate experience.

That is a good decision.

The researcher interface can show:

- SST maps,
- chlorophyll maps,
- currents,
- wave fields,
- historical comparison,
- source lineage,
- data downloads,
- uncertainty,
- catch observations,
- PFZ creation/analysis,
- model outputs,
- and deeper graphs.

The fisherman should not get this interface by default.

---

# 76. The fisherman and researcher views should use the same evidence

This is important.

They can share the same underlying source layer but display it differently.

## Researcher

“Chlorophyll anomaly + SST front + current structure + historical comparison.”

## Fisherman

“PFZ 02 looks more favourable for this trip.”

The science remains the same. The presentation changes.

---

# 77. What we should test in the first ORCA field prototype

The prototype should test six main things.

### Test 1 — Can the fisherman understand the home screen in 10 seconds?

### Test 2 — Can he find the best PFZ without training?

### Test 3 — Can he understand the route?

### Test 4 — Can he ask a question by voice?

### Test 5 — Can he understand an alert?

### Test 6 — Can he return to the harbour function without help?

If these six work, the core experience is strong.

---

# 78. Usability test method at Dholai

Instead of only asking what fishermen think, give them simple tasks.

## Task A

“Find today's best available fishing area.”

Measure:

- time,
- mistakes,
- whether they needed help.

## Task B

“Tell me what will happen after 11 AM.”

Measure whether they can find the forecast change.

## Task C

“Show me how you would return to the harbour.”

Observe route use.

## Task D

“Ask ORCA something using your voice.”

Observe whether the interaction feels natural.

## Task E

“Find what caused the warning.”

Check if the “WHY?” function is understandable.

---

# 79. Metrics to collect from the field

Useful metrics include:

- percentage using smartphone,
- percentage using GPS,
- percentage using marine navigation hardware,
- percentage checking multiple information sources,
- percentage using PFZ,
- percentage reporting network problems,
- percentage reporting phone usability problems,
- percentage preferring voice,
- percentage preferring Gujarati,
- percentage wanting route guidance,
- percentage wanting sea-condition summaries,
- percentage wanting PFZ explanation,
- percentage wanting return-to-harbour guidance.

Do not put guessed values on the PPT.

Only use values after the field survey.

---

# 80. The survey should produce direct product evidence

A strong result might look like:

> **28/35 fishermen check more than one information source before departure.**

> **24/35 prefer local-language information.**

> **21/35 reported difficulty using maps/apps on the boat.**

> **26/35 wanted a simpler weather/sea summary.**

> **20/35 wanted a direct route back to harbour.**

These are examples only. They must not be presented as actual results until collected.

---

# 81. Questions to ask boat owners separately

Boat owners can give different information from crew.

Ask:

- How is fuel use managed?
- How are fishing grounds selected?
- How much does distance affect the trip?
- What causes a trip to be cancelled?
- What navigation equipment is fitted?
- What information is trusted?
- Do they track boats?
- How are warnings communicated?
- What happens if a boat is overdue?
- What information would reduce wasted trips?

---

# 82. Questions to ask fish traders

Ask:

- When do boats usually arrive?
- How predictable is supply?
- What causes supply changes?
- How much does weather change fish availability?
- How do they learn expected arrivals?
- What problems occur with freshness/ice?
- What information would help them prepare?
- How are market prices communicated?

The Bilimora market research shows that a substantial local trading network exists around Navapura. [R30]

---

# 83. Questions to ask fisheries researchers

Ask:

- Which environmental indicators are actually useful?
- How should PFZ be interpreted?
- What is the lag between environmental conditions and fish aggregation?
- Which species respond differently?
- What data can be obtained reliably?
- What data should not be presented as real-time?
- Where do forecasts fail?
- How should uncertainty be communicated?

The recent PFZ research specifically highlights environmental lag, trophic relationships and species-specific forecasting as important research directions. [R12]

---

# 84. Questions to ask weather experts

Ask:

- Which variables are most important for fishermen?
- How accurate are local forecasts at the relevant time scales?
- How should forecast changes be displayed?
- Which warnings should interrupt the user?
- How much lead time is normally meaningful?
- How should uncertainty be expressed?

---

# 85. Questions to ask satellite/ocean-data experts

Ask:

- Which datasets have programmatic access?
- What is the update frequency?
- What is the spatial resolution?
- What happens under clouds or missing observations?
- How long does processing take?
- Which variables are most useful for PFZ work?
- Which services are authoritative?

This will help ORCA avoid promising data that cannot actually be delivered.

---

# 86. Questions to ask fisheries officers

Ask:

- Which advisories are already available?
- How are they delivered?
- Where does delivery break down?
- Which warnings are mandatory/official?
- What local-language material already exists?
- What information do fishermen repeatedly ask for?
- What is the role of cooperatives and harbour staff?

---

# 87. What we learned from Dholai/Bilimora specifically

Dholai is not simply a theoretical test site.

Recent research has studied fish landings at Dholai during 2025–2026 and reported a large active fishing fleet. [R27]

The 2024 socio-economic study looked at Bilimora, Dholai, Bhat and Mendar together, providing a local context for fishing families and livelihoods. [R28]

Bilimora has a documented wholesale fish market with 22 enrolled traders in the 2025 study, creating a useful second location for interviews. [R30]

Therefore a strong field plan is:

### Morning

Dholai harbour:

- fishermen,
- captains,
- boat owners,
- landing activity.

### Later morning

Bilimora/Navapura fish market:

- wholesalers,
- traders,
- vendors.

### Separate appointments

Navsari fisheries college/researchers:

- scientific/data interviews.

This gives a much richer validation than speaking only to 20 random people.

---

# 88. Dholai fisherman population: how to quote it safely

The 2016 Gujarat Marine Fisheries Census recorded:

- **Dholai active fishermen:** 1,189
- **Fish marketing-related people:** 400
- **Other fisheries-linked activities:** included in the same table
- **Navsari district active fishermen:** 6,220

[R29]

This is a **2016 census baseline** and should not be described as the present-day population without a newer census.

The 2026 Dholai harbour study reported approximately 250 registered and actively operating fishing vessels during its 2025–2026 study period. [R27]

These two numbers measure different things and come from different time periods, so they should not be directly combined into a current fisherman population estimate.

---

# 89. What the research says about adoption

A major lesson from recent fisheries technology studies is:

> **Installation does not equal adoption.**

The 2026 FISH app study says nearly 1,000 fishermen installed the app during the pilot, but active use and regular submissions remained relatively low. The authors linked this to the extra effort of the task, the need for training, and the need to clearly explain the benefit of participation. [R07]

This means ORCA must not rely on:

> “We have many registered users.”

The better metric is:

> **“Did the fisherman return to ORCA because it helped him make a real decision?”**

---

# 90. ORCA success metrics

For the fisherman product, measure:

### Usefulness

Did the fisherman get the answer he needed?

### Time

How long did it take to find the answer?

### Help required

Did someone have to teach him?

### Trust

Did he understand why the answer was given?

### Action

Did the answer change or confirm a decision?

### Repeat use

Did he use the feature again?

### Offline success

Could he still use the main functions without mobile data?

---

# 91. What the first version should look like

The first working fisherman prototype should not try to contain the entire marine ecosystem.

A good V1 can be:

## Home

Trip Decision + conditions + best PFZ

## PFZ

Nearby PFZs + freshness + route

## Map

Current location + route + hazards + restrictions

## Ask

Voice questions

## Alerts

Official warning + contextual warning

## Offline

Trip pack

## Feedback

Very short post-trip result

That is enough to demonstrate the core idea.

---

# 92. What can wait

Do not spend most of the hackathon on:

- marketplace,
- finance,
- full insurance systems,
- full government-scheme portal,
- species recognition for every fish,
- large social-network features,
- complex researcher dashboards,
- advanced climate modeling.

Those are future modules.

The core problem is marine decision support for the fisher.

---

# 93. Recommended ORCA fisherman journey

```text
OPEN APP
    ↓
TODAY AT SEA
    ↓
TRIP STATUS
    ↓
CURRENT CONDITIONS
    ↓
BEST AVAILABLE PFZ
    ↓
VIEW WHY
    ↓
GO TO PFZ
    ↓
ROUTE / MAP
    ↓
MONITOR CONDITIONS
    ↓
ALERT IF IMPORTANT CHANGE
    ↓
RETURN TO HARBOUR
    ↓
TRIP FEEDBACK
```

Voice can enter at any point:

> **ASK ORCA**

---

# 94. Recommended ORCA decision flow

```text
FISHERMAN QUESTION
        ↓
UNDERSTAND INTENT
        ↓
CHECK LOCATION / TIME / BOAT CONTEXT
        ↓
GET REQUIRED MARINE DATA
        ↓
CHECK SOURCE + FRESHNESS
        ↓
CALCULATE / COMPARE
        ↓
CHECK WARNINGS + RESTRICTIONS
        ↓
CHECK WHETHER EVIDENCE IS SUFFICIENT
        ↓
MAKE A DECISION-SUPPORT RESPONSE
        ↓
SHOW WHY
        ↓
OFFER ACTION
```

This is the technical system, but the fisherman should see only the useful result.

---

# 95. The most important product rule

The first screen should never make the fisherman think:

> “What should I click?”

It should make him think:

> “Okay, I understand the situation.”

Then the next action should be obvious.

That is what “simple” really means in ORCA.

---

# 96. The key research-backed product principles

## Principle 1 — Local language first

Evidence from Andhra Pradesh and the multilingual FISH deployment supports this. [R05][R07]

## Principle 2 — Offline first

FISH and NavIC-related fisher systems demonstrate this need. [R07][R08]

## Principle 3 — Reduce typing

Voice and simple controls should be available.

## Principle 4 — One decision at a time

Do not make the fisherman interpret a dashboard.

## Principle 5 — Keep the scientific detail behind “WHY?”

## Principle 6 — Show data freshness

## Principle 7 — Prefer official warnings for safety

## Principle 8 — PFZ needs context, not just coordinates

## Principle 9 — Navigation should include return-to-harbour

## Principle 10 — Local knowledge should be captured, not ignored

## Principle 11 — Do not overpromise fish prediction or safety

## Principle 12 — Adoption depends on clear personal value

---

# 97. The strongest ORCA feature set in one place

If the whole fisherman product had to be summarized in one list, it would be:

### 1. TODAY AT SEA

One-screen trip summary.

### 2. GO / CAUTION / AVOID

Simple trip state with explanation.

### 3. PFZ SCOUT

Find, compare and explain PFZ options.

### 4. BEST OPTION FOR THIS TRIP

Use distance, conditions, restrictions and freshness.

### 5. GO TO PFZ

Directional route.

### 6. RETURN TO HARBOUR

One-tap return route.

### 7. SEA NOW

Simple wind, wave, current, rain and warning view.

### 8. WHAT WILL CHANGE?

Upcoming changes that can affect the trip.

### 9. OFFICIAL ALERTS

Critical and important warnings first.

### 10. ASK ORCA

Voice-first questions.

### 11. WHY?

Simple evidence explanation.

### 12. OFFLINE TRIP PACK

Latest available data when leaving harbour.

### 13. LAST UPDATED

Show freshness.

### 14. MY FISHING GROUNDS

Private saved locations.

### 15. BOAT PROFILE

Basic boat context.

### 16. TRIP FEEDBACK

Short post-trip learning.

---

# 98. What makes the platform different

The difference should be presented as:

> **ORCA does not ask the fisherman to become a marine-data expert. It does the information work in the background and presents one clear decision with the reasons behind it.**

The system can combine:

- PFZ,
- weather,
- waves,
- currents,
- tide,
- restrictions,
- route,
- historical context,
- local observations,
- and official warnings.

But the fisherman can simply ask:

> **“Where should I go?”**

and receive a practical answer.

---

# 99. What to validate at Dholai before finalizing the UI

Before locking the design, get real evidence for:

1. Which navigation device is actually used.
2. Which mobile apps are actually used.
3. Whether fishermen use PFZ directly.
4. How often mobile network disappears.
5. How phones are charged on boats.
6. Whether typing is difficult.
7. Whether sunlight affects readability.
8. Whether local language is preferred.
9. Whether voice is preferred.
10. How weather information is received.
11. How official warnings are received.
12. How fishermen decide to return.
13. How fishing grounds are remembered.
14. Whether fishermen trust government advisories.
15. Whether fishermen compare several sources.
16. Whether fuel and distance change PFZ decisions.
17. Which information is most valuable while already at sea.
18. Which information is useful after returning.

The product should be changed according to these observations.

---

# 100. Final product definition

## ORCA Fisher

**A simple marine trip companion for fishermen.**

It brings together the marine information already available from trusted sources and turns it into clear trip guidance.

### The fisherman sees

**WHERE** — best available fishing option  
**WHEN** — when conditions are better/worse  
**HOW** — route and direction  
**RISK** — what to avoid  
**WHY** — evidence behind the recommendation  
**RETURN** — how to get home

### The system handles

- data collection,
- marine data processing,
- PFZ information,
- weather and ocean forecasts,
- geospatial rules,
- route evaluation,
- freshness,
- source checks,
- and explanations.

### The central design sentence

> **Make the system complicated so the fisherman does not have to be.**

---

# 101. Final recommendations for the first UI prototype

## Home

One decision card.

One conditions card.

One PFZ recommendation.

One “next change” line.

## Map

Current position.

PFZ.

Route.

Hazards.

Restrictions.

Harbour.

## Ask

Large microphone.

Quick questions.

Short answer.

Voice output.

## Alerts

Critical first.

Important second.

Everything else below.

## Profile

Boat information, home harbour and language.

Nothing more.

---

# 102. What I would deliberately avoid in V1

- Giant dashboard
- 20 data cards
- 15 map layers visible at the same time
- Large scientific charts on the first screen
- Long government-service menus
- Large registration form
- Continuous internet requirement
- English-only text
- Mandatory typing
- Exact fish-catch promises
- Automatic claims of “safe” travel
- Unverified data sources presented as official
- Sharing private fishing grounds by default

---

# 103. Research-backed answer to the original product question

The strongest fisher-facing ORCA is not an “app for fishermen” in the generic sense.

It is a **trip decision system** that has a very simple phone interface.

The fisherman should not have to know how the answer was produced.

He should be able to ask:

> **“Can I go?”**

> **“Where should I go?”**

> **“What is happening at sea?”**

> **“Is something dangerous?”**

> **“How do I return?”**

Everything else belongs behind those actions.

---

# 104. References and sources

> **Note:** This is the final reference section. References marked as “recent” are especially relevant to the 2024–2026 research window. A few older sources are retained because they provide direct evidence about fisher phone usability or long-running services.

## Government, science institutions and official systems

**[R01] INCOIS — SAMUDRA Mobile Application**  
Smart Access to Marine Data Resources and Advisories. Current service description covering active alerts, PFZ, tides, marine heat waves, ocean-state forecasts and tsunami information.  
https://incois.gov.in/site/SAMUDRA/index.html

**[R02] INCOIS — Ocean State Forecast Service**  
Description of wind, waves, swell, currents, temperature and other ocean-state forecasts.  
https://www.incois.gov.in/site/services/osf.jsp

**[R03] Press Information Bureau — National Rollout Plan for Vessel Communication and Support System (VCSS), 10 Feb 2026**  
One lakh marine fishing vessels; satellite-based two-way communication, adverse-weather alerts, no-fishing-zone alerts, IMBL geofencing and Nabhmitra integration.  
https://www.pib.gov.in/PressReleasePage.aspx?PRID=2225774&lang=1&reg=6

**[R04] National Fisheries Digital Platform (NFDP)**  
Official Department of Fisheries platform covering fisher identities, schemes, credit, insurance, training, marketing, traceability and related services.  
https://nfdp.dof.gov.in/nfdp/

**[R08] ISRO — Mobile Apps for Fishermen**  
MapmyIndia/NavIC-related fisher application description including offline operation, PFZ waypoints, live location, IMBL warning and INCOIS emergency messages.  
https://www.isro.gov.in/MobileApps.html

**[R09] Department of Fisheries / Nabhmitra and VCSS material**  
Covered through the national VCSS information and related government documentation.  
https://www.pib.gov.in/PressReleasePage.aspx?PRID=2225774&lang=1&reg=6

**[R10] INCOIS — Potential Fishing Zone Advisory**  
PFZ purpose, benefits, dissemination and field use.  
https://incois.gov.in/MarineFisheries/PfzAdvisory

**[R11] INCOIS — PFZ dissemination and local-language information**  
PFZ maps/text, distance/direction guidance, local-language dissemination, dynamic movement and wind information.  
https://incois.gov.in/MarineFisheries/PfzAdvisory

**[R18] Fishery Survey of India — Mandate**  
Marine fisheries forecasting, remote sensing, resource assessment, fish stock identification and information dissemination.  
https://fsi.gov.in/mandate

**[R19] Fishery Survey of India — PFZ information**  
PFZ definition, satellite SST/chlorophyll inputs and dissemination through fishing landing centres.  
https://fsi.gov.in/node

**[R25] Google Play — SAMUDRA**  
Current public application description; includes interactive maps/charts, five-day ocean-state forecasts and current English-language availability.  
https://play.google.com/store/apps/details?id=com.incois.mobileapp

**[R26] Google Play — Fisher Friend Mobile Application**  
Current application listing and feature description.  
https://play.google.com/store/apps/details?hl=en_IN&id=com.mssrf.ffma

**[R15] Indian Journal of Geo-Marine Sciences — Occupational hazards among small-scale motorised fishers, 2025**  
Reports major hazards including heat stress, musculoskeletal problems, cyclones, heavy rain, insomnia and overexertion.  
https://or.niscpr.res.in/index.php/IJMS/article/view/21664

**[R16] Discover Public Health — Environmental, occupational, and socioeconomic determinants of health among Indian fisherfolk, 2026**  
Recent qualitative synthesis of health and livelihood pressures among Indian fisherfolk.  
https://link.springer.com/article/10.1186/s12982-026-01406-2

**[R17] Government of India — Livelihoods of Fishers and Climate Resilience, 5 Aug 2025**  
Government description of climate-resilience work and coastal fisherman villages.  
https://www.pib.gov.in/PressReleasePage.aspx?PRID=2152506&lang=2&reg=48

## Recent research on digital use, fisher apps and usability

**[R05] Periginji et al. — Constraints in Social Media Use for Agriculture and Fisheries in Andhra Pradesh, 2026**  
Study of 80 fish farmers and 80 agricultural farmers; usability was the strongest constraint dimension for fish farmers, and preferred local-language content was the largest individual constraint.  
https://epubs.icar.org.in/index.php/IJEE/article/view/179536

**[R07] Lal et al. — Development and deployment of a pilot multilingual citizen-science mobile application for georeferenced marine catch observations in India, Frontiers in Marine Science, 2026**  
Major source for ORCA's offline, multilingual, simple-interface and adoption lessons. Includes the FISH app, field deployment and user-response findings.  
https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2026.1918530/full

**[R06] Vimala & Ravisankar — Fisher Friend Mobile Application — Fishery Technology**  
Older field evidence on screen size, scrolling, font size, time limits, GPS, voice messages and device preferences. The page was published online in 2025 but the underlying issue is an older Fisher Friend study, so it should be treated as supporting background rather than new 2025–2026 field evidence.  
https://epubs.icar.org.in/index.php/FT/article/view/22383

**[R24] MSSRF Annual Report 2024–2025**  
Reports Fisher Friend user growth, screen views and the launch of FisherWomenConnect.  
https://mssrf.org/sites/default/files/2025-09/Final_Annual%20Report%202025_22_09_2025_compressed.pdf

## PFZ and fisheries science

**[R12] Environmental Impact Assessment Review — PFZ validation and assessment along the southwest coast of India, 2025**  
Positive relationship with village fish landings, environmental lag effects and value of landing data for PFZ validation and fisheries forecasting.  
https://www.sciencedirect.com/science/article/pii/S0195925525001507

**[R13] E-Prints CMFRI — Study on PFZ dynamics using environmental proxies, 2024**  
Use of chlorophyll, SST fronts, wind, currents, Ekman transport and eddies for understanding PFZ dynamics.  
https://eprints.cmfri.org.in/18258/

**[R14] INCOIS — Ocean State Forecast service**  
Forecasting service used to support sea-state decisions for activities along the Indian coast.  
https://www.incois.gov.in/site/services/osf.jsp

## Recent Dholai / Bilimora material

**[R27] Tandel et al. — Fin Fish Diversity of Dholai Fishing Harbour, Gujarat, India, 2026**  
Study period September 2025–April 2026; describes Dholai as a major operational harbour and reports approximately 250 registered and actively operating vessels.  
https://mbimph.com/index.php/UPJOZ/article/view/5746

**[R28] Tandel et al. — Study on the socio-economic condition of fishermen in Gandevi taluka, Gujarat, 2024**  
Study covering Bilimora, Dholai, Bhat and Mendar, including approximately 300 fishing families in the selected villages.  
https://www.extensionjournal.com/uploads/archives/7-12-18-533.pdf

**[R29] CMFRI & Department of Fisheries — Marine Fisheries Census 2016: Gujarat**  
Historical baseline. Dholai recorded 1,189 active fishermen in the census table.  
https://eprints.cmfri.org.in/17502/1/GUJARAT%20Marine%20Fisheries%20Census%20India%202016.pdf

**[R30] Bengani et al. — Specification of Fish Species available at Bilimora fish market, Gujarat, India, 2025**  
Describes the Bilimora wholesale market, 22 enrolled traders and observed daily fish marketing activity.  
https://www.researchgate.net/publication/388993437_Specification_of_Fish_Species_available_at_Bilimora_fish_marketGujarat_India

## Safety, climate and livelihood studies

**[R20] Mohapatra — Climate Change Induced Migration in Marine Fishing Community in Odisha, 2025**  
Reports declining catch, extreme weather, coastal erosion and rising sea temperatures as livelihood pressures.  
https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5205941

**[R21] Climate change impacts on coastal fishing communities: industrial pollution, environmental degradation, and livelihood transformation, 2026**  
Case study from Yerrayapalem, Visakhapatnam, Andhra Pradesh; small-sample qualitative study on pollution and livelihood change.  
https://www.tandfonline.com/doi/full/10.1080/29931495.2026.2644640

**[R22] Frontiers — Environmental/water-quality impacts on fisher communities around Chilika, 2025**  
Study reporting fisher perceptions of water-quality degradation and impacts on catch and income.  
https://www.frontiersin.org/journals/sustainable-food-systems/articles/10.3389/fsufs.2025.1525142/full

**[R18] / FSI and marine survey references**  
Fishery resource surveys and marine fisheries forecasting material.  
https://fsi.gov.in/mandate

**[R23] Gujarat coastal fisheries social wellbeing research**  
Research describing debt and trader-credit relationships in Gujarat fishing communities.  
https://pmc.ncbi.nlm.nih.gov/articles/PMC10066161/

**[R19] DG Shipping / marine safety material**  
Recent marine safety investigations and fishing-vessel safety issues.  
https://www.dgma.gov.in/nautical-wing/nw-circulars/nautical-marine-casuality-investigation

---

# 105. Source quality notes

### Strongest sources for ORCA product decisions

- INCOIS official service descriptions
- ISRO fisher-app documentation
- Department of Fisheries / PIB official material
- recent peer-reviewed fisheries technology research
- 2026 FISH app paper
- 2026 Andhra Pradesh digital-use constraints study
- recent Dholai studies
- recent safety and occupational-hazard research

### Use with caution

- single-village case studies,
- very small qualitative samples,
- older Fisher Friend studies,
- commercial or secondary directories,
- old census counts used as present-day numbers.

### Rule for ORCA

If an item is safety-critical or legally sensitive, use an authoritative source and show its freshness. Do not use a general article as a substitute for an official warning or legal boundary.

---

# 106. Final internal product checklist

Before calling the fisherman app ready, ask:

### Simplicity

- Can the fisherman understand the home screen quickly?
- Is there one obvious next action?
- Are technical details hidden until requested?

### Language

- Is Gujarati available?
- Can the fisherman speak naturally?
- Can the system read the answer aloud?

### Navigation

- Can the fisherman reach a PFZ?
- Can he see direction and distance?
- Can he return to harbour quickly?

### PFZ

- Is the PFZ source clear?
- Is freshness visible?
- Is distance visible?
- Is the PFZ explained rather than merely displayed?

### Safety

- Are official warnings clearly separated from normal forecasts?
- Are critical warnings obvious?
- Are restricted areas understandable?

### Offline

- Does the main trip screen work without the internet?
- Can the map still work?
- Can the last data timestamp be seen?

### Trust

- Can the fisherman see why a recommendation was made?
- Are source names visible?
- Are location-sharing choices clear?

### Adoption

- Is the app useful before the first fishing trip?
- Does it save time?
- Does it reduce information confusion?
- Is there a reason to open it again?

---

# 107. Final research conclusion

The strongest conclusion from the combined research is simple:

> **The main opportunity is not to create more marine information. It is to make existing information easier to use.**

Indian fishermen already receive information through many channels. India already has PFZ services, weather services, ocean-state forecasts, navigation applications, vessel communication systems, geofencing, local-language advisories and digital fisheries platforms. [R01][R03][R04][R08][R10][R26]

Recent studies repeatedly bring the attention back to:

- usability,
- local language,
- training,
- offline use,
- clear value,
- and the difficulty of adding more digital work to a demanding fishing trip. [R05][R07]

The product response should therefore be:

### One simple screen

showing:

**trip condition + sea conditions + best available PFZ + next change**

### One map

for:

**route + PFZ + hazards + restrictions + harbour**

### One voice interface

for:

**questions and answers**

### One alert system

for:

**official and important warnings**

### One return action

for:

**return to harbour**

And behind all of this:

> **A system that collects, checks and combines the right evidence before giving the fisherman a simple answer.**

That is the strongest fisherman-facing direction for ORCA.

---

# END OF RESEARCH REFERENCE
