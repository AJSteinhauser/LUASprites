
from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()


setup(
    name = 'LUASprites',
    version = '0.0.1',
    author = 'AJ Steinhauser',
    author_email = 'ajsteinhauser11@gmail.com',
    license = 'MIT License',
    description = 'Generate spritesheets and lua modules for easy image reference',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/AJSteinhauser/LUASprites',
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        luasprite=spritesheet.cli:main
    '''
)