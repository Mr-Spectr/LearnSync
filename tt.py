from transformers import pipeline

def analyze_sentiment(text):
    sentiment_analyzer = pipeline('sentiment-analysis')
    result = sentiment_analyzer(text)
    return result[0]['label'], result[0]['score']

def main():
    print("Welcome to User-Friendly amAI Sentiment Analyzer!")
    user_input = input("Enter a sentence or phrase: ")

    sentiment_label, sentiment_score = analyze_sentiment(user_input)

    print("\nSentiment Analysis Result:")
    print(f"Sentiment: {sentiment_label}")
    print(f"Confidence Score: {sentiment_score:.2f}")

if __name__ == "__main__":
    main()

