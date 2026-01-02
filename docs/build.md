# Build from Source
Use this section if you would like to make changes to the source code for your own project.

## Requirements

- [Git](https://git-scm.com/install/)
- [UV Astral](https://docs.astral.sh/uv/)
- [Python 3.10+](https://www.python.org/)

## Prepare the Environment

1. Clone the repository to the location of your choosing.

    ```bash
    git clone https://github.com/td3447/flet-secure-storage.git
    ```

2. From the root directory, install flet with uv.

    ```bash
    uv sync
    ```

3. Change to the build directory.

    ```bash
    cd examples/flet_secure_storage_example
    ```

4. Build the project (initially). Choose your system (windows, macos, etc.)

    ```bash
    uv run flet build <system>
    ```

### Building wheel for PyPi
- Build extension

    ```bash title="Build for Windows"
    cd examples/flet_secure_storage_example
    flet build windows
    ```

    or

    ```bash title="Build for Android"
    cd examples/flet_secure_storage_example
    flet build apk
    ```

- Start from root, where overall pyproject.toml is located
- Install modules
    ```bash
    uv run pip install --upgrade build
    ```

    ```bash
    uv run py -m build
    ```

    ```bash title="output"
    Successfully built flet_secure_storage-0.2.0.tar.gz and flet_secure_storage-0.2.0-py3-none-any.whl
    ```

    ```py title="Build for PyPi"

    uv run pip install --upgrade twine
    ```

- Create .pypirc file C:/Users/<user>/.pypirc  with the following contents

    ```toml title=".pypirc"
    [distutils]
    index-servers = pypi

    [pypi]
    username = __token__
    password = pypi-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  <- token from PyPi
    ```

- Upload to PyPi

    ```bash
    uv run twine upload dist/*
    ```