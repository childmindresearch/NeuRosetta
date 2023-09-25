import re
from .definitions import OPERATIONS_DICT, FRAMEWORKS
import pathlib as pl


def fsafe(s):
    return re.sub(r"[^a-zA-Z0-9]+", "_", s)

def read_file(fname):
    with open(fname, "r") as f:
        return f.read()
    
def write_file(fname, contents):
    with open(fname, "w") as f:
        f.write(contents)

def normalize_framework_headings(contents: str):
    frameworks_normalized = [
        "AFNI",
        "ANTs",
        "FSL",
        "FreeSurfer",
        "MRtrix",
        "Python",
        "SPM",
        "R",
        "Workbench Command",
    ]

    # Generate regexes for each framework
    rx_or = "|".join(frameworks_normalized)
    
    # Normalize framework headings
    re_frameworks = f"(?:[a-zA-Z ]{{2,20}})?({rx_or}):?(?: [a-zA-Z \\(\\)]{{2,30}})?:?"

    print(f'^(?:\\d+. )?(?:\\*\\*)?({re_frameworks})(?:\\*\\*)? *$')
    print()

    contents = re.sub(f"^#+ {re_frameworks}$", r"## \1", contents, 0, re.MULTILINE)
    contents = re.sub(f"^{re_frameworks}$", r"## \1", contents, 0, re.MULTILINE)
    contents = re.sub(f'^(?:\\*\\*)?(?:\\d+. )?(?:\\*\\*)?{re_frameworks}(?:\\*\\*)? *$', r"## \1", contents, 0, re.MULTILINE)

    for framework in frameworks_normalized:
        contents = contents.replace(f"## {framework}", f'## <img src="../icons/{fsafe(framework).lower()}.png" height="24px" /> {framework}')

    return contents

# Remove "Sure, ", "Of course. ", etc.
def replace_sure(contents: str):
    contents = contents.replace("Sure. ", "")
    contents = contents.replace("Sure, ", "")
    contents = contents.replace("Of course. ", "")
    contents = contents.replace("Of course, ", "")
    contents = contents.replace("I'm sorry, but ", "")
    contents = contents.replace("Sorry, but ", "")
    contents = contents.replace("Sorry, ", "")

    return contents

# Generate mdbook SUMMARY.md
def main():
    for category in OPERATIONS_DICT:
        for operation in OPERATIONS_DICT[category]:
            fname = f"{fsafe(category).lower()}/{fsafe(operation).lower()}.md"
            source_path = pl.Path(f"src-generated/{fname}")
            dest_path = pl.Path(f"src/{fname}")
            dest_path.parent.mkdir(parents=True, exist_ok=True)

            contents = read_file(source_path)

            # Normalize framework headings
            contents = normalize_framework_headings(contents)

            # Remove "Sure, ", "Of course. ", etc.
            contents = replace_sure(contents)

            # Add a heading
            contents = f"# {operation}\n\n{contents}"

            # Add a link to the source code
            #contents += f"\n\n[Source code](

            # Write the file
            write_file(dest_path, contents)

if __name__ == "__main__":
    main()



            