from playwright.sync_api import sync_playwright

def create_browser(headless=False):
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=headless)
    context = context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36",
        viewport={"width": 1280, "height": 720}
    )
    page = context.new_page()
    return p, browser, context, page