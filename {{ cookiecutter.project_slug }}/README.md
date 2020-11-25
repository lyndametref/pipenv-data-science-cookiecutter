# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Project structure
```
{{ cookiecutter.project_slug }}
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
└── setup_env.py        <- script to setup project's environment variables
```

## Installation 
Insure python and pipenv are installed:

    $ python --version
    $ pipenv --version

Copy template and run in project folder:

    $ pyhton setup_env.py        # setup local pipenv environment variables
    $ pipenv install             # --dev to include test packages
