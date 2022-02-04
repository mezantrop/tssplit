from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='tssplit',
    version='1.0.5',
    py_modules=['tssplit.tssplit'],
    url='https://github.com/mezantrop/tssplit',
    license='bsd-2-clause',
    author='Mikhail Zakharov',
    author_email='zmey20000@yahoo.com',
    description='Trivial split for strings with quotes and escaped characters',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: General'
    ],
    keywords=['split', 'parse', 'quote', 'trim', 'strip', 'string', 'delimiter', 'separator'],

)
