import os
import configparser
import logging


def get_config() -> configparser.ConfigParser:
    config = configparser.ConfigParser(interpolation=None)
    config_file = os.environ['CONFIG_PATH']

    if config_file is not None:
        config.read(config_file)
    else:
        raise EnvironmentError("Environment variable CONFIG_PATH is not set or config file is missing, "
                               "try run setup_env.py to set it")

    return config


def get_path(path_type: str) -> str:
    config = get_config()
    if 'path' in config.sections():
        path_config = config['path']
    else:
        raise ValueError("No path section in " + os.environ['CONFIG_PATH'])
    if path_type in path_config:
        return os.path.abspath(os.path.join(os.environ['PROJECT_PATH'],
                                            config['path'][path_type]))
    else:
        raise ValueError(path_type + "not available in 'path' section of " + os.environ['CONFIG_PATH'])


def set_log_config(filename: str) -> logging:
    config = get_config()
    logfile = os.path.join(get_path('logs_path'), os.path.basename(filename) + ".log")
    print(filename)
    print(logfile)
    if 'logs' in config.sections():
        log_config = config['logs']
        log_level = getattr(logging, log_config.get('level'))
        log_format = log_config.get('format')
        logging.basicConfig(filename=logfile,
                            level=log_level,
                            format=log_format)
    else:
        raise ValueError("logs section not set in " + os.environ['CONFIG_PATH'])
    logging.info("Logger started")
    return logging.getLogger("LOG")
