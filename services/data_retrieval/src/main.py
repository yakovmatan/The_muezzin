from fastapi import FastAPI
from services.data_retrieval.src.config import *
from services.data_retrieval.src.manager import Manager
app = FastAPI()
manager = Manager()


@app.get("/all_podcasts")
def get_all_podcasts():
    try:
        result = manager.get_all_podcasts(INDEX_NAME)
        return result
    except Exception as e:
        return e

@app.get("/is_bds")
def get_is_bds():
    try:
        result = manager.get_is_bds_podcasts(INDEX_NAME)
        return result
    except Exception as e:
        return e

