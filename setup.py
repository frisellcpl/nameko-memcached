from setuptools import setup

setup(
    name='nameko-memcached',
    version='0.1.0',
    url='https://github.com/frisellcpl/nameko-memcached/',
    license='Apache License, Version 2.0',
    author='frisellcpl',
    author_email='johan@trell.se',
    py_modules=['nameko_memcached'],
    install_requires=[
        "nameko>=2.0.0",
        "python-binary-memcached",
    ],
    description='Memcached dependency for nameko services',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
