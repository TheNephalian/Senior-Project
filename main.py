from offensiveCR import cal_pros_offensive_CR
from offensiveCR import cal_pros_prof_bns

'''Testing of functions'''
print("***Testing cal_pros_offensive_CR***")
print(cal_pros_offensive_CR(2)); '''Should print 1/4'''
print(cal_pros_offensive_CR(21)); '''Should print 3'''
print(cal_pros_offensive_CR(210)); '''Should print 24'''
print(cal_pros_offensive_CR(410)); '''Should print error message. Also, prints 'None' as no value is actually returned by cal_offensive_CR'''

print()

print("***Testing cal_pros_prof_bns***")
print(cal_pros_prof_bns(0)); '''Should print 2'''
print(cal_pros_prof_bns(2)); '''Should print 2'''
print(cal_pros_prof_bns(4)); '''Should print 2'''
print(cal_pros_prof_bns(6)); '''Should print 3'''
print(cal_pros_prof_bns(13)); '''Should print 5'''
print(cal_pros_prof_bns(20)); '''Should print 6'''
print(cal_pros_prof_bns(26)); '''Should print 8'''
print(cal_pros_prof_bns(29)); '''Should print 9'''
print(cal_pros_prof_bns(33)); '''Should print error message. Also, prints 'None' as no value is actually returned by cal_pros_prof_bns'''