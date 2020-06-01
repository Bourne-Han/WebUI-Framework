from WebUI.PageObject.basic_page.BasicPage import BasicPage
from selenium.webdriver.common.by import By


class LoginPage(BasicPage):
    '''
        登录业务的页面对象类
    '''

    # 指定要使用的浏览器
    browser = 'C'
    # 指定url
    url = 'http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html'
    # 登录账号
    userName = (By.XPATH, '//input[@name="accounts"]')
    # 登录密码
    pwd = (By.XPATH, '//input[@name="pwd"]')
    # 登录按钮
    button = (By.XPATH, '//button[text()="登录"]')

    def __init__(self, browser=None, url=None):
        super().__init__(self.browser, self.url)

    def input_username(self, user):
        '''输入用户名'''
        self.locator(self.userName).send_keys(user)

    def input_pwd(self, pwd):
        '''输入密码'''
        self.locator(self.pwd).send_keys(pwd)

    def click_element(self):
        '''点击登录按钮'''
        self.locator(self.button).click()

    def login(self, user, pwd):
        self.input_username(user)
        self.input_pwd(pwd)
        self.click_element()


if __name__ == '__main__':
    a = LoginPage()
    a.login('admin123', 'admin123')
