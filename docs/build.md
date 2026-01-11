# Build from Source
Use this section if you would like to make changes to the source code for your own project.

## Requirements

### Minimum
- [Git](https://git-scm.com/install/)
- [UV Astral](https://docs.astral.sh/uv/)
- [Python 3.10+](https://www.python.org/)

### Optional
- [Android Studio](https://developer.android.com/studio)

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

4. Deactivate root environment
    ```bash
    deactivate
    ```   

5. Install the local dependencies needed based on the platform:
    ```bash
    uv sync
    ```

6. Modify `pyproject.toml` in the examples folder based on the host platform
    - Windows: Set an environment variable for `PROJECT_ROOT` or specify a absolute path.
    - Linux/Mac OS: Uncomment `# "flet-secure-storage @ file:///${PWD}/../..", # Linux` and comment out the windows line.

    
    * Windows
        ```toml
        dependencies = [
        # $env:PROJECT_ROOT = ($PWD.Path -replace '\\','/')  # Temporary Environment variable for Windows PowerShell
        # setx PROJECT_ROOT "$($PWD.Path)"                   # Permanent Environment variable for Windows PowerShell
        "flet-secure-storage @ file:///${PROJECT_ROOT}/../..", # for Windows
        # "flet-secure-storage @ file:///C:/path/to/flet-secure-storage", # Alternative Windows path
        # "flet-secure-storage @ file:///${PWD}/../..", # Linux
        # "flet-secure-storage @ file:///home/user/path/to/flet-secure-storage", # Alternative Linux path
        "flet>=0.80.0",
        ]
    ```
    * Linux
        ```toml
        dependencies = [
        "flet-secure-storage @ file:///${PWD}/../..", # Linux
        # "flet-secure-storage @ file:///home/user/path/to/flet-secure-storage", # Alternative Linux path
        "flet>=0.80.0",
        ]
        ```
7. Build the project. Choose your system (windows, linux, apk, etc.)
    ```bash
    uv run flet build -v <system>
    ```

8. Run the example to test build output.

- Desktop (Linux/Windows)
    ```bash
    uv run flet run -v
    ```

- Web
    ```bash
    uv run flet serve -v
    ```
    
- Android
    - Get the built `.apk` from `/examples/flet_secure_storage_example/build/apk/app-release.apk`
    - Run it in your emulator of choice. (e.g., drag apk onto Android Studios emulator)

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