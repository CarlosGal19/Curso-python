from fastapi import FastAPI

# py -m uvicorn main:app --reload (poder consultar en el host local)

app = FastAPI()

@app.get('/')
def raiz():
    return {"Hello":"World"}

@app.get('/items/{item_id}/{m}')
def read_items(item_id:int, m:str=None):
    return{'item id':item_id, 'm':m}
