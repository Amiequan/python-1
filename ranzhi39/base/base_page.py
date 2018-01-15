from base.log import Log
from base.ranzhi_driver import RanzhiDriver


class RanzhiBasePage:
    def __init__(self,base_driver:RanzhiDriver):
        self.base_driver = base_driver

    def log(self,msg):
        log = Log
        log.info(msg)