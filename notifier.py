import requests
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_IDS, DEFAULT_CHAT_ID

# ✅ Token del bot
TELEGRAM_BOT_TOKEN = "7865063228:AAF8HkSYc4bzdbNZP_DEiHGyudV9tbC560M"

# ✅ Chats según tipo de torneo
CHAT_IDS = {
    "ATP": "-1002869158222",
    "WTA": "-1002828128315",
    "CH":  "-1002873668801",
    "ITF M": "-1002719350888",   # Masculino
    "ITF F": "-1002603997514",   # Femenino
    "DEFAULT": "1026764890"      # Privado (o grupo general)
}

def get_chat_id(torneo):
    torneo = torneo.upper()
    for key in CHAT_IDS:
        if key in torneo:
            return TELEGRAM_CHAT_IDS[key]
    return DEFAULT_CHAT_ID

def build_message(torneo, jugador1, cuota1, jugador2, cuota2):
    return (
        f"🎾 {torneo}\n"
        f"{jugador1} @{cuota1}\n"
        f"{jugador2} @{cuota2}"
    )

def send_message(torneo, jugador1, cuota1, jugador2, cuota2):
    text = build_message(torneo, jugador1, cuota1, jugador2, cuota2)
    chat_id = get_chat_id(torneo)

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }

    response = requests.post(url, data=payload)
    print("Código de respuesta:", response.status_code)
    print("Respuesta de Telegram:", response.text)

# 💡 Test manual
if __name__ == "__main__":
    send_message("ATP Open", "Carlos Alcaraz", "1.95", "Jannik Sinner", "1.99")
