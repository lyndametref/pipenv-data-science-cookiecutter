# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Project structure
```
project_folder
├── cache          <- where cache files are saved (not committed)
├── data           <- to store data
├── logs           <- where logs are saved (not committed)
├── model          <- generated model
├── notebooks      <- to save notebooks
├── scripts        <- to save analysis script
├── src            <- source code of functions to be used in notebook or scripts
│   ├── cache.py    <- function for data caching
│   └── config.py   <- configuration helper function
├── config.ini      <- project parameterisation
├── .gitignore
├── Pipfile         <- to configure which package to install 
├── README.md
└── setup.py        <- setup script for the project

```

## Installation 
Insure python and pipenv are installed:

    $ python --version
    $ pipenv --version

Copy template and run in project folder:

    $ pyhton setup.py            # setup local pipenv environment variables
    $ pipenv install             # --dev to include test packages
