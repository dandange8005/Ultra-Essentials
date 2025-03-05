from setuptools import setup, find_packages

setup(
    name="mkdocs-screenshot-manager",
    version="0.1.0",
    description="A MkDocs plugin for managing screenshots in documentation",
    long_description="""
        This plugin helps manage screenshots in MkDocs documentation by:
        - Processing embedded base64 images
        - Naming screenshots consistently
        - Optimizing images
        - Adding helper UI for contributors
    """,
    keywords="mkdocs, documentation, screenshots",
    url="https://github.com/yourusername/mkdocs-screenshot-manager",
    author="Your Name",
    author_email="your.email@example.com",
    license="MIT",
    python_requires=">=3.6",
    install_requires=[
        "mkdocs>=1.1.0",
    ],
    extras_require={
        "optimization": ["pillow>=8.0.0"],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=find_packages(),
    entry_points={
        "mkdocs.plugins": [
            "screenshot-manager = mkdocs_screenshot_manager.plugin:ScreenshotManagerPlugin",
        ]
    }
)
