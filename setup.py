from os.path import join, dirname

import clube_stat
from setuptools import setup, find_packages

setup(
        name="clube_stat",
        # в __init__ пакета
        version=clube_stat.__version__,
        packages=find_packages(
                exclude=["*.exemple", "*.exemple.*", "exemple.*",
                         "exemple"]),
        include_package_data=True,
        long_description=open(
                join(dirname(__file__), 'README.rst')).read(),

        # install_requires=["PyQt5", "selenium", "pandas", "matplotlib"],
        install_requires=[],
        entry_points={
            'console_scripts':
                ['stat2 = clube_stat.main:main']
        }

)

