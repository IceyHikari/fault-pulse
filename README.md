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
The repository stores one unchanged GeoJSON snapshot from the USGS feed for all
earthquakes recorded during the preceding thirty days. Each feature represents
one recorded event and includes its time, longitude, latitude, depth in
kilometres and magnitude.

## What the picture shows

The first plot is deliberately provisional. It will test whether time, magnitude
and depth can form a legible visual pulse before the final artistic treatment is
chosen. The image will not reproduce every field in the USGS record: uncertainty,
felt reports and geological mechanism are outside its scope, so it must not be
read as a complete account of earthquake risk.

## Run it

```
uv run fetch.py
uv run plot.py
```
