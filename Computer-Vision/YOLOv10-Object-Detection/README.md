# YOLOv10 Object Detection Project

## Project Title
Image-Based Object Detection Using YOLOv10 with Multi-Epoch Performance Evaluation

## Description
This project implements object detection using the YOLOv10 model. The model was trained and evaluated on a custom dataset containing four object classes: Apple, Banana, Orange, and Potato.

## Dataset
- Source: Roboflow
- Version: 7
- Classes:
  - Apple
  - Banana
  - Orange
  - Potato

## Model
- YOLOv10
- Training performed on Google Colab
- GPU: Tesla T4

## Experiments
- Training for 10 Epochs
- Training for 20 Epochs
- Training for 30 Epochs

## Evaluation Metrics
- Precision
- Recall
- F1-Score
- mAP50
- mAP50-95

## Technologies Used
- Python
- YOLOv10
- PyTorch
- Google Colab
- Roboflow

## Results
The project compares model performance across multiple training epochs and evaluates object detection on unseen images.
## Best Results

| Metric | Value |
|----------|----------|
| Best Epoch | 20 |
| mAP50 | 0.9880 |
| mAP50-95 | 0.9710 |

## Project Structure

- Dataset
- Documentation
- Model
- Detection Results
- Training Results
## Author
Abdullah Mehboob
