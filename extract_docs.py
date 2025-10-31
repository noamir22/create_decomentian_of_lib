# extract_docs.py
"""
Extract all __doc__ strings from a Python package and export them as
Markdown dropdowns using <details> and <summary> HTML tags.

Usage:
    python extract_docs.py agent docs.md
"""

import importlib
import inspect
import pkgutil
import sys
from pathlib import Path


def extract_docs(package_name: str, output_file: str):
    """Extracts __doc__ strings recursively from a Python package."""
    pkg = importlib.import_module(package_name)
    docs = []

    # File tree section
    docs.append(f"files:\n```\n{package_name}\n")
    pkg_path = Path(pkg.__file__).parent
    for path in pkg_path.rglob("*.py"):
        rel = path.relative_to(pkg_path.parent)
        docs.append(f"├── {rel}\n")
    docs.append("```\n\n")

    # Commands section header
    docs.append("commands:\n\n")

    # Walk through all submodules
    for importer, modname, ispkg in pkgutil.walk_packages(pkg.__path__, pkg.__name__ + "."):
        try:
            mod = importlib.import_module(modname)
        except ImportError:
            print(f"⚠️ Skipping {modname} (cannot import on this platform)")
            continue

        for name, obj in inspect.getmembers(mod):
            if inspect.isfunction(obj) and obj.__doc__:
                doc = inspect.cleandoc(obj.__doc__)
                docs.append(f"<details>\n")
                docs.append(f"<summary><code>{modname}.{name}?</code></summary>\n\n")
                docs.append("```\n")
                docs.append(doc + "\n")
                docs.append("```\n")
                docs.append("</details>\n\n")

    # Write to file
    Path(output_file).write_text("".join(docs), encoding="utf-8")
    print(f"✅ Documentation written to {output_file}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python extract_docs.py <package_name> <output_file>")
        sys.exit(1)
    extract_docs(sys.argv[1], sys.argv[2])
