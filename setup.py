from setuptools import setup, find_packages

setup(
    name="lazyT",
    version='0.1',
    description='To do list',
    author='78RainDrops',
    author_email='smileyrence3@gmail.com',
    packages=find_packages(),
    entry_points = {
        'console_scripts' : [
            'lazyT=lazy_task.lazy:main'
        ],
    },
    install_requires=[
        'requests',
    ],
)