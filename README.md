# Kakhovka-dam-Mesa-simulation
I decided to study ABM using Mesa python library and make a case study on Kakhobka dam destruction by russian forces to bring avareness to damange caused to human lives and ecology of the region.

### Current progress:
Finished Mesa tutorial on 


## What is ABM?
Agent-based models are computer simulations involving multiple entities (the agents) acting and interacting with one another based on their programmed behavior

## What happened in Kakhovka?

The Kakhovka Dam was blown up by russian occupation forces in the early hours of 6 June 2023, causing extensive flooding along the lower Dnipro river. 

Between 2:18 and 2:20 a.m. local time loud sounds like explosions appeared. 

The day after the dam's destruction, Ukraine's prosecutor general estimated that about 40,000 people located in Ukrainian- and Russian-controlled land were likely to be impacted by flooding.

By the time alerts arrived in the morning, the closest villages have been already flooded.

Most people managed to evacuate with relatively low number of death casualties compared to size of catastrophe.



## Model approach

In Ukraine, Telegram is widely used for rapid news and alerts, often beating official channels. However, many affected in the Kakhovka incident were older, less proficient with phone technology, and missed early warnings.

The primary goal of this simplified model is to understand how informal social networks (neighbors) compensate for delayed or inaccessible formal warnings during a progressive emergency, and how this interacts with varying evacuation capacities (cars vs. rescue boats) and human hesitation (attachment to belongings).

### Assumptions

1. Water level
    - Every agent is assigned **House Elevation**
    - Environment has global water level rising each step
    - Rule: An agent is safe inside their home until `Water Level >= House Elevation`
        - If agent hasn't been alerted and water reaches it's considered death

1. Agent becomes alerted after they receive information via one of two channels:
    - Quicker Digital channel (phone, telegram etc.) ~60% of population
    - Physical and slower channels (tv, radio, **neighbours**): remaining ~40% of population

2. Model based on single village at distance reasonable to have enough evacuation window

3. Agents have mobility parameter and attachment which dictates how long it takes for them to leave home to evacuate
    - e.g. person that doesn't live home until they gather all their belongings

4. Evacuation bottlenecks:
    - quickest agents evacuate by cars
    - rest have to use limited capacity boats which is also affected by mobility





## Results

If official alerts are delayed or missing, does the "Telegram network" save the connected population while leaving the disconnected (e.g., the elderly) to die? Or does the slow, physical "neighbor network" eventually reach everyone in time?
- Result:

If everyone gets the info instantly via Telegram, do they all rush the bottleneck at the exact same time, causing a fatal jam? Conversely, does slower, neighbor-to-neighbor spreading actually save lives by staggering the arrival at the bottleneck?
- Result:

ow do mobility and information access intersect? Is an elderly person with low mobility doomed if they also lack a phone? Does high mobility compensate for late information?
- Result:

