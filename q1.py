from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import sys

def get_exchange_rate(date, currency_code):

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    try:
        driver.get("https://www.boc.cn/sourcedb/whpj/")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "pjname"))
        )

        date_input = driver.find_element(By.NAME, "erectDate")
        date_input.clear()
        date_input.send_keys(date)

        currency_input = driver.find_element(By.NAME, "pjname")
        currency_input.send_keys(currency_code)

        search_button = driver.find_element(By.CLASS_NAME, "submit")
        search_button.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//table[@class='BOC_main publish']"))
        )

        rate = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//table[@class='BOC_main publish']/tbody/tr[2]/td[7]"))
        ).text
        
        with open("result.txt", "w") as file:
            file.write(rate)

        print(f"日期：{date}, 货币代号：{currency_code}, 现汇卖出价：{rate}")

    except Exception as e:
        print(f"发生错误：{e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("使用方式：python3 yourcode.py 日期 货币代号")
    else:
        date = sys.argv[1]
        currency_code = sys.argv[2]
        get_exchange_rate(date, currency_code)
