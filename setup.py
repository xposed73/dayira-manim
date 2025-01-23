from setuptools import setup, find_packages

setup(
    name="dayira",  # Name of your library
    version="1.0.0",  # Initial version
    description="Utilities for custom Manim configurations and effects.",
    long_description=open("README.md").read(),  # Include a detailed description
    long_description_content_type="text/markdown",  # Specify Markdown format
    author="Nadeem Khan",  # Your name
    author_email="nadeemak755@.com",  # Your email
    url="https://github.com/xposed73/dayira-manim",  # GitHub or project URL
    license="MIT",  # License type
    packages=find_packages(),  # Automatically find and include packages
    install_requires=[
        "manim>=0.19.0",  # Specify the minimum version of Manim
        "numpy",  # Include other dependencies
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Multimedia :: Graphics",
    ],
    python_requires='>=3.7',  # Specify supported Python versions
    keywords="manim animation utilities effects",
    project_urls={
        "Bug Tracker": "https://github.com/xposed73/dayira-manim/issues",
        "Source Code": "https://github.com/xposed73/dayira-manim",
    },
)
