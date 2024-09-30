import os
from playwright.sync_api import Playwright, sync_playwright, expect

bing_email = "Your Email"
bing_password = "your password"

print(f"BING_EMAIL: {bing_email}")
print(f"BING_PASSWORD: {bing_password}")

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(channel="msedge", headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    page.goto("https://rewards.bing.com/redeem/")
    page.get_by_role("link", name="Sign in Default profile image").click()

    page.get_by_test_id("i0116").fill(bing_email)
    page.get_by_test_id("i0116").press("Enter")
    page.get_by_test_id("i0118").fill(bing_password)
    page.get_by_test_id("i0118").press("Enter")
    
    #page.get_by_role("link", name="Sign in Default profile image").click()

    page.goto("https://rewards.bing.com/redeem/")
    page.get_by_role("link", name="Points breakdown ").click()

    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="PC search").click()
    page1 = page1_info.value
    
    search_terms = [
        "naruto", "bleach", "one piece", "hunter x hunter", "clannad", "toradora",
        "elfen lied", "bakuman", "steins gate", "anohana", "durarara", "hellsing",
        "trigun", "beck", "air", "k-on", "fairy tail", "kino's journey", "erased",
        "flcl", "gantz", "noragami", "fruits basket", "made in abyss", "soul eater",
        "paranoia agent", "deadman wonderland", "another", "darker than black", "angel beats", "psycho-pass"
    ]
    
    games = [
        "The Legend of Zelda: Breath of the Wild",
        "Red Dead Redemption 2",
        "Minecraft",
        "The Witcher 3: Wild Hunt",
        "Among Us",
        "Fortnite",
        "Animal Crossing: New Horizons",
        "God of War (2018)",
        "Hades",
        "Cyberpunk 2077",
        "Elden Ring",
        "Super Mario Odyssey",
        "Overwatch",
        "Call of Duty: Warzone",
        "Apex Legends",
        "Stardew Valley",
        "Ghost of Tsushima",
        "Hollow Knight",
        "Sekiro: Shadows Die Twice",
        "Genshin Impact"
    ]
    
    for term in search_terms:
        try:
            search_box = page1.get_by_label("Enter your search here -")
            search_box.click()
            search_box.fill(term)
            search_box.press("Enter")
            page1.wait_for_timeout(10000) 
            
            clear_button = page1.locator('button[aria-label="Clear text"]')
            if clear_button.is_visible():
                clear_button.click()
            else:
                search_box.click()  
        except Exception as e:
            print(f"An error occurred while searching for '{term}': {e}")

    context.close()
    browser.close()

if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)
