#インパルス連射(非干渉)
from bitslicer import VirtualMemoryError, DebuggerError

class Script(object):
    def __init__(self):
        debug.log('Start:インパルス連射')
        res1 = vm.scanByteString('42 AE 20 3C')
        for index in range(len(res1)):
            debug.log(hex(res1[index]))
            res2 = vm.readFloat(res1[index] + 64)
            if res2 == 1:
                debug.log(hex(res1[index]))
                vm.writeInt32(res1[index] + 64,  0)
                vm.writeInt32(res1[index] + 4,  0)
                vm.writeInt32(res1[index] + 44,  0)
                debug.log('Success:インパルス連射')
        debug.log('Finish:インパルス連射')

    def finish(self):
        debug.log('Uncheck:インパルス連射')