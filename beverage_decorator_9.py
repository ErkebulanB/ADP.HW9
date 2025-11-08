from abc import ABC, abstractmethod

class Beverage(ABC):
    @abstractmethod
    def cost(self): ...
    @abstractmethod
    def description(self): ...

class Espresso(Beverage):
    def cost(self):
        return 700.0
    def description(self):
        return "Эспрессо"

class Tea(Beverage):
    def cost(self):
        return 500.0
    def description(self):
        return "Шай"

class Latte(Beverage):
    def cost(self):
        return 900.0
    def description(self):
        return "Латте"

class Mocha(Beverage):
    def cost(self):
        return 950.0
    def description(self):
        return "Мокка"

class BeverageDecorator(Beverage):
    def __init__(self, beverage):
        self.beverage = beverage
    def cost(self):
        return self.beverage.cost()
    def description(self):
        return self.beverage.description()

class Milk(BeverageDecorator):
    def cost(self):
        return super().cost() + 150.0
    def description(self):
        return super().description() + ", Сүт"

class Sugar(BeverageDecorator):
    def cost(self):
        return super().cost() + 50.0
    def description(self):
        return super().description() + ", Қант"

class WhippedCream(BeverageDecorator):
    def cost(self):
        return super().cost() + 200.0
    def description(self):
        return super().description() + ", Көпіртілген кілегей"

class Caramel(BeverageDecorator):
    def cost(self):
        return super().cost() + 180.0
    def description(self):
        return super().description() + ", Карамель"

class Soy(BeverageDecorator):
    def cost(self):
        return super().cost() + 160.0
    def description(self):
        return super().description() + ", Соя сүті"

def fmt(x):
    return f"{int(x)} ₸" if float(x).is_integer() else f"{x:.2f} ₸"

def choose_base():
    print("Негізгі сусынды таңдаңыз:")
    print("1) Эспрессо")
    print("2) Шай")
    print("3) Латте")
    print("4) Мокка")
    x = input("Таңдау: ").strip()
    if x == "1":
        return Espresso()
    if x == "2":
        return Tea()
    if x == "3":
        return Latte()
    return Mocha()

def menu():
    drink = choose_base()
    while True:
        print("\nАғымдағы сусын:", drink.description(), "-", fmt(drink.cost()))
        print("Қоспа таңдаңыз:")
        print("1) Сүт (+150)")
        print("2) Қант (+50)")
        print("3) Көпіртілген кілегей (+200)")
        print("4) Карамель (+180)")
        print("5) Соя сүті (+160)")
        print("6) Дайын")
        x = input("Таңдау: ").strip()
        if x == "1":
            drink = Milk(drink)
        elif x == "2":
            drink = Sugar(drink)
        elif x == "3":
            drink = WhippedCream(drink)
        elif x == "4":
            drink = Caramel(drink)
        elif x == "5":
            drink = Soy(drink)
        elif x == "6":
            print("\nСипаттама:", drink.description())
            print("Жалпы құны:", fmt(drink.cost()))
            break
        else:
            print("Дұрыс емес енгізу")

if __name__ == "__main__":
    menu()
