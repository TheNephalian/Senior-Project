import math

'''Function that adds creature's attack damage of seperate attacks
	Must be called separately between each attack, as a monster can have any number of attacks to determine the total damage a creature can do on its turn'''
def add_atk_dmg(atk_dmg, nxt_atk_dmg):
	tot_atk_dmg = atk_dmg + nxt_atk_dmg
	return tot_atk_dmg

'''Function that calculates an attack's damage'''
def cal_atk_dmg(num_d, dn, attr):
	if (dn == "d4"):
		dmg_per_die = 2.5

	elif (dn == "d6"):
		dmg_per_die = 3.5

	elif (dn == "d8"):
		dmg_per_die = 4.5

	elif (dn == "d10"):
		dmg_per_die = 5.5

	elif (dn == "d12"):
		dmg_per_die = 6.5

	else:
		print("Error in offensiveInputs.py cal_atk dmg.")

	base_dmg = dmg_per_die * num_d

	attr_bns = math.floor((attr - 10)/2)

	atk_dmg = math.floor(base_dmg + attr_bns)

	return atk_dmg