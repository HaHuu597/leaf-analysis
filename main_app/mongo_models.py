
from django.conf import settings
from pymongo import MongoClient
import certifi

# Kết nối với chứng chỉ CA
client = MongoClient(settings.MONGO_URI, tlsCAFile=certifi.where())

db = client["history"]   # tên DB bạn chọn trong URI
history_col = db["prediction_history"]
