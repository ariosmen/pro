from fastapi import FastAPI
from routes.routes import padron

app = FastAPI()

app.include_router(padron)

