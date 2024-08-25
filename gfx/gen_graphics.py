from anthropic import Anthropic
from typing import Literal
import warnings
import itertools
import os
import sys
import io
from pathlib import Path
from PIL import Image
import requests
import re
from importlib import reload, import_module

# import plot_funcs

def getenv_or_except(key: str) -> str:
    val = os.getenv(key)
    if val is None:
        raise KeyError(f"'{key}' not found in OS environment variables.")
    return val


def compile_msg_history(prompts: list[str], responses: list[str]) -> list[dict[str, str]]:
    """ Transforms lists of messages into a message history usable by the Anthropic API as the `messages` parameter. """
    return [{"role": "user" if i==0 else "assistant", "content": val if val else ""} for pair in itertools.zip_longest(prompts, responses) for i, val in enumerate(pair)]


def gen_data_and_plot(
        dataset_name: str, 
        data_prompt: str, 
        plot_prompt: str, 
        client: Anthropic | None = None, 
        model: Literal["claude-3-haiku-20240307", "claude-3-5-sonnet-20240620"] = "claude-3-haiku-20240307",
        # plot_file: str | Path | None = None,
        quiet: bool = True
        ) -> Path:
    """
    Generates a csv data file, plotting function, and png plot of the data according to NL prompts.

    # Parameters:
    - `dataset_name`: Identifier for this output. Data and plot image will be saved to `{dataset_name}.csv` and `{dataset_name}.png`.
    - `data_prompt`: LLM prompt for generating the data file. See implementation for what's already included in the system prompt.
    - `plot_prompt`: LLM prompt for generating the plotting code. See implementation for what's already included in the system prompt.
    - `quiet`: If False, model outputs will print to stdout as they are generated in addition to being saved to files.
    """
    def gen_data(prompt: str, context: list[dict: str, str] | None = None) -> Path:
        prompts.append(
        f"Generate data in CSV format. "
        f"Output only the data without any other text. "
        f"Include a header row with the column titles. "
        f"{prompt}"
        )
        gen_data = client.messages.create(
            model=model,
            max_tokens=1000,
            temperature=0.0,
            messages=context if context is not None else compile_msg_history(prompts, responses)
        )
        if not quiet:
            print(f"***Generated data***\n\n{gen_data.content[0].text}\n")
        responses.append(gen_data.content[0].text)
        data_file = Path("gfx")/"data"/(dataset_name+".csv")
        with open(data_file, "w") as f:
            f.write(responses[-1])
        return data_file

    def gen_plotting_code(prompt: str, context: list[dict: str, str] | None = None, use_system_prompt: bool = True):
        SYSTEM_PROMPT = "Include the line `from gfx.plot_funcs.import_common import *` at the top of the file outside the function. The first line in the function should load the data from the `filename` argument. Use the matplotlib library to construct the plot. Do not use seaborn. The figure should be 6 inches wide with font size no smaller than 8. The plot should appear appropriate for an academic paper. Include a title, legend, axis labels, and tick labels. Save the plot as a png with the same name as the `filename` argument. Output only commented Python code without any ``` backticks surrounding it."
        plot_func = "plot_"+dataset_name
        prompts.append(
            f"Write a python function called `{plot_func}` to plot the data you just generated per the following description. "
            f"{prompt} "
            f"{SYSTEM_PROMPT if use_system_prompt else ''}")
        gen_data = client.messages.create(
            model=model,
            max_tokens=1000,
            temperature=0.0,
            messages=context if context is not None else compile_msg_history(prompts, responses)
        )
        if gen_data.content[0].text[:9] == "```python":
            warnings.warn("Plotting code included '```python`' block. Tried manually deleting it, but plot code may not work.")
            responses.append(gen_data.content[0].text[9:-3])
        else:
            responses.append(gen_data.content[0].text)
        if not quiet:
            print(f"***Plotting code***\n\n{gen_data.content[0].text}\n")
        with open(plot_file, "w") as f:
            f.write(responses[-1])

    def gen_plot(plot_func: callable, data_file: Path | str, *plot_args, **plot_kwargs) -> Path:
        plot_func(data_file, *plot_args, **plot_kwargs)
        return Path(str(data_file).split(".")[0]+".png")

    if client is None:
        client = Anthropic(
            api_key=getenv_or_except("ANTHROPIC_API_KEY")
        )
    plot_file = Path("gfx")/"plot_funcs"/("plot_"+dataset_name+".py")
    prompts, responses = [], []
    # data_file = Path("gfx")/"data"/(dataset_name+".csv")
    data_file = gen_data(data_prompt)
    gen_plotting_code(plot_prompt)
    import_module(f"gfx.plot_funcs.plot_{dataset_name}")
    reload(sys.modules[f"gfx.plot_funcs.plot_{dataset_name}"])
    return gen_plot(getattr(sys.modules[f"gfx.plot_funcs.plot_{dataset_name}"], f"plot_{dataset_name}"), str(data_file))


