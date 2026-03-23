import random
import time

def human_delay(a=2, b=5):
    time.sleep(random.uniform(a, b))

def like_post(page, url):
    page.goto(url)

    human_delay()

    # Scroll para parecer humano
    page.mouse.wheel(0, random.randint(300, 1000))
    human_delay()

    # Selector (puede cambiar con el tiempo)
    like_button = page.locator("[aria-label*='Me gusta'], [aria-label*='Like']")

    if like_button.count() > 0:
        if "Ya no me gusta" in like_button.get_attribute("aria-label"):
            print("Ya tenía like")
        else:
            like_button.click()
    else:
        print("No se encontró el botón de like")