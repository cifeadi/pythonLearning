

import logging

"""testing git234"""


class Generic:

    test = 0
    def __init__(self, val):
        self.test = val

        return None





def main():
    v = Generic(6)
    print("Printing:" + str(v.test))



main()