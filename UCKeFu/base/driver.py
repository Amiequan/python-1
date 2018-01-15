# import time
# from enum import Enum, unique
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver import FirefoxProfile
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.select import Select
#
#
# @unique
# class BoxBrowser(Enum):
#     Chrome = 0
#     Firefox = 1
#     Ie = 2
#
# class BoxDriver(object):
#     """
#     a simple demo of selenium framework tool
#     """
#     base_driver = None
#     by_char = None
#
#     def __init__(self, browser_type=0, by_char=",", profile=None):
#         """
#         构造方法：实例化 BoxDriver 时候使用
#         :param by_char: 分隔符
#         :param firefox_profile:
#         可选择的参数，如果不传递，就是None
#         如果传递一个 profile，就会按照预先的设定启动火狐
#         去掉遮挡元素的提示框等
#         """
#         self.by_char = by_char
#         if browser_type == BoxBrowser.Chrome:
#             profile = webdriver.ChromeOptions()
#             profile.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
#             driver = webdriver.Chrome(chrome_options=profile)
#         elif browser_type == BoxBrowser.Firefox:
#             if profile is not None:
#                 profile = FirefoxProfile(profile)
#
#             driver = webdriver.Firefox(firefox_profile=profile)
#
#         elif browser_type == BoxBrowser.Ie:
#             driver = webdriver.Ie()
#         else:
#             driver = webdriver.PhantomJS()
#         try:
#             self.base_driver = driver
#             self.by_char = by_char
#         except Exception:
#             raise NameError("Browser %s Not Found! " % browser_type)
#
#     def clear_cookies(self):
#         """
#         clear all cookies after driver init
#         """
#         self.base_driver.delete_all_cookies()
#
#     def add_cookies(self, cookies):
#         """
#         Add cookie by dict
#         :param cookies:
#         :return:
#         """
#         self.base_driver.add_cookie(cookie_dict=cookies)
#
#     def add_cookie(self, cookie_dict):
#         """
#         Add single cookie by dict
#         添加 单个 cookie
#         如果该 cookie 已经存在，就先删除后，再添加
#         :param cookie_dict: 字典类型，有两个key：name 和 value
#         :return:
#         """
#         cookie_name = cookie_dict["name"]
#         cookie_value = self.base_driver.get_cookie(cookie_name)
#         if cookie_value is not None:
#             self.base_driver.delete_cookie(cookie_name)
#
#         self.base_driver.add_cookie(cookie_dict)
#
#     def remove_cookie(self, name):
#         """
#         移除指定 name 的cookie
#         :param name:
#         :return:
#         """
#         # 检查 cookie 是否存在，存在就移除
#         old_cookie_value = self.base_driver.get_cookie(name)
#         if old_cookie_value is not None:
#             self.base_driver.delete_cookie(name)
#
#     def refresh(self, url=None):
#         """
#         刷新页面
#         如果 url 是空值，就刷新当前页面，否则就刷新指定页面
#         :param url: 默认值是空的
#         :return:
#         """
#         if url is None:
#             self.base_driver.refresh()
#         else:
#             self.base_driver.get(url)
#
#     def maximize_window(self):
#         """
#         最大化当前浏览器的窗口
#         :return:
#         """
#         self.base_driver.maximize_window()
#
#     def navigate(self, url):
#         """
#         打开 URL
#         :param url:
#         :return:
#         """
#         self.base_driver.get(url)
#
#     def quit(self):
#         '''退出浏览器并关闭驱动'''
#         self.base_driver.quit()
#
#     def close_browser(self):
#         '''关闭浏览器'''
#         self.base_driver.close()
#
#     def _locate_element(self, selector):
#         """
#         to locate element by selector
#         :arg
#         selector should be passed by an example with "i,xxx"
#         "x,//*[@id='langs']/button"
#         :returns
#         DOM element
#         """
#         if self.by_char not in selector:
#             return self.base_driver.find_element_by_id(selector)
#
#         selector_by = selector.split(self.by_char)[0].strip()
#         selector_value = selector.split(self.by_char)[1].strip()
#         if selector_by == "i" or selector_by == 'id':
#             element = self.base_driver.find_element_by_id(selector_value)
#         elif selector_by == "n" or selector_by == 'name':
#             element = self.base_driver.find_element_by_name(selector_value)
#         elif selector_by == "c" or selector_by == 'class_name':
#             element = self.base_driver.find_element_by_class_name(selector_value)
#         elif selector_by == "l" or selector_by == 'link_text':
#             element = self.base_driver.find_element_by_link_text(u'%s' % selector_value)
#         elif selector_by == "p" or selector_by == 'partial_link_text':
#             element = self.base_driver.find_element_by_partial_link_text(u'%s' % selector_value)
#         elif selector_by == "t" or selector_by == 'tag_name':
#             element = self.base_driver.find_element_by_tag_name(selector_value)
#         elif selector_by == "x" or selector_by == 'xpath':
#             element = self.base_driver.find_element_by_xpath(selector_value)
#         elif selector_by == "s" or selector_by == 'css_selector':
#             element = self.base_driver.find_element_by_css_selector(selector_value)
#         else:
#             raise NameError("Please enter a valid type of targeting element.")
#         return element
#
#
#     def type(self, selector, text):  #向输入框输入内容
#         """
#         Operation input box.
#
#         Usage:
#         driver.type("i,el","selenium")
#         """
#         el = self._locate_element(selector)
#         el.clear()
#         el.send_keys(text)
#
#     def type_ent(self, selector, text):
#         el = self._locate_element(selector)
#         el.click()
#         el.send_keys(text)
#         el.send_keys(Keys.ENTER)
#
#
#     def click(self, selector):  #点击
#         """
#         It can click any text / image can be clicked
#         Connection, check box, radio buttons, and even drop-down box etc..
#
#         Usage:
#         driver.click("i,el")
#         """
#         el = self._locate_element(selector)
#         el.click()
#
#     def click_by_enter(self, selector):
#         """
#         It can type any text / image can be located  with ENTER key
#
#         Usage:
#         driver.click_by_enter("i,el")
#         """
#         el = self._locate_element(selector)
#         el.send_keys(Keys.ENTER)
#
#     def select_by_index(self, selector, index):
#         """
#         It can click any text / image can be clicked
#         Connection, check box, radio buttons, and even drop-down box etc..
#
#         Usage:
#         driver.select_by_index("i,el")
#         """
#         el = self._locate_element(selector)
#         Select(el).select_by_index(index)
#
#     def select_by_visible_text(self, selector, text):
#         """
#         It can click any text / image can be clicked
#         Connection, check box, radio buttons, and even drop-down box etc..
#
#         Usage:
#         driver.select_by_index("i,el")
#         """
#         el = self._locate_element(selector)
#         Select(el).select_by_visible_text(text)
#
#     def select_by_value(self, selector, value):
#         """
#         It can click any text / image can be clicked
#         Connection, check box, radio buttons, and even drop-down box etc..
#
#         Usage:
#         driver.select_by_index("i,el")
#         """
#         el = self._locate_element(selector)
#         Select(el).select_by_value(value)
#
#     def click_by_text(self, text):
#         """
#         Click the element by the link text
#
#         Usage:
#         driver.click_text("新闻")
#         """
#         self._locate_element('p,' + text).click()
#
#     def submit(self, selector):  #提交
#         """
#         Submit the specified form.
#
#         Usage:
#         driver.submit("i,el")
#         """
#         el = self._locate_element(selector)
#         el.submit()
#
#     def execute_js(self, script):
#         """
#         Execute JavaScript scripts.
#
#         Usage:
#         driver.js("window.scrollTo(200,1000);")
#         """
#         self.base_driver.execute_script(script)
#
#     def get_attribute(self, selector, attribute):  #获取元素属性
#         """
#         Gets the value of an element attribute.
#
#         Usage:
#         driver.get_attribute("i,el","type")
#         """
#         el = self._locate_element(selector)
#         return el.get_attribute(attribute)
#
#     def get_text(self, selector):  #获取文本信息
#         """
#         Get element text information.
#
#         Usage:
#         driver.get_text("i,el")
#         """
#         el = self._locate_element(selector)
#         return el.text
#
#     def get_display(self, selector):
#         """
#         Gets the element to display,The return result is true or false.
#
#         Usage:
#         driver.get_display("i,el")
#         """
#         el = self._locate_element(selector)
#         return el.is_displayed()
#
#     def get_title(self):  #定位窗口标题
#         '''
#         Get window title.
#
#         Usage:
#         driver.get_title()
#         '''
#         return self.base_driver.title
#
#     def get_url(self):  #获取当前页面网址
#         """
#         Get the URL address of the current page.
#
#         Usage:
#         driver.get_url()
#         """
#         return self.base_driver.current_url
#
#     def accept_alert(self):  #接受警告框
#         '''
#             Accept warning box.
#
#             Usage:
#             driver.accept_alert()
#             '''
#         self.base_driver.switch_to.alert.accept()
#
#     def dismiss_alert(self):  #驳回警告
#         '''
#         Dismisses the alert available.
#
#         Usage:
#         driver.dismissAlert()
#         '''
#         self.base_driver.switch_to.alert.dismiss()
#
#     def implicitly_wait(self, secs):  #隐藏页面上元素
#         """
#         Implicitly wait. All elements on the page.
#
#         Usage:
#         driver.implicitly_wait(10)
#         """
#         self.base_driver.implicitly_wait(secs)
#
#     def switch_to_frame(self, selector):  #切换到指定页面
#         """
#         Switch to the specified frame.
#
#         Usage:
#         driver.switch_to_frame("i,el")
#         """
#         el = self._locate_element(selector)
#         self.base_driver.switch_to.frame(el)
#
#     def switch_to_default(self):
#         """
#         Returns the current form machine form at the next higher level.
#         Corresponding relationship with switch_to_frame () method.
#
#         Usage:
#         driver.switch_to_frame_out()
#         """
#         self.base_driver.switch_to.default_content()
#
#     def switch_to_window_by_title(self, title):
#
#         for handle in self.base_driver.window_handles:
#             self.base_driver.switch_to.window(handle)
#             if self.base_driver.title == title:
#                 break
#             self.base_driver.switch_to.default_content()
#
#     def open_new_window(self, selector):
#         '''
#         Open the new window and switch the handle to the newly opened window.
#
#         Usage:
#         driver.open_new_window()
#         '''
#         original_windows = self.base_driver.current_window_handle
#         el = self._locate_element(selector)
#         el.click()
#         all_handles = self.base_driver.window_handles
#         for handle in all_handles:
#             if handle != original_windows:
#                 self.base_driver._switch_to.window(handle)
#
#     def wait(self, seconds):
#         time.sleep(seconds)
#
#     def move_to(self, selector):
#         """
#         to move mouse pointer to selector
#         :param selector:
#         :return:
#         """
#         el = self._locate_element(selector)
#         ActionChains(self.base_driver).move_to_element(el).perform()
#
#     def right_click(self, selector):
#         """
#         to click the selector by the right button of mouse
#         :param selector:
#         :return:
#         """
#         el = self._locate_element(selector)
#         ActionChains(self.base_driver).context_click(el).perform()
#
#     def _locate_elements(self, selector):
#         """
#         to locate element by selector
#         :arg
#         selector should be passed by an example with "i,xxx"
#         "x,//*[@id='langs']/button"
#         :returns
#         DOM element
#         """
#         if self.by_char not in selector:
#             return self.base_driver.find_elements_by_id(selector)
#
#         selector_by = selector.split(self.by_char)[0].strip()
#         selector_value = selector.split(self.by_char)[1].strip()
#
#         if selector_by == "i" or selector_by == 'id':
#             elements = self.base_driver.find_elements_by_id(selector_value)
#         elif selector_by == "n" or selector_by == 'name':
#             elements = self.base_driver.find_elements_by_name(selector_value)
#         elif selector_by == "c" or selector_by == 'class_name':
#             elements = self.base_driver.find_elements_by_class_name(selector_value)
#         elif selector_by == "l" or selector_by == 'link_text':
#             elements = self.base_driver.find_elements_by_link_text(selector_value)
#         elif selector_by == "p" or selector_by == 'partial_link_text':
#             elements = self.base_driver.find_elements_by_partial_link_text(selector_value)
#         elif selector_by == "t" or selector_by == 'tag_name':
#             elements = self.base_driver.find_elements_by_tag_name(selector_value)
#         elif selector_by == "x" or selector_by == 'xpath':
#             elements = self.base_driver.find_elements_by_xpath(selector_value)
#         elif selector_by == "s" or selector_by == 'css_selector':
#             elements = self.base_driver.find_elements_by_css_selector(selector_value)
#         else:
#             raise NameError("Please enter a valid type of targeting elements.")
#
#         return elements
#
#     def count_elements(self, selector):
#         '''统计元素个数'''
#         els = self._locate_elements(selector)
#         return len(els)
#
#     def save_snapshot(self, file_name):
#         """
#         save screen snapshot
#         :param file_name: the image file name and path
#         :return:
#         """
#         driver = self.base_driver
#         driver.save_screenshot(file_name)
#
#     def is_selected(self, selector):
#         """
#         to return the selected status of an WebElement
#         :param selector: selector to locate
#         :return: True False
#         """
#         el = self._locate_element(selector)
#         return el.is_selected()
#
#     def get_text_list(self, selector, url):
#         """
#         根据selector 获取多个元素，取得元素的text 列表
#         :param selector:
#         :param url ddddd
#         :return: list
#         """
#
#         el_list = self._locate_elements(selector)
#         print(el_list[0].text)
#         results = []
#         for el in el_list:
#             results.append(el.text)
#
#         return results
