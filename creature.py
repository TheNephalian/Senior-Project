class myCreature:
    def __init__(inputSize, die, hp, size):
        inputSize.die = die
        inputSize.hp = hp
        inputSize.size = size
    
    def myfun(inputSize):
        print(inputSize.size)