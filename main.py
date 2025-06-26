from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# 🔐 LinkedIn credentials
email = "test@mail.com"
password = "test123"

# 🔧 ChromeDriver path
chrome_driver_path = "C:\\chromedriver\\chromedriver.exe"

# ⚙️ Setup browser options
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")

# 🚀 Launch browser
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

# 🌐 Open LinkedIn login page
driver.get("https://www.linkedin.com/login")
driver.maximize_window()
time.sleep(2)

# 🔑 Login process
try:
    email_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")

    email_input.send_keys(email)
    password_input.send_keys(password)

    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    print("✅ Logged in successfully.")
    time.sleep(5)

    # 👇 Now keep browser open — don't quit
    print("🔁 Browser will stay open. Close manually when done.")
    while True:
        time.sleep(10)  # keeps script running without exiting

except Exception as e:
    print("❌ Error:", e)
