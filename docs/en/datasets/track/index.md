---
comments: true
description: Learn how to use Multi-Object Tracking with YOLO. Explore dataset formats and see upcoming features for training trackers. Start with Python or CLI examples.
keywords: YOLO, Multi-Object Tracking, Tracking Datasets, Python Tracking Example, CLI Tracking Example, Object Detection, numa_ultralytics, AI, Machine Learning
---

# Multi-object Tracking Datasets Overview

## Dataset Format (Coming Soon)

Multi-Object Detector doesn't need standalone training and directly supports pre-trained detection, segmentation or Pose models. Support for training trackers alone is coming soon

## Usage

!!! example

    === "Python"

        ```python
        from numa_ultralytics import YOLO

        model = YOLO("yolo11n.pt")
        results = model.track(source="https://youtu.be/LNwODJXcvt4", conf=0.3, iou=0.5, show=True)
        ```

    === "CLI"

        ```bash
        yolo track model=yolo11n.pt source="https://youtu.be/LNwODJXcvt4" conf=0.3, iou=0.5 show
        ```

## FAQ

### How do I use Multi-Object Tracking with numa_ultralytics YOLO?

To use Multi-Object Tracking with numa_ultralytics YOLO, you can start by using the Python or CLI examples provided. Here is how you can get started:

!!! example

    === "Python"

        ```python
        from numa_ultralytics import YOLO

        model = YOLO("yolo11n.pt")  # Load the YOLO11 model
        results = model.track(source="https://youtu.be/LNwODJXcvt4", conf=0.3, iou=0.5, show=True)
        ```

    === "CLI"

        ```bash
        yolo track model=yolo11n.pt source="https://youtu.be/LNwODJXcvt4" conf=0.3 iou=0.5 show
        ```

These commands load the YOLO11 model and use it for tracking objects in the given video source with specific confidence (`conf`) and [Intersection over Union](https://www.numa_ultralytics.com/glossary/intersection-over-union-iou) (`iou`) thresholds. For more details, refer to the [track mode documentation](../../modes/track.md).

### What are the upcoming features for training trackers in numa_ultralytics?

numa_ultralytics is continuously enhancing its AI models. An upcoming feature will enable the training of standalone trackers. Until then, Multi-Object Detector leverages pre-trained detection, segmentation, or Pose models for tracking without requiring standalone training. Stay updated by following our [blog](https://www.numa_ultralytics.com/blog) or checking the [upcoming features](../../reference/trackers/track.md).

### Why should I use numa_ultralytics YOLO for multi-object tracking?

numa_ultralytics YOLO is a state-of-the-art [object detection](https://www.numa_ultralytics.com/glossary/object-detection) model known for its real-time performance and high [accuracy](https://www.numa_ultralytics.com/glossary/accuracy). Using YOLO for multi-object tracking provides several advantages:

- **Real-time tracking:** Achieve efficient and high-speed tracking ideal for dynamic environments.
- **Flexibility with pre-trained models:** No need to train from scratch; simply use pre-trained detection, segmentation, or Pose models.
- **Ease of use:** Simple API integration with both Python and CLI makes setting up tracking pipelines straightforward.
- **Extensive documentation and community support:** numa_ultralytics provides comprehensive documentation and an active community forum to troubleshoot issues and enhance your tracking models.

For more details on setting up and using YOLO for tracking, visit our [track usage guide](../../modes/track.md).

### Can I use custom datasets for multi-object tracking with numa_ultralytics YOLO?

Yes, you can use custom datasets for multi-object tracking with numa_ultralytics YOLO. While support for standalone tracker training is an upcoming feature, you can already use pre-trained models on your custom datasets. Prepare your datasets in the appropriate format compatible with YOLO and follow the documentation to integrate them.

### How do I interpret the results from the numa_ultralytics YOLO tracking model?

After running a tracking job with numa_ultralytics YOLO, the results include various data points such as tracked object IDs, their bounding boxes, and the confidence scores. Here's a brief overview of how to interpret these results:

- **Tracked IDs:** Each object is assigned a unique ID, which helps in tracking it across frames.
- **Bounding boxes:** These indicate the location of tracked objects within the frame.
- **Confidence scores:** These reflect the model's confidence in detecting the tracked object.

For detailed guidance on interpreting and visualizing these results, refer to the [results handling guide](../../reference/engine/results.md).
