from setuptools import find_packages, setup
setup(
    name='exoedgesource',
    packages=find_packages(include=['exoedgesource']),
    version='0.1.0',
    description='Simple source for exodge',
    author='Me',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
