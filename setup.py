from pathlib import Path 
from setuptools import find_namespace_packages, setup 

# Directories
BASE_DIR = Path(__file__).parent 
with open(Path(BASE_DIR, "requirements.txt"), "r") as file:
    required_packages = [ln.strip() for ln in file.readlines()]

setup(
    name="miniGPT2",
    version=0.1,
    description="Mini GPT-2 deployed to production.",
    author="Jason Wheeler",
    python_requires=">=3.8",
    install_requires = [required_packages],
)