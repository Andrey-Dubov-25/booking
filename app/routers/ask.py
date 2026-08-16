from fastapi import APIRouter, HTTPException, status

from app.schemas import AskRequest, AskResponse
from app.services.ai_service import is_checkin_related, generate_reply

router = APIRouter()


@router.post("/api/ask", response_model=AskResponse)
def ask(req: AskRequest):
    if not is_checkin_related(req.message):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail="Сообщение не относится к теме заселения",
        )

    reply_text = generate_reply(req.message, req.passport_received)
    return AskResponse(reply=reply_text)