# 📩 SMS Spam Classifier

A simple **Streamlit-based SMS Spam Classifier** that identifies spam messages using a spam-specific vocabulary built with `CountVectorizer` and a custom word-matching threshold.

The application analyzes the words in an SMS and compares them against a vocabulary learned from spam messages to determine whether the message is Spam or Ham (Not Spam).

## ⚠️ Important Notice — Current Detection Limitations

**This model currently focuses ONLY on the following types of spam messages:**

- Fake retailer rewards and promotional offers.
- Fake gift card rewards and giveaways.
- Suspicious discount coupons and shopping-related offers.

**Please Note:**
- This is not a general-purpose SMS spam detection system.
- Messages belonging to other spam categories, such as banking scams, phishing links, lottery scams, job fraud, or other fraudulent messages, may not be detected correctly.
- A message classified as Ham is not guaranteed to be safe.
- Detection performance depends on the vocabulary and matching threshold used by the model.

Support for additional spam categories will be introduced in future updates.

## ✨ Features

- Simple and user-friendly Streamlit interface.
- SMS message input and instant prediction.
- Spam detection using a custom word-matching approach.
- Spam-specific vocabulary generated using CountVectorizer.
- Customizable word-matching threshold.
- Clear Spam and Ham prediction results.

## ⚙️ How It Works

The model follows a simple word-matching approach:

1. **SMS Input:** The user enters a message into the application.
2. **Word Splitting:** The input message is split into individual words.
3. **Vocabulary Matching:** Each word is checked against the spam-specific vocabulary extracted using `CountVectorizer`.
4. **Match Counting:** The application counts how many words match the vocabulary.
5. **Prediction:** A custom threshold of 5 matching words is used to determine the result.

### Classification Rule

| Matching Words | Prediction |
|---|---|
| 5 or more | Spam |
| Fewer than 5 | Ham |

**Note:** This is a custom rule-based detection approach, not a conventional machine learning classification model.

## 🛠️ Technology Stack

- **Python** — Core programming language.
- **Streamlit** — Web application interface.
- **Pandas** — Data handling.
- **Scikit-learn** — CountVectorizer for vocabulary extraction.
- **Pickle** — Saving and loading the trained vocabulary object.

## 📂 Project Structure

```text
sms-spam-classifier/
│
├── app.py
├── vectorizer.pkl
├── requirements.txt
├── spam.csv
├── spam-email-classifier.ipynb
└── README.md
```

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/princerawat603340-hue/sms-spam-detector
```

### 2. Navigate to the Project Directory

```bash
cd sms-spam-classifier
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

## 📦 Dependencies

```text
streamlit==1.51.0
pandas==2.3.3
scikit-learn==1.9.0
```

## 🔮 Future Improvements

The project will be improved gradually with the following features:

- Support for additional spam categories.
- Improved vocabulary and detection accuracy.
- Better handling of different message formats.
- More robust text preprocessing.
- Advanced machine learning-based classification.
- Improved user interface and prediction insights.

## 👨‍💻 Project Status

**Currently Functional — Initial Version**

This project is an initial implementation focused on fake retailer rewards, gift cards, and coupon-related spam messages. More spam categories and detection improvements are planned for future releases.

---

**Disclaimer:** This application is intended for educational and demonstration purposes. Do not rely on its predictions as the sole method of determining whether an SMS is safe or fraudulent.


## 🌐 Live Demo

Try the SMS Spam Classifier here:

### 🚀 [Open SMS Spam Classifier](https://sms-spam-detector-z3vfqjlqklutgapzh8wrtv.streamlit.app/)

**Note:** This is an online demo. The application currently focuses only on fake retailer rewards, gift cards, and coupon-related spam messages. Please read the detection limitations before using it.
