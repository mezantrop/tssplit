from setuptools import setup

setup(
    name='tssplit',
    version='1.0.1',
    py_modules=['tssplit.tssplit'],
    url='https://github.com/mezantrop/tssplit',
    license='bsd-2-clause',
    author='Mikhail Zakharov',
    author_email='zmey20000@yahoo.com',
    description='Trivial split for strings with escaped characters and quotes',
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
    keywords=['split', 'parse', 'quote'],

)
