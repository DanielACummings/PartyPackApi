from fastapi import FastAPI
from party_pack import get_party_pack, PartyPack

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Future, simple UI"}

@app.get("/party-pack", response_model=PartyPack)
def party_pack_endpoint():
    return get_party_pack()
