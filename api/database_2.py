import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel
# py -m uvicorn main:app --reload

conn = sqlite3.connect('hot100.db')

cursor= conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS ranking (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    artist TEXT NOT NULL,
                    song TEXT NOT NULL,
                    position INTEGER NOT NULL
                )''')

conn.commit()
conn.close()


class Item(BaseModel):
    song: str
    artist: str
    position: int

app = FastAPI()

@app.post("/agregar_elemento/")
async def agregar_elemento(item: Item):
    conn = sqlite3.connect("hot100.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ranking (artist, song, position) VALUES (?, ?, ?)", (item.artist, item.song, item.position))
    conn.commit()
    conn.close()
    return {"mensaje": "Datos agregados exitosamente"}


@app.get("/leer_elementos/")
async def leer_elementos():
    conn = sqlite3.connect("hot100.db")
    cursor = conn.cursor()
    cursor.execute("SELECT position, song, artist FROM ranking")
    resultados = cursor.fetchall()
    conn.close()
    if resultados:
        return [{"position": resultado[0], "song": resultado[1], "artist": resultado[2]} for resultado in resultados]
    else:
        return {"mensaje": "No hay datos en la base de datos"}


@app.get("/leer_elemento/{id}/")
async def leer_elemento(id: int):
    conn = sqlite3.connect("hot100.db")
    cursor = conn.cursor()
    cursor.execute("SELECT position, song, artist FROM ranking WHERE id=?", (id,))
    resultado = cursor.fetchone()
    conn.close()
    if resultado is not None:
        return {"position": resultado[0], "song": resultado[1], "artist": resultado[2]}
    else:
        return {"mensaje": "Datos no encontrados"}


@app.put("/actualizar_elemento/{id}/")
async def actualizar_elemento(id: int, item: Item):
    conn = sqlite3.connect("hot100.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE ranking SET artist=?, song=?, position=? WHERE id=?", (item.artist, item.song, item.position, id))
    conn.commit()
    conn.close()
    return {"mensaje": "Datos actualizados exitosamente"}


@app.delete("/eliminar_elemento/{id}/")
async def eliminar_elemento(id: int):
    conn = sqlite3.connect("hot100.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ranking WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return {"mensaje": "Datos eliminados exitosamente"}

