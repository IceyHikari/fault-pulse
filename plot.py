# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib"]
# ///

"""Read the cached USGS GeoJSON and make the first diagnostic picture."""

import json
from datetime import datetime, timezone
from pathlib import Path

import matplotlib.pyplot as plt

FILE = "usgs-earthquakes-past-30-days.geojson"
PICTURE = "plot.png"

HERE = Path(__file__).parent
DATA = HERE / "data" / FILE
OUT = HERE / "out"


def load_events(path):
    """Return time, magnitude and depth for each usable earthquake event."""
    document = json.loads(path.read_text(encoding="utf-8"))
    events = []
    for feature in document["features"]:
        magnitude = feature["properties"]["mag"]
        coordinates = feature["geometry"]["coordinates"]
        if magnitude is None or len(coordinates) < 3:
            continue
        event_time = datetime.fromtimestamp(
            feature["properties"]["time"] / 1000, tz=timezone.utc
        )
        events.append((event_time, float(magnitude), float(coordinates[2])))
    return events


def main():
    events = load_events(DATA)
    times, magnitudes, depths = zip(*events)
    print(f"{DATA.name}: {len(events)} usable events")
    print(
        f"magnitude {min(magnitudes):.2f} to {max(magnitudes):.2f}; "
        f"depth {min(depths):.2f} to {max(depths):.2f} km"
    )

    sizes = [max(3, 2 ** (magnitude + 1)) for magnitude in magnitudes]
    fig, ax = plt.subplots(figsize=(12, 5))
    points = ax.scatter(
        times,
        magnitudes,
        s=sizes,
        c=depths,
        cmap="cividis_r",
        alpha=0.55,
        linewidths=0,
    )
    ax.set_title("Thirty days of recorded earthquakes — first data test")
    ax.set_xlabel("event time (UTC)")
    ax.set_ylabel("magnitude")
    colour_key = fig.colorbar(points, ax=ax, pad=0.02)
    colour_key.set_label("depth (km)")
    fig.autofmt_xdate()
    fig.tight_layout()

    OUT.mkdir(exist_ok=True)
    fig.savefig(OUT / PICTURE, dpi=180)
    print(f"saved out/{PICTURE}")


if __name__ == "__main__":
    main()
