from setuptools import setup, find_packages

setup(
    name="numa_ultralytics",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "torch>=1.7.0",
        "torchvision>=0.8.1",
        "numpy>=1.18.5",
        "psutil",
        "PyYAML>=5.3.1",
    ],
)