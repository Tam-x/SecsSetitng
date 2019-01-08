
from Util import Utility
from Util.CRC8 import crc8

#数据帧
HEAD_FIRST_0 = 0xAA
HEAD_SECOND_1 = 0xFF
PROTOCOL_VERSION_2 = 0
LEN_HIGH_3 = 0
LEN_LOW_4 = 0
PROJECT_CODE_5 = 0
SUPPLIER_CODE_6 = 0
CMD_TYPE_10 = 0
TAIL_FIRST = 0xDD
TAIL_LAST = 0xEE

def create_frame(ip, order, timestamp, body=[]):
    CMD_TYPE_10 = order
    frame = [HEAD_FIRST_0, HEAD_SECOND_1, PROTOCOL_VERSION_2, LEN_HIGH_3, LEN_LOW_4, PROJECT_CODE_5, SUPPLIER_CODE_6]
    frame.extend(ip)
    frame.append(CMD_TYPE_10)
    frame.extend(timestamp)
    frame.extend(body)
    length = len(frame)+3
    frame[3], frame[4] = Utility.int_to_2bytes(length)
    c8 = crc8(bytes(frame)).hexdigest()
    frame.append(int(c8, 16))
    frame.extend([TAIL_FIRST, TAIL_LAST])
    return frame




