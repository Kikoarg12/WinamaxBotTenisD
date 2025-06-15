import json
from scraper import get_matches
from notifier import send_message

def load_old_matches():
    try:
        with open("history.json", "r", encoding="utf-8") as f:
            return set(tuple(match) for match in json.load(f))
    except:
        return set()

def save_matches(matches):
    with open("history.json", "w", encoding="utf-8") as f:
        json.dump([list(m) for m in matches], f)

def main():
    current_matches = set(get_matches())
    print("Partidos actuales:", current_matches)

    old_matches = load_old_matches()
    print("Historial previo:", old_matches)

    new_matches = current_matches - old_matches
    print("Nuevos partidos:", new_matches)

    if new_matches:
        for torneo, jug1, cuota1, jug2, cuota2 in new_matches:
            send_message(torneo, jug1, cuota1, jug2, cuota2)
        save_matches(current_matches)
    else:
        print("No hay partidos nuevos.")

if __name__ == "__main__":
    main()
