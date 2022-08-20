class Block:
    def __init__(self,list):
        self.width = list[0]
        self.length = list[1]
        self.height = list[2]

    def get_width(self):
        return self.width
    def get_height(self):
        return self.height
    def get_length(self):
        return self.length
    def get_volume(self):
        return self.height * self.length * self.width
    def get_surface_area(self):
        return (2 * self.length * self.width) + (2 * self.width * self.height) + (2 * self.length * self.height)