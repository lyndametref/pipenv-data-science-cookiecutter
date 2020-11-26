# Data science cookiecutter template using pipenv

[cookiecutter](https://cookiecutter.readthedocs.io) template for data scientists. Provide some useful utility
 functions while trying to stay technology agnostic (outside of pipenv for package manager, pandas for basic data
 frame caching and pytest for tests).
  
Notes:
- Use pipenv to save dependencies and create virtual environment. 
- The setup_env.py script allow to set the environment variable of the pipenv. 
- Some helper functions help to read the configuration parameter, generate cache files and configure logging. 
- Provide some scripts/notebook/data to check that everything is working
- Pandas is installed by default, jupyter is optional
- Pytest as test tool in dev
- Use configparser and config.ini to manage configuration parameters
- Path and other project properties can be added in config.ini
- Only for Python 3

## Installation
```
$ cookiecutter https://github.com/lyndametref/pipenv-data-science-cookiecutter
```

## Feedback
Feel free to give your feedback on github issue section. If you found a bug and know how to correct it, don't
 hesitate to create a  pull request.