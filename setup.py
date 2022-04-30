from setuptools import setup, find_packages

REQUIREMENT_FILE_NAME="requirements.txt"
REMOVE_PACKAGE="-e ."

def get_requirements_list(requirement_file_name=REQUIREMENT_FILE_NAME)->list:
    try:
        requirement_list = None
        with open(requirement_file_name, "r") as requirement_file:
            requirement_list = [requirement.replace("\n", "") for requirement in requirement_file]
            requirement_list.remove(REMOVE_PACKAGE)
        return requirement_list

    except Exception as e:
        raise e

setup(
    name='Text Classification using LSTM',
    license='MIT',
    description='This project is for Text Classification using LSTM',
    author='Diwanshu Asthana',
    packages=find_packages(),
    install_requires=get_requirements_list()
)