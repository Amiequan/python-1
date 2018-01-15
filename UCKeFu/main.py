from runner.uckefu_test_runner import UCKeFuTestRunner

class Main(object):
    def start_uckefu_test(self):
        test_runner = UCKeFuTestRunner()
        test_runner.runner()

if __name__ == '__main__':
    main = Main()
    main.start_uckefu_test()