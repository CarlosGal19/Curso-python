from fastapi import FastAPI

# py -m uvicorn main:app --reload

app = FastAPI()

@app.get('/')
def raiz():
    return {"Hello":"World"}

@app.get('/items/{item_id}/{m}')
def read_item(item_id:int, m:str=None):
    return{'item_id':item_id, 'm':m}
