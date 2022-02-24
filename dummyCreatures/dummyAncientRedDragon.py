from dummyCreature import *
class ancientRedDragon (creature):
	def __init__(self):
		ancientRedDragon.__init__

		self.armor_cls = 22
		self.hit_pts = 546
		self.curr_hp = self.hit_pts
		self.challnge_rtg = 24
		self.prof_bns = 7
		self.is_defeated = False

		self.strength = 30
		self.dexterity = 10
		self.constitution = 29
		self.intelligence = 18
		self.wisdom = 15
		self.charisma = 23

		self.dex_bns = 0
		self.atk_bns = 17
		#self.dmg_per_rnd = 55

		self.fbRecharge = True

		def attack():
			fireBreath()
		
			multiAttack()
			return

		def multiAttack():
			bite()

			claw()

			claw()
			return

		def bite():
			self.attack_roll()

			dmgRoll = random.randint(1,10) + random.randint(1,10) + 10

			return dmgRoll

		def claw():
			self.attack_roll()

			dmgRoll = random.randint(1,6) + random.randint(1,6) + 10
			return dmgRoll

		def fireBreath():
			if (self.fbRecharge == False):
				rechargeRoll = random.randint(1,6)
				if (rechargeRoll == 5 | rechargeRoll == 6):
					self.fbRecharge = True

			dmgRoll = 0

			if (self.fbRecharge == True):
				for i in range(26):
					dmgRoll = dmgRoll + random.randint(1,6)

				self.fbRecharge = False

			return dmgRoll