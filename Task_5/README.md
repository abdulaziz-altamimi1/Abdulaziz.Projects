# Deep Learning – Building and Evaluating Neural Networks

This task includes five deep learning projects using Keras and TensorFlow for both classification and regression tasks. Each project tackles a real-world dataset and aims to build a neural network through preprocessing, training, and evaluation.

---

## 1. Hotel Booking Cancellation Prediction

- **Problem**: Binary classification to predict if a hotel booking will be canceled or not.
- **Model Architecture**:
  - 3 layers with ReLU activation with Dropout and Batch Normalization
  - Output: Sigmoid layer
- **Loss Function**: Binary Crossentropy
- **Performance**:
  - Accuracy: 0.8545
  - Precision: 0.8156
  - Recall: 0.6068
  - F1 Score: 0.6959

---

## 2. Heart Disease Prediction

- **Problem**: Classify whether a person has heart disease or not.
- **Model Architecture**:
  - 4 layers with ReLU activation with Dropout and Batch Normalization
  - Output: Sigmoid layer
- **Loss Function**: Binary Crossentropy
- **Performance**:
  - Accuracy: 0.8704
  - Precision: 0.2986
  - Recall: 0.3221
  - F1 Score: 0.3099

---

## 3. Flight Satisfaction Classification

- **Problem**: Predict customer satisfaction or not.
- **Model Architecture**:
  - Input: 17 features (e.g. food, entertainment, comfort)
  - 4 layers with ReLU activation with Dropout and Batch Normalization
  - Output: Sigmoid
- **Loss Function**: Binary Crossentropy
- **Performance**:
  - Accuracy: 0.9632
  - Precision: 0.9696
  - Recall: 0.9447
  - F1 Score: 0.9570

---

## 4. California Housing Price Prediction

- **Problem**: Regression to predict median house values.
- **Model Architecture**:
  - 4 layers with ReLU activation with Dropout and Batch Normalization
  - Output: 1 neuron (Linear)
- **Loss Function**: MSE
- **Target Transformation**: Used Log-transform for smoothing
- **Performance**:
  - MAE: 0.18
  - RMSE: 0.26
  - R² Score: 0.7991

---

## 5. Walmart Weekly Sales Forecast

- **Problem**: Regression to predict weekly sales.
- **Model Architecture**:
  - 4 layers with ReLU activation with Dropout and Batch Normalization
  - Output: 1 neuron (Linear)
- **Loss Function**: MSE
- **Target Transformation**: Used Log-transform for smoothing
- **Performance**:
  - MAE: 0.53
  - RMSE: 0.82
  - R² Score: 0.8204

---

## Training Setup
- 70% train, 30% test
- Validation Split: 20%
- Optimizer: Adam
- Epochs: Up to 100 with EarlyStopping
- Evaluation Metrics:
  - Classification: Accuracy, Precision, Recall, F1 Score
  - Regression: MAE, RMSE, R²