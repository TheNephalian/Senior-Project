class monster():
    def __init__(self, window):
        self.ui = window
        
        self.make_creature(self.ui.nameLineEdit.text(), self.ui.strSpinBox.value(), self.ui.dexSpinBox.value(), self.ui.conSpinBox.value())

    def print_stats(self, ui):
        print("Name:", ui.nameLineEdit.text())
        print("STR:", ui.strSpinBox.value())
        print("DEX:", ui.dexSpinBox.value())
        print("CON", ui.conSpinBox.value())

    def make_creature(self, name, str, dex, con):
        self.name = name
        self.str = str
        self.dex = dex
        self.con = con

        self.print_stats(self.ui)

    '''
    def make_creature(creature,
    name, str, dex, con, int, wis, cha,
    hp, ac, size, die, dpr, att_bonus,
    multiatt1, multiatt2, multiatt3, multiatt4,
    attDice1, attDice2, attDice3, attDice4):

        creature.name = name
        creature.str = str
        creature.dex = dex
        creature.con = con
        creature.int = int
        creature.wis = wis
        creature.cha = cha
        creature.hp = hp
        creature.ac = ac 
        creature.size = size
        creature.die = die
        creature.dpr = dpr
        creature.att_bonus = att_bonus
        creature.multiatt1 = multiatt1
        creature.multiatt2 = multiatt2
        creature.multiatt3 = multiatt3 
        creature.multiatt4 = multiatt4
        creature.attDice1 = attDice1
        creature.attDice2 = attDice2
        creature.attDice3 = attDice3
        creature.attDice4 = attDice4
    '''
        