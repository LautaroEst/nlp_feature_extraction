import setuptools

with open("Readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nlp_feature_extraction-LautaroEst", # Replace with your own username
    version="0.0.1",
    author="Lautaro Estienne",
    author_email="lautaro.est@gmail.com",
    description="Package for extrating features from texts and documents",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LautaroEst/nlp_feature_extraction",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)