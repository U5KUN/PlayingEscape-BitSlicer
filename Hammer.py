#ハンマー連射
from bitslicer import VirtualMemoryError, DebuggerError

class Script(object):
    def __init__(self):
        debug.log('Start:ハンマー連射')
        result1 = vm.scanByteString("6A219462")
        for index in range(len(result1)):
            debug.log(result1[index])
            result2 = vm.readFloat(result1[index] + 64)
            if result2 == 0.5:
                vm.writeInt32(result1[index] + 64, 0)
                vm.writeInt32(result1[index] + 4, 0)
                vm.writeInt32(result1[index] + 44, 0)
                debug.log("Success:ハンマー連射")
        debug.log('Finish:ハンマー連射')

    def finish(self):
        debug.log('Uncheck:ハンマー連射')