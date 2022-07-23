import struct


class ModbusCodeC():
    """
    This CodeC class implement partly of Modbus encode and decode
    The chamber only offer 03H and 06H function-code for using
    """

    @staticmethod
    def MBAP_encode():
        transFlagHi = b'\x00'
        transFlagLo = b'\x00'
        protoFlag = b'\x00\x00'
        length = b'\x00\x06'
        unitFlag = b'\x00'
        mbap = transFlagHi + transFlagLo + protoFlag + length + unitFlag
        return mbap

    @staticmethod
    def PDU_encode(func, regi, num=1, data=None):
        funcList = {'r': b'\x03',
                    'w': b'\x06'}
        funcCode = funcList[func]
        registerStart = struct.pack('!H', regi)
        registerNum = struct.pack('!H', num)
        if data and func == 'w':
            dataCode = struct.pack('!H', data)
            pdu = funcCode + registerStart + dataCode
            return pdu
        pdu = funcCode + registerStart + registerNum
        return pdu

    @staticmethod
    def encode(func, regi, num, data=None):
        return ModbusCodeC.MBAP_encode() + ModbusCodeC.PDU_encode(func, regi, num, data)

    @staticmethod
    def MBAP_decode(s):
        m = {}
        m['transFlagHi'] = s[:1]
        m['transFlagLo'] = s[1:2]
        m['protoFlag'] = s[2:4]
        m['length'] = s[4:6]
        m['unitFlag'] = s[6:]
        return m

    @staticmethod
    def PDU_decode(s):
        p = {}
        '''
        p['funcCode'] = s[:1]
        p['registerStart'] = s[1:3]
        p['registerNum'] = s[3:5]
        p['data'] = s[5:]
        '''
        # TODO: Add bit number and data length check here
        p['funcCode'] = s[:1]
        p['bitNum'] = s[1:2]
        p['data'] = s[2:]
        return p

    @staticmethod
    def decode(msg):
        msg_de = {}
        mbap, pdu = msg[:7], msg[7:]
        msg_de['MBAP'] = ModbusCodeC.MBAP_decode(mbap)
        msg_de['PDU'] = ModbusCodeC.PDU_decode(pdu)
        return msg_de

if __name__ == '__main__':
    print(ModbusCodeC.encode('r', 5, 3))
    print(ModbusCodeC.encode('w', 5, 1, 8))