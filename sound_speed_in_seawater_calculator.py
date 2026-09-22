import matplotlib.pyplot as plt
import numpy as np

def calculate_sound_speed(temperature: float, salinity: float, depth: float) -> float:
    """
    Compute sound speed in seawater using the UNESCO (Chen-Millero) empirical equation.

    Parameters
    ----------
    temperature : float
        Water temperature in degrees Celsius (0 to 40).
    salinity : float
        Salinity in practical salinity units (0 to 42).
    depth : float
        Depth in meters (0 to 11000).

    Returns
    -------
    float
        Sound speed in meters per second.
    """
    T = temperature
    S = salinity
    z = depth
    c = (1449.2
         + 4.6 * T
         - 0.055 * T ** 2
         + 0.00029 * T ** 3
         + (1.34 - 0.01 * T) * (S - 35)
         + 0.016 * z)
    return c

def create_comparison_chart(seawater_speed: float) -> plt.Figure:
    """
    Generate a bar chart comparing the calculated sound speed with typical
    speeds in air (343 m/s) and fresh water (1480 m/s).

    Parameters
    ----------
    seawater_speed : float
        Sound speed in seawater (m/s) to include in the chart.

    Returns
    -------
    matplotlib.figure.Figure
        The figure object containing the bar chart.
    """
    categories = ["Air\n(343 m/s)", "Fresh Water\n(1480 m/s)", f"Seawater\n({seawater_speed:.1f} m/s)"]
    values = [343.0, 1480.0, seawater_speed]
    colors = ["#aed6f1", "#85c1e9", "#1a5276"]

    fig, ax = plt.subplots(figsize=(5, 3))
    bars = ax.bar(categories, values, color=colors, edgecolor="white", linewidth=1.2)
    ax.set_ylabel("Sound Speed (m/s)", fontsize=10)
    ax.set_ylim(0, max(values) * 1.15)
    ax.grid(axis="y", alpha=0.3)

    # Add value labels on bars
    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 10,
                f"{val:.0f}", ha="center", va="bottom", fontsize=9, fontweight="bold")

    ax.set_title("Sound Speed Comparison", fontsize=12, fontweight="bold")
    fig.tight_layout()
    return fig
