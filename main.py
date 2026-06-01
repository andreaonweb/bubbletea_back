from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.routes.bubbleteas import router as bubbleteas_router
from app.auth import verify_token 

app = FastAPI(title="BubbleTea Store API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(bubbleteas_router, dependencies=[Depends(verify_token)])

@app.get("/")
def root():
    return {"message": "BubbleTea Store API 🧋"}