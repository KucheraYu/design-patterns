from abc import ABC, abstractmethod


class Burger(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass


class Pizza(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass


class MeatBurger(Burger):
    def get_description(self) -> str:
        return "Бургер з курячою котлетою"


class MeatPizza(Pizza):
    def get_description(self) -> str:
        return "Піца Баварська з подвійним сиром"


class VeganBurger(Burger):
    def get_description(self) -> str:
        return "Бургер з соєвою котлетою"


class VeganPizza(Pizza):
    def get_description(self) -> str:
        return "Піца з тофу та грибами"


class MenuFactory(ABC):
    @abstractmethod
    def create_burger(self) -> Burger:
        pass

    @abstractmethod
    def create_pizza(self) -> Pizza:
        pass


class MeatMenuFactory(MenuFactory):
    def create_burger(self) -> Burger:
        return MeatBurger()

    def create_pizza(self) -> Pizza:
        return MeatPizza()


class VeganMenuFactory(MenuFactory):
    def create_burger(self) -> Burger:
        return VeganBurger()

    def create_pizza(self) -> Pizza:
        return VeganPizza()


def order_combo(factory: MenuFactory):

    burger = factory.create_burger()
    pizza = factory.create_pizza()

    print(f"{burger.get_description()}")
    print(f"{pizza.get_description()}")


if __name__ == "__main__":
    print("Клієнт замовив звичайне меню")
    order_combo(MeatMenuFactory())
    print()
    print("Клієнт замовив веганське меню")
    order_combo(VeganMenuFactory())