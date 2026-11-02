from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="RS vjezbe 1 - API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class ItemIn(BaseModel):
    name: str


# "baza" u memoriji (nestaje pri restartu servisa)
items = [{"id": 1, "name": "Prvi zapis"}]
next_id = 2


@app.get("/")
def root():
    return {"message": "RS vjezbe 1 - API radi"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/items")
def list_items():
    return items


@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item ne postoji")


@app.post("/items", status_code=201)
def create_item(data: ItemIn):
    global next_id
    item = {"id": next_id, "name": data.name}
    next_id += 1
    items.append(item)
    return item


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            items.remove(item)
            return {"deleted": item_id}
    raise HTTPException(status_code=404, detail="Item ne postoji")
