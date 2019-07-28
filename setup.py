import os
import os.path as osp
from setuptools import setup, find_packages


loc = os.path.dirname(os.path.abspath(__file__))


with open(osp.join(loc, 'requirements.txt')) as f:
    required = f.read().splitlines()


description_text = \
'''
-------- ARTIFICE --------
  "You Are What You See"

Artifice is a project which aims to unravel the
multi-faceted landscape of our modern media landscape.
Content is scraped from a wide variety of sources
and viewpoints and distilled into salient data,
which we use to train generative text models. The
output of these models is rendered in a realistic
mockup resembling a typical site one might encounter
on the web. In addition to the novelty of computer-
generated news stories, we also aim to decipher the
relationships between stories and the discussions
they spark. By tracking storylines from the first
mention to the point at which they influence the
national conversation around an issue, we can provide
insight into the mechanisms driving our understanding
of the modern news cycle.

[Web]
https://www.artifice-project.com/
[Source Code]
https://github.com/minelminel/artifice-project.git
'''


setup(
    version="0.0.1",
    name="Artifice",
    author=["@minelminel", "@liberty3000"],
    url="https://www.github.com/minelminel/artifice-project",
    description="You Are What You See",
    long_description=description_text,
    install_requires=required,
    packages=find_packages("src"),
    package_dir={"": "src"},
)
