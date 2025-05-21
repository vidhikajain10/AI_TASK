from textblob import TextBlob # type: ignore

# Function to analyze sentiment
def analyze_sentiment(input_text):
    sentiment = TextBlob(input_text).sentiment.polarity
    if sentiment > 0:
        return "positive"
    elif sentiment < 0:
        return "negative"
    else:
        return "neutral"

# Chatbot function
def chatbot():
    print("Hello! I am a simple chatbot. Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ").lower()
        
        # Exit condition
        if user_input == "exit":
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        # Analyze sentiment
        sentiment = analyze_sentiment(user_input)
        
        # Responses based on sentiment
        if sentiment == "positive":
            print("Chatbot: You seem happy! I'm glad to hear that!")
        elif sentiment == "negative":
            print("Chatbot: Oh no! I'm here to help if you want to talk.")
        elif sentiment == "neutral":
            # Regular predefined responses
            if "hello" in user_input or "hi" in user_input:
                print("Chatbot: Hello! How can I help you?")
            elif "how are you" in user_input:
                print("Chatbot: I'm just a program, but I'm functioning perfectly! How about you?")
            elif "name" in user_input:
                print("Chatbot: I am Chatbot 1.0. What's your name?")
            elif "weather" in user_input:
                print("Chatbot: I can't provide live weather updates yet, but it's always sunny in my world!")
            else:
                print("Chatbot: Sorry, I don't understand that. Can you try rephrasing?")

# Run the chatbot
chatbot() 
