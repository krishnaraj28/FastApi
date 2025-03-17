from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

# Mount static files (CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Jinja2 Template setup
templates = Jinja2Templates(directory="templates")

# Fake database (in-memory dictionary)
items = {}

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "items": items})

@app.post("/items/{item_id}")
def create_item(item_id: int, name: str, price: float):
    items[item_id] = {"name": name, "price": price}
    return {"message": "Item created", "item_id": item_id, "name": name, "price": price}

@app.get("/items")
def get_all_items():
    return items

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return items.get(item_id, {"message": "Item not found"})

@app.put("/items/{item_id}")
def update_item(item_id: int, name: str, price: float):
    if item_id in items:
        items[item_id] = {"name": name, "price": price}
        return {"message": "Item updated", "item_id": item_id, "name": name, "price": price}
    return {"message": "Item not found"}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id in items:
        del items[item_id]
        return {"message": "Item deleted"}
    return {"message": "Item not found"}
