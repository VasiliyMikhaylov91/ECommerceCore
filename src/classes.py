class Product:
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
            self.__price = price
            self.quantity = quantity
            Product.products.append(self)

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


class Category:
    name: str
    description: str
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("Объект не принадлежит классу продуктов")
        self.__products.append(product)
        Category.product_count += 1

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
