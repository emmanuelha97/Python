"""
The SimUDuck App - Strategy Design Pattern

Joe works for a company that makes a highly successful duck
pond simulation game, SimUDuck. The game can show a large
variety of duck species swimming and making quacking sounds.
"""

###############################################################################
# Ducks
###############################################################################

# Abstract class Duck


class Duck:
    fly_behavior = None
    quack_behavior = None

    def display(self):
        pass

    def fly(self):
        self.fly_behavior.fly()


    def quack(self):
        self.quack_behavior.quack();

        # TODO: write the set_quack_behavior method
        def setFlyBehavior(self, new_fly_behavior):
            self.fly_behavior = new_fly_behavior

        # TODO: write the set_fly_behavior method
        def setQuackBehavior(self, new_quack_behavior):
            self.quack_behavior = new_quack_behavior

    def swim(self):
        print("All ducks float, even decoys!!")


class MallardDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def display(self):
        print("I'm a real Mallard duck")


class DecoyDuck(Duck):

    # TODO: write the init method
    def __init__(self):
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = MuteQuack()

    # TODO: write the display method
    def display(self):
        print("I'am a Decoy Duck")


class RubberDuck(Duck):

    # TODO: write the init method
    def __init__(self):
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = Squeak();

    # TODO: write the display method
    def display(self):
        print("I'am a Rubber Duck")


class RedHeadDuck(Duck):

    # TODO: write the init method
    def __init__(self):
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack();


    # TODO: write the display method
    def display(self):
        print("looks like a redhead")

    # TODO: write the ModelDuck class

class ModelDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = FakeQuack();

    def display(self):
        print("Am a model duck")



    ###############################################################################
    # Quack behaviors
    ###############################################################################


class QuackBehavior:
    def quack(self):
        pass


class Quack(QuackBehavior):
    def quack(self):
        print("Quack")

# TODO: write the MuteQuack class
class MuteQuack(QuackBehavior):
    def MuteQuack(self):
        print("....")

# TODO: write the Squeak class
class Squeak(QuackBehavior):
    def squeak(self):
        print("squeak")

# TODO: write the FakeQuack class
class FakeQuack(QuackBehavior):
    def FakeQuack(self):
        print("Fake Quack")

###############################################################################
# Fly behaviors
###############################################################################


class FlyBehavior():
    def fly(self):
        pass


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I'm flying!!")


# TODO: write the FlyNoWay class
class FlyNoWay(FlyBehavior):
    def fly(self):
        print("Fly no Way")

# TODO: write the FlyRocketPowered class
class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print("FlyRocketPowered")

if __name__ == '__main__':

    # TODO: instantiate an object of MallardDuck
    mallard = MallardDuck();
    mallard.quack()
    mallard.fly()
    mallard.display()


    # TODO: instantiate an object of RedHeadDuck
    red = RedHeadDuck();
    red.quack()
    red.fly()
    red.display()
    red.setQuackBehavior(FakeQuack())
    red.quack()


    # TODO: instantiate an object of ModelDuck
    model = ModelDuck();
    model.quack()
    model.fly()
    model.display()

    # """
    # References:
    # This lecture was designed by Dr Gregory Reis based on the book
    # Elisabeth Freeman, Eric Freeman, Bert Bates, and Kathy Sierra. 2004
    # Head First Design Patterns. O' Reilly & Associates, Inc.,
    # Dr Kip Irvine's class notes, and using the simuduck.py written
    # by Miguel Alba and modified by Dr Gregory Reis
    # """
