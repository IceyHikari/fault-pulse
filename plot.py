# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib"]
# ///

"""Turn a cached USGS earthquake snapshot into a thirty-day seismic score."""

import json
from datetime import datetime, timezone
from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

FILE = "usgs-earthquakes-past-30-days.geojson"
PICTURE = "plot.png"
MIN_MAGNITUDE = 2.5

HERE = Path(__file__).parent
DATA = HERE / "data" / FILE
OUT = HERE / "out"


def load_events(path, minimum_magnitude):
    """Return the fields used by the picture for each qualifying event."""
    document = json.loads(path.read_text(encoding="utf-8"))
    events = []
    for feature in document["features"]:
        magnitude = feature["properties"]["mag"]
        coordinates = feature["geometry"]["coordinates"]
        if magnitude is None or magnitude < minimum_magnitude or len(coordinates) < 3:
            continue
        event_time = datetime.fromtimestamp(
            feature["properties"]["time"] / 1000, tz=timezone.utc
        )
        events.append(
            {
                "time": event_time,
                "magnitude": float(magnitude),
                "depth": float(coordinates[2]),
                "place": feature["properties"]["place"] or "Unnamed location",
            }
        )
    return events


def main():
    events = load_events(DATA, MIN_MAGNITUDE)
    times = [event["time"] for event in events]
    time_numbers = mdates.date2num(times)
    magnitudes = [event["magnitude"] for event in events]
    depths = [event["depth"] for event in events]
    print(f"{DATA.name}: {len(events)} events at M{MIN_MAGNITUDE}+ ")
    print(
        f"magnitude {min(magnitudes):.2f} to {max(magnitudes):.2f}; "
        f"depth {min(depths):.2f} to {max(depths):.2f} km"
    )

    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(16, 9), facecolor="#071018")
    ax.set_facecolor("#071018")

    stems = [[(time, 0), (time, depth)] for time, depth in zip(time_numbers, depths)]
    stem_colours = [
        plt.cm.cividis_r(max(0, min(depth, 600)) / 600) for depth in depths
    ]
    ax.add_collection(
        LineCollection(stems, colors=stem_colours, linewidths=0.45, alpha=0.18)
    )

    sizes = [5 + (magnitude - MIN_MAGNITUDE + 0.25) ** 3 * 7 for magnitude in magnitudes]
    points = ax.scatter(
        time_numbers,
        depths,
        s=sizes,
        c=depths,
        cmap="cividis_r",
        vmin=0,
        vmax=600,
        alpha=0.78,
        linewidths=0.2,
        edgecolors="#e7f0f4",
    )

    strongest = sorted(events, key=lambda event: event["magnitude"], reverse=True)[:6]
    summary = ["STRONGEST PULSES"]
    for event in strongest:
        place = event["place"]
        if len(place) > 34:
            place = place[:31] + "…"
        summary.append(
            f"M{event['magnitude']:.1f}  {event['time']:%d %b}  {place}"
        )

    ax.axhline(0, color="#e7f0f4", linewidth=1.0, alpha=0.9)
    ax.set_ylim(650, -22)
    ax.set_xlim(min(time_numbers), max(time_numbers))
    ax.xaxis_date()
    ax.xaxis.set_major_locator(mdates.AutoDateLocator(minticks=5, maxticks=9))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%d %b"))
    ax.set_xlabel("THIRTY DAYS OF RECORDED TIME · UTC", color="#9eafb9", labelpad=14)
    ax.set_ylabel("DEPTH BELOW THE REFERENCE SURFACE · KM", color="#9eafb9", labelpad=14)
    ax.set_title(
        "FAULT PULSE",
        loc="left",
        fontsize=30,
        fontweight="bold",
        color="#f4f0e6",
        pad=28,
    )
    ax.text(
        0,
        1.025,
        "2,069 EARTHQUAKES OF MAGNITUDE 2.5+ · 18 AUG—17 SEP 2026",
        transform=ax.transAxes,
        fontsize=11,
        color="#c3d0d7",
        va="bottom",
    )
    fig.text(
        0.765,
        0.84,
        "\n".join(summary),
        fontsize=9.5,
        color="#dce5e9",
        va="top",
        linespacing=1.55,
        bbox={"facecolor": "#071018", "edgecolor": "#42535d", "alpha": 1.0, "pad": 9},
    )

    ax.grid(axis="y", color="#6d7d86", linewidth=0.5, alpha=0.2)
    ax.grid(axis="x", visible=False)
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.spines["bottom"].set_color("#42535d")
    ax.tick_params(colors="#9eafb9")
    colour_axis = fig.add_axes([0.945, 0.18, 0.012, 0.42])
    colour_key = fig.colorbar(points, cax=colour_axis)
    colour_key.set_label("DEPTH · KM", color="#9eafb9", labelpad=12)
    colour_key.ax.tick_params(colors="#9eafb9")

    magnitude_handles = []
    for magnitude in (3.0, 5.0, 6.5):
        handle = ax.scatter(
            [], [],
            s=5 + (magnitude - MIN_MAGNITUDE + 0.25) ** 3 * 7,
            facecolors="none",
            edgecolors="#dce5e9",
            linewidths=0.8,
            label=f"M{magnitude:g}",
        )
        magnitude_handles.append(handle)
    legend = fig.legend(
        handles=magnitude_handles,
        title="MAGNITUDE",
        loc="lower left",
        bbox_to_anchor=(0.755, 0.17),
        frameon=False,
        labelcolor="#dce5e9",
    )
    plt.setp(legend.get_title(), color="#9eafb9")

    fig.text(
        0.012,
        0.015,
        "USGS monthly GeoJSON snapshot · position is omitted; each stem ends at reported depth",
        color="#71838d",
        fontsize=8.5,
    )
    fig.subplots_adjust(left=0.07, right=0.735, bottom=0.12, top=0.88)

    OUT.mkdir(exist_ok=True)
    fig.savefig(OUT / PICTURE, dpi=180)
    print(f"saved out/{PICTURE}")


if __name__ == "__main__":
    main()
