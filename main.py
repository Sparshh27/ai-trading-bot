from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from bot import predict_price

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/predict", response_class=HTMLResponse)
async def get_prediction(request: Request, symbol: str):
    try:
        price = predict_price(symbol)
        return templates.TemplateResponse("index.html", {
            "request": request,
            "symbol": symbol.upper(),
            "price": price
        })
    except Exception as e:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "symbol": symbol.upper(),
            "price": f"Error: {str(e)}"
        })
