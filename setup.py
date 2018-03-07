from setuptools import setup

setup(
    name='hellopackagerscript',
    version='0.1.0',
    packages=['hello'],
    url='',
    license='',
    author='University of Illinois at Urbana Champaign',
    author_email='',
    description='',
    install_requires=["ruamel.yaml"],
    entry_points={"console_scripts": ["hello = hello.__main__:main"]}

)
