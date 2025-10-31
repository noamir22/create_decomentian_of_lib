# extract_docs.py
"""
Extract all __doc__ strings from a Python package and save them to a Markdown file.
Usage:
    python extract_docs.py agent docs2.md
"""

import importlib
import inspect
import pkgutil
import sys
from pathlib import Path

def extract_docs(package_name, output_file):
    pkg = importlib.import_module(package_name)
    docs = []

    docs.append(f"files:\n```\n{package_name}")
    pkg_path = Path(pkg.__file__).parent
    for path in pkg_path.rglob("*.py"):
        rel = path.relative_to(pkg_path.parent)
        docs.append(f"├── {rel}")
    docs.append("```\n\n")

    docs.append("commands:\n")

    for importer, modname, ispkg in pkgutil.walk_packages(pkg.__path__, pkg.__name__ + "."):
        mod = importlib.import_module(modname)
        for name, obj in inspect.getmembers(mod):
            if inspect.isfunction(obj) and obj.__doc__:
                docs.append(f"* `{modname}.{name}?`\n")
                doc = inspect.cleandoc(obj.__doc__)
                indented = "\n".join("    " + line for line in doc.splitlines())
                docs.append(f"```\n{indented}\n```\n\n")

    Path(output_file).write_text("\n".join(docs), encoding="utf-8")
    print(f"✅ Docs extracted to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python extract_docs.py <package_name> <output_file>")
        sys.exit(1)
    extract_docs(sys.argv[1], sys.argv[2])
