from fastapi import FastAPI
from scraper import get_current_rates

app = FastAPI()

@app.get("/get_rates")
def get_rates():
    try:
        rates = get_current_rates()
        return {'data': rates}

    except Exception as e:
        return {'msg': str(e)}
    
    