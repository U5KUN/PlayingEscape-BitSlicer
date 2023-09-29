#テレポート連射
from bitslicer import VirtualMemoryError, DebuggerError

class Script(object):
    def __init__(self):
        debug.log('Start:テレポート連射')
        res1 = vm.scanByteString('F813C66C')
        for index in range(len(res1)):
            res2 = vm.readFloat(res1[index] + 64)
            if res2 == 0.5:
                vm.writeInt32(res1[index] + 64, 0)
                vm.writeInt32(res1[index] + 44, 0)
                debug.log("Success:テレポート連射")
        debug.log('Finish:テレポート連射')

    def finish(self):
        debug.log('Uncheck:テレポート連射')