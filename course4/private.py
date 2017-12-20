class Base(object):


    def __private(self):
        print("private value in Base")


    def _protected(self):
        print("protected value in Base")


    def public(self):
        print("public value in Base")
        self.__private()
        self._protected()


class Derived(Base):
    def __private(self):
        print("override private")

    def _protected(self):
        print("override protected")



dir(Base)
print("=" * 80)
d = Derived()
d.public()
d._protected()
d._Derived__private()
print("=" * 80)
d.__private()