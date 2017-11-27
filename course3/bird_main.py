from  Bird import Bird


if __name__ == "__main__":
    sparrow = Bird('Sparrow', True)
    print(sparrow)
    sparrow.fly()
    print(sparrow.lay_egg)
    print()

    pigeon = Bird('Pigeon', False)
    print(pigeon)
    print(pigeon.lay_egg)
    pigeon.fly()