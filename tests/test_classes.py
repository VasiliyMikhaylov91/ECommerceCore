from typing import Any

from src.classes import Category, Product


def test_category() -> None:
    Category.product_count = 0
    Category.category_count = 0
    Product.products = []
    product = Product("product1", "some product", 1.0, 7)
    category = Category("category1", "some category", [product])
    assert category.name == "category1"
    assert category.description == "some category"
    assert category.products == "product1, 1.0 руб. Остаток 7 шт.\n"


def test_product() -> None:
    Category.product_count = 0
    Category.category_count = 0
    Product.products = []
    product = Product("product1", "some product", 1.0, 7)
    assert product.name == "product1"
    assert product.description == "some product"
    assert product.price == 1.0
    assert product.quantity == 7


def test_product_count() -> None:
    Category.product_count = 0
    Category.category_count = 0
    Product.products = []
    product1 = Product("product1", "some product", 1.0, 7)
    product2 = Product("product2", "some product", 1.0, 7)
    product3 = Product("product3", "some product", 1.0, 7)
    category = Category("category1", "some category", [product1, product2, product3])
    assert category.product_count == 3


def test_category_count() -> None:
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
    Category.product_count = 0
    Category.category_count = 0
    Product.products = []
    product1 = Product("product1", "some product", 1.0, 7)
    category = Category("category1", "some category", [product1])
    product2 = Product("product2", "some product", 1.0, 7)
    category.add_product(product2)
    assert category.products == "product1, 1.0 руб. Остаток 7 шт.\nproduct2, 1.0 руб. Остаток 7 шт.\n"


def test_new_product() -> None:
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
    Category.product_count = 0
    Category.category_count = 0
    Product.products = []
    product1 = Product("product1", "some product", 2, 7)
    print(product1)
    product2 = Product("product1", "some product", 1, 7)
    assert product2.price == 2
    assert product2.quantity == 14


def test_set_price(capsys: Any) -> None:
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
