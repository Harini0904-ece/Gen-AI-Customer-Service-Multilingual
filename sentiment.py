import openai
from langdetect import detect
from textblob import TextBlob  # Lightweight for basic sentiment

def process_user_message(text, conversation_id):
    user_lang = detect(text)
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": text}]
    )
    answer = response['choices'][0]['message']['content']

    sentiment = TextBlob(text).sentiment.polarity
    # Save msg, lang, sentiment, answer, context to MongoDB here

    return {'answer': answer, 'sentiment': sentiment, 'lang': user_lang}
