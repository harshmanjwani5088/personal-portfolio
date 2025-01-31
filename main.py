import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI()

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Serve static files (CSS, images, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/about", response_class=HTMLResponse)
async def read_about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@app.get("/projects", response_class=HTMLResponse)
async def read_projects(request: Request):
    return templates.TemplateResponse("projects.html", {"request": request})

# if __name__ == "__main__":
#     uvicorn.run(app, port=5000)
