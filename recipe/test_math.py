import ctypes
import os
from pathlib import Path
import subprocess
import sys

prefix = Path(os.environ["PREFIX"])
if sys.platform == "win32":
    directory = prefix / "Library" / "bin"
    dll_directory = os.add_dll_directory(str(directory))
    library = directory / "cmark-gfm-extensions.dll"
else:
    suffix = "dylib" if sys.platform == "darwin" else "so"
    library = prefix / "lib" / f"libcmark-gfm-extensions.{suffix}"

extensions = ctypes.CDLL(str(library))
get_display = extensions.cmark_gfm_extensions_get_math_display
get_display.argtypes = [ctypes.c_void_p]
get_display.restype = ctypes.c_bool
assert not get_display(None)

rendered = subprocess.check_output(
    ["cmark-gfm", "--extension", "math"], input="$x$ and $$y$$\n", text=True
)
assert rendered == (
    '<p><span class="math inline">\\(x\\)</span> and '
    '<span class="math display">\\[y\\]</span></p>\n'
)

commonmark = subprocess.check_output(
    ["cmark-gfm", "--extension", "math", "--to", "commonmark"],
    input="cost $5 and $10, plus $x$\n", text=True,
)
assert r"\$5" in commonmark
assert "$x$" in commonmark
