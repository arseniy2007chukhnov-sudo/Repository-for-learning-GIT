from setuptools import setup, find_packages

setup(
    name = "ndfl-aosu",
    version = "0.2.0",
    long_description = "Tax calculator\n" \
    "\n" \
    "Исходный код:\n"\
    "https://github.com/arseniy2007chukhnov-sudo/Repository-for-learning-GIT/tree/feature/testing-tdd/testing_tdd",
    long_description_content_type = "text/markdown",
    package_dir = {"": "src"},
    packages = find_packages(where="src"),
    author ='Arseniy Chukhnov',
    author_email='arseniy2007chukhnov@gmail.com'
)