# Natural Language Processing Projects

This task contains projects that demonstrate the application of Natural Language Processing (NLP) using Python and deep learning. Each project focuses on a different NLP task using real datasets and compares traditional machine learning models with deep learning models.

---

## Project 1: Sentiment Analysis

**Dataset:**  
Amazon Fine Food Reviews  
- Original dataset was filtered to remove neutral reviews (score = 3).  
- Reviews with a score > 3 were labeled as **positive** (1), and ≤ 3 as **negative**

**Text Preprocessing:**  
- Lowercasing
- Removing URLs, HTML tags, punctuation, stopwords, and special characters  
- Tokenization and TF-IDF vectorization (for Naive Bayes)  
- Word embeddings and padding (for LSTM)

**Models Used:**
- Naive Bayes (TF-IDF)
- LSTM with Embedding layer

**Evaluation Metrics:**
| Model         | Accuracy | Precision | Recall | F1 Score |
|---------------|----------|-----------|--------|----------|
| Naive Bayes   | 0.84     | 0.84      | 1      | 0.91     |
| LSTM          | 0.93     | 0.94      | 0.97   | 0.96     |

---

## Project 2: Spam Email Detection

**Dataset:**  
Combined dataset of emails labeled as `SPAM` or `HAM`.

**Text Preprocessing:**  
- Lowercasing 
- Removing URLs, HTML tags, punctuation, stopwords  
- Lemmatization  
- Removal of top 10 most common words  
- TF-IDF vectorization and Tokenization

**Models Used:**
- Naive Bayes (TF-IDF)
- Bidirectional LSTM

**Evaluation Metrics:**
| Model         | Accuracy | Precision | Recall | F1 Score |
|---------------|----------|-----------|--------|----------|
| Naive Bayes   | 0.97     | 0.99      | 0.92   | 0.98     |
| LSTM          | 0.98     | 0.99      | 0.98   | 0.98     |

---

## Project 3: Spell Correction

**Dataset:**  
- *Sherlock Holmes* Book Text Data.

**Tool Used:**  
- [Spello], a neural spell corrector for English.

**Text Preprocessing:**  
- Lowercasing  
- Removing punctuation, URLs, stopwords, HTML tags, and special characters

**Model Training:**
- Trained Spello’s `SpellCorrectionModel` using cleaned *Sherlock Holmes* text.

**Sample Output:**
- Input: `Please beleive me` → Output: `Please believe me`  
- Input: `I want to paly mon` → Output: `I want to play money`

---

## Project 4: Next Word Prediction

**Dataset:**  
- *Sherlock Holmes* Book Text Data.

**Text Preprocessing:**  
- Removal of newline and tab characters  
- Tokenization and sequence generation using n-gram approach  
- Padding for uniform sequence lengths

**Sample Output:**
- Input: `sherlock`  
- Output: `sherlock holmes and the man who`

---

## Conclusion

Each NLP project highlighted the importance of preprocessing and model selection. While traditional models like Naive Bayes performed well, deep learning models (LSTM, Bi-LSTM) consistently delivered higher accuracy, particularly for longer and more complex text inputs.