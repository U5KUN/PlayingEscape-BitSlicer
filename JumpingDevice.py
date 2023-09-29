#バネ連射
from bitslicer import VirtualMemoryError, DebuggerError

class Script(object):
    def __init__(self):
        debug.log('Start:バネ連射')
        res1 = vm.scanByteString("5088C462")
        for index in range(len(res1)):
            debug.log(res1[index])
            res2 = vm.readFloat(res1[index] + 64)
            if res2 == 0.5:
                vm.writeInt32(res1[index] + 64, 0)
                vm.writeInt32(res1[index] + 4, 0)
                vm.writeInt32(res1[index] + 44, 0)
                debug.log("Success:バネ連射")
        debug.log('Finish:バネ連射')

    def finish(self):
        debug.log('Uncheck:バネ連射')