#スナイパー連射(非干渉)
from bitslicer import VirtualMemoryError, DebuggerError

class Script(object):
    def __init__(self):
        debug.log('Start:狙撃連射')
        res1 = vm.scanByteString("53ACC142")
        for index in range(len(res1)):
            res2 = vm.readFloat(res1[index] + 64)
            if res2 == 0.5:
                debug.log(hex(res1[index]))
                vm.writeInt32(res1[index] + 64,  0)
                vm.writeInt32(res1[index] + 4,  0)
                vm.writeInt32(res1[index] + 44,  0)
                debug.log('Success:狙撃連射')
        debug.log('Finish:狙撃連射')

    def finish(self):
        debug.log('Uncheck:狙撃連射')