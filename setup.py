from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = "-e ."

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "book-recommendation-system-using-collaborative-filtering"
SRC_REPO = "src"


# funtion to add requirement to the list
def get_requirements() -> List[str]:
    """
    Returns the list of requirements
    """
    requirement_list: List[str] = []
    with open("requirements.txt", "r") as r:
        requirements = r.read()
    for requirement in requirements.split("\n"):
        requirement_list.append(requirement)
    if HYPEN_E_DOT in requirement_list:
        requirement_list.remove(HYPEN_E_DOT)
    return requirement_list


setup(
    name=REPO_NAME,
    version="0.0.1",
    author="Aniket Andhale",
    description="A small package for Book Recommender System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aniketandhale08/Book-recommendation-system-using-collaborative-filtering",
    author_email="aniketandhale94@gmail.com",
    packages=find_packages(),
    license="MIT",
    python_requires=">=3.7",
    install_requires=get_requirements(),
)
