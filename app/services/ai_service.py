from groq import Groq

from app.config import GROQ_API_KEY, MODEL
from app.prompts import SYSTEM_PROMPT, CLASSIFIER_PROMPT
from .constants import MAX_TOKEN_CHECKING, MAX_TOKEN_REPLY


client = Groq(api_key=GROQ_API_KEY)


def is_checkin_related(message: str) -> bool:
    completion = client.chat.completions.create(
        model=MODEL,
        max_tokens=MAX_TOKEN_CHECKING,
        messages=[
            {"role": "system", "content": CLASSIFIER_PROMPT},
            {"role": "user", "content": message},
        ],
    )
    answer = (completion.choices[0].message.content or "").strip().lower()
    return answer.startswith("да")


def generate_reply(message: str, passport_received: bool) -> str:
    status_text = "получен" if passport_received else "не получен"
    system = f"{SYSTEM_PROMPT}\nТекущий статус паспорта: {status_text}"

    completion = client.chat.completions.create(
        model=MODEL,
        max_tokens=MAX_TOKEN_REPLY,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": message},
        ],
    )
    return (completion.choices[0].message.content or "").strip()
