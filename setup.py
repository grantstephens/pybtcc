from setuptools import setup, find_packages
with open('pybtcc/_version.py') as f:
    exec(f.read())

setup(
    name='pybtcc',
    version=__version__,
    packages=find_packages(exclude=['tests']),
    description='A btcc API for Python',
    author='Grant Stephens',
    author_email='grant@stephens.co.za',
    # scripts=['demo.py'],
    install_requires=[
        'futures>=3.0.3',
        'nose>=1.3.7',
        'requests>=2.8.1',
        'pandas>=0.17.0'
    ],
    license='MIT',
    url='https://github.com/grantstephens/pybtcc',
    download_url='https://github.com/grantstephens/pybtcc/tarball/%s'
        % (__version__, ),
    keywords='btcc Bitcoin exchange API',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Office/Business :: Financial',
        'Topic :: Utilities',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only'
    ],
    # test_suite='tests',
    # tests_require=[
    #     'requests-mock>=0.7.0'
    # ]
)
