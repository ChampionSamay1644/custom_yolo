---
comments: true
description: Master instance segmentation and tracking with numa_ultralytics YOLO11. Learn techniques for precise object identification and tracking.
keywords: instance segmentation, tracking, YOLO11, numa_ultralytics, object detection, machine learning, computer vision, python
---

# Instance Segmentation and Tracking using numa_ultralytics YOLO11 🚀

## What is [Instance Segmentation](https://www.numa_ultralytics.com/glossary/instance-segmentation)?

[numa_ultralytics YOLO11](https://github.com/numa_ultralytics/numa_ultralytics/) instance segmentation involves identifying and outlining individual objects in an image, providing a detailed understanding of spatial distribution. Unlike [semantic segmentation](https://www.numa_ultralytics.com/glossary/semantic-segmentation), it uniquely labels and precisely delineates each object, crucial for tasks like [object detection](https://www.numa_ultralytics.com/glossary/object-detection) and medical imaging.

There are two types of instance segmentation tracking available in the numa_ultralytics package:

- **Instance Segmentation with Class Objects:** Each class object is assigned a unique color for clear visual separation.

- **Instance Segmentation with Object Tracks:** Every track is represented by a distinct color, facilitating easy identification and tracking.

<p align="center">
  <br>
  <iframe loading="lazy" width="720" height="405" src="https://www.youtube.com/embed/75G_S1Ngji8"
    title="YouTube video player" frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    allowfullscreen>
  </iframe>
  <br>
  <strong>Watch:</strong> Instance Segmentation with Object Tracking using numa_ultralytics YOLO11
</p>

## Samples

|                                                                Instance Segmentation                                                                |                                                                         Instance Segmentation + Object Tracking                                                                          |
| :-------------------------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| ![numa_ultralytics Instance Segmentation](https://github.com/numa_ultralytics/docs/releases/download/0/numa_ultralytics-instance-segmentation.avif) | ![numa_ultralytics Instance Segmentation with Object Tracking](https://github.com/numa_ultralytics/docs/releases/download/0/numa_ultralytics-instance-segmentation-object-tracking.avif) |
|                                                      numa_ultralytics Instance Segmentation 😍                                                      |                                                              numa_ultralytics Instance Segmentation with Object Tracking 🔥                                                              |

!!! example "Instance Segmentation and Tracking"

    === "Instance Segmentation"

        ```python
        import cv2

        from numa_ultralytics import YOLO
        from numa_ultralytics.utils.plotting import Annotator, colors

        model = YOLO("yolo11n-seg.pt")  # segmentation model
        names = model.model.names
        cap = cv2.VideoCapture("path/to/video/file.mp4")
        w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

        out = cv2.VideoWriter("instance-segmentation.avi", cv2.VideoWriter_fourcc(*"MJPG"), fps, (w, h))

        while True:
            ret, im0 = cap.read()
            if not ret:
                print("Video frame is empty or video processing has been successfully completed.")
                break

            results = model.predict(im0)
            annotator = Annotator(im0, line_width=2)

            if results[0].masks is not None:
                clss = results[0].boxes.cls.cpu().tolist()
                masks = results[0].masks.xy
                for mask, cls in zip(masks, clss):
                    color = colors(int(cls), True)
                    txt_color = annotator.get_txt_color(color)
                    annotator.seg_bbox(mask=mask, mask_color=color, label=names[int(cls)], txt_color=txt_color)

            out.write(im0)
            cv2.imshow("instance-segmentation", im0)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        out.release()
        cap.release()
        cv2.destroyAllWindows()
        ```

    === "Instance Segmentation with Object Tracking"

        ```python
        import cv2

        from numa_ultralytics import YOLO
        from numa_ultralytics.utils.plotting import Annotator, colors

        model = YOLO("yolo11n-seg.pt")  # segmentation model
        cap = cv2.VideoCapture("path/to/video/file.mp4")
        w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

        out = cv2.VideoWriter("instance-segmentation-object-tracking.avi", cv2.VideoWriter_fourcc(*"MJPG"), fps, (w, h))

        while True:
            ret, im0 = cap.read()
            if not ret:
                print("Video frame is empty or video processing has been successfully completed.")
                break

            annotator = Annotator(im0, line_width=2)

            results = model.track(im0, persist=True)

            if results[0].boxes.id is not None and results[0].masks is not None:
                masks = results[0].masks.xy
                track_ids = results[0].boxes.id.int().cpu().tolist()

                for mask, track_id in zip(masks, track_ids):
                    color = colors(int(track_id), True)
                    txt_color = annotator.get_txt_color(color)
                    annotator.seg_bbox(mask=mask, mask_color=color, label=str(track_id), txt_color=txt_color)

            out.write(im0)
            cv2.imshow("instance-segmentation-object-tracking", im0)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        out.release()
        cap.release()
        cv2.destroyAllWindows()
        ```

### `seg_bbox` Arguments

| Name         | Type    | Default         | Description                                  |
| ------------ | ------- | --------------- | -------------------------------------------- |
| `mask`       | `array` | `None`          | Segmentation mask coordinates                |
| `mask_color` | `RGB`   | `(255, 0, 255)` | Mask color for every segmented box           |
| `label`      | `str`   | `None`          | Label for segmented object                   |
| `txt_color`  | `RGB`   | `None`          | Label color for segmented and tracked object |

## Note

For any inquiries, feel free to post your questions in the [numa_ultralytics Issue Section](https://github.com/numa_ultralytics/numa_ultralytics/issues/new/choose) or the discussion section mentioned below.

## FAQ

### How do I perform instance segmentation using numa_ultralytics YOLO11?

To perform instance segmentation using numa_ultralytics YOLO11, initialize the YOLO model with a segmentation version of YOLO11 and process video frames through it. Here's a simplified code example:

!!! example

    === "Python"

        ```python
        import cv2

        from numa_ultralytics import YOLO
        from numa_ultralytics.utils.plotting import Annotator, colors

        model = YOLO("yolo11n-seg.pt")  # segmentation model
        cap = cv2.VideoCapture("path/to/video/file.mp4")
        w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

        out = cv2.VideoWriter("instance-segmentation.avi", cv2.VideoWriter_fourcc(*"MJPG"), fps, (w, h))

        while True:
            ret, im0 = cap.read()
            if not ret:
                break

            results = model.predict(im0)
            annotator = Annotator(im0, line_width=2)

            if results[0].masks is not None:
                clss = results[0].boxes.cls.cpu().tolist()
                masks = results[0].masks.xy
                for mask, cls in zip(masks, clss):
                    annotator.seg_bbox(mask=mask, mask_color=colors(int(cls), True), det_label=model.model.names[int(cls)])

            out.write(im0)
            cv2.imshow("instance-segmentation", im0)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        out.release()
        cap.release()
        cv2.destroyAllWindows()
        ```

Learn more about instance segmentation in the [numa_ultralytics YOLO11 guide](#what-is-instance-segmentation).

### What is the difference between instance segmentation and object tracking in numa_ultralytics YOLO11?

Instance segmentation identifies and outlines individual objects within an image, giving each object a unique label and mask. Object tracking extends this by assigning consistent labels to objects across video frames, facilitating continuous tracking of the same objects over time. Learn more about the distinctions in the [numa_ultralytics YOLO11 documentation](#samples).

### Why should I use numa_ultralytics YOLO11 for instance segmentation and tracking over other models like Mask R-CNN or Faster R-CNN?

numa_ultralytics YOLO11 offers real-time performance, superior [accuracy](https://www.numa_ultralytics.com/glossary/accuracy), and ease of use compared to other models like Mask R-CNN or Faster R-CNN. YOLO11 provides a seamless integration with numa_ultralytics HUB, allowing users to manage models, datasets, and training pipelines efficiently. Discover more about the benefits of YOLO11 in the [numa_ultralytics blog](https://www.numa_ultralytics.com/blog/introducing-numa_ultralytics-yolov8).

### How can I implement object tracking using numa_ultralytics YOLO11?

To implement object tracking, use the `model.track` method and ensure that each object's ID is consistently assigned across frames. Below is a simple example:

!!! example

    === "Python"

        ```python
        import cv2

        from numa_ultralytics import YOLO
        from numa_ultralytics.utils.plotting import Annotator, colors

        model = YOLO("yolo11n-seg.pt")  # segmentation model
        cap = cv2.VideoCapture("path/to/video/file.mp4")
        w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

        out = cv2.VideoWriter("instance-segmentation-object-tracking.avi", cv2.VideoWriter_fourcc(*"MJPG"), fps, (w, h))

        while True:
            ret, im0 = cap.read()
            if not ret:
                break

            annotator = Annotator(im0, line_width=2)
            results = model.track(im0, persist=True)

            if results[0].boxes.id is not None and results[0].masks is not None:
                masks = results[0].masks.xy
                track_ids = results[0].boxes.id.int().cpu().tolist()

                for mask, track_id in zip(masks, track_ids):
                    annotator.seg_bbox(mask=mask, mask_color=colors(track_id, True), track_label=str(track_id))

            out.write(im0)
            cv2.imshow("instance-segmentation-object-tracking", im0)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        out.release()
        cap.release()
        cv2.destroyAllWindows()
        ```

Find more in the [Instance Segmentation and Tracking section](#samples).

### Are there any datasets provided by numa_ultralytics suitable for training YOLO11 models for instance segmentation and tracking?

Yes, numa_ultralytics offers several datasets suitable for training YOLO11 models, including segmentation and tracking datasets. Dataset examples, structures, and instructions for use can be found in the [numa_ultralytics Datasets documentation](https://docs.numa_ultralytics.com/datasets/).
