import random
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Initialize NLTK components
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english')) #Stop words are common words in a language, such as "the", "a", "an", "in", "of", etc.

# Define a list of possible responses
greetings = ["Hello! Welcome to our Customer Interaction Chatbot. How can I assist you today?",
             "Hi there! How can I help you today?",
             "Welcome to our Customer Interaction Chatbot! How may I assist you?"]

customer_support = ["What can I assist you with today?",
                    "How can I help you? Please let me know your query.",
                    "I'm here to assist you. What do you need help with?"]

order_status = ["To check your order status, please provide your order number.",
                "I can help you with your order status. Please provide me with your order number.",
                "Sure, I can assist you with your order status. Please provide your order number."]

payment_issues = ["I apologize for the inconvenience. To resolve payment issues, please contact our customer support at 123-456-7890.",
                  "I'm sorry to hear about the payment issues. Please reach out to our customer support team at 123-456-7890 for assistance.",
                  "To address payment issues, it's best to contact our customer support team directly at 123-456-7890."]

product_information = ["Could you please let me know which product you would like information about?",
                       "I can provide you with product information. Please specify the product you are interested in.",
                       "Sure, I can help you with product information. Please provide the name or description of the product."]

goodbyes = ["Thank you for chatting with me. Have a great day!",
            "If you have any more questions, feel free to ask. Goodbye!",
            "It was a pleasure assisting you. Goodbye and take care!"]

# Define a function to preprocess the user's input
def preprocess_input(input_text):
    # Tokenization refers to the process of breaking a text into smaller units, such as words or sentences.
    words = nltk.word_tokenize(input_text.lower())
    # Lemmatization is the process of reducing words to their base or dictionary form, known as the lemma.
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    return ' '.join(words)

# Define a function to generate a response to the user's input
def generate_response(user_input):
    preprocessed_input = preprocess_input(user_input)
    for keyword_list, response_list in [(["hello", "hi", "hey"], greetings),
                                        (["support", "assist", "help"], customer_support),
                                        (["order", "status"], order_status),
                                        (["payment", "issue"], payment_issues),
                                        (["product", "information"], product_information),
                                        (["bye", "goodbye", "see you"], goodbyes)]:
        if any(keyword in preprocessed_input for keyword in keyword_list):
            return random.choice(response_list)
    return "I'm sorry, I'm not sure how to help with that. Could you please provide more information?"

def run_chatbot():
    print("Welcome to our Customer Interaction Chatbot!")
    print("Type 'exit' at any time to end the chat.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = generate_response(user_input)
        print("Chatbot:", response)
    print("Thank you for chatting with me. Goodbye!")

run_chatbot()