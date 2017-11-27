class Bird:
    __name=''
    __has_feather=True
    lay_egg='Yes, we can lay eggs.'

    def __init__(self,name,has_feather):
        self.__name=name
        self.__has_feather=has_feather

    def getName(self):
        return  self.__name

    def fly(self):
        if(self.__has_feather):
            print(self.__name+ ' can fly.')
        else:print(self.__name+ ' can not fly.')

    def __str__(self):
        return "Name: %s"%self.__name
