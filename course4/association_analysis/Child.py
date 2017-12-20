from course4.association_analysis.Parent import Parent


class Child(Parent):
    def __init__(self):
        # super().__init__()
        print('child')


if __name__ == "__main__":
    jim= Child()
    print(jim.name)
