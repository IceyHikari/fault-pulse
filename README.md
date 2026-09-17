# Fault Pulse

![what the picture is](out/plot.png)

## The phenomenon

Earthquakes make the planet's internal movement briefly measurable at the
surface. I am interested in the contrast between the calm appearance of a world
map and the continuous sequence of ruptures recorded underneath it. This project
will turn thirty days of global earthquake observations into a visual rhythm,
with each event treated as both a measured occurrence and a mark left by the
moving Earth.

## The source

The raw data comes from the
[United States Geological Survey earthquake feed](https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php).
The repository stores one unchanged GeoJSON snapshot generated on 17 September
2026. It contains 11,087 events recorded from 18 August to 17 September 2026.
Each feature represents one recorded event and includes its time, longitude,
latitude, depth in kilometres and magnitude.

## What the picture shows

The first plot is deliberately provisional: horizontal position shows event
time, vertical position shows magnitude, circle size repeats magnitude and colour
shows depth. It reveals the density of small recorded events and the relative
rarity of the strongest ones, while testing whether time, magnitude and depth can
form a legible visual pulse. It hides geographic position, measurement
uncertainty, felt reports and geological mechanism, so it must not be read as a
complete account of earthquake distribution or risk.

## Run it

```
uv run fetch.py
uv run plot.py
```
