import gradio as gr
from sound_speed_in_seawater_calculator import calculate_sound_speed, create_comparison_chart

def compute_and_plot(temp, sal, depth):
    speed = calculate_sound_speed(temp, sal, depth)
    fig = create_comparison_chart(speed)
    return f"{speed:.2f} m/s", fig

with gr.Blocks(
    title="Sound Speed in Seawater Calculator",
    theme=gr.themes.Soft(primary_hue="blue"),
    css="""
    .gr-button { background-color: #1a5276 !important; color: white !important; }
    .output-number { font-size: 2rem; font-weight: bold; color: #0b3d5f; }
    """
) as demo:
    gr.Markdown("## 🌊 Sound Speed in Seawater Calculator")
    gr.Markdown("Based on the UNESCO (Chen-Millero) equation. Valid ranges: Temperature 0–40 °C, Salinity 0–42 PSU, Depth 0–11000 m.")

    with gr.Row():
        with gr.Column():
            temp = gr.Slider(0, 40, value=20, step=0.1, label="Temperature (°C)")
            sal = gr.Slider(0, 42, value=35, step=0.1, label="Salinity (PSU)")
            depth = gr.Slider(0, 11000, value=0, step=1, label="Depth (m)")
            calc_btn = gr.Button("Calculate", variant="primary")
        with gr.Column():
            output_text = gr.Textbox(label="Sound Speed", elem_classes="output-number", lines=1)
            output_plot = gr.Plot(label="Comparison with Typical Speeds")

    calc_btn.click(fn=compute_and_plot, inputs=[temp, sal, depth], outputs=[output_text, output_plot])

demo.launch(server_name="0.0.0.0", server_port=7860)
