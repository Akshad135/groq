from setuptools import setup, find_packages

setup(
    name='groq_cli_chat',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'groq',
        'python-dotenv',
    ],
    entry_points={
        'console_scripts': [
            'grc=groq_cli_chat.work:main'
        ],
    }
)
