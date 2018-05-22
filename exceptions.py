
# bases:
# Exception -> 常规异常
# AttributeError -> 对象没有这个属性
# KeyError -> 没有这个键
# RuntimeError -> 运行时错误
# NotImplementedError -> 未实现的方法
# TypeError -> 类型错误
# ValueError -> 传入参数错误


class CardInfoError(TypeError):
    def __init__(self, arg):
        self.args = 'Wrong card info: ' + arg
        TypeError.__init__(self, arg)

class ProducingError(TypeError):
    def __init__(self, arg):
        self.args = 'Wrong in producing: ' + arg
        TypeError.__init__(self, arg)

class CountryNotFoundError(ValueError):
    def __init__(self, arg):
        self.args = 'Country not found: ' + arg
        ValueError.__init__(self, arg)

class InvalidArgumentError(ValueError):
    def __init__(self, arg):
        self.args = 'Invalid argument: ' + arg
        ValueError.__init__(self, arg)