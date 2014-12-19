#Python 3.4.2
import abc


#Check method
def overrides(interface_class):
    def overrider(method):
        assert(method.__name__ in dir(interface_class))
        return method
    return overrider


#Dog class
class Dog():
    def __init__(self, barkBehavior, walkBehavior):
        self._barkBehavior = barkBehavior
        self._walkBehavior = walkBehavior

    def bark(self):
        self._barkBehavior.bark()

    def walk(self):
        self._walkBehavior.walk()
       
    def giveEnergy(self):
        print("Every dog needs Energy. Either food or a battery.")


#Labrador class
#Default: Walks fast and barks loudly
class Labrador(Dog):
    def __init__(self):
        Dog.__init__(self, BarkLoudly(), WalkFast())
        

#Poodle class
#Default: Walks slowly and barks quietly
class Poodle(Dog):
    def __init__(self):
        Dog.__init__(self, BarkQuietly(), WalkSlowly())


#ToyDog class
#Default: Doesn't walk / bark
class ToyDog(Dog):
    def __init__(self):
        Dog.__init__(self, MuteBark(), NotWalking())
        

#Abstract class
class WalkBehavior(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def walk(self):
        pass #do nothing


class WalkFast(WalkBehavior):
    #Not needed but makes sure that the method walk exists
    #@overrides(WalkBehavior)
    def walk(self):
        print("Walking fast!!!!!!")


class WalkSlowly(WalkBehavior):
    #@overrides(WalkBehavior)
    def walk(self):
        print("Walking slooooowly.")


class NotWalking(WalkBehavior):
    #@overrides(WalkBehavior)
    def walk(self):
        print("Not walking right now.")


#Abstract class
class BarkBehavior(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def bark(self):
        pass #do nothing
    
    
class BarkLoudly(BarkBehavior):
    #not needed but makes sure that the method bark exists
    #@overrides(BarkBehavior)
    def bark(self):
       print("BARKING LOUD!")

    
class BarkQuietly(BarkBehavior):
    #@overrides(BarkBehavior)
    def bark(self):
        print("barking quiet.")


class MuteBark(BarkBehavior):
    #@overrides(BarkBehavior)
    def bark(self):
        print("I'm not barking.")

        
#-----------------------------------------


if __name__ == "__main__":
    print("-----------------------------")
    print("----Dog Simulator started----")
    print("-----------------------------")
    print("Labrador")
    Labrador1 = Labrador()
    Labrador1.bark()
    Labrador1._barkBehavior = BarkQuietly()
    #ignore this line: labrador1.setBark(BarkQuietly())
    Labrador1.bark()

    print("Labrador Walk:")
    Labrador1.walk()
    Labrador1._walkBehavior = WalkSlowly()
    Labrador1.walk()
    
    Labrador1.giveEnergy()
    print("-----------------------------")
    print("Poodle")
    Poodle1 = Poodle()
    Poodle1.bark()
    Poodle1._barkBehavior = BarkLoudly()
    Poodle1.bark()
    
    print("Poodle Walk:")
    Poodle1.walk()
    Poodle1._walkBehavior = WalkFast()
    Poodle1.walk()
    
    Poodle1.giveEnergy()
    print("-----------------------------")
    print("Toy Dog")
    ToyDog1 = ToyDog()
    ToyDog1.bark()
    #pushing button to bark
    ToyDog1._barkBehavior = BarkQuietly()
    ToyDog1.bark()
    ToyDog1._barkBehavior = MuteBark()
    
    print("Toy Dog Walk:")
    ToyDog1.walk()
    #pushing button to walk
    ToyDog1._walkBehavior = WalkFast()
    ToyDog1.walk()
    ToyDog1._walkBehavior = NotWalking()
    ToyDog1.walk()
    
    ToyDog1.giveEnergy()
