from offensiveCR import *
from defensiveCR import *
import math

def cal_crtr_CR(dmg, exptd_CR, attr_scr, uses_saves, ac, hp):
    off_CR = cal_init_off_CR(dmg, exptd_CR, attr_scr, uses_saves)
    def_CR = cal_init_def_CR(hp, ac)

    crtr_CR = (off_CR + def_CR) / 2
    return math.floor(crtr_CR)