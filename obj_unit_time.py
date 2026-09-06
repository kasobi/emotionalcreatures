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


# note: spent today's time working on the logic of the operations. wanting 0(n) processing.
# thinking about making the lattice expand and contract on itself based on the volume in between.
# how to represent different angles of connection for map vs actual. thinking as the angle through a wormhole.
# each integer point in each line has an "interaction zone" between them. This represents the motion of transitioning into that value.
# work on 1-d first, then attempt additional. 3D scaffold creates interactions I am looking for, so 2D complexity isn't of much interest. 







    







#unit spacetime needs to have sphere on each side of a cube's face. inside and out. A sort of torus mapped to a sphere. 
#there is a single way in and out. you travel through 6 interconnected cubes mapped to 6 sections of a sphere.
#each new unit gets added like a graph, or links on a chain. it can only communicate with it's neighbors. 
    
#unit sphere interaction is within the sphere. the distance from one sphere to the next. A 3-dimensional logorythmic compresion.
#it is in the volumes between, not the lines and points. use relation between circle and square to create motion. it's the point in between.
#positives must create negatives tha go the opposite way
#what happens what two streets meet? the motion must go in two directions at the least. It actually goes in all directions at a time. it just fans out less or more in things like magenets vs. gravity.

# Notes from boots
#Synchronous State Ring practice


class State:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_ring(values):
    if len(values) < 1:
        return []
    state_list = []

    for i in values:
        state = State(i)
        state_list.append(state)

    count = len(state_list)
    index = 0

    for i in state_list:
        i.left = state_list[(index - 1)% count]
        i.right = state_list[(index + 1)% count]
        index += 1

    return state_list


def step_ring(states):
    new_values = []
    for i in states:
        new_values.append(i.left.value + i.right.value)

    for i in range(len(new_values)):
        states[i].value = new_values[i]

    return states

#A wrapping (toroidal) grid would instead do:

up = grid[(row - 1) % height][col]
down = grid[(row + 1) % height][col]
left = grid[row][(col - 1) % width]
right = grid[row][(col + 1) % width]



def get_neighbors_3d(grid, x, y, z, size_x, size_y, size_z):
    neighbors = []
    neighbors.append(grid[(x - 1) % size_x][y][z])
    neighbors.append(grid[(x + 1) % size_x][y][z])
    neighbors.append(grid[x][(y - 1) % size_y][z])
    neighbors.append(grid[x][(y + 1) % size_y][z])
    neighbors.append(grid[x][y][(z - 1) % size_z])
    neighbors.append(grid[x][y][(z + 1) % size_z])
    return neighbors


## no pythong today. did server install onto old hardware using bootable drive.
# many headache. all the terminal. hours and hours. still trying to update nvidia drivers

# trying to figure out how to do the color changing in main.py play, but as "buckets" with specific spectral emitance.
# make each point an atom, then have the "energy" share between them at allowable frequencies. The rest bouncing around in a 4D central
# volume. have a relation to the amount in the volume to a quantity of rotation to that point. have the amount of sharing of energy
# between one "emitance" be between the suroundings. figuring out sharing ratio for [n] points. making it a constant is just making
# the formula for them. but it must work for anything that is put in it.
# how do I handle "too much"? What ratio or value is there? there can be lots of greens, but maybe an alpha?
# represent rotation as spirals around the color wheel with black being 0 and 1 being white. the red, green, blue are laid out as
# a line around a sphere/cylinder to make the color.
# this shows orientation in 3D space. making 0 be pointed maximally away from you and 1 being pointed maximally toward you.
# the color shows the orientation otherwise.
# 
# it doesn't matter how big black and white are. they can be infinite or nothing. as long as they are connected by the finite.
# all of now is simply the finite of the infinite.
#
# treat the "top" and "bottom" as two circles. the amount of rotation between them rotates the connecting lines by some angle.
# the "compression" or "tension" between them is the curve between them.
#
# as two points meet, the compression points are on the surface of the spherical explosion. translate the sphere into
# a single point by turing it's coordinates into GRB and it's radii into brightness.
# use matrix multiplication to have all neighbors interact. the volume calculation should grow by O(n*j) where n is the number of pieces
# and j is the number of neighbors. Or otherwords, it grows by N number of points.
# you could have it grow by log(n) points if you knew how to calculate the exact way a volume moves by only seeing the boundary.
# can you know the entire volume through only the boundary? more, "How much of the volume is needed to store knowledge of the whole volume?"
# something is always lost, so what do you take with you?
#
# trying to use geometry to think through the math of what I want to show always feels like an acid trip or something.
# it's helpful because I feel some sort of causality or momentum, vs pure math where equations feel empty. 