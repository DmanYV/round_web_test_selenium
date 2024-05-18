import pytest
from selenium import webdriver


@pytest.fixture(autouse=True, scope='function')
def driver(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1920,1080')
    # chrome_options.add_argument('--incognito')  # режим инкогнито
    # chrome_options.add_argument('--headless')  # режим без UI
    # chrome_options.add_argument('--ignore-certificate-errors')  # режим игнорирования сертификата
    driver = webdriver.Chrome(options=chrome_options)
    request.cls.driver = driver

    yield driver

    driver.quit()
