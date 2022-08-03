import os
import uvicorn
from fastapi import FastAPI, Body, HTTPException, status
from fastapi.responses import Response
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List

app = FastAPI()

@app.get("/", response_description="receives pod1 msg",)
async def get_msg(msg: str):
    print(msg)
    return "I got it, roger"