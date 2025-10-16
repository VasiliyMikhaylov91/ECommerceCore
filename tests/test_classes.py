from src.classes import Category, Product

def test_category():
    product = Product("product1", "some product", 1.0, 7)
    category = Category("category1", "some category",
                        [product])
    assert category.name == "category1"
    assert category.description == "some category"
    assert category.products == [product]
    Category.product_count = 0
    Category.category_count = 0

def test_product():
    product = Product("product1", "some product", 1.0, 7)
    assert product.name == "product1"
    assert product.description == "some product"
    assert product.price == 1.0
    assert product.quantity == 7
    Category.product_count = 0
    Category.category_count = 0

def test_product_count():
    product1 = Product("product1", "some product", 1.0, 7)
    product2 = Product("product2", "some product", 1.0, 7)
    product3 = Product("product3", "some product", 1.0, 7)
    assert Category.product_count == 3
    Category.product_count = 0
    Category.category_count = 0

def test_category_count():
    product1 = Product("product1", "some product", 1.0, 7)
    product2 = Product("product2", "some product", 1.0, 7)
    product3 = Product("product3", "some product", 1.0, 7)
    category1 = Category("category1", "some category", [product1])
    category2 = Category("category2", "some category", [product2, product3])
    assert category1.category_count == 2
    assert category2.category_count == 2
    Category.product_count = 0
    Category.category_count = 0