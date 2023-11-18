from setuptools import setup, find_packages
import LCFLib
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="LoCyanFrpLib",
    version=LCFLib.__version__,
    author="LxHTT",
    author_email="lxhtt@vip.qq.com",
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.6, <=3.11',
    url="https://github.com/LxHTT/LoCyanFrpLib",
    packages=find_packages(),
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests>=2.31.0"
    ],
    project_urls={
        'Documentation': 'https://github.com/LxHTT/LoCyanFrpLib/blob/master/README.md',
        'Source Code': 'https://github.com/LxHTT/LoCyanFrpLib',
        'Bug Tracker': 'https://github.com/LxHTT/LoCyanFrpLib/issues',
    }
)
