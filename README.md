![NORA logo](https://i.ibb.co/0VJCC9Gf/IMG-20260114-WA0008.jpg)
 
# Sound Speed in Seawater Calculator
 
*For oceanographers and marine geoscientists: enter temperature, salinity, and depth to instantly compute the sound speed in seawater using the UNESCO equation.*
 
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
 

## Overview
 
**Industry:** Oceanography / Marine Geoscience
 
Inputs: (1) Temperature in degrees Celsius (0 to 40, step 0.1); (2) Salinity in practical salinity units (0 to 42, step 0.1); (3) Depth in meters (0 to 11000, step 1). The core calculation implements the UNESCO (Chen-Millero) equation for sound speed: c = 1449.2 + 4.6T − 0.055T^2 + 0.00029T^3 + (1.34 − 0.01T)(S − 35) + 0.016z, where T is temperature, S is salinity, z is depth. This formula is valid for the given ranges. The Gradio UI will have three number sliders with labels and units. A 'Calculate' button triggers the computation. Output: a single large number display showing sound speed in m/s with two decimal places. Additionally, a small bar chart is shown comparing the calculated speed to typical sound speeds in air (343 m/s) and fresh water (1480 m/s) for context. The interface is clean, with a blue marine-themed color scheme. No AI/ML component is used; the tool relies entirely on the standard empirical equation.
 
## Run it
 
```bash
docker build -t sound-speed-in-seawater-calculator .
docker run -p 7860:7860 sound-speed-in-seawater-calculator
```
 
Then open http://localhost:7860 in your browser.
 
## About
 
This tool was generated and published automatically by the **NORA Earth Intelligence**
tool factory, an autonomous pipeline maintained by **NORA Research Lab** that turns
one idea per run into a small, working geoscience tool — end to end, with an
LLM writing and Docker-testing the code, and another model generating the
banner above.
 
- Platform: [https://noraearth.xyz](https://noraearth.xyz)
- Parent lab: [https://noraresearchlab.site](https://noraresearchlab.site)
 
Built 2026-09-22.
 
---
 
### Maintainer
 
**NORA Research Lab**
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
