from fastapi import FastAPI, APIRouter
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from party_pack import get_party_pack, PartyPack

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Root route - serves demo UI
@app.get("/")
def read_root():
    return FileResponse("static/index.html")

# API routes grouped with prefix
api_router = APIRouter()

@api_router.get("/party-pack", response_model=PartyPack)
def party_pack_endpoint():
    return get_party_pack()

# Include the API router with /api prefix
app.include_router(api_router, prefix="/api")
