from CONSTANTS import Value_type

#The spirits and souls that inhabit creatures
class Animus():
    #The animus is the thing that give life. It is a singular entity for motion and existance. That which give movement.
    def __init__(self, host):
        self.host = []
        pass

    def possess(self, host):
        host.spirit.append(self)
        self.host.append(host)

    def exercise(self, host):
        self.host.remove(host)
        host.spirit.remove(self)

    def action():
        pass

    def sense():
        pass


class Force(Animus):
    #A force is the simplest spirit of motion. Gravity, Momentum, Electromagnetic, etc.
    def __init__(self, host):
        super().__init__(host)


class Spririt(Animus):
    pass

class Soul(Spririt):
    pass





#The bodies these creatures inhabit
class Corpus():
    #The corpus is the basis of all form that exists. The thing that can be experienced. Its only sense is a sense of time
    def __init__(self):
        self.spirit = []
        self.temporalrate = 1

    #interal clock (relitive temporal speed) as an absolute value, percent of current, or percent of target
    def adjustinternalclock(self, value: int, value_type: Value_type, target=None) -> None:
        if value_type is Value_type.ABSOLUTE:
            self.temporalrate = value
        elif value_type is Value_type.RATIO:
            if target is None:
                self.temporalrate = (value / 100) * self.temporalrate
            elif target is not None:
                self.temporalrate = (value / 100) * target.temporalrate
        else:
            raise Exception (f"Error in adjustinternalclock(value: {value}, value_type: {Value_type}, target: {target})")



class Particle(Corpus):
    #The particle is a variably scale thing that only reacts to forces. Water, rocks, dust, wind, planets, etc.
    def __init__(self, ):
        super().__init__()



