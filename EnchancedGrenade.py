#連射グレネード連射
from bitslicer import VirtualMemoryError, DebuggerError

class Script(object):
    def __init__(self):
        debug.log('Start::連射グレネード連射')
        result1 = vm.scanByteString("DAF4E15A")
        for index in range(len(result1)):
            debug.log(result1[index])
            result2 = vm.readFloat(result1[index] + 64)
            if result2 == 0.5:
                vm.writeInt32(result1[index] + 12, 0)
                vm.writeInt32(result1[index] + 16, 0)
                vm.writeInt32(result1[index] + 28, 0)
                vm.writeInt32(result1[index] + 32, 0)
                vm.writeInt32(result1[index] + 64, 0)
                debug.log("Success:連射グレネード連射")
        debug.log('Finish:連射グレネード連射')

    def finish(self):
        debug.log('Uncheck:連射グレネード連射')

