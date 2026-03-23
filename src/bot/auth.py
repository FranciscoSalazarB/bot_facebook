import json
import os

COOKIES_PATH = "storage/cookies.json"

def load_cookies(context):
    if os.path.exists(COOKIES_PATH):
        with open(COOKIES_PATH, "r") as f:
            cookies = json.load(f)
            context.add_cookies(cookies)
        return True
    return False

def save_cookies(context):
    cookies = context.cookies()
    with open(COOKIES_PATH, "w") as f:
        json.dump(cookies, f)

def login(page, account):
    page.goto("https://www.facebook.com")

    page.fill("input[name='email']", account["email"])
    page.fill("input[name='pass']", account["password"])

    try:
        page.click("button[name='login']", timeout=5000)
    except:
        print("No se pudo hacer click en login (probablemente ya cambió la página)")

    print("🧠 Completa el captcha / verificación manualmente...")

    # Tiempo para intervención humana
    page.wait_for_timeout(120000)

    print("Login posiblemente completado")