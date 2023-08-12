from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

# py -m uvicorn main:app --reload (poder consultar en el host local)

class Libro(BaseModel):
    titulo:str
    autor:str
    paginas:int
    editorial: Optional[str]

app = FastAPI()

@app.get('/')
def raiz():
    return {"Hello":"World"}

@app.get('/items/{item_id}/{m}')
def read_items(item_id:int, m:str=None):
    return{'item id':item_id, 'm':m}

@app.get('/libro/{id}')
def regresar_id(id:int):
    return{'data ':id}

@app.post('/libros/')
async def insertar_libros(libro:Libro):
    return{'Message ': f'Libro: {libro.titulo} insertado correctamente'}
