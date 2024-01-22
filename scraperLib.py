from webdriver_manager.chrome import ChromeDriverManager
import selenium
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def scrape_bestbuy_products(product, num):
    # Set line to "headless"
    line = 'm'

    if line == 'headless':
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
    else:
        driver = webdriver.Chrome()

    url = f"https://www.bestbuy.ca/en-ca/search?search={product}"
    driver.get(url)
    time.sleep(2)

    # Scroll down to load more items (adjust the number of scrolls as needed)
    for _ in range(num):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    # Extract product names, image URLs, and prices using Selenium
    name_elements = driver.find_elements(By.CLASS_NAME, 'productItemName_3IZ3c')
    image_elements = driver.find_elements(By.CLASS_NAME, 'productItemImage_1en8J')
    price_elements = driver.find_elements(By.XPATH, '//div[@class=""]')

    product_data = []
    for name_element, image_element, price_element in zip(name_elements[:10], image_elements[:10], price_elements[:10]):
        product_name = name_element.text
        image_url = image_element.get_attribute('src')
        product_price = price_element.text
        product_data.append({'Product Name': product_name, 'Image URL': image_url, 'Price': product_price})

    # Create a DataFrame from the extracted data
    df = pd.DataFrame(product_data)

    # Drop rows with NaN (None) values
    df = df.dropna()

    # Fetch additional data if needed to have a total of 10 items
    while len(df) < 10:
        # Scroll down and extract more data
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        additional_name_elements = driver.find_elements(By.CLASS_NAME, 'productItemName_3IZ3c')
        additional_image_elements = driver.find_elements(By.CLASS_NAME, 'productItemImage_1en8J')
        additional_price_elements = driver.find_elements(By.XPATH, '//div[@class=""]')

        for name_element, image_element, price_element in zip(additional_name_elements, additional_image_elements, additional_price_elements):
            product_name = name_element.text
            image_url = image_element.get_attribute('src')
            product_price = price_element.text
            product_data.append({'Product Name': product_name, 'Image URL': image_url, 'Price': product_price})

        # Update the DataFrame
        df = pd.DataFrame(product_data)
        df = df.dropna()

    # Close the webdriver
    driver.quit()

    return df
