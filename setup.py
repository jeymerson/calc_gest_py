from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="gest_init",
    version="0.0.1",
    author="Jeymerson Silvar Sousa",
    author_email="jeymerson.jss@gmail.com",
    description="Um pacote com a finalidade de auxiliar em cálculos gestacionais",
    long_description=page_description, 
    long_description_content_type="text/markdown", 
    url="https://github.com/jeymerson/calc_gest_py.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8'
)
