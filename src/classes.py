from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):

    @abstractmethod
    def new_product(self, *args: Any, **kwargs: Any) -> "Product":
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __add__(self, other: "Product") -> float:
        pass


class Info:

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__()
        self.args = args
        print(f"{self.__class__.__name__}{self.args}")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}{self.args}"


class Product(Info, BaseProduct):
    name: str
    description: str
    quantity: int
    products: list = []

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        for i in range(len(Product.products)):
            if Product.products[i].name == name:
                self.__price = price if price > Product.products[i].price else Product.products[i].price
                self.quantity = quantity + Product.products[i].quantity
                Product.products[i] = self
                break
        else:
            if not quantity:
                raise ValueError("Товар с нулевым количеством не может быть добавлен.")
            self.__price = price
            self.quantity = quantity
            Product.products.append(self)
            super().__init__(name, description, price, quantity)

    @classmethod
    def new_product(cls, info: dict) -> "Product":
        return cls(info["name"], info["description"], info["price"], info["quantity"])

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if self.__price > price and input("Вы уверены что хотите понизить цену товара Y - да, N - нет").upper() != "Y":
            return
        self.__price = price

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        if type(self) is not type(other):
            raise TypeError("Можно складывать только одинаковые классы продуктов")
        return self.price * self.quantity + other.price * other.quantity


class ProductInfo(ABC):

    @property
    @abstractmethod
    def products(self) -> str:
        pass


class ZeroQuantityException(Exception):

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self.message = args[0] if args else "Нельзя добавить товар с нулевым количеством"

    def __str__(self) -> str:
        return self.message


class Category(ProductInfo):
    name: str
    description: str
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        self.name = name
        self.description = description
        for product in products:
            if not product.quantity:
                raise ZeroQuantityException
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("Объект не принадлежит классу продуктов")
        if not product.quantity:
            raise ZeroQuantityException
        self.__products.append(product)
        Category.product_count += 1

    def middle_price(self) -> float:
        try:
            result = sum([x.price for x in self.__products]) / Category.product_count
        except ZeroDivisionError:
            result = 0.0
        return result

    @property
    def products(self) -> str:
        result = ""
        for product in self.__products:
            result += str(product) + "\n"
        return result

    def __str__(self) -> str:
        return f"{self.name}, количество продуктов: {sum(x.quantity for x in self.__products)} шт."


class ProductsIterator:

    def __init__(self, category: Category) -> None:
        self.products = category.products.split("\n")

    def __iter__(self) -> "ProductsIterator":
        return self

    def __next__(self) -> str:
        if not self.products:
            raise StopIteration
        else:
            return self.products.pop(0)


class Smartphone(Product):

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    @classmethod
    def new_product(cls, info: dict) -> "Smartphone":
        return cls(
            info["name"],
            info["description"],
            info["price"],
            info["quantity"],
            info["efficiency"],
            info["model"],
            info["memory"],
            info["color"],
        )


class LawnGrass(Product):

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    @classmethod
    def new_product(cls, info: dict) -> "LawnGrass":
        return cls(
            info["name"],
            info["description"],
            info["price"],
            info["quantity"],
            info["country"],
            info["germination_period"],
            info["color"],
        )


class Order(ProductInfo):

    def __init__(self, product: Product, quantity: int) -> None:
        if not product.quantity:
            raise ZeroQuantityException
        self.quantity = quantity
        order_price = product.price * quantity
        self.__price = order_price
        self.__product = product

    @property
    def price(self) -> float:
        return self.__price

    @property
    def products(self, *args: Any, **kwargs: Any) -> str:
        result = ""
        result += f"{self.__product.name}\t{self.quantity}\t{self.price}\n"
        return result
