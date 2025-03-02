from pydantic import BaseModel

class FIORequest(BaseModel):
    first_name: str
    last_name: str
    middle_name: str