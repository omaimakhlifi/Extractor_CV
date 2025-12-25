from typing import Optional
from pydantic import BaseModel


class CvResult(BaseModel):
    
    nom: Optional [str] = None
    prenom: Optional [str] = None
    email: Optional [str] = None
    telephone: Optional [str] = None
    diplome_principal: Optional [str] = None

    