#近接連射
from bitslicer import VirtualMemoryError, DebuggerError

class Script(object):
    def __init__(self):
        debug.log('Start:近接連射')
        punch = vm.scanByteString("664F61AC")
        for index in range(len(punch)):
            debug.log(punch[index])
            ispunch = vm.readFloat(punch[index] + 44)
            if ispunch == 0.5:
                vm.writeInt32(punch[index] + 44, 0)
                debug.log("Success:パンチ連射")
        debug.log("Finish:パンチ連射")

        stick = vm.scanByteString("E9E29EB7")
        for index in range(len(stick)):
            debug.log(stick[index])
            isstick = vm.readInt32(stick[index] + 64)
            if isstick == 1061997773:
                vm.writeInt32(stick[index] + 64, 0)
                debug.log("Success:人狼棒連射")
        debug.log("Finish:人狼棒連射")

        racket = vm.scanByteString("B5B79FB1")
        for index in range(len(racket)):
            debug.log(racket[index])
            isracket = vm.readInt32(racket[index] + 64)
            if isracket == 1061997773:
                vm.writeInt32(racket[index] + 64, 0)
                debug.log("Success:ラケット連射")
        debug.log("Finish:ラケット連射")

    def finish(self):
        debug.log('Uncheck:近接連射')