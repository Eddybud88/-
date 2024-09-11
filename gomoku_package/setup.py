from setuptools import setup, find_packages

setup(
    name='gomoku',
    version='0.1.0',
    description='一个具有AI的五子棋游戏',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'Pillow'
    ],
    entry_points={
        'console_scripts': [
            'gomoku=gomoku.gui:main',
        ],
    },
)

