from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def read_root():
    with open('pages/index.html', 'r') as f:
        html_content = f.read()
    return html_content


@app.get("/{page_name}", response_class=HTMLResponse)
def serve_page(page_name: str):
    try:
        with open(f'pages/{page_name}.html', 'r') as f:
            html_content = f.read()
        return html_content
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Page not found")