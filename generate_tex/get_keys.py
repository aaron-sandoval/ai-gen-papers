import os
import streamlit


# import plot_funcs

def getenv_or_except(key: str) -> str:
    val = os.getenv(key)
    if val is None:
        raise KeyError(f"'{key}' not found in OS environment variables.")
    return val

def get_anthropic_key():
    try:
        return getenv_or_except("ANTHROPIC_API_KEY")
    except KeyError:
        # a = streamlit.secrets
        ...