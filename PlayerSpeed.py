#人物加速(無効化対応)
from bitslicer import VirtualMemoryError, DebuggerError

class Script(object):
    def __init__(self):
        debug.log('Start:人物加速')
        res = vm.scanByteString('000080BF0000807F0000807F0000807F000080FF000080FF000080FF')
        for index in range(len(res)):
            vm.writeFloat(res[index] - 64, 2)#跳躍力
            vm.writeFloat(res[index] - 32, 2.5)#東西速度
            vm.writeFloat(res[index] - 12, 2.5)#南北速度
            debug.log(hex(res[index]))
            debug.log("Success:人物加速")
        debug.log('Finish:人物加速')

    def finish(self):
        debug.log('Uncheck:人物加速')
		  for index in range(len(res)):
            vm.writeFloat(res[index] - 64, 1)
            vm.writeFloat(res[index] - 32, 1)
            vm.writeFloat(res[index] - 12, 1)
            debug.log(hex(res[index]))
            debug.log("Disable:人物加速")
        debug.log('Finish:人物加速')