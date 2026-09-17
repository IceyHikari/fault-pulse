# Process

## Tools

I used Codex to read the assignment specification, compare possible public data
sources and prepare the repository from the official course template. I retained
responsibility for the phenomenon, the visual argument and every decision about
what the transformation should reveal or omit.

## Kept

I kept the suggestion to use the official USGS thirty-day GeoJSON feed. It is a
public, machine-readable source that requires no account or API key, and its
event-level fields support both an informative and an artistic interpretation.

## Rejected

I rejected a conventional weather line chart. It would satisfy the file and code
requirements, but it would not yet connect the assignment to my interest in
expressive systems and art direction. I also rejected fetching live data every
time the plot runs because that would make the result irreproducible and would
break the assignment's offline requirement.

## 17 September 2026 — choosing the material

I created the repository from the official template and replaced the example
temperature source with the USGS earthquake feed. At this stage the visual form
is intentionally unresolved. The next test is a rough plot that checks the real
range and density of the data before I decide how much geographic structure the
finished image needs.

The frozen snapshot contained 11,087 events, with magnitudes from -1.25 to 6.7
and reported depths from -3.48 to 628.976 kilometres. I kept negative values
rather than silently discarding them: negative magnitude is valid on the
logarithmic magnitude scale, while negative depth can describe an event located
above the reference surface used by the feed. The first plot is a diagnostic
scatter plot, not the final artwork. It establishes what the data actually looks
like before visual styling begins.

## Developing the seismic score

The first scatter plot repeated depth only as colour and placed magnitude on a
conventional vertical axis. I rejected it as the final image because it described
the dataset without making a strong visual decision, and because 11,087 marks
gave disproportionate visual weight to microearthquakes detected by dense local
networks.

I kept the complete raw file but filtered the picture to 2,069 events of
magnitude 2.5 or greater. The revision maps time horizontally, depth vertically
and magnitude to circle area. A faint stem joins the reference surface to each
hypocentre, making reported depth readable without relying on colour alone. I
also kept a list of the six strongest events so that the largest marks retain a
place and date even though the main image deliberately removes geography.

The first attempt at the stem layer failed because Matplotlib's `LineCollection`
does not accept `datetime` objects even though `scatter` does. I corrected the
representation by converting every timestamp once with `matplotlib.dates.date2num`
and then using the same numeric coordinates for both layers. I kept this explicit
conversion rather than hiding it inside plotting calls because it makes the
coordinate transformation inspectable.
