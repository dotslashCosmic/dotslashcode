from pathlib import Path

from setuptools import find_packages
from setuptools import setup

DOCS_PATH = Path(__file__).parents[0] / "docs/README.md"
PATH = Path("README.md")
if not PATH.exists():
    with Path.open(DOCS_PATH, encoding="utf-8") as f1:
        with Path.open(PATH, "w+", encoding="utf-8") as f2:
            f2.write(f1.read())

setup(
    name="dotslashcode",
    version="2",
    license="MIT",
    author="dotslashCosmic",
    author_email="dotslashcosmic@protonmail.com",
    description="Bing-Chat-API",
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="https://github.com/dotslashCosmic/dotslashcode",
    project_urls={"Bug Report": "https://github.com/dotslashCosmic/dotslashcode/issues/new"},
    entry_points={
        "console_scripts": [
            # Update these with your actual console scripts
            "dotslashcode = BingChat.main:main",
        ],
    },
    install_requires=[
        "aiohttp",
        "BingImageCreator",
        "certifi",
        "httpx",
        "prompt_toolkit",
        "requests",
        "rich",
    ],
    long_description=Path.open(PATH, encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    py_modules=["BingChat"],  # Update this with your actual Python modules
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Programming Language :: Python :: 3.6",
    ],
)
