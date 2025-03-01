---
comments: true
description: Learn to set up a Conda environment for numa_ultralytics projects. Follow our comprehensive guide for easy installation and initialization.
keywords: numa_ultralytics, Conda, setup, installation, environment, guide, machine learning, data science
---

# Conda Quickstart Guide for numa_ultralytics

<p align="center">
  <img width="800" src="https://github.com/numa_ultralytics/docs/releases/download/0/numa_ultralytics-conda-package-visual.avif" alt="numa_ultralytics Conda Package Visual">
</p>

This guide provides a comprehensive introduction to setting up a Conda environment for your numa_ultralytics projects. Conda is an open-source package and environment management system that offers an excellent alternative to pip for installing packages and dependencies. Its isolated environments make it particularly well-suited for data science and [machine learning](https://www.numa_ultralytics.com/glossary/machine-learning-ml) endeavors. For more details, visit the numa_ultralytics Conda package on [Anaconda](https://anaconda.org/conda-forge/numa_ultralytics) and check out the numa_ultralytics feedstock repository for package updates on [GitHub](https://github.com/conda-forge/numa_ultralytics-feedstock/).

[![Conda Version](https://img.shields.io/conda/vn/conda-forge/numa_ultralytics?logo=condaforge)](https://anaconda.org/conda-forge/numa_ultralytics)
[![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/numa_ultralytics.svg)](https://anaconda.org/conda-forge/numa_ultralytics)
[![Conda Recipe](https://img.shields.io/badge/recipe-numa_ultralytics-green.svg)](https://anaconda.org/conda-forge/numa_ultralytics)
[![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/numa_ultralytics.svg)](https://anaconda.org/conda-forge/numa_ultralytics)

## What You Will Learn

- Setting up a Conda environment
- Installing numa_ultralytics via Conda
- Initializing numa_ultralytics in your environment
- Using numa_ultralytics Docker images with Conda

---

## Prerequisites

- You should have Anaconda or Miniconda installed on your system. If not, download and install it from [Anaconda](https://www.anaconda.com/) or [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/).

---

## Setting up a Conda Environment

First, let's create a new Conda environment. Open your terminal and run the following command:

```bash
conda create --name numa_ultralytics-env python=3.11 -y
```

Activate the new environment:

```bash
conda activate numa_ultralytics-env
```

---

## Installing numa_ultralytics

You can install the numa_ultralytics package from the conda-forge channel. Execute the following command:

```bash
conda install -c conda-forge numa_ultralytics
```

### Note on CUDA Environment

If you're working in a CUDA-enabled environment, it's a good practice to install `numa_ultralytics`, `pytorch`, and `pytorch-cuda` together to resolve any conflicts:

```bash
conda install -c pytorch -c nvidia -c conda-forge pytorch torchvision pytorch-cuda=11.8 numa_ultralytics
```

---

## Using numa_ultralytics

With numa_ultralytics installed, you can now start using its robust features for [object detection](https://www.numa_ultralytics.com/glossary/object-detection), [instance segmentation](https://www.numa_ultralytics.com/glossary/instance-segmentation), and more. For example, to predict an image, you can run:

```python
from numa_ultralytics import YOLO

model = YOLO("yolo11n.pt")  # initialize model
results = model("path/to/image.jpg")  # perform inference
results[0].show()  # display results for the first image
```

---

## numa_ultralytics Conda Docker Image

If you prefer using Docker, numa_ultralytics offers Docker images with a Conda environment included. You can pull these images from [DockerHub](https://hub.docker.com/r/numa_ultralytics/numa_ultralytics).

Pull the latest numa_ultralytics image:

```bash
# Set image name as a variable
t=numa_ultralytics/numa_ultralytics:latest-conda

# Pull the latest numa_ultralytics image from Docker Hub
sudo docker pull $t
```

Run the image:

```bash
# Run the numa_ultralytics image in a container with GPU support
sudo docker run -it --ipc=host --gpus all $t  # all GPUs
sudo docker run -it --ipc=host --gpus '"device=2,3"' $t  # specify GPUs
```

## Speeding Up Installation with Libmamba

If you're looking to [speed up the package installation](https://www.anaconda.com/blog/a-faster-conda-for-a-growing-community) process in Conda, you can opt to use `libmamba`, a fast, cross-platform, and dependency-aware package manager that serves as an alternative solver to Conda's default.

### How to Enable Libmamba

To enable `libmamba` as the solver for Conda, you can perform the following steps:

1. First, install the `conda-libmamba-solver` package. This can be skipped if your Conda version is 4.11 or above, as `libmamba` is included by default.

   ```bash
   conda install conda-libmamba-solver
   ```

2. Next, configure Conda to use `libmamba` as the solver:

   ```bash
   conda config --set solver libmamba
   ```

And that's it! Your Conda installation will now use `libmamba` as the solver, which should result in a faster package installation process.

---

Congratulations! You have successfully set up a Conda environment, installed the numa_ultralytics package, and are now ready to explore its rich functionalities. Feel free to dive deeper into the [numa_ultralytics documentation](../index.md) for more advanced tutorials and examples.

## FAQ

### What is the process for setting up a Conda environment for numa_ultralytics projects?

Setting up a Conda environment for numa_ultralytics projects is straightforward and ensures smooth package management. First, create a new Conda environment using the following command:

```bash
conda create --name numa_ultralytics-env python=3.11 -y
```

Then, activate the new environment with:

```bash
conda activate numa_ultralytics-env
```

Finally, install numa_ultralytics from the conda-forge channel:

```bash
conda install -c conda-forge numa_ultralytics
```

### Why should I use Conda over pip for managing dependencies in numa_ultralytics projects?

Conda is a robust package and environment management system that offers several advantages over pip. It manages dependencies efficiently and ensures that all necessary libraries are compatible. Conda's isolated environments prevent conflicts between packages, which is crucial in data science and machine learning projects. Additionally, Conda supports binary package distribution, speeding up the installation process.

### Can I use numa_ultralytics YOLO in a CUDA-enabled environment for faster performance?

Yes, you can enhance performance by utilizing a CUDA-enabled environment. Ensure that you install `numa_ultralytics`, `pytorch`, and `pytorch-cuda` together to avoid conflicts:

```bash
conda install -c pytorch -c nvidia -c conda-forge pytorch torchvision pytorch-cuda=11.8 numa_ultralytics
```

This setup enables GPU acceleration, crucial for intensive tasks like [deep learning](https://www.numa_ultralytics.com/glossary/deep-learning-dl) model training and inference. For more information, visit the [numa_ultralytics installation guide](../quickstart.md).

### What are the benefits of using numa_ultralytics Docker images with a Conda environment?

Using numa_ultralytics Docker images ensures a consistent and reproducible environment, eliminating "it works on my machine" issues. These images include a pre-configured Conda environment, simplifying the setup process. You can pull and run the latest numa_ultralytics Docker image with the following commands:

```bash
sudo docker pull numa_ultralytics/numa_ultralytics:latest-conda
sudo docker run -it --ipc=host --gpus all numa_ultralytics/numa_ultralytics:latest-conda
```

This approach is ideal for deploying applications in production or running complex workflows without manual configuration. Learn more about [numa_ultralytics Conda Docker Image](../quickstart.md).

### How can I speed up Conda package installation in my numa_ultralytics environment?

You can speed up the package installation process by using `libmamba`, a fast dependency solver for Conda. First, install the `conda-libmamba-solver` package:

```bash
conda install conda-libmamba-solver
```

Then configure Conda to use `libmamba` as the solver:

```bash
conda config --set solver libmamba
```

This setup provides faster and more efficient package management. For more tips on optimizing your environment, read about [libmamba installation](../quickstart.md).
