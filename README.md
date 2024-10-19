# Python, now with 39% more GUI 🐍💻

Template for pythons apps with GUI. Features automated builds on release with binaries for Windows, MacOS and Linux users to download.
Contains linting, formatting and testing tools.

## Requirements 📋

- Python 3.12.0+

## Usage 🚀

- Go to the `Releases` page of the GitHub repository.

- Under the `Assets` section for the latest release, click the folder with the app name for your operating system.

- After downloading, extract the top content from the `.zip` to anywhere you want.

### Windows

- Run the `main.exe` file inside, you can create a shortcut with any name you like for this file.

### Linux

- Run the `main.bin` file inside. Note that compilation is targeted at Ubuntu, other distributions may need additional actions to run the app.

### MacOS

- Run the bundle installer extracted from the `.zip` file.

## Development 🛠️

- Clone the repository and open a terminal **inside** it.

- Install the dependencies:

  ```shell
  # It is it recommend that a virtual environment is set before doing this!

  pip install .
  ```

- Start the app:

  ```shell
  python src/main.py
  ```

## Tooling 🧰

- Ruff is used as a linter and formatter:

  ```shell
  pip install .[check]
  ruff check fix
  ruff format
  ```

- PyTest andPyTest-QT are used for testing:

  ```shell
  pip install .[test]
  pytest
  ```

- Nuitka is used for cross-compiling to all supported platforms:

  ```shell
  pip install .[build]
  nuitka <options>
  ```

  See the build [workflow](./.github/workflows/build.yaml) for a list of options used for each platform.

## Notes 📝

When using this repository as a template make sure to:

- Edit the project name and version in the `pyproject.toml` file.

- Edit the constants that refer to the app in the `utils/constants.py` file.

- Make sure the string in the `version.py` file matches the project version in the `pyproject.toml` file. This is only needed for the initial setup, after that the `release.yaml` workflow will ensure they are always both incremented and kept in sync.

- Update most of the `ENV` variables in the `build.yaml` workflow for the final build manifest.
