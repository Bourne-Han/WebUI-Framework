from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


class KeyWords:
    '''
    关键字驱动，实现web自动化
    '''

    def __init__(self, browser, url):
        self.OpenBrowser(browser)
        self.driver.implicitly_wait(10)
        self.AppointUrl(url)

    def OpenBrowser(self, browser):
        '''打开指定浏览器'''
        if browser == 'ff':
            self.driver = webdriver.Firefox()
        elif browser == 'ie':
            self.driver = webdriver.Ie()
        elif browser == 'c':
            self.driver = webdriver.Chrome()

    def AppointUrl(self, url):
        '''指定url并窗体最大化'''
        self.driver.get(url)
        self.driver.maximize_window()

    def SearchElement(self, *tuple):
        '''获取指定元素'''
        self.driver.find_element(*tuple)

    def click_element(self, *tuple):
        '''点击'''
        self.driver.find_element(*tuple).click()

    def input_text(self, *tuple, text):
        '''输入'''
        self.driver.find_element(*tuple).send_keys(text)

    def clear(self, *tuple):
        '''清除input标签中的值'''
        self.driver.find_element(*tuple).clear()

    def mouse_over(self, *tuple):
        '''鼠标悬浮'''
        ActionChains(self.driver).move_to_element(self.driver.find_element(*tuple)).perform()

    def show_display(self, timeout, poll_frequency, *tuple):
        '''显示等待'''
        WebDriverWait(self.driver, timeout, poll_frequency).until(lambda el: self.driver.find_element(*tuple))

    def swtich_handle(self, c=None):
        '''切换句柄'''
        handles = self.driver.window_handles
        # 是否关闭当前句柄
        if c == None:
            self.driver.close()
        self.driver.switch_to.window(handles[1])

    def switch_frame(self, *tuple):
        '''切换到iframe窗体'''
        self.driver.switch_to.frame(self.driver.find_element(*tuple))

    def close_frame(self):
        '''退出ifrme窗体'''
        self.driver.switch_to.default_content()

    def drop_down_box(self, *tuple, index=None, value=None, text=None):
        '''下拉框选择'''
        if index != None:
            Select(self.SearchElement(*tuple)).select_by_index(index)
        elif value != None:
            Select(self.SearchElement(*tuple)).select_by_value(value)
        elif text != None:
            Select(self.SearchElement(*tuple)).select_by_visible_text(text)

    def quit(self):
        '''关闭浏览器，释放资源'''
        self.driver.quit()


if __name__ == '__main__':
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
