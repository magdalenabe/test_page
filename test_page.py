from selenium import webdriver
import time
import pytest

@pytest.fixture()
def open_close():
    global driver
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()
    print("The test is completed")

# spawdzenie funkcjonalności wyszukiwania wielu przedmiotów u jednegp sprzedawcy
def test_search(open_close):
    driver.get("https://allegro.pl/")
    accept_cookies = driver.find_element_by_xpath("/html/body/div[2]/div[8]/div/div/div/div/div[2]/div[2]/button[1]")
    accept_cookies.click()
    driver.find_element_by_link_text("szukaj wielu").click()
    driver.find_element_by_id("input0").send_keys("mapa")
    driver.find_element_by_id("input1").send_keys("przewodnik turystyczny")
    driver.find_element_by_css_selector("button.m7er_k4").click()
    time.sleep(3)

# sprawdzenie funkcji "nie pamiętma hasła" podczas próby logowania
def test_trylogin(open_close):
    driver.get("https://allegro.pl/")
    accept_cookies = driver.find_element_by_xpath("/html/body/div[2]/div[8]/div/div/div/div/div[2]/div[2]/button[1]")
    accept_cookies.click()
    driver.find_element_by_css_selector(".opbox-btn").click()
    driver.find_element_by_css_selector("a.lc0vi:nth-child(1)").click()
    driver.find_element_by_id("entry-input").send_keys("testing@com.pl")
    time.sleep(3)
  
# wejście na podstronę "https://about.allegro.eu/" 
def test_about(open_close):
    driver.get("https://allegro.pl/")
    accept_cookies = driver.find_element_by_xpath("/html/body/div[2]/div[8]/div/div/div/div/div[2]/div[2]/button[1]")
    accept_cookies.click()
   
    action = webdriver.ActionChains(driver)
    driver.execute_script("window.scrollTo(0, document. body. scrollHeight)") 
    driver.find_element_by_link_text("O nas").click()
    time.sleep(3)

