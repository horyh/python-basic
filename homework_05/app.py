from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.routing import APIRouter
from views.views import view_router

app = FastAPI()
app.include_router(view_router, prefix="/api")

templates = Jinja2Templates(directory="templates")

# Regular views
@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse(
      "index.html", {"request": request, "title": "Home"}
    )

@app.get("/about/")
async def about_page(request: Request):
    return templates.TemplateResponse(
      "about.html", {"request": request, "title": "About"})
