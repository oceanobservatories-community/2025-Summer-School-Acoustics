# Development README
Some helpful guidelines for creating code to go into this repository.

**thoughts on python versions**
I (John) have been developing in python 3.12. I think it would be a good idea to choose a single version of python and all use the same version. I'm happy for it to be a different version though depending on other people's needs.

**scientific python** I'm basing the package structure on the current scientific python best practices guidelines. This is a really neat resource that can be found [here](https://learn.scientific-python.org/development/)


## pyproject.toml
We can specify python package requirements in the pyproject.toml for the summer school. We can also add extra dependencies for development. The section for this is copied below:

```toml
dependencies = [
  "numpy",
  "scipy",
]

[project.optional-dependencies]
dev = [
  "hatch",
]
```

to install the development dependancies, first navigate to the repository (should be inside folder containing pyproject.toml). Then type this command. (-e flag means editible, which means you can change the code, "." means current directory).

```bash
pip install -e ".[dev]"