def gen_image(
        name: str,
        prompt: str,
        negative_prompt: str = "",
        aspect_ratio: Literal["21:9", "16:9", "3:2", "5:4", "1:1", "4:5", "2:3", "9:16", "9:21"] = "1:1",
        seed: int = 0,
        output_format: Literal["webp", "jpeg", "png"] = "png"
        ):
    """
    Generate and save an image using the Stable Diffusion API.

    # Parameters:
    - `name`: File name of the output image without file extension. All images are saved in gfx/data.
    """
    def send_generation_request(host, params):    
        headers = {
            "Accept": "image/*",
            "Authorization": f"Bearer {getenv_or_except('STABILITY_API_KEY')}"
        }

        # Encode parameters
        files = {}
        image = params.pop("image", None)
        mask = params.pop("mask", None)
        if image is not None and image != '':
            files["image"] = open(image, 'rb')
        if mask is not None and mask != '':
            files["mask"] = open(mask, 'rb')
        if len(files)==0:
            files["none"] = ''

        # Send request
        print(f"Sending REST request to {host}...")
        response = requests.post(
            host,
            headers=headers,
            files=files,
            data=params
        )
        if not response.ok:
            raise Exception(f"HTTP {response.status_code}: {response.text}")

        return response

    host = f"https://api.stability.ai/v2beta/stable-image/generate/core"

    params = {
        "prompt" : prompt,
        "negative_prompt" : negative_prompt,
        "aspect_ratio" : aspect_ratio,
        "seed" : seed,
        "output_format": output_format
    }
    
    generated = Path("gfx")/"data"/f"{name}.{output_format}"
    response = send_generation_request(
        host,
        params
    )

    # Decode response
    output_image = response.content
    finish_reason = response.headers.get("finish-reason")
    seed = response.headers.get("seed")

    # Check for NSFW classification
    if finish_reason == 'CONTENT_FILTERED':
        raise Warning("Generation failed NSFW classifier")

    # Display result
    PILimage: Image = Image.open(io.BytesIO(output_image))

    # Save result
    PILimage.save(generated, "PNG")
    print(f"Saved image {generated}")


def extract_graphics_prompts(tex_file: str | Path) -> tuple[list[tuple[int, str, str]], list[tuple[int, str]]]:
    with open(tex_file, "r") as f:
        tex = f.read()
    plot_pattern = r'\[IMAGE PLACEHOLDER ([0-9]+) \(chart\)([^\]]*)\]'
    plot_matches = re.findall(plot_pattern, tex)
    chart_prompts = []
    if len(plot_matches) > 0:
        for serial, m in plot_matches:
            re_matches = re.search(r'data_prompt: (.*)\nplot_prompt: (.*)', m)
            data_prompt, plot_prompt = re_matches.group(1), re_matches.group(2)
            chart_prompts.append((serial, data_prompt, plot_prompt))
    image_pattern = r'\[IMAGE PLACEHOLDER ([0-9]+) \(picture\)([^\]]*)\]'
    image_matches = re.findall(image_pattern, tex)
    image_prompts = [(serial, raw.strip().replace("\n", " ")) for serial, raw in image_matches]
    return chart_prompts, image_prompts

def gen_graphics_from_tex(
    tex_file: str | Path, 
    plot_llm: Literal["claude-3-haiku-20240307", "claude-3-5-sonnet-20240620"] = "claude-3-5-sonnet-20240620"
) -> list[Path]:
    """ Generates and saves plots and images"""
    plot_prompts, image_prompts = extract_graphics_prompts(tex_file)
    gfx_files = {}
    if len(plot_prompts) > 0:
        client = Anthropic(
            api_key=getenv_or_except("ANTHROPIC_API_KEY")
        )
        for serial, data_prompt, plot_prompt in plot_prompts:
            name = f"IMG_{serial}"
            gfx_files[serial] = gen_data_and_plot(name, data_prompt, plot_prompt, client=client)
    for serial, image_prompt in image_prompts:
        name = f"IMG_{serial}"
        gfx_files[serial] = gen_image(name, image_prompt)
    return gfx_files


if __name__ == "__main__":
    gen_data_and_plot(
        "Heights",
        data_prompt="""The data shows the heights in inches of 30 children aged 12 years old. 
        The data has 2 columns labeled 'Height' and 'Gender'.  
        The values should show realistic heights for American children.""",
        plot_prompt="""Histogram with stacked bars. One set of bars is pink for female, and the other set is baby blue for male. 
        The legend labels the colors. """,
        model="claude-3-5-sonnet-20240620",
        # model="claude-3-haiku-20240307",
    )
