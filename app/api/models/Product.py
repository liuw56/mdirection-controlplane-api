from pydantic import BaseModel

class Product(BaseModel):
    ID: str
    categories: str
    description: str
    source: str
    sequence: str
    enSpecies: str
    tags: str
    bioactivity: str
    genID: str
    swiss_pot: str
    synonyms: str
    aa_sequence: str
    purity: str
    endotoxin: str
    formulation: str
    reconsitiution: str
    storage: str
    background: str
    molecular_weight: str