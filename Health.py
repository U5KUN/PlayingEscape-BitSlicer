#体力無限
from bitslicer import VirtualMemoryError, DebuggerError

class Script(object):
    def __init__(self):
        debug.log('Start:体力無限')
        res1 = vm.scanByteString("FFFDF7FF")
        for index in range(len(res1)):
            debug.log(res1[index])
            res2 = vm.readInt32(res1[index] + 40)
            if res2 == 200:
                vm.writeInt32(res1[index] + 16, 0)
                vm.writeInt32(res1[index] + 36, 0)
                debug.log('Success:人狼無敵')
            elif res2 == 100:
                vm.writeInt32(res1[index] + 16, 0)
                vm.writeInt32(res1[index] + 36, 0)
                debug.log('Success:市民無敵')
        debug.log('Finish:体力無限')

    def finish(self):
        debug.log('Uncheck:体力無限')