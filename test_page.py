from selenium import webdriver
import pytest

@pytest.fixture()
def test_browser():
    global driver
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()
    print("Test zakończony")

def test_search(test_browser):
    driver.get("https://allegro.pl/")
    accept_cookies = driver.find_element_by_xpath("/html/body/div[2]/div[8]/div/div/div/div/div[2]/div[2]/button[1]")
    accept_cookies.click()
    driver.find_element_by_link_text("szukaj wielu").click()
    driver.find_element_by_id("input0").send_keys("mapa")
    driver.find_element_by_id("input1").send_keys("przewodnik turystyczny")
    driver.find_element_by_css_selector("button.m7er_k4").click()


# def test_done():
#     driver.close()
#     driver.quit()
#     print("Test zakończony")