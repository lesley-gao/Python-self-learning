class Phone:
    __is_5g_enable = True

    # private method
    def __check_5g(self):
        if self.__is_5g_enable:
            print("5G on")
        else:
            print("5G off, use 4G.")

    # public method
    def call_by_5g(self):
        self.__check_5g()
        print("On a call")


phone = Phone()
phone.call_by_5g()