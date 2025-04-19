from fastapi import FastAPI
from typing import Optional
from router import house
app = FastAPI()

app.include_router(house.router)


@app.get('/home')
def index():
    return {'message':'Hello World !'}

@app.get('/House/{estate}/{id}')
def get_house(id:int,estate:str):
    return {'message':'Found House{id},in Estate{str}'}
