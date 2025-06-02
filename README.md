# JingBot - FAQ Chat Assistant for Jing Darjeeling Tea 🍵

**JingBot** is a lightweight chatbot that answers frequently asked questions about **Jing Darjeeling tea**. It uses basic Natural Language Processing (NLP) with `NLTK` and `NumPy` to understand user queries and return the most relevant response from a predefined set.

---

## 🚀 Features

- ✅ Handles 14+ common questions about Jing Darjeeling tea
- 🧠 Accepts questions phrased differently from the original ones
- 🌿 Informative responses based on a handcrafted FAQ database
- 📦 Uses Python with `NLTK` for preprocessing and `NumPy` for similarity matching

---

## 📦 Requirements

- Python 3.x
- `nltk`
- `numpy`

Install required packages with:

```bash
pip install nltk numpy
````

---

## 🛠 How It Works

1. **Text Preprocessing**

   * Tokenizes input
   * Converts to lowercase
   * Removes stopwords and punctuation
   * Applies lemmatization to standardize words

2. **Similarity Matching**

   * Uses Jaccard similarity to compare the user's input with each known question
   * Returns the most relevant answer

3. **Command-line Interface**

   * Interactive and text-based
   * Type `0` to exit anytime

---

## 🧪 Example Interaction

```
👋 Welcome to the JingBot Assistant!
Ask me anything about Jing Darjeeling tea and I'll do my best to help you.

YOU: Is this tea organic?
JingBot: Yes, Jing Darjeeling tea bags are made from pure organic tea leaves with no chemicals or artificial additives.
```

---

## 📌 Important Notes

> 🔍 This chatbot matches your input to a predefined FAQ using keyword similarity.
> 💡 For more accurate answers, use wording close to the original FAQ entries.
> ⚠️ It doesn't handle multi-turn conversations or deep reasoning — it's a single-turn assistant.

---

## 📁 File Structure

```
jingbot/
│
├── jingbot.py        # Main chatbot script
├── README.md         # Project description and usage guide
```

---

## 📚 Built With

* [NLTK](https://www.nltk.org/) — Natural Language Toolkit for text processing
* [NumPy](https://numpy.org/) — Numerical library used for similarity scoring

---

## 📄 License

This project is licensed under the MIT License — feel free to use and modify.

---

## 👤 Author

AFFAKI AYA

```

---

Would you like me to generate the Markdown file so you can download it? Or include your actual name and GitHub link?
```
