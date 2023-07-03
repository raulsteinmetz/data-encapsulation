import crc

class Frame:
    def __init__(self):
        self.id = -1
        self.data = ''
        self.entire_frame = ''

    
    def code_frame(self, data, id):
        self.data = data
        # turn id to binary with 3 digits
        self.id = bin(id)[2:].zfill(3)
        self.entire_frame = str(self.id) + self.data


    def decode_frame(self, entire_frame):
        self.entire_frame = entire_frame
        self.id = int(entire_frame[:3], 2)
        self.data = entire_frame[3:]


class FrameList:
    def __init__(self):
        self.id_counter = 0
        self.frame_list = []

    def add_frame_by_message(self, message):
        frame = Frame()
        frame.code_frame(message, self.id_counter)
        self.frame_list.append(frame)
        self.id_counter += 1
        if (self.id_counter == 7):
            self.id_counter = 0
    
    def add_frame_by_frame(self, frame_string):
        frame = Frame()
        frame.decode_frame(frame_string)
        self.frame_list.append(frame)
        self.id_counter += 1
        if (self.id_counter == 7):
            self.id_counter = 0