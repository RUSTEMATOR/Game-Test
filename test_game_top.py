from playwright.sync_api import Playwright, sync_playwright, expect, Page
import time

game_names = [
    'Wild Spin',
    'Wild Cash',
    'Buffalo Goes Wild',
    'Book Of Demi Gods II - The Golden Era',
    'Burning Classics',
    'Zeus the Thunderer',
    'Pop&Drop'
]


email = "canada@loshara.com"
password = "LOL12lol"

def take_screenshot_and_save(page, game_name):
    screenshot_path = f"Desktop/Game Screenshots_TOP/{game_name}.png"
    page.screenshot(path=screenshot_path)
    print(f"Screenshot for {game_name} saved at {screenshot_path}")
    

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.kingbillycasino.com")
    #page.get_by_role("button", name="Decline").click()
    page.get_by_role("link", name="Log in").click()
    page.get_by_placeholder("Enter your email").click()
    page.get_by_placeholder("Enter your email").fill(email)
    page.get_by_placeholder("Enter your password").click()
    page.get_by_placeholder("Enter your password").fill(password)
    page.get_by_placeholder("Enter your password").press("Enter")
    
    for game_name in game_names:
        # Enter the game name into the search box
        page.get_by_role("link", name="Search").click()
        
        # Click on the game in the search results
        page.get_by_role("textbox", name="Trouvez votre jeu").fill(game_name)
        page.locator("a").filter(has_text=game_name).first.click()
        
        time.sleep(20)
        
        # Take a screenshot and save it
        take_screenshot_and_save(page, game_name)
        page.goto("https://www.kingbillycasino.com")

    # ---------------------
    context.close()
    browser.close()

