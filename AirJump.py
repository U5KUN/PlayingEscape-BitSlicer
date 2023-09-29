#跳躍無限(無効化対応)
from bitslicer import VirtualMemoryError, DebuggerError

class Script(object):
    def __init__(self):
        debug.log('Start:跳躍無限')
        res = vm.scanByteString("FFFDF7FF")
        for index in range(len(res)):
            vm.writeInt32(res[index], -1)

    def finish(self):
        debug.log('Uncheck:跳躍無限')
		  for index in range(len(res)):
            vm.writeInt32(res[index], -524801)
				debug.log(res[index])
				debug.log('Disable:跳躍無限')
			debug.log('Finish:跳躍無限')