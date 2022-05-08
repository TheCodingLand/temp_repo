from os import listdir
from fastapi import APIRouter, Depends, HTTPException

from typing import List
from pydantic import BaseModel, Field
from fastapi import File, UploadFile, Form

class AiModelTraining(BaseModel):
    dataset_name: str

class Attachment(BaseModel):

    file_name = str 
    file_path :str
    mimetype : str
    inline: bool
    content : bytes
 

class ClassificationInput(BaseModel):
    model_name: str

    @classmethod
    def as_form(
            cls,
            any_param: str = Form(...),
            any_other_param: int = Form(1)
        ) -> "ClassificationInput":
            return cls(any_param=any_param, any_other_param=any_other_param)

    

class Classification(BaseModel):
    predicted_class: str = Field(...)
    probability: float


class ClassifiedAttachment(BaseModel):
    attachment: Attachment
    classifications: List[Classification]
import requests



ai_router = APIRouter(prefix='/ai')

@ai_router.get("/doc_classifier/models/", response_model=List[str])
async def models():
    res = requests.get("http://document_classifer/list_models/")
    models : List[str] = res.json()
    return models


@ai_router.post("/doc_classifier/predict/", response_model=List[Classification])
async def predict(myfile: UploadFile = File(...), document: ClassificationInput = Depends()):
    res = requests.post("http://document_classifer/list_models/", )
    prediction = res.json()
    #prediction = run_prediction(document.model_name, await myfile.read())
    return prediction