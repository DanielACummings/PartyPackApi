import random
import tomllib
from pydantic import BaseModel

class PartyPack(BaseModel):
    joke: str
    life_hack: str
    party_trick: str
    pick_up_line: str

def get_party_pack():
    with open("responses.toml", "rb") as f:
        config = tomllib.load(f)
    return PartyPack(
        joke=random.choice(config["jokes"]),
        life_hack=random.choice(config["life_hacks"]),
        party_trick=random.choice(config["party_tricks"]),
        pick_up_line=random.choice(config["pick_up_lines"]),
    )
