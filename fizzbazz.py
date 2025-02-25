def get_info(name: str) -> str:
    """
    IDI NAXUI
    :param name: Your name
    :return: Your name gigi
    """
    if name == "LEXA":
        yield "You are Pidor"
    else:
        yield "You're blessed"


print(get_info('LEXA'))
print(get_info('Burp'))
