from pathlib import Path
from anthropic import Anthropic

from generate_tex import get_keys, gen_paper_text
from gfx import gen_graphics


def gen_paper(user_prompt: str | None = None, tex_file: Path | None = None, gfx_files: list[Path] | None = None) -> Path:
    client = Anthropic(api_key=get_keys.get_anthropic_key())
    if tex_file is None:
        if user_prompt is None:
            raise ValueError("Either user-prompt or tex_file is required")
        tex_file = gen_paper_text.gen_paper_text(user_prompt, client)
    if gfx_files is None:
        gfx_files = gen_graphics.gen_graphics_from_tex(Path("tex")/"generated_paper_with_ref7.tex")
    tex_file_w_figs = gen_graphics.insert_graphics(tex_file, gfx_files)
    return Path(tex_file)

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

if __name__ == "__main__":
    gfx_path = Path("gfx")/"data"
    # gen_paper("LLM safety")
    gen_paper(tex_file=Path("tex")/"generated_paper_with_ref7.tex", gfx_files=[gfx_path/"IMG_1.png", gfx_path/"IMG_2.png"])