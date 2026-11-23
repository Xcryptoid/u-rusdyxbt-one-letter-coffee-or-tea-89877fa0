"""One Letter: Coffee or Tea — copy the pre-written entry.txt to the output dir.

Stdlib-only entrypoint: no third-party imports, no network, no writes
into this directory. The grader runs `python3 -P -s main.py` with only
MAKEFUN_OUTPUT_DIR writable.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")

os.makedirs(OUT, exist_ok=True)
shutil.copyfile(os.path.join(HERE, "entry.txt"), os.path.join(OUT, "entry.txt"))
print("wrote " + os.path.join(OUT, "entry.txt"))
