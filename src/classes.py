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
        self.__products.append(product)

    @property
    def products(self) -> str:
        result = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток {product.quantity} шт.\n"
        return result
