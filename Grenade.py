#グレネード連射(非干渉)
from bitslicer import VirtualMemoryError, DebuggerError

class Script(object):
    def __init__(self):
        debug.log('Start:グレネード連射')
        res1 = vm.scanByteString("4B0B9253")
        for index in range(len(res1)):
            debug.log(res1[index])
            res2 = vm.readFloat(res1[index] + 64)
            if res2 == 1:
                vm.writeInt32(res1[index] + 64, 0)
                vm.writeInt32(res1[index] + 4, 0)
                vm.writeInt32(res1[index] + 44, 0)
                debug.log("Success:グレネード連射")
        debug.log('Finish:グレネード連射')

    def finish(self):
        debug.log('Uncheck:グレネード連射')
