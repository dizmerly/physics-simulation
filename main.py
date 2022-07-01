import math

"""
This is a program that simulates the orbit of a planet around a star
TODO: Write code to calculate the physics of the process. --- DONE
TODO: Process the code into coordinates to represent on an array
TODO: Use a drawing tool to animate this
"""


class Vector:

    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

    def __repr__(self):
        return repr("<" + str(self.x) + "," + str(self.y) + ">")

    def setx(self, x): self.x = float(x)

    def sety(self, y):  self.y = float(y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    def __divmod__(self, other):
        return "\n\x1B[3mINVALID OPERATION \x1B[0m"

    def __abs__(self):
        return Vector(abs(self.x), abs(self.y))



obj = {
    'Sun': {"name": "Sun", 'm': 100, 'radius': 30, 'distFromSun': 0},
    'obj1': {'name': 'earth', 'm': 5, 'radius': 2, 'distFromSun': 100}
}


gConst = 6.67 * (pow(10,-11))


# finds the tangential velocity of the orbiting mass
def orbit_velocity(g, m, r):
    try:
        return math.sqrt((g*m)/r)
    except:
        return "\n\x1B[3mFailed to calculate orbit velocity \x1B[0m"


# used try and except here to prevent the program not being able to calculate the value


# finds the gravitational force between two masses
def gravitational_force(g, m1, m2, r):
    try:
        F = (-g * m1 * m2)/math.pow(r, 2)
        return F, "N"
    except Exception as e: print("\n"+str(e) + "\n\x1B[3mFailed to calculate gravitational force \x1B[0m")


# finds the acceleration with the force and mass
def find_acceleration(force, m):
    try:
        return force[0] / m, "m/s^2"
    except Exception as e:
        print("\n"+str(e) + "\n\x1B[3mFailed to find acceleration\x1B[0m")


print(obj['Sun']['name'])


print(orbit_velocity(gConst, obj['Sun'].get('m'), obj['obj1'].get('distFromSun')))


print(gravitational_force(gConst, obj["Sun"].get('m'), obj["obj1"].get('m'), obj["obj1"].get('distFromSun')))


print(find_acceleration(gravitational_force(gConst, obj["Sun"].get('m'), obj["obj1"].get('m'),
                                            obj["obj1"].get('distFromSun')), obj["obj1"].get('m')))



v1 = Vector(-3, 5)
v2 = Vector(2, 10)

print(v1)
print(abs(v1))
print(v2)

