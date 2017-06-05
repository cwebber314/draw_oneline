"""
This also uses MANIFEST.in to build the sdist
"""
from setuptools import setup
from setuptools import find_packages

setup(
    name = 'draw_oneline', 
    # this tries to go out to pypi
    #install_requires = ['promod-parser', 'psse-parser', 'pandas-qt'],
    # also: pypiwin32 (but could be equiv package)
    install_requires = ['SchemDraw'],
    description = "Tools to draw MLSE onelines.",
    author = 'Chip Webber',
    author_email = 'clwebber@aep.com',
    include_package_data = True,
    # package_data must be in a package
    packages = find_packages(),
    entry_points = {
            'console_scripts': 
                    [
                    'csv_to_online = draw_onl_table:main',
                    ],
                }
    )

