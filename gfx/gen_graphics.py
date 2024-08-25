from anthropic import Anthropic
from typing import Literal
import warnings
import itertools
import os
import sys
from pathlib import Path
from importlib import reload, import_module

# import plot_funcs


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
        quiet: bool = False
        ) -> None:
    """
    Generates a csv data file, plotting function, and png plot of the data according to NL prompts.
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
        SYSTEM_PROMPT = "Use the matplotlib library with the seaborn-v0_8 style. The figure should be 5 inches wide with font size no smaller than 8. You first need to load the data from the `filename` argument. The graph should appear appropriate for an academic paper. Include a title, legend, axis labels, and tick labels. Save the plot as a png with the same name as the filename argument. Output only commented Python code without any ``` backticks surrounding it."
        plot_func = "plot_"+dataset_name
        prompts.append(
            f"Write a python function called `{plot_func}` to plot the data you just generated per the following description. "
            f"{prompt} "
            f"{SYSTEM_PROMPT if use_system_prompt else ''}")
        gen_data = client.messages.create(
            model=model,
            max_tokens=1000,
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

    def gen_plot(plot_func: callable, data_file: Path | str, *plot_args, **plot_kwargs):
        plot_func(data_file, *plot_args, **plot_kwargs)

    if client is None:
        client = Anthropic(
            api_key=os.getenv("ANTHROPIC_API_KEY")
        )
    plot_file = Path("gfx")/"plot_funcs"/("plot_"+dataset_name+".py")
    prompts, responses = [], []
    # data_file = Path("gfx")/"data"/(dataset_name+".csv")
    data_file = gen_data(data_prompt)
    gen_plotting_code(plot_prompt)
    import_module(f"plot_funcs.plot_{dataset_name}")
    reload(sys.modules[f"plot_funcs.plot_{dataset_name}"])
    gen_plot(getattr(sys.modules[f"plot_funcs.plot_{dataset_name}"], f"plot_{dataset_name}"), str(data_file))

if __name__ == "__main__":
    gen_data_and_plot(
        "Heights",
        """The data shows the heights in inches of 30 children aged 12 years old. 
        The data has 2 columns labeled 'Height' and 'Gender'.  
        The values should show realistic heights for American children.""",
        """Histogram with stacked bars. One set of bars is pink for female, and the other set is baby blue for male. 
        The legend labels the colors. """,
        model="claude-3-5-sonnet-20240620",
        # model="claude-3-haiku-20240307",
    )