def test(x, y):
    print(x + y)

# "if __name__ == '__main__':" ensures the test function is only called when the current file is executed directly,
# and it will not be executed when the file is imported into another file.
if __name__ == '__main__':
    test(1,1)