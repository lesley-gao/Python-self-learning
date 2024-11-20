"""
These functions will be used in package.py
"""


def str_reverse(s):
    """
    Function: Reverse the given string
    :param s: The string to be reversed
    :return: The reversed string
    """
    reversed_str = s[::-1]
    return reversed_str # 切片操作实现反转


def substr(s, x, y):
    """
    Function: Slice the given string based on the specified indices
    :param s: The string to be sliced
    :param x: The starting index of the slice
    :param y: The ending index of the slice
    :return: The sliced substring
    """
    sliced_str = s[x:y]
    return sliced_str

if __name__ == '__main__':
    print(str_reverse("hello"))
    print(substr("hello", 0, 3))
