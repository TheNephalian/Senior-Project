'''Function that calculates the Offensive Challenge Rating (CR) of the creature based on its damage per round (dmg_per_rnd)'''
'''	This is the first step of calculating a creature's overall CR, '''
''' 	which is to calculate its Offensive CR'''
'''	Returns the prospective Offensive CR (pros_Off_CR), to be used in further calculation'''
def cal_Offensive_CR(dmg_per_rnd):
	if (dmg_per_rnd <= 1):
		pros_Off_CR = 0
		return pros_Off_CR

	elif (dmg_per_rnd <= 3):
		pros_Off_CR = 1/8
		return pros_Off_CR

	elif (dmg_per_rnd <= 5):
		pros_Off_CR = 1/4
		return pros_Off_CR

	elif (dmg_per_rnd<= 8):
		pros_Off_CR = 1/2
		return pros_Off_CR

	elif (dmg_per_rnd <= 14):
		pros_Off_CR = 1
		return pros_Off_CR

	elif (dmg_per_rnd <= 14):
		pros_Off_CR = 1
		return pros_Off_CR

	elif (dmg_per_rnd <= 20):
		pros_Off_CR = 2
		return pros_Off_CR

	elif (dmg_per_rnd <= 26):
		pros_Off_CR = 3
		return pros_Off_CR

	elif (dmg_per_rnd <= 32):
		pros_Off_CR = 4
		return pros_Off_CR

	elif (dmg_per_rnd <= 38):
		pros_Off_CR = 5
		return pros_Off_CR

	elif (dmg_per_rnd <= 44):
		pros_Off_CR = 6
		return pros_Off_CR

	elif (dmg_per_rnd <= 50):
		pros_Off_CR = 7
		return pros_Off_CR

	elif (dmg_per_rnd <= 56):
		pros_Off_CR = 8
		return pros_Off_CR

	elif (dmg_per_rnd <= 62):
		pros_Off_CR = 9
		return pros_Off_CR

	elif (dmg_per_rnd <= 68):
		pros_Off_CR = 10
		return pros_Off_CR

	elif (dmg_per_rnd <= 74):
		pros_Off_CR = 11
		return pros_Off_CR

	elif (dmg_per_rnd <= 80):
		pros_Off_CR = 12
		return pros_Off_CR

	elif (dmg_per_rnd <= 86):
		pros_Off_CR = 13
		return pros_Off_CR

	elif (dmg_per_rnd <= 92):
		pros_Off_CR = 14
		return pros_Off_CR

	elif (dmg_per_rnd <= 98):
		pros_Off_CR = 15
		return pros_Off_CR

	elif (dmg_per_rnd <= 104):
		pros_Off_CR = 16
		return pros_Off_CR

	elif (dmg_per_rnd <= 110):
		pros_Off_CR = 17
		return pros_Off_CR

	elif (dmg_per_rnd <= 116):
		pros_Off_CR = 18
		return pros_Off_CR

	elif (dmg_per_rnd <= 122):
		pros_Off_CR = 19
		return pros_Off_CR

	elif (dmg_per_rnd <= 140):
		pros_Off_CR = 20
		return pros_Off_CR

	elif (dmg_per_rnd <= 158):
		pros_Off_CR = 21
		return pros_Off_CR

	elif (dmg_per_rnd <= 176):
		pros_Off_CR = 22
		return pros_Off_CR

	elif (dmg_per_rnd <= 194):
		pros_Off_CR = 23
		return pros_Off_CR

	elif (dmg_per_rnd <= 212):
		pros_Off_CR = 24
		return pros_Off_CR

	elif (dmg_per_rnd <= 230):
		pros_Off_CR = 25
		return pros_Off_CR

	elif (dmg_per_rnd <= 248):
		pros_Off_CR = 26
		return pros_Off_CR

	elif (dmg_per_rnd <= 266):
		pros_Off_CR = 27
		return pros_Off_CR

	elif (dmg_per_rnd <= 284):
		pros_Off_CR = 28
		return pros_Off_CR

	elif (dmg_per_rnd <= 302):
		pros_Off_CR = 29
		return pros_Off_CR

	elif (dmg_per_rnd <= 320):
		pros_Off_CR = 30
		return pros_Off_CR

	elif (dmg_per_rnd > 320):
		print("Damage per round is too high. Damage must be within 0-320.")

	else:
		print("Error when reading Damage per Round.")