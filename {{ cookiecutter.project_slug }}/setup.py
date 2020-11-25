import os

project_path = os.path.abspath(os.getcwd())
config_file = os.path.join(project_path, "config.ini")
env_file = os.path.join(project_path, ".env")

with open(env_file, 'w') as env:
    env.write("PYTHONPATH=${PYTHONPATH}" + project_path + "\n")
    env.write("PROJECT_PATH=" + project_path + "\n")
    env.write("CONFIG_PATH=" + os.path.join(project_path, config_file) + "\n")
