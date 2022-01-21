from offensiveCR import *

'''Main test function
	Call other test functions and comment out as desired'''
def function_test():
	print("***Testing functions...***")
	#test_cal_pros_offensive_CR
	#test_cal_pros_prof_bns
	#test_cal_str_bns()
	#test_cal_dex_bns()
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

def test_cal_str_bns():
	print("*Testing of cal_str_bns*")
	print(cal_str_bns(0)); '''Should print -5'''
	print(cal_str_bns(2)); '''Should print -4'''
	print(cal_str_bns(6)); '''Should print -2'''
	print(cal_str_bns(10)); '''Should print 0'''
	print(cal_str_bns(14)); '''Should print 2'''
	print(cal_str_bns(20)); '''Should print 5'''
	print(cal_str_bns(30)); '''Should print 10'''
	return

def test_cal_dex_bns():
	print("*Testing of cal_dex_bns*")
	print(cal_dex_bns(1)); '''Should print -5'''
	print(cal_dex_bns(5)); '''Should print -3'''
	print(cal_dex_bns(9)); '''Should print -1'''
	print(cal_dex_bns(11)); '''Should print 0'''
	print(cal_dex_bns(17)); '''Should print 3'''
	print(cal_dex_bns(23)); '''Should print 6'''
	print(cal_dex_bns(29)); '''Should print 9'''
	return