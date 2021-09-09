"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib
import os
import sys

sys.path.append("mwa_preprocess")
import version

def package_files(package_dir, subdirectory):
    # walk the input package_dir/subdirectory
    # return a package_data list
    paths = []
    directory = os.path.join(package_dir, subdirectory)
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            path = path.replace(package_dir + '/', '')
            paths.append(os.path.join(path, filename))
    return paths

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')
#data_files = package_files('mwa_preprocess')

setup(
    name='mwa_preprocess',  # Required
    version=version.version,
    description='Scripts to prepare MWA data for the HERA lstbinner.',  # Optional
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    url='https://github.com/aewallwi/nwa_preprocess',  # Optional
    author='A. Ewall-Wice',  # Optional
    author_email='aaronew@berkeley.edu',  # Optional
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='21cm, cosmology, foregrounds, radio astronomy, cosmic dawn',
    package_dir={'mwa_preprocess': 'mwa_preprocess'},
    packages=['mwa_preprocess'],
    python_requires='>=3.6, <4',
    install_requires=[
                      'httplib2<=0.15.0',
                      'pyuvdata',
                      'numpy',
                      'pydrive',
                      'tqdm',
                      ],
    #include_package_data=True,
    scripts=['scripts/mwa_cal_and_split.py', 'scripts/mwa_download_gdrive.py', 'scripts/mwa_upload_gdrive.py'],
    #package_data={'mwa_preprocess': data_files},
    zip_safe = False,
    )
