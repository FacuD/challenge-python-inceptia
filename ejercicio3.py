_AVAILABLE_DISCOUNT_CODES = [
    "Primavera2021",
    "Verano2021",
    "Navidad2x1",
    "heladoFrozen",
]


def count_differences(discount_code1: str, discount_code2: str):
    return len(list(set(discount_code1) ^ set(discount_code2)))


def validate_discount_code(discount_code):
    """
    Ejemplo:
    "primavera2021" deberia devolver True, ya que al compararlo:
    vs "Primavera2021" = 2 caracteres de diferencia ("p" y "P")
    vs "Verano2021" = 7 caracteres de diferencia ('i', 'n', 'o',
    'm', 'V', 'p', 'v')
    vs "Navidad2x1" = 8 caracteres de diferencia ('N', 'm', '0',
    'x', 'e', 'd', 'p', 'r')
    vs "heladoFrozen" = 14 caracteres de diferencia ('z', 'i',
    'v', 'n', 'o', 'm', '2', '0', 'd', 'p', '1', 'F', 'h', 'l')
    """
    return [
        count_differences(discount_code, code) < 3 for code in _AVAILABLE_DISCOUNT_CODES
    ].count(True) > 0


if __name__ == "__main__":
    print(validate_discount_code("primavera2021"))
