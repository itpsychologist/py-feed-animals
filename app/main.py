#  write your code here
class Animal:

    def __init__(self,
                 name: str,
                 appetite: int,
                 is_hungry: bool = True) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite
        else:
            return 0


class Cat(Animal):

    def __init__(self,
                 name: str,
                 is_hungry: bool = True) -> None:
        self.name = name
        self.is_hungry = is_hungry
        super().__init__(name, appetite=3, is_hungry=is_hungry)

    def catch_mouse(self) -> None:
        print("The hunt began!")


class Dog(Animal):

    def __init__(self,
                 name: str,
                 is_hungry: bool = True) -> None:
        self.name = name
        self.is_hungry = is_hungry
        super().__init__(name, appetite=7, is_hungry=is_hungry)

    def bring_slippers(self) -> None:
        print("The slippers delivered!")


def feed_animals(animals: list) -> int:
    animal_feed = 0
    for animal in animals:
        animal_feed += animal.feed()
    return animal_feed
