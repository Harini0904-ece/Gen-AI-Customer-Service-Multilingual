from datetime import datetime, timedelta
def get_daily_stats():
    today = datetime.utcnow()
    start = today - timedelta(days=1)
    return conversations.aggregate([
        {"$match": {"created_at": {"$gte": start, "$lt": today}}},
        {"$group": {"_id": "$lang", "total": {"$sum": 1}}}
    ])
