import unittest
from WebUI.keywordsDriver.keywords import KeyWords
from selenium.webdriver.common.by import By


class Run(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_case1(self):
        s = KeyWords('c', 'http://39.98.138.157/shopxo/')
        s.click_element(By.XPATH, '/html/body/div[2]/div/ul[1]/div/div/a[1]')
        s.input_text(By.XPATH, "//input[@name='accounts']", text='admin123')
        s.input_text(By.XPATH, "//input[@name='pwd']", text='admin123')
        s.click_element(By.XPATH, "//button[text()='登录']")
        s.show_display(10, 0.5, By.XPATH, "//em[text()='admin123，欢迎来到']")
        s.mouse_over(By.XPATH, "//a[text()='数码办公']")
        s.click_element(By.XPATH, "//span[text()='手机']")
        s.click_element(By.XPATH, "//p[contains(text(),'苹果')]")
        s.swtich_handle()
        s.show_display(10, 0.5, By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[1]/h1')
        s.click_element(By.XPATH, '//li[@data-value="套餐一"]')
        s.click_element(By.XPATH, '//li[@data-value="金色"]')
        s.click_element(By.XPATH, '//li[@data-value="128G"]')
        s.clear(By.XPATH, "//input[@id='text_box']")
        s.input_text(By.XPATH, "//input[@id='text_box']", text=10)
        s.click_element(By.XPATH, '//button[@title="加入购物车"]')
        s.click_element(By.XPATH, '//span[text()="购物车"]')
        s.show_display(10, 0.5, By.XPATH, '//a[contains(text(),"苹果")]')
        s.quit()

    def test_case2(self):
        a = KeyWords('c', 'http://www.baidu.com')
        a.input_text(By.ID, 'kw', text='测码学院')
        a.click_element(By.ID, 'su')
        a.click_element(By.XPATH, '//*[@id="1"]/h3/a')
        a.swtich_handle()
        a.click_element(By.LINK_TEXT,'登录')
        a.click_element(By.XPATH,'/html/body/div[4]/div/div[2]/div[2]/a[1]')
        a.switch_frame(By.NAME, 'login_frame_qq')
        a.show_display(10, 0.5, By.LINK_TEXT, '帐号密码登录')
        a.click_element(By.LINK_TEXT, '帐号密码登录')
        a.input_text(By.XPATH, '//*[@id="u"]', text='2728074350')
        a.input_text(By.XPATH, '//*[@id="p"]', text='yuansir6638380')
        a.click_element(By.XPATH, '//*[@id="login_button"]')
        a.close_frame()
        a.quit()


if __name__ == '__main__':
    unittest.main()
