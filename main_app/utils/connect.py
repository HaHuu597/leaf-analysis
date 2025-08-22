# main_app/utils/connect.py
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# MongoDB Atlas URI
# Thay <username>, <password>, <cluster-url> cho đúng
uri = "mongodb+srv://hahuu5972:Qb8sy8V0SPrBdMuu@huuai.plp6z8s.mongodb.net/?retryWrites=true&w=majority&appName=HuuAI"

# Tạo kết nối tới Mongo
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Test ping để kiểm tra kết nối thành công
    client.admin.command('ping')
    print("✅ Kết nối MongoDB thành công!")
except Exception as e:
    print("❌ Kết nối MongoDB thất bại:", e)
