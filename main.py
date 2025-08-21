from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import Optional, List

app = FastAPI()

class Film(BaseModel):
    id: Optional[UUID] = None
    title: str
    type: str
    rating: int


films = []

@app.post("/films/", response_model=Film)
def add_film(film: Film):
    film.id = uuid4()

    if film.rating < 0:
        film.rating = 0
    elif film.rating > 10:
        film.rating = 10

    films.append(film)
    return film

@app.get("/films/", response_model=List[Film])
def get_all_films():
    return films

@app.delete("/films/{film_id}")
def delete_film(film_id: UUID):
    for idx, film in enumerate(films):
        if film.id == film_id:
            films.pop(idx)
            return {"title": "{film.title}", "message": "DELETED"}
    
    raise HTTPException(status_code=404, detail="This movie/series could not be found")

@app.put("/films/{film_id}")
def update_film(film_id: UUID, update: Film):
    for idx, film in enumerate(films):
        if film.id == film_id:
            updated_film = film.copy(update=update.dict(exclude_unset=True))
            if updated_film.rating < 0:
                updated_film.rating = 0

            elif updated_film.rating > 10:
                updated_film.rating = 10

            films[idx] = updated_film
            return {"title": "{films[idx].title}", "message": "UPDATED"}

    raise HTTPException(status_code=404, detail="This movie/series could not be found")

@app.get("/films/{film_id}", response_model=Film)
def get_film(film_id: UUID):
    for film in films:
        if film.id == film_id:
            return film
    
    raise HTTPException(status_code=404, detail="This movie/series could not be found")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
