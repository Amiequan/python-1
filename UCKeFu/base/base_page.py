from base.log import Log
from base.uckefu_driver import UCKeFuDriver


class BasePage:
    def __init__(self,base_driver:UCKeFuDriver):
        self.base_driver = base_driver

    def log(self,msg):
        log = Log('logs')
        log.info(msg)