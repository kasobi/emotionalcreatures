import pygame




class UnitSpace():
    def __init__(self, coordinates):
        #past
        self.top = None
        self.bottom = None
        self.left = None
        self.right = None
        self.forward = None
        self.backward = None

        #future / present
        # coordinates go x->y->z
        self.coordinates = coordinates

        



class UnitTimeLink():
    def __init__(self, sphere_1, sphere_2):
        self.sphere_1 = sphere_1
        self.sphere_2 = sphere_2
        self.orientation_1_to_2 = None
        self.orientation_2_to_1 = None


class UnitSphere():
    def __init__(self, radius, spin, link, space):
        self.radius = radius
        self.spin = spin
        self.time = link
        self.space = space

class SpaceTimeLattice():
    def __init__(self):
        observer = UnitSphere(1, 0, None, None)
        self.observer = observer
        self.lattice_points = []

    
    def create_lattice(self, x, y, z):
        for z in range(1, z + 1):
            for y in range(1, y + 1):
                for x in range(1, x + 1):
                    self.lattice_points.append(f"x{x}y{y}z{z}")

lattice = SpaceTimeLattice()
lattice.create_lattice(5,5,5)

for i in lattice.lattice_points:
    print(i)

        #steps to make
# start with a line of x. loop end to beginning.
# create additional lines in y direction. loop together, loop ends at each x. loop y's at the end.
# create z layers in z direction. loop z 1s to z ends.







    







#unit spacetime needs to have sphere on each side of a cube's face. inside and out. A sort of torus mapped to a sphere. 
#there is a single way in and out. you travel through 6 interconnected cubes mapped to 6 sections of a sphere.
#each new unit gets added like a graph, or links on a chain. it can only communicate with it's neighbors. 
    
#unit sphere interaction is within the sphere. the distance from one sphere to the next. A 3-dimensional logorythmic compresion.
#it is in the volumes between, not the lines and points. use relation between circle and square to create motion. it's the point in between.
#positives must create negatives tha go the opposite way
#what happens what two streets meet? the motion must go in two directions at the least. It actually goes in all directions at a time. it just fans out less or more in things like magenets vs. gravity.