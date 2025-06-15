from playwright.sync_api import sync_playwright
import re

def get_matches():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        print("Abriendo página...")
        try:
            page.goto("https://www.winamax.es/apuestas-deportivas/sports/5", timeout=30000)
            page.wait_for_timeout(3000)

            try:
                page.click("button:has-text('Aceptar todo')")
            except:
                print("No apareció botón de cookies.")

            page.wait_for_timeout(2000)
            content = page.inner_text("body")

            with open("pagina.txt", "w", encoding="utf-8") as f:
                f.write(content)

            browser.close()
        except Exception as e:
            print("❌ Error al abrir la página:", e)
            browser.close()
            return []

    # Detección avanzada
    pattern = re.compile(
        r"(ATP|WTA|CH|ITF)[^\n]{0,40}.*?\n+([A-Z][a-zA-Z .'/\-]+(?:/[A-Z][a-zA-Z .'/\-]+)?)\n+([A-Z][a-zA-Z .'/\-]+(?:/[A-Z][a-zA-Z .'/\-]+)?).*?\n.*?([0-9]{1,2}[.,][0-9]{2})\n.*?([0-9]{1,2}[.,][0-9]{2})",
        re.DOTALL
    )

    matches = []
    for m in re.finditer(pattern, content):
        raw_torneo = m.group(0)

        # Clasifica ITF en masculino o femenino
        if "Femenino" in raw_torneo or "Women" in raw_torneo or "W-" in raw_torneo or "W15" in raw_torneo or "W25" in raw_torneo or "W60" in raw_torneo or "W100" in raw_torneo:
            torneo = "ITF F"
        elif "Masculino" in raw_torneo or "Men" in raw_torneo or "M-" in raw_torneo or "M15" in raw_torneo or "M25" in raw_torneo:
            torneo = "ITF M"
        else:
            #torneo = m.group(0)  # ATP, WTA, CH, ITF (neutral)
            torneo_match = re.search(r"(ATP|WTA|CH|ITF)[^\n]{0,40}", raw_torneo)
            torneo = torneo_match.group(0).strip() if torneo_match else "Unknown"

        jugador1 = m.group(2).strip()
        jugador2 = m.group(3).strip()
        cuota1 = m.group(4).replace(",", ".")
        cuota2 = m.group(5).replace(",", ".")
        matches.append((torneo, jugador1, cuota1, jugador2, cuota2))

    return matches
