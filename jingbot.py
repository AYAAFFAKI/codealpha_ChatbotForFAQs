import nltk
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from string import punctuation

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Predefined FAQ dictionary for Jing Darjeeling Tea
jingbot_faq_data = {
    "What is Jing Darjeeling tea?":
        "Jing Darjeeling tea is a premium black tea grown in the Darjeeling region of India. It is known for its floral aroma and unique, delicate flavor.",
    "What does the number 308 mean?":
        "308 is the product reference number used by the 'Japanese' store to identify this specific item.",
    "Is this tea organic?":
        "Yes, Jing Darjeeling tea bags are made from pure organic tea leaves with no chemicals or artificial additives.",
    "How do I prepare Jing Darjeeling tea?":
        "Place the tea bag in a cup, pour hot water (90-95°C) over it, and let it steep for 3 to 5 minutes depending on your taste preference.",
    "Can I add milk or sugar to it?":
        "You can, but it is traditionally enjoyed plain to appreciate its natural flavor. Add milk or sugar only if you prefer.",
    "What are the ingredients of this tea?":
        "Only pure Darjeeling tea leaves. No added flavors, no chemicals.",
    "What kind of tea bags are used?":
        "The tea bags are plastic-free, eco-friendly, and made from plant-based, biodegradable materials.",
    "What is the shelf life of Jing Darjeeling tea?":
        "Typically 18 to 24 months from the production date. Always check the packaging for the exact date.",
    "How should I store the tea?":
        "Keep the tea in a cool, dry place, away from direct sunlight and moisture. Reseal the pack tightly after opening.",
    "Where can I buy this product?":
        "You can purchase it from the Japanese online store or by visiting one of their physical branches.",
    "Is international shipping available?":
        "Yes, the store offers international delivery. Please check their shipping policy for more details.",
    "Is it available in larger sizes or other packs?":
        "Currently, it is only available in one size. Follow the store for future updates and new pack sizes.",
    "Is the tea strong in flavor?":
        "Darjeeling tea is known for its subtle, refined flavor with floral notes. The strength can be adjusted by steeping time.",
    "What makes Jing different from other Darjeeling teas?":
        "Jing uses carefully selected high-quality leaves, offering a luxurious tea experience with elegant packaging that preserves freshness."
}

# Prepare stop words and lemmatizer
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    tokens = word_tokenize(text)
    lower_tokens = [word.lower() for word in tokens]
    filtered_tokens = [word for word in lower_tokens if word not in stop_words and word not in punctuation]
    lemmatized_tokens = [lemmatizer.lemmatize(word, pos='v') for word in filtered_tokens]
    return lemmatized_tokens

def build_processed_faq(faq_data):
    processed_faq = {}
    for question, answer in faq_data.items():
        processed_question = preprocess_text(question)
        processed_faq[" ".join(processed_question)] = answer
        print('\t.\t', end='')
    return processed_faq

def find_best_answer(user_input_tokens, processed_faq):
    scores = []
    answers = []
    for question_text, answer in processed_faq.items():
        question_tokens = set(preprocess_text(question_text))
        user_tokens = set(user_input_tokens)
        if not question_tokens and not user_tokens:
            similarity = 0
        else:
            similarity = len(user_tokens & question_tokens) / len(user_tokens | question_tokens)
        scores.append(similarity)
        answers.append(answer)
    best_match_index = np.argmax(scores)
    return answers[best_match_index]

if __name__ == '__main__':
    print('Loading JingBot FAQ knowledge base...')
    processed_faq = build_processed_faq(jingbot_faq_data)

    print("\n👋 Welcome to the JingBot Assistant!")
    print("Ask me anything about Jing Darjeeling tea and I'll do my best to help you.")
    print("\n🔍 Note: This assistant matches your question with predefined ones based on keywords.")
    print("💡 For better answers, try to use wording similar to known questions.")
    print("\nTo exit, type '0' at any time.")

    while True:
        user_input = input('\n\tYOU: ')
        if user_input.strip() == '0':
            print("Exiting chat...")
            break
        input_tokens = preprocess_text(user_input)
        bot_reply = find_best_answer(input_tokens, processed_faq)
        print(f'\tJingBot: {bot_reply}')
