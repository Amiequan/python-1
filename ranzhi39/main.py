from runner.ranzhi_test_runner import RanzhiTestRunner

class Main(object):
    def start_ranzhi_test(self):
        ranzhi_test_runner = RanzhiTestRunner()
        ranzhi_test_runner.runner()

if __name__ == '__main__':
    main = Main()
    main.start_ranzhi_test()