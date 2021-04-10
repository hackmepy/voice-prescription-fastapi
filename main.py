from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from fastapi import FastAPI, Query, Path
from ner_model import check_name_entity_recognition, POS
import json 

app = FastAPI()

origins = [
    "http://localhost:3000",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)	



class Payload(BaseModel):
    data: str = ""

@app.post('/data')
async def main(payload: Payload = None):
    print(payload)
    out = await check_name_entity_recognition(payload.data)
    data= {"item" : out }
    data=json.dumps(data)
    data = data.encode("utf-8")
    print(payload)
    return data;

"""
class User(BaseModel):
    Input: str

@app.post('/data')#,response_class=HTMLResponse)
async def main(text: User):
    out = await check_name_entity_recognition(text.Input)
    return out;

"""
