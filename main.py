import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_price_range(driver):
    wait = WebDriverWait(driver, 10)
    price_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div[2]/div[1]/div[2]")))
    price_range = price_element.text
    return price_range


def save_screenshot(driver, screenshot_name):
    driver.save_screenshot(screenshot_name)


def add_prices_to_json(hotel_name, date, provider, price, screenshot_name):
    data = {
        hotel_name: {
            date: {
                "provider": provider,
                "price": price,
                "screenshot": screenshot_name
            }
        }
    }
    with open("prices.json", "r") as f:
        json_data = json.load(f)
        json_data.update(data)

    with open("prices.json", "w") as f:
        json.dump(json_data, f)


def main():
    hotel_name = "Grosvenor Hotel"
    date = "2023-07-22"
    provider = "TripAdvisor"
    screenshot_name = "screenshot.png"
    driver = webdriver.Firefox()
    driver.get(
        "https://www.tripadvisor.ru/Restaurant_Review-g255103-d2572011-Reviews-Grosvenor_Hotel-Perth_Greater_Perth_Western_Australia.html")
    try:
        price_range = get_price_range(driver)
        save_screenshot(driver, screenshot_name)
        driver.quit()
        add_prices_to_json(hotel_name, date, provider, price_range, screenshot_name)
    except Exception as e:
        print("Помилка: ", str(e))
        driver.quit()



if __name__ == "__main__":
    main()
