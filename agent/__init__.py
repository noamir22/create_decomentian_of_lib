# agent/__init__.py
from types import SimpleNamespace
from . import info

# Create an easy-to-browse namespace object
agent = SimpleNamespace(
    info=info
)

# Expose submodules as attributes
__all__ = ["info"]


def load_ipython_extension(ipython):
    ipython.push({'agent': agent})
    print("✅ Agent module loaded into IPython.")

def unload_ipython_extension(ipython):
    print("👋 Agent module unloaded.")