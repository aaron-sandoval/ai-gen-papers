from pathlib import Path

from gfx.gen_graphics import gen_graphics_from_tex


gfx_files = gen_graphics_from_tex(Path("tex")/"generated_paper_with_ref7.tex")

# extract_graphics_prompts(Path("tex")/"generated_paper_with_ref7.tex")

# gen_data_and_plot(
#     "GDP_growth",
#     data_prompt="""The first column of the data is the year. 
#     The data has 3 columns labeled 'China', 'USA', and 'Russia' tracking GDP in USD from 1980 until 2020. 
#     The values in each column are generally increasing in a jagged fashion, but 'China' is increasing most quickly. 
#     The values should be of a realistic magnitude for the countries labeled.""",
#     plot_prompt="Simple line chart.",
#     model="claude-3-5-sonnet-20240620",
#     quiet=True
# )

# gen_image(
#     "melting",
#     "View of a tall, pristine, white ice shelf with a huge chunk of ice falling and splashing into a deep blue ocean, photorealistic",
#     aspect_ratio="16:9",
#     output_format="png"
# )