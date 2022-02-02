from offensiveCR import *
from defensiveCR import *

'''Main test function
	Call other test functions and comment out as desired'''
def function_test():
	print("***Testing functions...***")
	#test_cal_pros_offensive_CR()
	#test_cal_pros_prof_bns()
	#test_cal_attr_bns()
	#test_HP_def_CR()
	#test_true_CR()
	return

'''Individual test functions'''
def test_cal_pros_offensive_CR():
	print("*Testing cal_pros_offensive_CR*")
	print(cal_pros_offensive_CR(2)); '''Should print 1/4'''
	print(cal_pros_offensive_CR(21)); '''Should print 3'''
	print(cal_pros_offensive_CR(210)); '''Should print 24'''
	print(cal_pros_offensive_CR(410)); '''Should print error message. Also, prints 'None' as no value is actually returned by cal_offensive_CR'''
	return

def test_cal_pros_prof_bns():
	print("*Testing cal_pros_prof_bns*")
	print(cal_pros_prof_bns(0)); '''Should print 2'''
	print(cal_pros_prof_bns(2)); '''Should print 2'''
	print(cal_pros_prof_bns(4)); '''Should print 2'''
	print(cal_pros_prof_bns(6)); '''Should print 3'''
	print(cal_pros_prof_bns(13)); '''Should print 5'''
	print(cal_pros_prof_bns(20)); '''Should print 6'''
	print(cal_pros_prof_bns(26)); '''Should print 8'''
	print(cal_pros_prof_bns(29)); '''Should print 9'''
	print(cal_pros_prof_bns(33)); '''Should print error message. Also, prints 'None' as no value is actually returned by cal_pros_prof_bns'''
	return

def test_cal_attr_bns():
	print("*Testing cal_attr_bns with even attribute scores*")
	print(cal_attr_bns(0)); '''Should print -5'''
	print(cal_attr_bns(2)); '''Should print -4'''
	print(cal_attr_bns(6)); '''Should print -2'''
	print(cal_attr_bns(10)); '''Should print 0'''
	print(cal_attr_bns(14)); '''Should print 2'''
	print(cal_attr_bns(20)); '''Should print 5'''
	print(cal_attr_bns(30)); '''Should print 10'''
	print("*Testing of cal_attr_bns with odd attribute scores*")
	print(cal_attr_bns(1)); '''Should print -5'''
	print(cal_attr_bns(5)); '''Should print -3'''
	print(cal_attr_bns(9)); '''Should print -1'''
	print(cal_attr_bns(11)); '''Should print 0'''
	print(cal_attr_bns(17)); '''Should print 3'''
	print(cal_attr_bns(23)); '''Should print 6'''
	print(cal_attr_bns(29)); '''Should print 9'''
	return

'''More complex function tests'''
def test_cal_init_off_CR(dmg_per_rnd, exptd_CR, attr, uses_saves):
	print("*Testing of cal_init_off_CR with given arguments*")
	print(cal_init_off_CR(dmg_per_rnd, exptd_CR, attr, uses_saves))
	return


def test_HP_def_CR():
    print("Testing Defensive CR")
    print(cal_HP_defensive_CR(116)); '''Should print 4'''
    print(cal_HP_defensive_CR(330)); '''Should print 18'''
    print(cal_HP_defensive_CR(823)); '''Should print 30'''
    print(cal_HP_defensive_CR(1)); '''Should print 0'''
    print(cal_HP_defensive_CR(500)); '''Should print 23'''
    
def test_true_CR():
    print("Testing Defensive CR the real one")
    current_creature_CR = cal_HP_defensive_CR(115)
    curr_AC = calculate_stuff(115)
    print(get_CR_rating(curr_AC ,current_creature_CR, 19)) ; '''Should print 6'''
    