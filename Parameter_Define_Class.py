from attr import attrs, attrib, fields
class Parameters:

    def __init__(self,att_name):
        print(att_name)
        self.__keys = att_name
        print(self.__dict__)

    def print_all(self):
        for i, k in enumerate(self.__keys):
            print("{}={}".format(k, getattr(self, k)))

    def load_vals(self, vals):
        for i, k in enumerate(self.__keys):
            setattr(self, k, vals[i])
        print(vals)
    def get_vals(self):
        ulist =[]
        for i, k in enumerate(self.__keys):
            ulist.append(getattr(self,k))
        return ulist
    def print_line(self):
        res = ''
        for i, k in enumerate(self.__keys):
            if i > 0:
                res += ' '
            res += getattr(self, k)
        return res


if __name__ == "__main__":

    va_name = ['_ON', '_OFF', '_IP', '_PL', '_V', '_HP', '_PP', '_AL', '_OC', '_LD']
    va_data = ['50','20','30','-','500','1','5','3','4','6']
    n = Parameters(va_name)
    # #print(n.__keys)
    n.load_vals(va_data)
    print('the end..')
    print(n.get_vals())
    # #print(n.__dict__)
    # #n.load_vals(va_name,va_data)
    # n.print_all()
    # va_data = ['1', '2', '3', '4', '5', '1', '5', '3', '4', '6']
    # n.load_vals(va_data)
    # n.print_all()
    # print(n._ON)
    # #print(n.print_line())

