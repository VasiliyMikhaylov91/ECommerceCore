from typing import Any

import pytest

from src.classes import Category, LawnGrass, Product, ProductsIterator, Smartphone


def test_category() -> None:
    """Проверка создания объекта категория"""

    Category.product_count = 0
    Category.category_count = 0
    Product.products = []
    product = Product("product1", "some product", 1.0, 7)
    category = Category("category1", "some category", [product])
    assert category.name == "category1"
    assert category.description == "some category"
    assert category.products == "product1, 1.0 руб. Остаток: 7 шт.\n"


def test_product() -> None:
    """Проверка создания объекта продукт"""

    Category.product_count = 0
    Category.category_count = 0
    Product.products = []
    product = Product("product1", "some product", 1.0, 7)
    assert product.name == "product1"
    assert product.description == "some product"
    assert product.price == 1.0
    assert product.quantity == 7


def test_product_count() -> None:
    """Проверка подсчета продуктов в категории"""

    Category.product_count = 0
    Category.category_count = 0
    Product.products = []
    product1 = Product("product1", "some product", 1.0, 7)
    product2 = Product("product2", "some product", 1.0, 7)
    product3 = Product("product3", "some product", 1.0, 7)
    category = Category("category1", "some category", [product1, product2, product3])
    assert category.product_count == 3


def test_category_count() -> None:
    """Проверка подсчета количества категорий"""

    Category.product_count = 0
    Category.category_count = 0
    Product.products = []
    product1 = Product("product1", "some product", 1.0, 7)
    product2 = Product("product2", "some product", 1.0, 7)
    product3 = Product("product3", "some product", 1.0, 7)
    category1 = Category("category1", "some category", [product1])
    category2 = Category("category2", "some category", [product2, product3])
    assert category1.category_count == 2
    assert category2.category_count == 2


def test_add_product() -> None:
    """Проверка добавления продукта в категорию"""

    Category.product_count = 0
    Category.category_count = 0
    Product.products = []
    product1 = Product("product1", "some product", 1.0, 7)
    category = Category("category1", "some category", [product1])
    product2 = Product("product2", "some product", 1.0, 7)
    category.add_product(product2)
    assert category.products == "product1, 1.0 руб. Остаток: 7 шт.\nproduct2, 1.0 руб. Остаток: 7 шт.\n"


def test_new_product() -> None:
    """Проверка создания нового экземпляра продукта с помощью словаря"""

    Category.product_count = 0
    Category.category_count = 0
    Product.products = []
    product1 = Product.new_product(
        {"name": "some product", "description": "some product", "price": 100, "quantity": 7}
    )
    assert product1.name == "some product"
    assert product1.description == "some product"
    assert product1.price == 100
    assert product1.quantity == 7


def test_add_identical_name_product() -> None:
    """Проверка добавления продукта с таким же именем в категорию"""

    Category.product_count = 0
    Category.category_count = 0
    Product.products = []
    product1 = Product("product1", "some product", 2, 7)
    print(product1)
    product2 = Product("product1", "some product", 1, 7)
    assert product2.price == 2
    assert product2.quantity == 14


def test_set_price() -> None:
    """Проверка установки цены продукту"""

    Category.product_count = 0
    Category.category_count = 0
    Product.products = []
    product1 = Product("product1", "some product", 1.0, 7)
    product1.price = 4
    assert product1.price == 4


def test_set_bad_price(capsys: Any) -> None:
    """Попытка установить нулевую или отрицательную цену продукту"""

    Category.product_count = 0
    Category.category_count = 0
    Product.products = []
    product = Product("product1", "some product", 1000.0, 7)
    product.price = 0
    captured = capsys.readouterr()
    assert captured.out == "Цена не должна быть нулевая или отрицательная\n"
    product.price = -70.0
    captured = capsys.readouterr()
    assert captured.out == "Цена не должна быть нулевая или отрицательная\n"


def test_product_str() -> None:
    """Проверка строкового представления продукта"""

    Category.product_count = 0
    Category.category_count = 0
    Product.products = []
    product = Product("product1", "some product", 1.0, 7)
    assert str(product) == "product1, 1.0 руб. Остаток: 7 шт."


def test_category_str() -> None:
    """Проверка строкового представления категории"""

    Category.product_count = 0
    Category.category_count = 0
    Product.products = []
    product1 = Product("product1", "some product", 1.0, 7)
    product2 = Product("product2", "some product", 1.0, 7)
    category = Category("category1", "some category", [product1, product2])
    assert str(category) == "category1, количество продуктов: 14 шт."


def test_add_products() -> None:
    """Проверка сложения продуктов"""

    Category.product_count = 0
    Category.category_count = 0
    Product.products = []
    product1 = Product("product1", "some product", 2.0, 5)
    product2 = Product("product2", "some product", 1.0, 10)
    assert product1 + product2 == 20


def test_products_iterator() -> None:
    """Проверка итератора продуктов в категории"""

    Category.product_count = 0
    Category.category_count = 0
    Product.products = []
    product1 = Product("product1", "some product", 2.0, 5)
    product2 = Product("product2", "some product", 1.0, 10)
    category = Category("category1", "some category", [product1, product2])
    test_iter = ProductsIterator(category)
    assert next(test_iter) == "product1, 2.0 руб. Остаток: 5 шт."
    assert next(test_iter) == "product2, 1.0 руб. Остаток: 10 шт."


def test_new_smartphone() -> None:
    """Проверка создания объекта смартфон"""

    Category.product_count = 0
    Category.category_count = 0
    Product.products = []
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"


def test_new_lawn_grass() -> None:
    """Проверка создания газонная трава"""

    Category.product_count = 0
    Category.category_count = 0
    Product.products = []
    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    assert grass1.name == "Газонная трава"
    assert grass1.description == "Элитная трава для газона"
    assert grass1.price == 500.0
    assert grass1.quantity == 20
    assert grass1.country == "Россия"
    assert grass1.germination_period == "7 дней"
    assert grass1.color == "Зеленый"


def test_different_type_products_add_error() -> None:
    """Проверка исключения при попытке сложить разные продукты"""

    Category.product_count = 0
    Category.category_count = 0
    Product.products = []
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    with pytest.raises(TypeError):
        smartphone1 + grass1


def test_add_not_product_to_error() -> None:
    """Проверка исключения при попытке добавления не продукта в категорию"""
    Category.product_count = 0
    Category.category_count = 0
    Product.products = []
    product1 = Product("product1", "some product", 1.0, 7)
    category = Category("category1", "some category", [product1])
    with pytest.raises(TypeError):
        category.add_product("Not a Product")
