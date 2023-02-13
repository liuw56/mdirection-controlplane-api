from ast import List
from enum import Enum
from pydantic import BaseModel
class ExpressSystem(BaseModel):
    BACTERIA="Bacteria/Bactéries"
    YEAST="Yeast/Levure"
    BACULOVIRUS_INSECTCELL="Baculovirus/Insect Cell/Baculovirus/Cellule d'insecte"
    MAMMALIAN_CELL="Mammalian Cell / Cellule de mammifère"

class StartFrom(BaseModel):
    GENE_SYNTHESIS="Gene Synthesis"
    SUBCLONING_WITH_YOUR_CDNA="Subcloning with your cDNA"
    SUPPLIED_EXPRESSION_READY="Your supplied expression ready vectorher / Votre vecteur d'expression fourni prêt à l'emploi"

class CustomizationItem(BaseModel):
    proteinName: str
    expressSystem: list
    genBankID:str
    startFrom: str
    comments: str

class CustomizationRequest(BaseModel):
    items: list
    fullName: str
    email: str
    message: str
