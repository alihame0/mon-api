from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 🔓 Had l'guelb kiy-7el l'bab d la sécurité l'any Frontend (b7al port 8080)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Kiy-khli l'browser d Windows y-fetch-i la data completely bla blocks
    allow_credentials=True,
    allow_methods=["*"],  # Kiy-7el GET, POST, etc.
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur mon API conteneurisée avec Docker ! 🚀", "status": "Online"}