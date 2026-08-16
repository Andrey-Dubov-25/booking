from pydantic import BaseModel


class AskRequest(BaseModel):
    message: str
    passport_received: bool


class AskResponse(BaseModel):
    reply: str
