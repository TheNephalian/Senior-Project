import math

'''Function that calculates the prospective Offensive Challenge Rating (pros_off_CR) of the creature
	This is the first step of calculating a creature's overall Challenge Rating: to calculate its Offensive Challenge Rating
	Determined by:
		the creature's damage per round (dmg_per_rnd)

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

	elif (dmg_per_rnd <= 8):
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
		pros_off_CR = 30
		return pros_off_CR

'''Function that calculates the prospected proficiency bonus (pros_prof_bns) of the creature
	Expected CR is input by the user and used to calculate initial proficiency bonuses to the creature
	Determined by:
		the creature's expected Challenge Rating (exptd_CR)

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

'''Function that calculates the creature's attribute bonus (attr_bns)
	Determined by:
		the creature's attribute given to the function (attr)
	
	Returns attr_bns'''
def cal_attr_bns(attr):
	attr_bns = int(math.floor((attr - 10)/2))
	return attr_bns

'''Function that calculates the creature's prospective attack bonus (pros_atk_bns) for attacks
	Determined by:
		the creature's prospective proficiency bonus (pros_prof_bns)
		the creature's attribute bonus associated with the attack (attr_bns)
	
	Returns pros_atk_bns'''
def cal_pros_atk_bns(pros_prof_bns, attr_bns):
	pros_atk_bns = pros_prof_bns + attr_bns
	return pros_atk_bns

'''Function that calculates the creature's save DC (ctr_save_DC)
	Used only if the creature's offensive abilities use saves
	Determined by:
		the creature's associated attribute (attr)
		the creature's expected Challenge Rating (exptd_CR)
		
	Returns the creature's save DC'''
def cal_save_DC(exptd_CR, attr):
	pros_prof_bns = cal_pros_prof_bns(exptd_CR)
	attr_bns = cal_attr_bns(attr)

	ctr_save_DC = 8 + pros_prof_bns + attr_bns
	return ctr_save_DC

'''Function that calculates the creature's corrected Offensive Challenge Rating (corr_off_CR)
	Determined by:
		the creature's calculated proficiency bonus (pros_pros_bns)
		the creature's attribute bonus (attr_bns)'''
def cal_corr_off_CR(exptd_CR, attr, uses_saves):
	pros_prof_bns = cal_pros_prof_bns(exptd_CR)
	attr_bns = cal_attr_bns(attr)

	if (uses_saves == False):
		atk_bns = cal_pros_atk_bns(pros_prof_bns, attr_bns)
		
		print("Prospective attack bonus is ")

		if (atk_bns <=3):
			corr_off_CR = 1/2
			return corr_off_CR

		elif (atk_bns == 4):
			corr_off_CR = 3
			return corr_off_CR

		elif (atk_bns == 5):
			corr_off_CR = 4
			return corr_off_CR

		elif (atk_bns == 6):
			corr_off_CR = 6
			return corr_off_CR

		elif (atk_bns == 7):
			corr_off_CR = 9
			return corr_off_CR

		elif (atk_bns == 8):
			corr_off_CR = 13
			return corr_off_CR

		elif (atk_bns == 9):
			corr_off_CR = 16
			return corr_off_CR

		elif (atk_bns == 10):
			corr_off_CR = 18
			return corr_off_CR

		elif (atk_bns == 11):
			corr_off_CR = 22
			return corr_off_CR

		elif (atk_bns == 12):
			corr_off_CR = 25
			return corr_off_CR

		elif (atk_bns == 13):
			corr_off_CR = 28
			return corr_off_CR

		elif (atk_bns >= 14):
			corr_off_CR = 30
			return corr_off_CR

		else:
			print("Error. Could not determine atk_bns during cal_corr_off_CR")

	elif (uses_saves == True):
		save_DC = cal_save_DC(exptd_CR, attr)

		if (save_DC <= 13):
			corr_off_CR = 1/2
			return corr_off_CR

		elif (save_DC == 14):
			corr_off_CR = 4
			return corr_off_CR

		elif (save_DC == 15):
			corr_off_CR = 6
			return corr_off_CR

		elif (save_DC == 16):
			corr_off_CR = 9
			return corr_off_CR

		elif (save_DC == 17):
			corr_off_CR = 11
			return corr_off_CR

		elif (save_DC == 18):
			corr_off_CR = 14
			return corr_off_CR

		elif (save_DC == 19):
			corr_off_CR = 18
			return corr_off_CR

		elif (save_DC == 20):
			corr_off_CR = 22
			return corr_off_CR

		elif (save_DC == 21):
			corr_off_CR = 25
			return corr_off_CR

		elif (save_DC == 22):
			corr_off_CR = 28
			return corr_off_CR

		elif (save_DC >= 23):
			corr_off_CR = 30
			return corr_off_CR

		else:
			print("Error. Could not determine save_DC during cal_corr_off_CR")

	else:
		print("Error. Could not determine if creature uses Save DCs during cal_corr_off_CR.")

	
