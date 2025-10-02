from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["customer_service"]
conversations = db["conversations"]

def save_message(conversation_id, user_input, answer, lang, sentiment):
    conversations.update_one(
        {'_id': conversation_id},
        {'$push': {'messages': {
            'user': user_input, 'bot': answer,
            'lang': lang, 'sentiment': sentiment
        }}},
        upsert=True
    )

# For handoff, pass the full conversation record to the human agent UI
