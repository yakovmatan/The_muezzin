import os

ES_HOST = os.getenv('ES_HOST', 'localhost')
KAFKA_BROKER = os.getenv('KAFKA_BROKER', 'localhost:9092')
MONGO_USER = os.getenv("MONGODB_USER", "admin")
MONGO_PASSWORD = os.getenv("MONGODB_PASSWORD", "yakov")
MONGO_DB = os.getenv("MONGODB_DATABASE", "the_muezzin")
MONGO_HOST = os.getenv("MONGODB_HOST", "localhost")
MONGO_PORT = os.getenv("MONGODB_PORT", "27017")
AUTH_DB = os.getenv("MONGODB_AUTH_DB", "admin")