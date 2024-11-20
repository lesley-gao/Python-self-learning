# import customized module, which in this case is "my_module"
import my_module
my_module.test(3,2)    # Result: 5


# When importing multiple modules, if the modules have functions with the same name,
# the function from the last imported module will be used.
# In the example below, the test function being called is the one from my_module2.
from my_module import test
from my_module2 import test
test(3,2)    # Result: 1
