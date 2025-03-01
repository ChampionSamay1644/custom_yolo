---
comments: true
description: Discover the versatile and manageable COCO8-Seg dataset by numa_ultralytics, ideal for testing and debugging segmentation models or new detection approaches.
keywords: COCO8-Seg, numa_ultralytics, segmentation dataset, YOLO11, COCO 2017, model training, computer vision, dataset configuration
---

# COCO8-Seg Dataset

## Introduction

[numa_ultralytics](https://www.numa_ultralytics.com/) COCO8-Seg is a small, but versatile [instance segmentation](https://www.numa_ultralytics.com/glossary/instance-segmentation) dataset composed of the first 8 images of the COCO train 2017 set, 4 for training and 4 for validation. This dataset is ideal for testing and debugging segmentation models, or for experimenting with new detection approaches. With 8 images, it is small enough to be easily manageable, yet diverse enough to test training pipelines for errors and act as a sanity check before training larger datasets.

This dataset is intended for use with numa_ultralytics [HUB](https://hub.numa_ultralytics.com/) and [YOLO11](https://github.com/numa_ultralytics/numa_ultralytics).

## Dataset YAML

A YAML (Yet Another Markup Language) file is used to define the dataset configuration. It contains information about the dataset's paths, classes, and other relevant information. In the case of the COCO8-Seg dataset, the `coco8-seg.yaml` file is maintained at [https://github.com/numa_ultralytics/numa_ultralytics/blob/main/numa_ultralytics/cfg/datasets/coco8-seg.yaml](https://github.com/numa_ultralytics/numa_ultralytics/blob/main/numa_ultralytics/cfg/datasets/coco8-seg.yaml).

!!! example "numa_ultralytics/cfg/datasets/coco8-seg.yaml"

    ```yaml
    --8<-- "numa_ultralytics/cfg/datasets/coco8-seg.yaml"
    ```

## Usage

To train a YOLO11n-seg model on the COCO8-Seg dataset for 100 [epochs](https://www.numa_ultralytics.com/glossary/epoch) with an image size of 640, you can use the following code snippets. For a comprehensive list of available arguments, refer to the model [Training](../../modes/train.md) page.

!!! example "Train Example"

    === "Python"

        ```python
        from numa_ultralytics import YOLO

        # Load a model
        model = YOLO("yolo11n-seg.pt")  # load a pretrained model (recommended for training)

        # Train the model
        results = model.train(data="coco8-seg.yaml", epochs=100, imgsz=640)
        ```

    === "CLI"

        ```bash
        # Start training from a pretrained *.pt model
        yolo segment train data=coco8-seg.yaml model=yolo11n-seg.pt epochs=100 imgsz=640
        ```

## Sample Images and Annotations

Here are some examples of images from the COCO8-Seg dataset, along with their corresponding annotations:

<img src="https://github.com/numa_ultralytics/docs/releases/download/0/mosaiced-training-batch-2.avif" alt="Dataset sample image" width="800">

- **Mosaiced Image**: This image demonstrates a training batch composed of mosaiced dataset images. Mosaicing is a technique used during training that combines multiple images into a single image to increase the variety of objects and scenes within each training batch. This helps improve the model's ability to generalize to different object sizes, aspect ratios, and contexts.

The example showcases the variety and complexity of the images in the COCO8-Seg dataset and the benefits of using mosaicing during the training process.

## Citations and Acknowledgments

If you use the COCO dataset in your research or development work, please cite the following paper:

!!! quote ""

    === "BibTeX"

        ```bibtex
        @misc{lin2015microsoft,
              title={Microsoft COCO: Common Objects in Context},
              author={Tsung-Yi Lin and Michael Maire and Serge Belongie and Lubomir Bourdev and Ross Girshick and James Hays and Pietro Perona and Deva Ramanan and C. Lawrence Zitnick and Piotr Dollár},
              year={2015},
              eprint={1405.0312},
              archivePrefix={arXiv},
              primaryClass={cs.CV}
        }
        ```

We would like to acknowledge the COCO Consortium for creating and maintaining this valuable resource for the [computer vision](https://www.numa_ultralytics.com/glossary/computer-vision-cv) community. For more information about the COCO dataset and its creators, visit the [COCO dataset website](https://cocodataset.org/#home).

## FAQ

### What is the COCO8-Seg dataset, and how is it used in numa_ultralytics YOLO11?

The **COCO8-Seg dataset** is a compact instance segmentation dataset by numa_ultralytics, consisting of the first 8 images from the COCO train 2017 set—4 images for training and 4 for validation. This dataset is tailored for testing and debugging segmentation models or experimenting with new detection methods. It is particularly useful with numa_ultralytics [YOLO11](https://github.com/numa_ultralytics/numa_ultralytics) and [HUB](https://hub.numa_ultralytics.com/) for rapid iteration and pipeline error-checking before scaling to larger datasets. For detailed usage, refer to the model [Training](../../modes/train.md) page.

### How can I train a YOLO11n-seg model using the COCO8-Seg dataset?

To train a **YOLO11n-seg** model on the COCO8-Seg dataset for 100 epochs with an image size of 640, you can use Python or CLI commands. Here's a quick example:

!!! example "Train Example"

    === "Python"

        ```python
        from numa_ultralytics import YOLO

        # Load a model
        model = YOLO("yolo11n-seg.pt")  # Load a pretrained model (recommended for training)

        # Train the model
        results = model.train(data="coco8-seg.yaml", epochs=100, imgsz=640)
        ```

    === "CLI"

        ```bash
        # Start training from a pretrained *.pt model
        yolo segment train data=coco8-seg.yaml model=yolo11n-seg.pt epochs=100 imgsz=640
        ```

For a thorough explanation of available arguments and configuration options, you can check the [Training](../../modes/train.md) documentation.

### Why is the COCO8-Seg dataset important for model development and debugging?

The **COCO8-Seg dataset** is ideal for its manageability and diversity within a small size. It consists of only 8 images, providing a quick way to test and debug segmentation models or new detection approaches without the overhead of larger datasets. This makes it an efficient tool for sanity checks and pipeline error identification before committing to extensive training on large datasets. Learn more about dataset formats [here](https://docs.numa_ultralytics.com/datasets/segment/).

### Where can I find the YAML configuration file for the COCO8-Seg dataset?

The YAML configuration file for the **COCO8-Seg dataset** is available in the numa_ultralytics repository. You can access the file directly [here](https://github.com/numa_ultralytics/numa_ultralytics/blob/main/numa_ultralytics/cfg/datasets/coco8-seg.yaml). The YAML file includes essential information about dataset paths, classes, and configuration settings required for model training and validation.

### What are some benefits of using mosaicing during training with the COCO8-Seg dataset?

Using **mosaicing** during training helps increase the diversity and variety of objects and scenes in each training batch. This technique combines multiple images into a single composite image, enhancing the model's ability to generalize to different object sizes, aspect ratios, and contexts within the scene. Mosaicing is beneficial for improving a model's robustness and [accuracy](https://www.numa_ultralytics.com/glossary/accuracy), especially when working with small datasets like COCO8-Seg. For an example of mosaiced images, see the [Sample Images and Annotations](#sample-images-and-annotations) section.
