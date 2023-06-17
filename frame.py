class Frame:
    def __init__(self):
        self.id = -1
        self.data = ''
        

        pass

    
    def code_frame(self, data, id):
        self.data = data
        # turn id to binary with 3 digits
        self.id = bin(id)[2:].zfill(3)
        self.entire_frame = str(self.id) + self.data


    def decode_frame(self, entire_frame):
        self.entire_frame = entire_frame
        self.id = int(entire_frame[:3], 2)
        self.data = entire_frame[3:]