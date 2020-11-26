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

Clone project and run in project folder:

    $ pyhton setup_env.py        # setup local pipenv environment variables
    $ pipenv install             # --dev to include test packages

Notes:
- If you move the folder you need to rerun `setup_env.py` in order to correct the path stored in `.env`. 
- As `.env` is automatically generated, it will be overwritten each time `setup_env.py` is run. thus, it is not
 advisable to modify it manually. Instead you can modify `setup_env.py` to include your modifications.
 
## Use

### Configuration
You can create configuration parameters by modifying or extending `config.ini`. All configuration parameters set in
   `config.ini` are available through the `get_config()` function which must be imported with `from src.config import
    get_config`.
    
The file `config.ini` contains a section `path` which contain path of various item relative to the project. The
 corresponding absolute system path can be queried with the function `get_path()` again to import with  `from src
 .config import get_path`. More function can be added in the `config` module if other specific parameters are added
  to the `config.ini` file.
  
### Logging
The file `config.ini` contains by default a section `logs` giving some basic logging parameters (log level and
 message format). Logging can be then activated in a script by calling the `set_logging(filename)` function and
 specify the filename where the log should be saved. The logfiles are all saved in the path specified in the
 `logs_path` parameter.
 
### Caching
To save transformed data and avoid to read it again and again from the raw data source, you can use the functions
 `read_cache_pickle()` and `write_cache_picke()` imported from the `cache` module. The data frame provided will be
  saved in the pickle format. Other format can be added by creating new functions in the cache module. All cache
   files are store in the path given by the `cache_path` parameter.  
   
### Check everything is working
You can try the various functionalities by running the script `caching_example.py`. It will import the config, create
 a cache file and read it, and create some log entries. If you are using jupyter, the notebook `read_cache_example
 ` read the cache created in the `caching_example.py`, thus don't forget to run the script before the notebook!