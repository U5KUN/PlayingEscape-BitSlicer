#全体百倍速(無効化対応)
from bitslicer import VirtualMemoryError, DebuggerError

class Script(object):
    def __init__(self):
        debug.log('Start:全体加速')
        res = vm.scanByteString("0000803F CDCCCC3D8FC2F53C")
        for index in range(len(res)):
            debug.log(hex(res[index]))
            vm.writeFloat(res[index], 100)#ここの100が速度
        debug.log('Finish:全体加速')

    def finish(self):
        debug.log('Uncheck:全体加速')
		  for index in range(len(res)):
            debug.log(hex(res[index]))
            vm.writeFloat(res[index], 1)
        debug.log('Finish:全体加速')