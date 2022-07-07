import math

"""
This is a program that simulates the orbit of a planet around a star
TODO: Write code to calculate the physics of the process. --- DONE
TODO: Process the code into coordinates to represent on an array --- SORT OF DONE
TODO: Use a drawing tool to animate this
"""

gConst = 6.67 * (pow(10, -11))


class Coordinate:
    def __init__(self, x=0.0, y=0.0):
        self.x, self.y = x, y

    def __repr__(self):
        return repr("(" + str(self.x) + "," + str(self.y) + ")")

    def setx(self, x): self.x = float(x)

    def sety(self, y):  self.y = float(y)

    def get_distance(self, other):
        return float(math.sqrt(pow((self.x-other.x), 2) + pow((self.y - other.y), 2)))

    def set_coord(self, x, y):
        self.setx(x)
        self.sety(y)


class Vector:

    def __init__(self, x=0.0, y=0.0, vertex=Coordinate()):
        self.x, self.y, self.vertex = x, y, vertex

    def __repr__(self):
        return repr("<" + str(self.x) + "," + str(self.y) + ">" + ", Vertex = ("
                    + str(self.vertex.x) + ", " + str(self.vertex.y) + ")")

    def setx(self, x): self.x = float(x)

    def sety(self, y):  self.y = float(y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y
        # returns the dot product of two vectors

    def __divmod__(self, other):
        return "\n\x1B[3mINVALID OPERATION \x1B[0m"
        # since you cannot divide a vector by a vector, it will simply return an invalid if you attempt to

    def __abs__(self):
        return Vector(abs(self.x), abs(self.y))

    def magnitude(self):
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))
        # finds the magnitude of the vector

    def get_angle(self, other):
        return math.acos(float((self * other) / (self.magnitude() * other.magnitude())))
        # this function might turn out useless

    def unit_vector(self, other):
        # try:
        return Vector((-self.x/(self.vertex.get_distance(other))), (-self.x/(self.vertex.get_distance(other))))
        #except:
        #    return Vector(0, 0)



        """       
        This here currently is not the correct way to find unit vectors. 
        Look at it on khan academy
        The idea is that the unit vector is in fact (1,0), the horizontal direction, and (0,1) for vertical direction
        with some sort of scalar quantity next to it, i.e. vector (3,4) would be represented by 3i + 4j, etc. 
        """


class Velocity(Vector):
    def __init(self, x=0, y=0):
        Vector.__init__(self, x, y)

    def __repr__(self):
        return f"Velocity = {self.magnitude()} meters per second"


class Acceleration(Vector):
    def __init__(self, x=0, y=0):
        Vector.__init__(self, x, y)

    def __repr__(self):
        return f"Acceleration = {self.magnitude()} meters per second squared"


class Object:
    def __init__(self, name='', mass=0, radius=0, dist_from_sun=0, position=Coordinate(0, 0)):
        self.name, self.mass, self.radius, self.dist_from_sun, self.position = name, mass, radius,\
                                                                               dist_from_sun, position

    def __repr__(self):
        return f"{self.name}, mass = {self.mass}, radius = {self.radius}, distance from the sun = " \
               f"{self.dist_from_sun}, and it\'s position is {self.position} "

    def set_name(self, name): self.name = name
    def set_mass(self, mass): self.mass = mass
    def set_radius(self, radius): self.radius = radius
    def set_dist(self, dist): self.dist_from_sun = dist
    def set_position(self, position): self.position = position
    # functions that set the variables of the object

    def get_name(self): return self.name
    def get_mass(self): return self.mass
    def get_radius(self): return self.radius
    def get_dist(self): return self.dist_from_sun
    def get_pos(self): return self.position
    # objects that get the variables


obj = {
    'Sun': Object(name="Sun", position=Coordinate(0, 0)),
    'earth': Object(name='Earth')
}


# finds the tangential velocity of the orbiting mass

def orbit_velocity(g, m, r):
    try:
        return math.sqrt((g * m) / r), "m/s"
    except Exception as e:
        print("\n" + str(e) + "\n\x1B[3mFailed to calculate orbital velocity \x1B[0m")


# used try and except here to prevent the program not being able to calculate the value


# finds the gravitational force between two masses
def gravitational_force(g, m1, m2, r):
    try:
        F = (-g * m1 * m2) / math.pow(r, 2)
        return F, "N"
    except Exception as e:
        print("\n" + str(e) + "\n\x1B[3mFailed to calculate gravitational force \x1B[0m")


# finds the acceleration with the force and mass
def find_acceleration(force, m):
    try:
        return force[0] / m, "m/s^2"
    except Exception as e:
        print("\n" + str(e) + "\n\x1B[3mFailed to find acceleration\x1B[0m")


print(obj['Sun'].get_radius())

v1 = Vector(1, 1, vertex=Coordinate(3, 4))
v2 = Vector(12, 940, vertex=Coordinate(0, 0))

print("\n\n--------------------------------------------------------------------\n\n")
print(v1)
print(abs(v1))
print(v2)

print(v1 * v2)
print(math.degrees(v1.get_angle(v2)))


earth = Object("sun", radius=20)

print(earth)

print("\n\n--------------------------------------------------------------------\n\n")

print(v1.unit_vector(obj['Sun'].position))












