import pandas as pd

_PRODUCT_DF = pd.DataFrame(
    {
        "product_name": ["Chocolate", "Granizado", "Limon", "Dulce de Leche"],
        "quantity": [3, 10, 0, 5],
    }
)


class ProductDoesntExistException(Exception):
    pass


def is_product_available(product_name, quantity):
    products_dict = _PRODUCT_DF.set_index("product_name").to_dict()["quantity"]

    try:
        product_quantity = products_dict[product_name]
        return product_quantity >= quantity
    except KeyError:
        raise ProductDoesntExistException


if __name__ == "__main__":
    queried_products = []
    product_name = input("Enter a product name: ")
    quantity = int(input("Enter a quantity: "))

    while product_name not in queried_products:
        queried_products.append(product_name)
        is_product_available(product_name, quantity)
        product_name = input("Enter a product name: ")
        quantity = int(input("Enter a quantity: "))

    print("You already queried that product.")
