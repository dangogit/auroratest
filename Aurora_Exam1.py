#!\usr\bin\envpython

from ctypes import *
import subprocess
class Aurora_Exam():


    def replaceFun(self):
        print("------------------------Enter to the replace Function Please Enter the value that you want-------------------------------------")
        print('Enter your Value:')
        try:
            self.index = str(int(input()))
        except Exception:
            raise ("Please enter an Integer value")
        fin = open('main.c', 'r')
        # read file contents to string
        data = fin.read()
        fin.close()
        fin1 = open('main.c', 'w')
        # replace all occurrences of the required string

        if data.find('__VALUE__') > 0:
            data = data.replace('__VALUE__', self.index)
        fin1.write(data)
        fin1.close()

    def modifiedandCreateExeFun(self):
        print("------------------------Enter to modify and Create Exe File--------------------------------------------------------------------")
        self.res = subprocess.call(["gcc", 'main.c', "-o", 'main.exe'], shell=True)
        if self.res != 0:
            raise Exception("Failed to compile main.c")

    def modifiedandRunExeFun(self):
        print("------------------------Enter to modify and Run Exe File--------------------------------------------------------------------")
        self.res1 = subprocess.call("main.exe")



    def checkFun(self):
        print("------------------------Check the Value if it's the same or not--------------------------------------------------------------------")
        if self.res1 != int(self.index):
            raise Exception("Oops! That was Not the same values, received = {0} expected = {1}".format(self.res1, int(self.index)))
        else:
            print("It's the same value, received = {0} expected = {1}".format(self.res1, int(self.index)))