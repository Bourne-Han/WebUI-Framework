from selenium import webdriver


class BasicPage:
    '''
        提供功能测试的基础方法，初始化，释放资源...
    '''

    def __init__(self, browser, url):
        self.driver = self.open_browser(browser)
        self.driver.implicitly_wait(10)
        self.open_url(url)
        self.driver.maximize_window()

    def open_browser(self, browser):
        '''打开指定浏览器'''
        if browser == 'C':
            driver = webdriver.Chrome()
            return driver
        elif browser == 'F':
            driver = webdriver.Firefox()
            return driver
        elif browser == 'I':
            driver = webdriver.Ie()
            return driver

    def open_url(self, url):
        '''指定将要打开网站的url'''
        self.driver.get(url)

    def locator(self, args):
        '''定位元素'''
        el = self.driver.find_element(*args)
        return el

    def quit(self):
        '''关闭浏览器，释放资源'''
        self.driver.quit()


if __name__ == '__main__':
    s = BasicPage('C', 'http://www.baidu.com')
    s.quit()
