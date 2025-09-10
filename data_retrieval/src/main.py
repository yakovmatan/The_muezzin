from fastapi import FastAPI
from data_retrieval.src.config import *
from data_retrieval.src.manager import Manager
app = FastAPI()
manager = Manager()


@app.get("/all_podcasts")
def get_all_podcasts():
    try:
        result = manager.get_all_podcasts(INDEX_NAME)
        return result
    except Exception as e:
        return e

