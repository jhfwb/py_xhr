from abc import ABCMeta, abstractmethod


class Browser(metaclass=ABCMeta):
    @abstractmethod
    def open_browser(self):
        pass

    @abstractmethod
    def close_browser(self):
        pass

    @abstractmethod
    def click(self):
        pass


class BrowserImp(Browser):
    def __init__(self):
        print('初始化浏览器核心组件...此步骤比较耗时!')

    def open_browser(self):
        print('打开浏览器')

    def close_browser(self):
        print('关闭浏览器')

    def click(self):
        print('执行点击...')


class BrowserProxy(Browser):
    def __init__(self, browser):
        self.browser = browser

    def open_browser(self):
        self.browser.open_browser()

    def close_browser(self):
        raise PermissionError('权限不足，无法使用改方法')
        self.browser.close_browser()

    def click(self):
        print('这是代理模式的点击：')
        self.browser.click()


if __name__ == '__main__':
    b = BrowserProxy(BrowserImp())
    b.click()
    b.close_browser()
