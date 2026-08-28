

class Volume_Space():
    def __init__(self, scale, observer):
        self.scale = scale #spacio/temporal scale. very general. the unit size of distance over time. effects certainty. "flair" can happen, causing "halting" verify ranges (limits) if not frequency (infinately circular)
        self.lattice = []
        self.attributes = set()
        self.observer = observer

    def bifrost_next(self, time_step):
        for pixel in range(len(self.lattice)):
            for attribute in self.attributes:
                self.lattice.pixel.next(time_step)




class Volume_Pixel():
    def __init__(self, x, y, z, vector, scalar):
        self.vector = vector #orientation relative to observer
        self.scalar = scalar #spacio temporal scale relative to observer
        self.x = x
        self.y = y
        self.z = z
        self.attribute = 




# create grid of volumetric points with set attributes, momentum, electricity, etc. Then know how they affect each other. 
# to function, translate attribute definitions/funtions/equations into slerps along the time_line.
# for example, a volume pixel with momentum along a vector will have that momentum as an attribute. The momentum attribute will be 
# connected to an "observer" in the past, to observer in the future.
# values in momentum must be enough to calculate end step. 
#
# identify what is stored where. values should be passed along to future pixel, erased, and neighbor recieves. 
# "scalar" acts a capacitor to initiate "action frequency"- whismhurt charge, then snap. permeability of space