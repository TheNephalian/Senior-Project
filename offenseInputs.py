import math

'''Function that adds creature's attack damage of seperate attacks
	Must be called separately between each attack, as a monster can have any number of attacks to determine the total damage a creature can do on its turn'''
def add_atk_dmg(atk_dmg, nxt_atk_dmg):
	tot_atk_dmg = atk_dmg + nxt_atk_dmg
	return tot_atk_dmg

'''Function that calculates an attack's damage for a Melee or Ranged Weapon attack
	Determined by:
		the number of damage dice (num_d)
		the die type (dt)
		the creature's associated attribute (attr)
	Returns the attack's damage (atk_dmg)'''
def cal_atk_dmg(num_d, dt, attr):
	if (dt == "d4"):
		dmg_per_die = 2.5

	elif (dt == "d6"):
		dmg_per_die = 3.5

	elif (dt == "d8"):
		dmg_per_die = 4.5

	elif (dt == "d10"):
		dmg_per_die = 5.5

	elif (dt == "d12"):
		dmg_per_die = 6.5

	else:
		print("Error in offensiveInputs.py cal_atk dmg.")

	base_dmg = dmg_per_die * num_d

	attr_bns = math.floor((attr - 10)/2)

	atk_dmg = math.floor(base_dmg + attr_bns)

	return atk_dmg

'''Function that calculates an attack's damage for an attack that isn't categorically a Melee or Ranged Weapon Attack
	This usually means the attack is an area of effect (AOE) and can damage >=2 other creatures
	Determined by:
		the number of damage dice (num_d)
		the die type (dt)
		a boolean expressing whether the attack is an AOE or not, if so a doubling factor is required <- we always assume 2 creatures are hit by the attack
	Returns the attack's damage (atk_dmg)'''
def cal_atk_dmg(num_d, dt, is_aoe):
	if (dt == "d4"):
		dmg_per_die = 2.5

	elif (dt == "d6"):
		dmg_per_die = 3.5

	elif (dt == "d8"):
		dmg_per_die = 4.5

	elif (dt == "d10"):
		dmg_per_die = 5.5

	elif (dt == "d12"):
		dmg_per_die = 6.5

	else:
		print("Error in offensiveInputs.py cal_atk dmg. Cannot determine die type (dt)")

	base_dmg = dmg_per_die * num_d

	if (is_aoe == True):
		atk_dmg = math.floor(base_dmg * 2)

	elif (is_aoe == False):
		atk_dmg = math.floor(base_dmg)

	else:
		print("Error in offensive.Inputs.py cal_atk_dmg. Cannot determine is_aoe")

	return atk_dmg