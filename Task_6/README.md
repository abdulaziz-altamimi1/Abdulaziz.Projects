# Computer Vision Projects

This task includes multiple computer vision projects built using deep learning and traditional techniques. Each project solves a different classification or detection task:

1. **Car vs Truck Classification**
2. **Cat vs Dog Classification**
3. **Digit Classification (0–9)**
4. **Object Detection using YOLO**

---

## 1. Car vs Truck Classification

- **Task**: Classify images as either a car or a truck.
- **Model**: CNN
- **Model Architecture**:
  - 6 layers with ReLU activation with MaxPool2D and Dropout
  - Output: Sigmoid layer
- **Dataset**: Kaggle's Car or Truck dataset (10,000 images)
- **Training**:
  - Binary cross-entropy loss
  - Accuracy metric

---

## 2. Cat vs Dog Classification

- **Task**: Binary classification (cat or dog)
- **Model**: CNN
- **Model Architecture**:
  - 6 layers with ReLU activation with MaxPool2D and Dropout
  - Output: Sigmoid layer
- **Dataset**: Kaggle's Cat and Dog dataset (27,500 images)
- **Training**:
  - Binary cross-entropy loss
  - Accuracy metric

---

## 3. Digit Classification (MNIST)

- **Task**: Classify handwritten digits (0–9)
- **Model**: CNN
- **Model Architecture**:
  - 4 layers with ReLU activation with MaxPool2D and Dropout
  - Output: (softmax 10) layer
- **Dataset**: MNIST (70,000 images)
- **Training**:
  - Binary cross-entropy loss
  - Accuracy metric

---

## 4. Object Detection using YOLO

- **Task**: Detect and classify multiple objects in an image
- **Model**: YOLOv8
- **Steps**:
  - Load pre-trained YOLOv8 model
  - Run prediction
  - Draw bounding boxes and labels

---

## Conclusion

Each model demonstrates different applications of deep learning in computer vision:
- Binary image classification
- Multiclass digit classification
- object detection