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
        

def type_like_human(page, text):
    for char in text:
        page.keyboard.type(char)
        time.sleep(random.uniform(0.05, 0.15))

last_comment = None

def get_unique_comment(comments):
    global last_comment

    options = [c for c in comments if c != last_comment]
    comment = random.choice(options)

    last_comment = comment
    return comment

def comment_post(page, comments):
    human_delay()

    # Variantes de selector (Facebook cambia mucho esto)
    comment_box = page.locator(
        "[aria-label*='comentario'], [aria-label*='comment']"
    )

    if comment_box.count() == 0:
        print("No se encontró caja de comentario")
        return

    box = comment_box.first
    
    # Scroll antes de comentar
    page.mouse.wheel(0, random.randint(500, 1200))
    human_delay(3, 7)

    # Click en la caja
    box.click()
    human_delay()

    # Elegir comentario aleatorio
    comment = get_unique_comment(comments)

    print(f"Comentando: {comment}")

    # Escribir como humano
    type_like_human(page, comment)

    human_delay()

    # Enviar comentario
    page.keyboard.press("Enter")

    print("Comentario enviado")