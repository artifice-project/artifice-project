from setuptools import setup

setup(
    version="0.0.1",
    name="Artifice",
    author="@minelminel, @liberty3000",
    description="you are what you see",
    long_description="content distilled from hundred of news sources, \
        training multiple generative models, which produces results \
        which are then rendered as a faux news site.",
    install_requires=[
        "",
    ],
    modules=[
        artifice.database,
        artifice.graphql,
        artifice.model,
        artifice.rest,
        artifice.scraper,
        artifice.util,
    ]
)
