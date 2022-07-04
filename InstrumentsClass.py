from abc import ABCMeta, abstractmethod
"""This serves as a template for Lab #2 - Strategy for Musical Instruments"""
###############################################################################
# Instruments
###############################################################################
"""The Instrument interface contains one class variable named play_behavior 
and three methods: display, play and set_play_behavior"""
class Instrument:
    __metaclass__ = ABCMeta
    # please include the class variable and the three required methods here
    play_behavior = None
    def display(self):
        pass
    def play(self):
        self.play_behavior.play()
# conditional to see if new behaviour is the same one it has. In order to avoid
# adding a behavior that does not belong once it is set. If else can be removed
# to allow new behaviors to be set/overwrite existing behaviors
    def set_play_behavior(self, new_play_behavior):
        if(new_play_behavior != self.play_behavior):
            pass
        else:
            self.play_behavior = new_play_behavior
"""The DoubleBass class is already written for you! :)
You should use as a template for the following 4 classes"""
class DoubleBass(Instrument):
    def __init__(self):
        self.play_behavior = PlayWithBow()
    def display(self):
        print("I am a double bass.")
"""The Clarinet class should contain one initializer method (hint: __init__) 
and one method: display"""
class Clarinet(Instrument):
    def __init__(self):
        self.play_behavior = BuzzAReed()
    def display(self):
        print("I am a clarinet.")
"""The Harp class should contain one initializer method (hint: __init__) 
and one method: display"""
class Harp(Instrument):
    def __init__(self):
        self.play_behavior = PluckWithFingers()
    def display(self):
        print("I am a harp.")
"""The Tuba class should contain one initializer method (hint: __init__) 
and one method: display"""
class Tuba(Instrument):
    def __init__(self):
        self.play_behavior = BuzzWithLips()
    def display(self):
        print("I am a tuba.")
"""The Violin class should contain one initializer method (hint: __init__) 
and one method: display"""
class Violin(Instrument):
    def __init__(self):
        self.play_behavior = PlayWithBow()
    def display(self):
        print("I am a violin.")
###############################################################################
# Play behaviors
###############################################################################
"""The PlayBehavior interface is already implemented"""
class PlayBehavior:
    __metaclass__ = ABCMeta
    @abstractmethod
    def play(self):
        pass
"""Write class PlayWithBow with only one method: play"""
class PlayWithBow(PlayBehavior):
    # delete the pass word below and write the required method
    def play(self):
        print("Play me with a bow")
"""Write class BuzzAReed with only one method: play"""
class BuzzAReed(PlayBehavior):
    # delete the pass word below and write the required method
    def play(self):
        print("Play me by blowing and by buzzing a reed")
"""Write class BuzzWithLips with only one method: play"""
class BuzzWithLips(PlayBehavior):
    # delete the pass word below and write the required method
    def play(self):
        print("Play me by blowing and by buzzing your lips")
"""Write class PluckWithFingers with only one method: play"""
class PluckWithFingers(PlayBehavior):
    # delete the pass word below and write the required method
    def play(self):
        print("Play me by plucking my strings")
"""I already instantiated some objects and created a list containing those objects
in the for loop the methods display and play are called for each object. Then a new
object of DoubleBass() is instantiated, but a setter methods was called to change 
the
behavior of this object"""
if __name__ == '__main__':
    violin = Violin()
    tuba = Tuba()
    clarinet = Clarinet()
    harp = Harp()
    doublebass = DoubleBass()
    instruments = [violin, tuba, clarinet, harp, doublebass]
    for i in instruments:
        i.display()
        i.play()
    # new_doublebass = DoubleBass()
    # new_doublebass.set_play_behavior(PluckWithFingers())
    # new_doublebass.play()
    # new_doublebass.display()
