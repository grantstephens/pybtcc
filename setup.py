from setuptools import setup, find_packages
import pyluno

setup(
    name='pyluno',
    version=pyluno.__version__,
    packages=find_packages(exclude=['tests']),
    description='A Luno API for Python',
    author='Cayle Sharrock',
    author_email='cayle@nimbustech.biz',
    scripts=['demo.py'],
    install_requires=[
        'futures>=3.0.3',
        'nose>=1.3.7',
        'requests>=2.8.1',
        'pandas>=0.17.0'
    ],
    license='MIT',
    url='https://github.com/grantstephens/pyluno',
    download_url='https://github.com/grantstephens/pyluno/tarball/%s'
        % (pyluno.__version__, ),
    keywords='Luno Bitcoin exchange API',
    classifiers=[],
    test_suite='tests',
    tests_require=[
        'requests-mock>=0.7.0'
    ]
)
