# Machine Learning – Building and Evaluating Prediction Models

This task involves data preprocessing steps, model training, evaluation, and visualizations for both regression and classification tasks using multiple datasets.

---

## Project Overview

This task focuses on two types of supervised learning:

1. **Regression**
   - Predict continuous outcomes such as home prices and weekly sales.  
   - Models: Linear Regression, Random Forest Regressor.

2. **Classification**
   - Predict categorical outcomes such as booking cancellations, presence of disease, and passenger satisfaction.  
   - Models: Logistic Regression, Random Forest Classifier.

Each workflow covers:
- Data cleaning
- Feature encoding
- Train/test split
- Model training  
- Performance evaluation
- Comparative visualizations

---

## Datasets

1. **California Housing**  
   - **Goal**: Predict `median_house_value` using features like median income, house age, and population.  

2. **Walmart Weekly Sales**  
   - **Goal**: Predict `Weekly_Sales` for Walmart stores based on store information, CPI, unemployment, and holidays.  

3. **Hotel Booking Cancellations**  
   - **Goal**: Classify whether a booking will be **canceled** or **not** based on guest, booking, and hotel features.  

4. **Heart Disease**  
   - **Goal**: Classify the presence of heart disease using clinical variables.  

5. **Flight Satisfaction**  
   - **Goal**: Classify passenger **satisfaction** based on flight and service attributes.  

---

## Model Evaluation Metrics

### Regression Metrics
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

### Classification Metrics
- Accuracy
- Precision
- Recall
- F1‑score
- Confusion Matrix

---

## Model Results

### Regression Results

#### California Housing

**Linear Regression:**
- MAE: 51078.007
- MSE: 4854757886.131
- RMSE: 69676.093
- R²: 0.63

**Random Forest Regressor:**
- MAE: 32343.659
- MSE: 2510603342.637
- RMSE: 50105.921
- R²: 0.809

#### Walmart Weekly Sales

**Linear Regression:**
- MAE: 14581.109
- MSE: 470806624.287
- RMSE: 21698.079
- R²: 0.085

**Random Forest Regressor:**
- MAE: 1734.483
- MSE: 23164895.792
- RMSE: 4812.992
- R²: 0.955

---

### Classification Results

#### Hotel Bookings

**Logistic Regression 1:**
- Accuracy Score: 0.988
- Precission_score: 1.0
- Recall score: 0.956
- F1-score: 0.977

**Random Forest Classifier 1:**
- Accuracy Score: 1.0
- Precission_score: 1.0
- Recall score: 1.0
- F1-score: 1.0

**Logistic Regression 2:**
- Accuracy Score: 0.782
- Precission_score: 0.675
- Recall score: 0.39
- F1-score: 0.494

**Random Forest Classifier 2:**
- Accuracy Score: 0.874
- Precission_score: 0.821
- Recall score: 0.69
- F1-score: 0.75

#### Heart Disease

**Logistic Regression:**
- Accuracy Score: 0.91
- Precission_score: 0.499
- Recall score: 0.089
- F1-score: 0.15

**Random Forest Classifier:**
- Accuracy Score: 0.9
- Precission_score: 0.33
- Recall score: 0.114
- F1-score: 0.17

#### Flight Satisfaction

**Logistic Regression:**
- Accuracy Score: 0.866
- Precission_score: 0.852
- Recall score: 0.835
- F1-score: 0.843

**Random Forest Classifier:**
- Accuracy Score: 0.962
- Precission_score: 0.972
- Recall score: 0.94
- F1-score: 0.956
