# Fault Pulse

![A thirty-day seismic score plotting earthquake time, reported depth and magnitude](out/plot.png)

## The phenomenon

Earthquakes make the planet's internal movement briefly measurable at the
surface. I am interested in the contrast between the calm appearance of the
ground and the continuous sequence of ruptures recorded underneath it. This
project turns thirty days of observations into a seismic score, with each event
treated as both a measurement and a mark left by the moving Earth.

## The source

The raw data comes from the United States Geological Survey's
[all-earthquakes monthly GeoJSON endpoint](https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson),
documented on the [USGS earthquake feed page](https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php).
The repository stores one unchanged snapshot fetched on 17 September 2026. It
contains 11,087 events recorded from 18 August to 17 September 2026. Each
GeoJSON feature is one recorded event: `time` is Unix time in milliseconds;
longitude and latitude are decimal degrees; depth is kilometres relative to the
reference surface; and `mag` is the reported, unitless logarithmic magnitude
value, with its scale identified separately by `magType`.

## What the picture shows

The picture retains the 2,069 events of magnitude 2.5 or greater. Time runs from
left to right, every vertical stem ends at the event's reported depth, circle
size represents magnitude, and colour reinforces depth. The threshold reduces
the visual and regional bias produced by thousands of locally detected
microearthquakes, but does not remove differences in monitoring coverage. Six
qualifying events have small negative reported depths and therefore sit just
above the zero reference line rather than being silently changed.

The score shows a continuous field of mostly shallow events punctuated by a few
large or unusually deep shocks. It deliberately hides longitude and latitude so
that time and depth become the main structure. It also omits uncertainty, felt
reports and geological mechanism; consequently, it is not a map of earthquake
risk or a complete record of everything the Earth did.

## Run it

```
uv run plot.py
```
