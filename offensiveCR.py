import math

'''Function that calculates the prospecteve Offensive Challenge Rating (pros_off_CR) of the creature based on its damage per round (dmg_per_rnd)
	This is the first step of calculating a creature's overall CR, which is to calculate its Offensive CR

	dmg_per_round must be a value between 0-320
	Returns pros_Off_CR'''
def cal_pros_offensive_CR(dmg_per_rnd):
	if (dmg_per_rnd <= 1):
		pros_off_CR = 0
		return pros_off_CR

	elif (dmg_per_rnd <= 3):
		pros_off_CR = 1/8
		return pros_off_CR

	elif (dmg_per_rnd <= 5):
		pros_off_CR = 1/4
		return pros_off_CR

	elif (dmg_per_rnd<= 8):
		pros_off_CR = 1/2
		return pros_off_CR

	elif (dmg_per_rnd <= 14):
		pros_off_CR = 1
		return pros_off_CR

	elif (dmg_per_rnd <= 14):
		pros_off_CR = 1
		return pros_off_CR

	elif (dmg_per_rnd <= 20):
		pros_off_CR = 2
		return pros_off_CR

	elif (dmg_per_rnd <= 26):
		pros_off_CR = 3
		return pros_off_CR

	elif (dmg_per_rnd <= 32):
		pros_off_CR = 4
		return pros_off_CR

	elif (dmg_per_rnd <= 38):
		pros_off_CR = 5
		return pros_off_CR

	elif (dmg_per_rnd <= 44):
		pros_off_CR = 6
		return pros_off_CR

	elif (dmg_per_rnd <= 50):
		pros_off_CR = 7
		return pros_off_CR

	elif (dmg_per_rnd <= 56):
		pros_off_CR = 8
		return pros_off_CR

	elif (dmg_per_rnd <= 62):
		pros_off_CR = 9
		return pros_off_CR

	elif (dmg_per_rnd <= 68):
		pros_off_CR = 10
		return pros_off_CR

	elif (dmg_per_rnd <= 74):
		pros_off_CR = 11
		return pros_off_CR

	elif (dmg_per_rnd <= 80):
		pros_off_CR = 12
		return pros_off_CR

	elif (dmg_per_rnd <= 86):
		pros_off_CR = 13
		return pros_off_CR

	elif (dmg_per_rnd <= 92):
		pros_off_CR = 14
		return pros_off_CR

	elif (dmg_per_rnd <= 98):
		pros_off_CR = 15
		return pros_off_CR

	elif (dmg_per_rnd <= 104):
		pros_off_CR = 16
		return pros_off_CR

	elif (dmg_per_rnd <= 110):
		pros_off_CR = 17
		return pros_off_CR

	elif (dmg_per_rnd <= 116):
		pros_off_CR = 18
		return pros_off_CR

	elif (dmg_per_rnd <= 122):
		pros_off_CR = 19
		return pros_off_CR

	elif (dmg_per_rnd <= 140):
		pros_off_CR = 20
		return pros_off_CR

	elif (dmg_per_rnd <= 158):
		pros_off_CR = 21
		return pros_off_CR

	elif (dmg_per_rnd <= 176):
		pros_off_CR = 22
		return pros_off_CR

	elif (dmg_per_rnd <= 194):
		pros_off_CR = 23
		return pros_off_CR

	elif (dmg_per_rnd <= 212):
		pros_off_CR = 24
		return pros_off_CR

	elif (dmg_per_rnd <= 230):
		pros_off_CR = 25
		return pros_off_CR

	elif (dmg_per_rnd <= 248):
		pros_off_CR = 26
		return pros_off_CR

	elif (dmg_per_rnd <= 266):
		pros_off_CR = 27
		return pros_off_CR

	elif (dmg_per_rnd <= 284):
		pros_off_CR = 28
		return pros_off_CR

	elif (dmg_per_rnd <= 302):
		pros_off_CR = 29
		return pros_off_CR

	elif (dmg_per_rnd <= 320):
		pros_off_CR = 30
		return pros_off_CR

	else:
		print("Error. Damage must be within 0-320.")

'''Function that calculates the prospected proficiency bonus (pros_prof_bns) of the creature based on its expected Challenge Rating (CR)
	Expected CR is input by the user and used to calculate initial proficiency bonuses to the creature

	expted_CR must be a value between 0-30
	Returns pros_prof_bns'''
def cal_pros_prof_bns(exptd_CR):
	if (exptd_CR in range(0, 5)):
		pros_prof_bns = 2
		return pros_prof_bns

	elif (exptd_CR in range(5, 9)):
		pros_prof_bns = 3
		return pros_prof_bns

	elif (exptd_CR in range(9, 13)):
		pros_prof_bns = 4
		return pros_prof_bns

	elif (exptd_CR in range(13, 17)):
		pros_prof_bns = 5
		return pros_prof_bns

	elif (exptd_CR in range(17, 21)):
		pros_prof_bns = 6
		return pros_prof_bns

	elif (exptd_CR in range(21, 25)):
		pros_prof_bns = 7
		return pros_prof_bns

	elif (exptd_CR in range(25, 29)):
		pros_prof_bns = 8
		return pros_prof_bns

	elif (exptd_CR in range(29, 31)):
		pros_prof_bns = 9
		return pros_prof_bns

	else:
		print("Error. Expected Challenge Rating must be between 0-30.")

'''Function that calculates the creature's Strength bonus (STR_bns)
	This is determined by the creature's Strength (STR)
	
	Returns STR_bns'''
def cal_str_bns(STR):
	STR_bns = math.floor((STR - 10)/2)
	return STR_bns

'''Function that calculates the creature's Dexterity bonus (DEX_bns)
	This is determined by the creature's Dexterity (DEX)
	
	Returns DEX_bns'''
def cal_dex_bns(DEX):
	DEX_bns = math.floor((DEX - 10)/2)
	return DEX_bns

'''Function that calculates the monster's prospective attack bonus (pros_atk_bns) for melee or ranged attacks
	This requires several parameters:
		the prospective proficiency bonus (pros_prof_bns)
		the creature's Strength bonus (STR_bns) or
		the creature's Dexterity bonus (DEX_bns)
		and whether the attack uses the creature's STR or DEX (str_or_dex)
	
	Returns pros_atk_bns'''
def cal_pros_atk_bns(pros_prof_bns, STR_bns, DEX_bns, str_or_dex):
	if (str_or_dex == "STR"):
		pros_atk_bns = pros_prof_bns + STR_bns
		return pros_atk_bns

	elif (str_or_dex == "DEX"):
		pros_atk_bns = pros_prof_bns + DEX_bns
		return pros_atk_bns

	else:
		print("Error. Could not calculate prospective Attack Bonus.")
