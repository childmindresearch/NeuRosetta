import openai
import os
import pathlib as pl
import re
from .definitions import OPERATIONS_DICT, FRAMEWORKS

openai.api_key = os.environ["OAI_API_KEY"]
openai.organization = os.environ["OAI_ORG"]

def string_enumerate_english(items):
    if len(items) == 0:
        return ""
    elif len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return " and ".join(items)
    else:
        return ", ".join(items[:-1]) + ", and " + items[-1]

def get_prompt(operation):
    output = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
                {"role": "system", "content": "You are a helpful assistant in brain imaging."},
                {"role": "user", "content": f"Show a short minimal example script that does {operation} "
                 f"in each of {string_enumerate_english([enquote(i) for i in FRAMEWORKS])} with a heading for "
                 f"each of them. Do not include instructions about installing software or downloading data."},
            ]
    )
    return output

def fsafe(s):
    return re.sub(r"[^a-zA-Z0-9]+", "_", s)

def enquote(s):
    return f'"{s}"'

# save output to file
OUT_DIR = pl.Path("src")

def ops():
    for category in OPERATIONS_DICT.keys():
        for op in OPERATIONS_DICT[category]:
            yield category, op

operations = list(ops())

for operation_idx, (category, operation) in enumerate(operations):
    out_file = OUT_DIR / fsafe(category).lower() / f"{fsafe(operation).lower()}.md"
    out_file.parent.mkdir(exist_ok=True, parents=True)
    
    if not out_file.exists():
        print(f"Generating {operation}... ({operation_idx+1}/{len(operations)})")
        output = get_prompt(operation)
        with open(out_file, "w") as f:
            f.write(output.choices[0].message.content)
    else:
        print(f"Skipping {operation}...")
