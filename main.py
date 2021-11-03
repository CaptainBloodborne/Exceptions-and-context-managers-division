from typing import Union


def divide(str_with_ints: str) -> Union[float, str]:
    """
    Returns the result of dividing two numbers or an error message.
    :arg
        str_with_ints: str, ex. "4 2";
    :return
        result of dividing: float, ex. 2.0 (4 / 2 = 2.0);
        error response in "Error code: {error message}: str;
    """
    try:
        a, b = str_with_ints.split(" ", maxsplit=1)
        return int(a) / int(b)
    except Exception as error:
        return f"Error code: {error}"


print(divide("7 2 "))
