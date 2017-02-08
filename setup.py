from setuptools import setup, find_packages
import pybtcc

setup(
    name='pybtcc',
    version=pybtcc.__version__,
    packages=find_packages(exclude=['tests']),
    description='A btcc API for Python',
    author='Grant Stephens',
    author_email='grant@stephens.co.za',
    scripts=['demo.py'],
    install_requires=[
        'futures>=3.0.3',
        'nose>=1.3.7',
        'requests>=2.8.1',
        'pandas>=0.17.0'
    ],
    license='MIT',
    url='https://github.com/grantstephens/pybtcc',
    download_url='https://github.com/grantstephens/pybtcc/tarball/%s'
        % (pybtcc.__version__, ),
    keywords='btcc Bitcoin exchange API',
    classifiers=[],
    test_suite='tests',
    tests_require=[
        'requests-mock>=0.7.0'
    ]
)
