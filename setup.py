from setuptools import setup, find_packages

setup(
    name='groq-cli',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'groq'
    ],
    entry_points={
        'console_scripts': [
            'grc=groq_cli_chat.work:main'
        ],
    },
    description='A CLI package for interacting with the Groq API.',
    author='Akshad Agrawal',
    url='https://github.com/Akshad135/groq-cli',
)
