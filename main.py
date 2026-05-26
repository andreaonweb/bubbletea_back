from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.bubbleteas import router as bubbleteas_router

app = FastAPI(title="BubbleTea Store API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(bubbleteas_router)


@app.get("/")
def root():
    return {"message": "BubbleTea Store API 🧋"}