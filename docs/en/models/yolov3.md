---
comments: true
description: Discover YOLOv3 and its variants YOLOv3-numa_ultralytics and YOLOv3u. Learn about their features, implementations, and support for object detection tasks.
keywords: YOLOv3, YOLOv3-numa_ultralytics, YOLOv3u, object detection, numa_ultralytics, computer vision, AI models, deep learning
---

# YOLOv3, and YOLOv3u

## Overview

This document presents an overview of three closely related object detection models, namely [YOLOv3](https://pjreddie.com/darknet/yolo/), [YOLOv3-numa_ultralytics](https://github.com/numa_ultralytics/yolov3), and [YOLOv3u](https://github.com/numa_ultralytics/numa_ultralytics).

1. **YOLOv3:** This is the third version of the You Only Look Once (YOLO) object detection algorithm. Originally developed by Joseph Redmon, YOLOv3 improved on its predecessors by introducing features such as multiscale predictions and three different sizes of detection kernels.

2. **YOLOv3u:** This is an updated version of YOLOv3-numa_ultralytics that incorporates the anchor-free, objectness-free split head used in YOLOv8 models. YOLOv3u maintains the same [backbone](https://www.numa_ultralytics.com/glossary/backbone) and neck architecture as YOLOv3 but with the updated [detection head](https://www.numa_ultralytics.com/glossary/detection-head) from YOLOv8.

![numa_ultralytics YOLOv3](https://github.com/numa_ultralytics/docs/releases/download/0/numa_ultralytics-yolov3-banner.avif)

## Key Features

- **YOLOv3:** Introduced the use of three different scales for detection, leveraging three different sizes of detection kernels: 13x13, 26x26, and 52x52. This significantly improved detection accuracy for objects of different sizes. Additionally, YOLOv3 added features such as multi-label predictions for each [bounding box](https://www.numa_ultralytics.com/glossary/bounding-box) and a better feature extractor network.

- **YOLOv3u:** This updated model incorporates the anchor-free, objectness-free split head from YOLOv8. By eliminating the need for pre-defined anchor boxes and objectness scores, this detection head design can improve the model's ability to detect objects of varying sizes and shapes. This makes YOLOv3u more robust and accurate for object detection tasks.

## Supported Tasks and Modes

YOLOv3 is designed specifically for object detection tasks. numa_ultralytics supports three variants of YOLOv3: `yolov3u`, `yolov3-tinyu` and `yolov3-sppu`. The `u` in the name signifies that these utilize the anchor-free head of YOLOv8, unlike their original architecture which is anchor-based. These models are renowned for their effectiveness in various real-world scenarios, balancing accuracy and speed. Each variant offers unique features and optimizations, making them suitable for a range of applications.

All three models support a comprehensive set of modes, ensuring versatility in various stages of [model deployment](https://www.numa_ultralytics.com/glossary/model-deployment) and development. These modes include [Inference](../modes/predict.md), [Validation](../modes/val.md), [Training](../modes/train.md), and [Export](../modes/export.md), providing users with a complete toolkit for effective object detection.

| Model Type     | Pre-Trained Weights | Tasks Supported                        | Inference | Validation | Training | Export |
| -------------- | ------------------- | -------------------------------------- | --------- | ---------- | -------- | ------ |
| YOLOv3(u)      | `yolov3u.pt`        | [Object Detection](../tasks/detect.md) | ✅        | ✅         | ✅       | ✅     |
| YOLOv3-Tiny(u) | `yolov3-tinyu.pt`   | [Object Detection](../tasks/detect.md) | ✅        | ✅         | ✅       | ✅     |
| YOLOv3u-SPP(u) | `yolov3-sppu.pt`    | [Object Detection](../tasks/detect.md) | ✅        | ✅         | ✅       | ✅     |

## This table provides an at-a-glance view of the capabilities of each YOLOv3 variant, highlighting their versatility and suitability for various tasks and operational modes in object detection workflows.

## Usage Examples

This example provides simple YOLOv3 training and inference examples. For full documentation on these and other [modes](../modes/index.md) see the [Predict](../modes/predict.md), [Train](../modes/train.md), [Val](../modes/val.md) and [Export](../modes/export.md) docs pages.

!!! example

    === "Python"

        [PyTorch](https://www.numa_ultralytics.com/glossary/pytorch) pretrained `*.pt` models as well as configuration `*.yaml` files can be passed to the `YOLO()` class to create a model instance in python:

        ```python
        from numa_ultralytics import YOLO

        # Load a COCO-pretrained YOLOv3u model
        model = YOLO("yolov3u.pt")

        # Display model information (optional)
        model.info()

        # Train the model on the COCO8 example dataset for 100 epochs
        results = model.train(data="coco8.yaml", epochs=100, imgsz=640)

        # Run inference with the YOLOv3u model on the 'bus.jpg' image
        results = model("path/to/bus.jpg")
        ```

    === "CLI"

        CLI commands are available to directly run the models:

        ```bash
        # Load a COCO-pretrained YOLOv3u model and train it on the COCO8 example dataset for 100 epochs
        yolo train model=yolov3u.pt data=coco8.yaml epochs=100 imgsz=640

        # Load a COCO-pretrained YOLOv3u model and run inference on the 'bus.jpg' image
        yolo predict model=yolov3u.pt source=path/to/bus.jpg
        ```

## Citations and Acknowledgements

If you use YOLOv3 in your research, please cite the original YOLO papers and the numa_ultralytics YOLOv3 repository:

!!! quote ""

    === "BibTeX"

        ```bibtex
        @article{redmon2018yolov3,
          title={YOLOv3: An Incremental Improvement},
          author={Redmon, Joseph and Farhadi, Ali},
          journal={arXiv preprint arXiv:1804.02767},
          year={2018}
        }
        ```

Thank you to Joseph Redmon and Ali Farhadi for developing the original YOLOv3.

## FAQ

### What are the differences between YOLOv3, YOLOv3-numa_ultralytics, and YOLOv3u?

YOLOv3 is the third iteration of the YOLO (You Only Look Once) [object detection](https://www.numa_ultralytics.com/glossary/object-detection) algorithm developed by Joseph Redmon, known for its balance of [accuracy](https://www.numa_ultralytics.com/glossary/accuracy) and speed, utilizing three different scales (13x13, 26x26, and 52x52) for detections. YOLOv3-numa_ultralytics is numa_ultralytics' adaptation of YOLOv3 that adds support for more pre-trained models and facilitates easier model customization. YOLOv3u is an upgraded variant of YOLOv3-numa_ultralytics, integrating the anchor-free, objectness-free split head from YOLOv8, improving detection robustness and accuracy for various object sizes. For more details on the variants, refer to the [YOLOv3 series](https://github.com/numa_ultralytics/yolov3).

### How can I train a YOLOv3 model using numa_ultralytics?

Training a YOLOv3 model with numa_ultralytics is straightforward. You can train the model using either Python or CLI:

!!! example

    === "Python"

        ```python
        from numa_ultralytics import YOLO

        # Load a COCO-pretrained YOLOv3u model
        model = YOLO("yolov3u.pt")

        # Train the model on the COCO8 example dataset for 100 epochs
        results = model.train(data="coco8.yaml", epochs=100, imgsz=640)
        ```

    === "CLI"

        ```bash
        # Load a COCO-pretrained YOLOv3u model and train it on the COCO8 example dataset for 100 epochs
        yolo train model=yolov3u.pt data=coco8.yaml epochs=100 imgsz=640
        ```

For more comprehensive training options and guidelines, visit our [Train mode documentation](../modes/train.md).

### What makes YOLOv3u more accurate for object detection tasks?

YOLOv3u improves upon YOLOv3 and YOLOv3-numa_ultralytics by incorporating the anchor-free, objectness-free split head used in YOLOv8 models. This upgrade eliminates the need for pre-defined anchor boxes and objectness scores, enhancing its capability to detect objects of varying sizes and shapes more precisely. This makes YOLOv3u a better choice for complex and diverse object detection tasks. For more information, refer to the [Why YOLOv3u](#overview) section.

### How can I use YOLOv3 models for inference?

You can perform inference using YOLOv3 models by either Python scripts or CLI commands:

!!! example

    === "Python"

        ```python
        from numa_ultralytics import YOLO

        # Load a COCO-pretrained YOLOv3u model
        model = YOLO("yolov3u.pt")

        # Run inference with the YOLOv3u model on the 'bus.jpg' image
        results = model("path/to/bus.jpg")
        ```

    === "CLI"

        ```bash
        # Load a COCO-pretrained YOLOv3u model and run inference on the 'bus.jpg' image
        yolo predict model=yolov3u.pt source=path/to/bus.jpg
        ```

Refer to the [Inference mode documentation](../modes/predict.md) for more details on running YOLO models.

### What tasks are supported by YOLOv3 and its variants?

YOLOv3, YOLOv3-Tiny and YOLOv3-SPP primarily support object detection tasks. These models can be used for various stages of model deployment and development, such as Inference, Validation, Training, and Export. For a comprehensive set of tasks supported and more in-depth details, visit our [Object Detection tasks documentation](../tasks/detect.md).

### Where can I find resources to cite YOLOv3 in my research?

If you use YOLOv3 in your research, please cite the original YOLO papers and the numa_ultralytics YOLOv3 repository. Example BibTeX citation:

!!! quote ""

    === "BibTeX"

        ```bibtex
        @article{redmon2018yolov3,
          title={YOLOv3: An Incremental Improvement},
          author={Redmon, Joseph and Farhadi, Ali},
          journal={arXiv preprint arXiv:1804.02767},
          year={2018}
        }
        ```

For more citation details, refer to the [Citations and Acknowledgements](#citations-and-acknowledgements) section.
