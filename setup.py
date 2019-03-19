from setuptools import setup, find_packages

setup(
    name='ampackage',
    version=0.1,
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA hackathon solution AOBAKWE',
    long_description=open('README.md').read(),
    install_requires=['random'],
    url='https://github.com/aobakwemmokwa/ampackage',
    author='Aobakwe Mmokwa',
    author_email='alloy.masala@gmail.com'
)
