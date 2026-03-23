import json
from bot.browser import create_browser
from bot.auth import load_cookies, save_cookies, login
from bot.actions import like_post, comment_post, human_delay
import config

def main():
    with open("account.json") as f:
        account = json.load(f)

    p, browser, context, page = create_browser(config.HEADLESS)

    # Intentar usar cookies
    has_session = load_cookies(context)

    page.goto("https://www.facebook.com")

    if not has_session:
        print("No hay sesión, haciendo login...")
        login(page, account)
        save_cookies(context)
    else:
        print("Sesión cargada desde cookies")

    # 🔥 LOOP MULTI-POST
    for i, post_url in enumerate(config.POSTS):
        print(f"\n--- Procesando post {i+1} ---")

        try:
            like_post(page, post_url)
            human_delay(3, 8)

            comment_post(page, config.COMMENTS)
            human_delay(10, 25)

        except Exception as e:
            print(f"Error en post: {e}")

    print("\n✅ Todos los posts procesados")

    input("Presiona ENTER para cerrar...")

    browser.close()
    p.stop()

if __name__ == "__main__":
    main()