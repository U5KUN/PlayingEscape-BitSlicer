#足止め無効(無効化対応)
from bitslicer import VirtualMemoryError, DebuggerError

class Script(object):
    def __init__(self):
        debug.log('Start:足止め無効')
        res1 = vm.scanByteString("1CC806001CC8060001000000")
        for index in range(len(res1)):
            res2 = vm.readFloat(res1[index] + 100)
            if res2 == 6.0:
                vm.writeFloat(res1[index] + 100, 0)
                debug.log('Success:足止め無効')
        debug.log('Finish:足止め無効')

    def finish(self):
        debug.log('Uncheck:足止め無効')
        for index in range(len(res1)):
            res2 = vm.readFloat(res1[index] + 100)
            if res2 == 0:
                vm.writeFloat(res1[index] + 100, 6)
                debug.log('Disable:足止め無効')
        debug.log('Finish:足止め無効')