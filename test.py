class Test:
    def __init__(self, **kwargs):
        self.item_dict = {item: name for item, name in kwargs.items()}
        self.one = self.item_dict['test1']
        self.two = self.item_dict['test2']


    def func_1(self):
        print(self.item_dict)
        print(sum([self.one, self.two]))

a = Test(test1=1, test2=2)
a.func_1()


def type_test(smth):
    if type(smth) is tuple:
        print('tuple')
    elif type(smth) is str:
        print('str')
    else:
        print('enough')

type_test('test')
type_test((1,2,3,4))