'''Function that calculates the creature's initial Offensive Challenge Rating based on user's input
	Determined by:
		the creature's prospective Offensive Challenge Rating (pros_off_CR)
			which is determined by:
				the creature's damage per round (dmg_per_rnd)
		the creature's corrective Offensive Challenge Rating (corr_off_CR)
			which is determined by:
				the creature's exptected Challenge Rating (exptd_CR)
				the creature's associated attribute bonus'''
def cal_init_off_CR(dmg_per_rnd, attr, uses_saves):
	pros_off_CR = cal_pros_offensive_CR(dmg_per_rnd)
	corr_off_CR = cal_atk_bns_CR(attr, uses_saves)

	init_off_CR = math.floor((pros_off_CR + corr_off_CR)/2)
	return init_off_CR	

def cal_atk_bns_CR(atk_bns, uses_saves):
	if (uses_saves == False):
		#print("Uses saves is False.")

		if (atk_bns <=3):
			corr_off_CR = 1/2
			return corr_off_CR

		elif (atk_bns == 4):
			corr_off_CR = 3
			return corr_off_CR

		elif (atk_bns == 5):
			corr_off_CR = 4
			return corr_off_CR

		elif (atk_bns == 6):
			corr_off_CR = 6
			return corr_off_CR

		elif (atk_bns == 7):
			corr_off_CR = 9
			return corr_off_CR

		elif (atk_bns == 8):
			corr_off_CR = 13
			return corr_off_CR

		elif (atk_bns == 9):
			corr_off_CR = 16
			return corr_off_CR

		elif (atk_bns == 10):
			corr_off_CR = 18
			return corr_off_CR

		elif (atk_bns == 11):
			corr_off_CR = 22
			return corr_off_CR

		elif (atk_bns == 12):
			corr_off_CR = 25
			return corr_off_CR

		elif (atk_bns == 13):
			corr_off_CR = 28
			return corr_off_CR

		elif (atk_bns >= 14):
			corr_off_CR = 30
			return corr_off_CR

		else:
			print("Error. Could not determine atk_bns during cal_corr_off_CR")

	elif (uses_saves == True):
		print("Uses saves is True.")
		save_DC = atk_bns + 10

		if (save_DC <= 13):
			corr_off_CR = 1/2
			return corr_off_CR

		elif (save_DC == 14):
			corr_off_CR = 4
			return corr_off_CR

		elif (save_DC == 15):
			corr_off_CR = 6
			return corr_off_CR

		elif (save_DC == 16):
			corr_off_CR = 9
			return corr_off_CR

		elif (save_DC == 17):
			corr_off_CR = 11
			return corr_off_CR

		elif (save_DC == 18):
			corr_off_CR = 14
			return corr_off_CR

		elif (save_DC == 19):
			corr_off_CR = 18
			return corr_off_CR

		elif (save_DC == 20):
			corr_off_CR = 22
			return corr_off_CR

		elif (save_DC == 21):
			corr_off_CR = 25
			return corr_off_CR

		elif (save_DC == 22):
			corr_off_CR = 28
			return corr_off_CR

		elif (save_DC >= 23):
			corr_off_CR = 30
			return corr_off_CR

		else:
			print("Error. Could not determine save_DC during cal_corr_off_CR")

	else:
		print("Error. Could not determine if creature uses Save DCs during cal_corr_off_CR.")

def cal_off_CR(dmg_CR, atk_bns_CR):
	off_CR = math.floor((dmg_CR + atk_bns_CR)/2)
	return off_CR