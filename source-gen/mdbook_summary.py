import re
from .definitions import OPERATIONS_DICT

def fsafe(s):
    return re.sub(r"[^a-zA-Z0-9]+", "_", s)

# Generate mdbook SUMMARY.md
def generate_mdbook_summary():
    buf = "# Summary\n\n[Introduction](README.md)\n\n# Operations\n\n"
    for category in OPERATIONS_DICT:
        buf += f"- [{category}](#)\n"
        for operation in OPERATIONS_DICT[category]:
            buf += f"  - [{operation}]({fsafe(category).lower()}/{fsafe(operation).lower()}.md)\n"
        buf += "\n"
    with open("src/SUMMARY.md", "w") as f:
        f.write(buf)

# Generate mdbook config
def generate_mdbook_config():
    buf = """[book]
title = "NeuRosetta"
authors = ["NeuRosetta Contributors"]
language = "en-US"
multilingual = false
"""
    with open("book.toml", "w") as f:
        f.write(buf)


if __name__ == "__main__":
    generate_mdbook_summary()
    generate_mdbook_config()