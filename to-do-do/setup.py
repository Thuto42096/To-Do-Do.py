from setuptools import setup, find_packages

setup(
    name="to-do-do",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'todo=todo.__main__:main',
        ],
    },
    install_requires=[],
    author="Thuto R",
    author_email="thuto42096@gmail.com",
    description="A simple To Do List application",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/Thuto42096/to-do-do",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)