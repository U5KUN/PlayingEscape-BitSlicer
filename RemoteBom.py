#リモボ連射(非干渉)
from bitslicer import VirtualMemoryError, DebuggerError

class Script(object):
    def __init__(self):
        debug.log('Start:遠隔爆弾連射')
        res1 = vm.scanByteString("C6587565")
        for index in range(len(res1)):
            debug.log(res1[index])
            res2 = vm.readFloat(res1[index] + 64)
            if res2 == 1:
                vm.writeInt32(res1[index] + 64, 0)
                vm.writeInt32(res1[index] + 72, 0)
                vm.writeInt32(res1[index] + 4, 0)
                vm.writeInt32(res1[index] + 44, 0)
                debug.log("Success:遠隔爆弾連射")
			debug.log('Finish:遠隔爆弾連射')

    def finish(self):
        debug.log('Uncheck:遠隔爆弾連射')