> [!IMPORTANT]
> This project is under development. All source code and features on the main branch are for the purpose of testing or evaluation and not production ready.

# MFD Testing

## Usage

test

### Available commands

When installing `mfd-testing`.\
So you can just type `mfd-help` in your terminal without a need to call it from Python.


> `mfd-testing1`\
> mfd-testing1

> `mfd-testing2`\
> test1.\
> test2'.


All commands can be combined with `--project-dir` parameter, which should point to the root directory of your repository.
If this parameter is not given current working directory will be assumed to be root directory.

### Configuration files
We are using 3 configuration files:
- `ruff.toml` - for ruff configuration
- `pyproject.toml` - for project/generic configuration
- `.pre-commit-config.yaml` - for pre-commit configuration

### Custom configuration
Some modules have custom configuration files. Files are stored in `mfd_testing` directory. Configuration files are merged with generic one during configuration process.

## OS supported:

OS agnostic

## Issue reporting

If you encounter any bugs or have suggestions for improvements, you're welcome to contribute directly or open an issue [here](https://github.com/mfd-testing/issues).