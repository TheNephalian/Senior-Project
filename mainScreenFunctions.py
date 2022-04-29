#functions for mainScreen_WIP
from mainScreen_WIP import Ui_MainWindow as mainScree
from secondwindow_copy import *

class funcs(object):
    def HelloWorld():
        print("Hello World, From another file")
    
    def open_window(self):
        self.name = QtWidgets.QLineEdit()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SecondWindow()
        self.ui.setupUi(self.window)
        creature_name = mainScree.nameLineEdit.text()
        self.ui.label.setText(creature_name)
        armor_value = self.ArmorSpinBox.value()
        self.ui.label_3.setText(str(armor_value))
        hp_value = self.hitPointsSpinBox.value()
        self.ui.label_5.setText(str(hp_value))
        str_value = self.strSpinBox.value()
        dex_value = self.dexSpinBox.value()
        con_value = self.conSpinBox.value()
        int_value = self.intSpinBox.value()
        wis_value = self.wisSpinBox.value()
        cha_value = self.chaSpinBox.value()
        self.ui.label_12.setText(str(str_value))
        self.ui.label_13.setText(str(dex_value))
        self.ui.label_14.setText(str(con_value))
        self.ui.label_15.setText(str(int_value))
        self.ui.label_16.setText(str(wis_value))
        self.ui.label_17.setText(str(cha_value))
        CR_value = self.sliderValTxt.text()
        self.ui.label_24.setText(CR_value)
        sizeofDie = str(self.diceSpinBox.value())
        sizeofDie += self.diceLabel.text()
        self.ui.label_19.setText(sizeofDie)
        size = self.sizeComboBox.currentText()
        self.ui.label_28.setText(size)
        typeofcreature = self.typeComboBox.currentText() 
        self.ui.label_30.setText(typeofcreature)
        align = self.allignmentComboBox.currentText()
        self.ui.label_29.setText(align)
        traits = ""
        if(self.aggressiveCheckBox.isChecked()):
            if(traits == ""):
                traits += self.aggressiveCheckBox.text()
            else:
                traits += ", "
                traits += self.aggressiveCheckBox.text()
        if(self.angelicWeaponsCheckBox.isChecked()):
            if(traits == ""):
                traits += self.angelicWeaponsCheckBox.text()
            else:
                traits += ", "
                traits += self.angelicWeaponsCheckBox.text()
        if(self.avoidanceCheckBox.isChecked()):
            if(traits == ""):
                traits += self.avoidanceCheckBox.text()
            else:
                traits += ", "
                traits += self.avoidanceCheckBox.text()
        if(self.bloodFrenzyCheckBox.isChecked()):
            if(traits == ""):
                traits += self.bloodFrenzyCheckBox.text()
            else:
                traits += ", "
                traits += self.bloodFrenzyCheckBox.text()
        if(self.constructCheckBox.isChecked()):
            if(traits == ""):
                traits += self.constructCheckBox.text()
            else:
                traits += ", "
                traits += self.constructCheckBox.text()
        if(self.damageTransferCheckBox.isChecked()):
            if(traits == ""):
                traits += self.damageTransferCheckBox.text()
            else:
                traits += ", "
                traits += self.damageTransferCheckBox.text()
        if(self.enlargeCheckBox.isChecked()):
            if(traits == ""):
                traits += self.enlargeCheckBox.text()
            else:
                traits += ", "
                traits += self.enlargeCheckBox.text()
        if(self.frightfulPresenceCheckBox.isChecked()):
            if(traits == ""):
                traits += self.frightfulPresenceCheckBox.text()
            else:
                traits += ", "
                traits += self.frightfulPresenceCheckBox.text()
        if(self.heatedBodyCheckBox.isChecked()):
            if(traits == ""):
                traits += self.heatedBodyCheckBox.text()
            else:
                traits += ", "
                traits += self.heatedBodyCheckBox.text()
        if(self.horrifyingVisageCheckBox.isChecked()):
            if(traits == ""):
                traits += self.horrifyingVisageCheckBox.text()
            else:
                traits += ", "
                traits += self.horrifyingVisageCheckBox.text()
        if(self.legendaryResistanceCheckBox.isChecked()):
            if(traits == ""):
                traits += self.legendaryResistanceCheckBox.text()
            else:
                traits += ", "
                traits += self.legendaryResistanceCheckBox.text()
        if(self.magicResistanceCheckBox.isChecked()):
            if(traits == ""):
                traits += self.magicResistanceCheckBox.text()
            else:
                traits += ", "
                traits += self.magicResistanceCheckBox.text()
        if(self.martialAdvantageCheckBox.isChecked()):
            if(traits == ""):
                traits += self.martialAdvantageCheckBox.text()
            else:
                traits += ", "
                traits += self.martialAdvantageCheckBox.text()
        if(self.nimbleEscapeCheckBox.isChecked()):
            if(traits == ""):
                traits += self.nimbleEscapeCheckBox.text()
            else:
                traits += ", "
                traits += self.nimbleEscapeCheckBox.text()
        if(self.packTacticsCheckBox.isChecked()):
            if(traits == ""):
                traits += self.packTacticsCheckBox.text()
            else:
                traits += ", "
                traits += self.packTacticsCheckBox.text()
        if(self.parryCheckBox.isChecked()):
            if(traits == ""):
                traits += self.parryCheckBox.text()
            else:
                traits += ", "
                traits += self.parryCheckBox.text()
        if(self.possessionCheckBox.isChecked()):
            if(traits == ""):
                traits += self.possessionCheckBox.text()
            else:
                traits += ", "
                traits += self.possessionCheckBox.text()
        if(self.regenerationCheckBox.isChecked()):
            if(traits == ""):
                traits += self.regenerationCheckBox.text()
            else:
                traits += ", "
                traits += self.regenerationCheckBox.text()
        if(self.relentlessCheckBox.isChecked()):
            if(traits == ""):
                traits += self.relentlessCheckBox.text()
            else:
                traits += ", "
                traits += self.relentlessCheckBox.text()
        if(self.shadowStealthCheckBox.isChecked()):
            if(traits == ""):
                traits += self.shadowStealthCheckBox.text()
            else:
                traits += ", "
                traits += self.shadowStealthCheckBox.text()
        if(self.stenchCheckBox.isChecked()):
            if(traits == ""):
                traits += self.stenchCheckBox.text()
            else:
                traits += ", "
                traits += self.stenchCheckBox.text()
        if(self.superiorInvisibilityCheckBox.isChecked()):
            if(traits == ""):
                traits += self.superiorInvisibilityCheckBox.text()
            else:
                traits += ", "
                traits += self.superiorInvisibilityCheckBox.text()
        if(self.udeadFortitudeCheckBox.isChecked()):
            if(traits == ""):
                traits += self.udeadFortitudeCheckBox.text()
            else:
                traits += ", "
                traits += self.udeadFortitudeCheckBox.text()
        if(self.webCheckBox.isChecked()):
            if(traits == ""):
                traits += self.webCheckBox.text()
            else:
                traits += ", "
                traits += self.webCheckBox.text()
            
        self.ui.label_105.setText(traits)
        resOrimmu = self.resComboBox.currentText()
        self.ui.label_33.setText(resOrimmu)
        langues = ""
        if(self.elvishCheckBox.isChecked()):
            if(langues == ""):
                langues += self.elvishCheckBox.text()
            else:
                langues += ", "
                langues += self.elvishCheckBox.text()
        if(self.giantCheckBox.isChecked()):
            if(langues == ""):
                langues += self.giantCheckBox.text()
            else:
                langues += ", "
                langues += self.giantCheckBox.text()
        if(self.gnomishCheckBox.isChecked()):
            if(langues == ""):
                langues += self.gnomishCheckBox.text()
            else:
                langues += ", "
                langues += self.gnomishCheckBox.text()
        if(self.goblinCheckBox.isChecked()):
            if(langues == ""):
                langues += self.goblinCheckBox.text()
            else:
                langues += ", "
                langues += self.goblinCheckBox.text()
        if(self.halflingCheckBox.isChecked()):
            if(langues == ""):
                langues += self.halflingCheckBox.text()
            else:
                langues += ", "
                langues += self.halflingCheckBox.text()
        if(self.orcCheckBox.isChecked()):
            if(langues == ""):
                langues += self.orcCheckBox.text()
            else:
                langues += ", "
                langues += self.orcCheckBox.text()
        if(self.primordialCheckBox.isChecked()):
            if(langues == ""):
                langues += self.primordialCheckBox.text()
            else:
                langues += ", "
                langues += self.primordialCheckBox.text()
        if(self.sylvanCheckBox.isChecked()):
            if(langues == ""):
                langues += self.sylvanCheckBox.text()
            else:
                langues += ", "
                langues += self.sylvanCheckBox.text()
        if(self.thievesCantCheckBox.isChecked()):
            if(langues == ""):
                langues += self.thievesCantCheckBox.text()
            else:
                langues += ", "
                langues += self.thievesCantCheckBox.text()
        if(self.undercommonCheckBox.isChecked()):
            if(langues == ""):
                langues += self.undercommonCheckBox.text()
            else:
                langues += ", "
                langues += self.undercommonCheckBox.text()
        
        self.ui.label_32.setText(langues)
        
        ####PROFICIENCY BONUS
        pb = 0
        if(CR_value != ''):
                if(int(CR_value) <= 1):
                        pb = 2
                        self.ui.label_26.setText(str(pb))
                else:
                        cr = int(CR_value)
                        pb = (cr + 8) / 4
                        self.ui.label_26.setText(str(int(pb)))
        
        ### actions
        firstaction = self.actionName_1.text()
        self.ui.label_47.setText(firstaction)
        meleeORrange = self.actionType_1.currentText()
        self.ui.label_48.setText(meleeORrange)
        reach = self.reachSpinBox_1.value()
        self.ui.label_52.setText(str(reach))
        attdie = str(self.numDieSpinBox.value())
        attdie += "d"
        attdie += self.actionDice_1.currentText()
        attboun = 0
        if(self.attrComboBox_1.currentText() == "STR"):
                attribute = self.strSpinBox.value()
                attboun = ((attribute - 10)/2) + int(pb)
                if(attboun < 0):
                        attboun = 0
                attdie += "+"
                attdie += str(int(attboun))
        elif(self.attrComboBox_1.currentText() == "DEX"):
                attribute = self.dexSpinBox.value()
                attboun = ((attribute - 10)/2) + int(pb)
                if(attboun < 0):
                        attboun = 0
                attdie += "+"
                attdie += str(int(attboun))
        elif(self.attrComboBox_1.currentText() == "CON"):
                attribute = self.conSpinBox.value()
                attboun = ((attribute - 10)/2) + int(pb)
                if(attboun < 0):
                        attboun = 0
                attdie += "+"
                attdie += str(int(attboun))
        elif(self.attrComboBox_1.currentText() == "INT"):
                attribute = self.intSpinBox.value()
                attboun = ((attribute - 10)/2) + int(pb)
                if(attboun < 0):
                        attboun = 0
                attdie += "+"
                attdie += str(int(attboun))
        elif(self.attrComboBox_1.currentText() == "WIS"):
                attribute = self.wisSpinBox.value()
                attboun = ((attribute - 10)/2) + int(pb)
                if(attboun < 0):
                        attboun = 0
                attdie += "+"
                attdie += str(int(attboun))
        elif(self.attrComboBox_1.currentText() == "CHA"):
                attribute = self.chaSpinBox.value()
                attboun = ((attribute - 10)/2) + int(pb)
                if(attboun < 0):
                        attboun = 0
                attdie += "+"
                attdie += str(int(attboun))
        self.ui.label_57.setText(attdie)
        damageType = self.actionDamageType_1.currentText()
        self.ui.label_60.setText(damageType)  
        numAttks = self.spinBox.value()
        self.ui.label_55.setText(str(numAttks))
        
        secondaction = self.actionName_2.text()
        self.ui.label_68.setText(secondaction)
        meleeORrange2 = self.actionType_2.currentText()
        self.ui.label_69.setText(meleeORrange2)
        reach2 = self.reachSpinBox_2.value()
        self.ui.label_62.setText(str(reach2))
        attdie2 = str(self.numDieSpinBox_2.value())
        attdie2 += "d"
        attdie2 += str(self.actionDice_2.currentText())
        attboun2 = 0
        if(self.attrComboBox_2.currentText() == "STR"):
                attribute2 = self.strSpinBox.value()
                attboun2 = ((attribute2 - 10)/2) + int(pb)
                if(attboun2 < 0):
                        attboun2 = 0
                attdie2 += "+"
                attdie2 += str(int(attboun2))
        elif(self.attrComboBox_2.currentText() == "DEX"):
                attribute2 = self.dexSpinBox.value()
                attboun2 = ((attribute2 - 10)/2) + int(pb)
                if(attboun2 < 0):
                        attboun2 = 0
                attdie2 += "+"
                attdie2 += str(int(attboun2))
        elif(self.attrComboBox_2.currentText() == "CON"):
                attribute2 = self.conSpinBox.value()
                attboun2 = ((attribute2 - 10)/2) + int(pb)
                if(attboun2 < 0):
                        attboun2 = 0
                attdie2 += "+"
                attdie2 += str(int(attboun2))
        elif(self.attrComboBox_2.currentText() == "INT"):
                attribute2 = self.intSpinBox.value()
                attboun2 = ((attribute2 - 10)/2) + int(pb)
                if(attboun2 < 0):
                        attboun2 = 0
                attdie2 += "+"
                attdie2 += str(int(attboun2))
        elif(self.attrComboBox_2.currentText() == "WIS"):
                attribute2 = self.wisSpinBox.value()
                attboun2 = ((attribute2 - 10)/2) + int(pb)
                if(attboun2 < 0):
                        attboun2 = 0
                attdie2 += "+"
                attdie2 += str(int(attboun2))
        elif(self.attrComboBox_2.currentText() == "CHA"):
                attribute2 = self.chaSpinBox.value()
                attboun2 = ((attribute2 - 10)/2) + int(pb)
                if(attboun2 < 0):
                        attboun2 = 0
                attdie2 += "+"
                attdie2 += str(int(attboun2))
        self.ui.label_65.setText(attdie2)
        damageType2 = self.actionDamageType_2.currentText()
        self.ui.label_63.setText(damageType2)  
        numAttks2 = self.spinBox_2.value()
        self.ui.label_61.setText(str(numAttks2))
        
        thirdaction = self.actionName_3.text()
        self.ui.label_49.setText(thirdaction)
        meleeORrange3 = self.actionType_3.currentText()
        self.ui.label_50.setText(meleeORrange3)
        reach3 = self.reachSpinBox_3.value()
        self.ui.label_72.setText(str(reach3))
        attdie3 = str(self.numDieSpinBox_3.value())
        attdie3 += "d"
        attdie3 += str(self.actionDice_3.currentText())
        attboun3 = 0
        if(self.attrComboBox_3.currentText() == "STR"):
                attribute3 = self.strSpinBox.value()
                attboun3 = ((attribute3 - 10)/2) + int(pb)
                if(attboun3 < 0):
                        attboun3 = 0
                attdie3 += "+"
                attdie3 += str(int(attboun3))
        elif(self.attrComboBox_3.currentText() == "DEX"):
                attribute3 = self.dexSpinBox.value()
                attboun3 = ((attribute3 - 10)/2) + int(pb)
                if(attboun3 < 0):
                        attboun3 = 0
                attdie3 += "+"
                attdie3 += str(int(attboun3))
        elif(self.attrComboBox_3.currentText() == "CON"):
                attribute3 = self.conSpinBox.value()
                attboun3 = ((attribute3 - 10)/2) + int(pb)
                if(attboun3 < 0):
                        attboun3 = 0
                attdie3 += "+"
                attdie3 += str(int(attboun3))
        elif(self.attrComboBox_3.currentText() == "INT"):
                attribute3 = self.intSpinBox.value()
                attboun3 = ((attribute3 - 10)/2) + int(pb)
                if(attboun3 < 0):
                        attboun3 = 0
                attdie3 += "+"
                attdie3 += str(int(attboun3))
        elif(self.attrComboBox_3.currentText() == "WIS"):
                attribute3 = self.wisSpinBox.value()
                attboun3 = ((attribute3 - 10)/2) + int(pb)
                if(attboun3 < 0):
                        attboun3 = 0
                attdie3 += "+"
                attdie3 += str(int(attboun3))
        elif(self.attrComboBox_3.currentText() == "CHA"):
                attribute3 = self.chaSpinBox.value()
                attboun3 = ((attribute3 - 10)/2) + int(pb)
                if(attboun3 < 0):
                        attboun3 = 0
                attdie3 += "+"
                attdie3 += str(int(attboun3))
        self.ui.label_75.setText(attdie3)
        damageType3 = self.actionDamageType_3.currentText()
        self.ui.label_73.setText(damageType3)  
        numAttks3 = self.spinBox_3.value()
        self.ui.label_59.setText(str(numAttks3))

        forthaction = self.actionName_4.text()
        self.ui.label_87.setText(forthaction)
        meleeORrange4 = self.actionType_4.currentText()
        self.ui.label_88.setText(meleeORrange4)
        reach4 = self.reachSpinBox_4.value()
        self.ui.label_81.setText(str(reach4))
        attdie4 = str(self.numDieSpinBox_4.value())
        attdie4 += "d"
        attdie4 += str(self.actionDice_4.currentText())
        attboun4 = 0
        if(self.attrComboBox_4.currentText() == "STR"):
                attribute4 = self.strSpinBox.value()
                attboun4 = ((attribute4 - 10)/2) + int(pb)
                if(attboun4 < 0):
                        attboun4 = 0
                attdie4 += "+"
                attdie4 += str(int(attboun4))
        elif(self.attrComboBox_4.currentText() == "DEX"):
                attribute4 = self.dexSpinBox.value()
                attboun4 = ((attribute4 - 10)/2) + int(pb)
                if(attboun4 < 0):
                        attboun4 = 0
                attdie4 += "+"
                attdie4 += str(int(attboun4))
        elif(self.attrComboBox_4.currentText() == "CON"):
                attribute4 = self.conSpinBox.value()
                attboun4 = ((attribute4 - 10)/2) + int(pb)
                if(attboun4 < 0):
                        attboun4 = 0
                attdie4 += "+"
                attdie4 += str(int(attboun4))
        elif(self.attrComboBox_4.currentText() == "INT"):
                attribute4 = self.intSpinBox.value()
                attboun4 = ((attribute4 - 10)/2) + int(pb)
                if(attboun4 < 0):
                        attboun4 = 0
                attdie4 += "+"
                attdie4 += str(int(attboun4))
        elif(self.attrComboBox_4.currentText() == "WIS"):
                attribute4 = self.wisSpinBox.value()
                attboun4 = ((attribute - 10)/2) + int(pb)
                if(attboun4 < 0):
                        attboun4 = 0
                attdie4 += "+"
                attdie4 += str(int(attboun4))
        elif(self.attrComboBox_4.currentText() == "CHA"):
                attribute4 = self.chaSpinBox.value()
                attboun4 = ((attribute4 - 10)/2) + int(pb)
                if(attboun4 < 0):
                        attboun4 = 0
                attdie4 += "+"
                attdie4 += str(int(attboun4))
        self.ui.label_84.setText(attdie4)
        damageType4 = self.actionDamageType_4.currentText()
        self.ui.label_82.setText(damageType4)  
        numAttks4 = self.spinBox_3.value()
        self.ui.label_80.setText(str(numAttks4))
        
        ### speed
        ground = str(self.movementSpinBox.value())
        ground += "ft.,"
        self.ui.label_93.setText(ground)
        burrow = str(self.burrowSpinBox.value())
        burrow += "ft.,"
        self.ui.label_94.setText(burrow)
        climb = str(self.climbSpinBox.value())
        climb += "ft.,"
        self.ui.label_97.setText(climb)
        fly = str(self.flySpinBox.value())
        fly += "ft.,"
        self.ui.label_99.setText(fly)
        swim = str(self.swimSpinBox.value())
        swim += "ft.,"
        self.ui.label_101.setText(swim)
        
        ###senses
        senses = ""
        if(self.blindedCheckBox.isChecked()):
            if(senses == ""):
                senses += self.blindedCheckBox.text()
            else:
                senses += ", "
                senses += self.blindedCheckBox.text()
        if(self.darkvisionCheckBox.isChecked()):
            if(senses == ""):
                senses += self.darkvisionCheckBox.text()
            else:
                senses += ", "
                senses += self.darkvisionCheckBox.text()
        if(self.tremorsenseCheckBox.isChecked()):
            if(senses == ""):
                senses += self.tremorsenseCheckBox.text()
            else:
                senses += ", "
                senses += self.tremorsenseCheckBox.text()
        if(self.truesightCheckBox.isChecked()):
            if(senses == ""):
                senses += self.truesightCheckBox.text()
            else:
                senses += ", "
                senses += self.truesightCheckBox.text()
        self.ui.label_103.setText(senses)
        
        ####condition immunities
        condImmu = ""
        if(self.blindedCheckBox.isChecked()):
            if(condImmu == ""):
                condImmu += self.blindedCheckBox.text()
            else:
                condImmu += ", "
                condImmu += self.blindedCheckBox.text() 
        if(self.charmedCheckBox.isChecked()):
            if(condImmu == ""):
                condImmu += self.charmedCheckBox.text()
            else:
                condImmu += ", "
                condImmu += self.charmedCheckBox.text() 
        if(self.deafendedCheckBox.isChecked()):
            if(condImmu == ""):
                condImmu += self.deafendedCheckBox.text()
            else:
                condImmu += ", "
                condImmu += self.deafendedCheckBox.text() 
        if(self.exhaustionCheckBox.isChecked()):
            if(condImmu == ""):
                condImmu += self.exhaustionCheckBox.text()
            else:
                condImmu += ", "
                condImmu += self.exhaustionCheckBox.text()
        if(self.frightenedCheckBox.isChecked()):
            if(condImmu == ""):
                condImmu += self.frightenedCheckBox.text()
            else:
                condImmu += ", "
                condImmu += self.frightenedCheckBox.text() 
        if(self.grappledCheckBox.isChecked()):
            if(condImmu == ""):
                condImmu += self.grappledCheckBox.text()
            else:
                condImmu += ", "
                condImmu += self.grappledCheckBox.text() 
        if(self.incapacitatedCheckBox.isChecked()):
            if(condImmu == ""):
                condImmu += self.incapacitatedCheckBox.text()
            else:
                condImmu += ", "
                condImmu += self.incapacitatedCheckBox.text() 
        if(self.invisibleCheckBox.isChecked()):
            if(condImmu == ""):
                condImmu += self.invisibleCheckBox.text()
            else:
                condImmu += ", "
                condImmu += self.invisibleCheckBox.text() 
        if(self.paralyzedCheckBox.isChecked()):
            if(condImmu == ""):
                condImmu += self.paralyzedCheckBox.text()
            else:
                condImmu += ", "
                condImmu += self.paralyzedCheckBox.text()
        if(self.petrifiedCheckBox.isChecked()):
            if(condImmu == ""):
                condImmu += self.petrifiedCheckBox.text()
            else:
                condImmu += ", "
                condImmu += self.petrifiedCheckBox.text()
        if(self.poisonedCheckBox.isChecked()):
            if(condImmu == ""):
                condImmu += self.poisonedCheckBox.text()
            else:
                condImmu += ", "
                condImmu += self.poisonedCheckBox.text() 
        if(self.proneCheckBox.isChecked()):
            if(condImmu == ""):
                condImmu += self.proneCheckBox.text()
            else:
                condImmu += ", "
                condImmu += self.proneCheckBox.text() 
        if(self.restrainedCheckBox.isChecked()):
            if(condImmu == ""):
                condImmu += self.restrainedCheckBox.text()
            else:
                condImmu += ", "
                condImmu += self.restrainedCheckBox.text() 
        if(self.stunnedCheckBox.isChecked()):
            if(condImmu == ""):
                condImmu += self.stunnedCheckBox.text()
            else:
                condImmu += ", "
                condImmu += self.stunnedCheckBox.text()
        if(self.unconsciosCheckBox.isChecked()):
            if(condImmu == ""):
                condImmu += self.unconsciosCheckBox.text()
            else:
                condImmu += ", "
                condImmu += self.unconsciosCheckBox.text()
            
        self.ui.label_107.setText(condImmu)
        
        ####saving Throws
        if(self.strSavingThrowCheckBox.isChecked()):
                attribute = self.strSpinBox.value()
                strST = ((attribute - 10)/2) + int(pb)
                if(strST < 0):
                        strST = 0
                strSTs = "+"
                strSTs += str(int(strST))
                self.ui.label_41.setText(strSTs)
        else:
                strSTs = "+0"
                self.ui.label_41.setText(strSTs)
        if(self.dexSavingThrowCheckBox.isChecked()):
                attribute2 = self.dexSpinBox.value()
                strST2 = ((attribute2 - 10)/2) + int(pb)
                if(strST2 < 0):
                        strST2 = 0
                strSTs2 = "+"
                strSTs2 += str(int(strST2))
                self.ui.label_42.setText(strSTs2)
        else:
                strSTs2 = "+0"
                self.ui.label_42.setText(strSTs2)
        if(self.conSavingThrowCheckBox.isChecked()):
                attribute3 = self.conSpinBox.value()
                strST3 = ((attribute3 - 10)/2) + int(pb)
                if(strST3 < 0):
                        strST3 = 0
                strSTs3 = "+"
                strSTs3 += str(int(strST3))
                self.ui.label_43.setText(strSTs3)
        else:
                strSTs3 = "+0"
                self.ui.label_43.setText(strSTs3)
        if(self.intSavingThrowCheckBox.isChecked()):
                attribute4 = self.intSpinBox.value()
                strST4 = ((attribute4 - 10)/2) + int(pb)
                if(strST4 < 0):
                        strST4 = 0
                strSTs4 = "+"
                strSTs4 += str(int(strST4))
                self.ui.label_44.setText(strSTs4)
        else:
                strSTs4 = "+0"
                self.ui.label_44.setText(strSTs4)
        if(self.wisSavingThrowCheckBox.isChecked()):
                attribute5 = self.wisSpinBox.value()
                strST5 = ((attribute5 - 10)/2) + int(pb)
                if(strST5 < 0):
                        strST5 = 0
                strSTs5 = "+"
                strSTs5 += str(int(strST5))
                self.ui.label_45.setText(strSTs5)
        else:
                strSTs5 = "+0"
                self.ui.label_45.setText(strSTs5)
        if(self.chaSavingThrowCheckBox.isChecked()):
                attribute6 = self.chaSpinBox.value()
                strST6 = ((attribute6 - 10)/2) + int(pb)
                if(strST6 < 0):
                        strST6 = 0
                strSTs6 = "+"
                strSTs6 += str(int(strST6))
                self.ui.label_46.setText(strSTs6)
        else:
                strSTs6 = "+0"
                self.ui.label_46.setText(strSTs6)
                
        ####skills
        skills = ""
        if(self.acrobaticsCheckBox.isChecked()):
            if(skills == ""):
                skills += self.acrobaticsCheckBox.text()
                ###skill bonus
                attribute = self.dexSpinBox.value()
                strST = ((attribute - 10)/2) + int(pb)
                if(strST < 0):
                        strST = 0
                strSTs = " +"
                strSTs += str(int(strST))
                skills += strSTs
            else:
                skills += ", "
                skills += self.acrobaticsCheckBox.text()
                ###skill bonus
                attribute = self.dexSpinBox.value()
                strST = ((attribute - 10)/2) + int(pb)
                if(strST < 0):
                        strST = 0
                strSTs = " +"
                strSTs += str(int(strST))
                skills += strSTs
        if(self.animalHandlingCheckBox.isChecked()):
            if(skills == ""):
                skills += self.animalHandlingCheckBox.text()
                ###skill bonus
                attribute = self.wisSpinBox.value()
                strST = ((attribute - 10)/2) + int(pb)
                if(strST < 0):
                        strST = 0
                strSTs = " +"
                strSTs += str(int(strST))
                skills += strSTs
            else:
                skills += ", "
                skills += self.animalHandlingCheckBox.text()
                ###skill bonus
                attribute = self.dexSpinBox.value()
                strST = ((attribute - 10)/2) + int(pb)
                if(strST < 0):
                        strST = 0
                strSTs = " +"
                strSTs += str(int(strST))
                skills += strSTs
        if(self.arcanaCheckBox.isChecked()):
            if(skills == ""):
                skills += self.arcanaCheckBox.text()
                ###skill bonus
                attribute = self.intSpinBox.value()
                strST = ((attribute - 10)/2) + int(pb)
                if(strST < 0):
                        strST = 0
                strSTs = " +"
                strSTs += str(int(strST))
                skills += strSTs
            else:
                skills += ", "
                skills += self.arcanaCheckBox.text()
                ###skill bonus
                attribute = self.intSpinBox.value()
                strST = ((attribute - 10)/2) + int(pb)
                if(strST < 0):
                        strST = 0
                strSTs = " +"
                strSTs += str(int(strST))
                skills += strSTs
        if(self.athleticsCheckBox.isChecked()):
            if(skills == ""):
                skills += self.athleticsCheckBox.text()
                ###skill bonus
                attribute = self.strSpinBox.value()
                strST = ((attribute - 10)/2) + int(pb)
                if(strST < 0):
                        strST = 0
                strSTs = " +"
                strSTs += str(int(strST))
                skills += strSTs
            else:
                skills += ", "
                skills += self.athleticsCheckBox.text()
                ###skill bonus
                attribute = self.strSpinBox.value()
                strST = ((attribute - 10)/2) + int(pb)
                if(strST < 0):
                        strST = 0
                strSTs = " +"
                strSTs += str(int(strST))
                skills += strSTs
        if(self.deceptionCheckBox.isChecked()):
            if(skills == ""):
                skills += self.deceptionCheckBox.text()
                ###skill bonus
                attribute = self.chaSpinBox.value()
                strST = ((attribute - 10)/2) + int(pb)
                if(strST < 0):
                        strST = 0
                strSTs = " +"
                strSTs += str(int(strST))
                skills += strSTs
            else:
                skills += ", "
                skills += self.deceptionCheckBox.text()
                ###skill bonus
                attribute = self.chaSpinBox.value()
                strST = ((attribute - 10)/2) + int(pb)
                if(strST < 0):
                        strST = 0
                strSTs = " +"
                strSTs += str(int(strST))
                skills += strSTs
        if(self.historyCheckBox.isChecked()):
            if(skills == ""):
                skills += self.historyCheckBox.text()
                ###skill bonus
                attribute = self.intSpinBox.value()
                strST = ((attribute - 10)/2) + int(pb)
                if(strST < 0):
                        strST = 0
                strSTs = " +"
                strSTs += str(int(strST))
                skills += strSTs
            else:
                skills += ", "
                skills += self.historyCheckBox.text()
                ###skill bonus
                attribute = self.intSpinBox.value()
                strST = ((attribute - 10)/2) + int(pb)
                if(strST < 0):
                        strST = 0
                strSTs = " +"
                strSTs += str(int(strST))
                skills += strSTs
        if(self.insightCheckBox.isChecked()):
            if(skills == ""):
                skills += self.insightCheckBox.text()
                ###skill bonus
                attribute = self.wisSpinBox.value()
                strST = ((attribute - 10)/2) + int(pb)
                if(strST < 0):
                        strST = 0
                strSTs = " +"
                strSTs += str(int(strST))
                skills += strSTs
            else:
                skills += ", "
                skills += self.insightCheckBox.text()
                ###skill bonus
                attribute = self.wisSpinBox.value()
                strST = ((attribute - 10)/2) + int(pb)
                if(strST < 0):
                        strST = 0
                strSTs = " +"
                strSTs += str(int(strST))
                skills += strSTs
        if(self.intimidationCheckBox.isChecked()):
            if(skills == ""):
                skills += self.intimidationCheckBox.text()
                ###skill bonus
                attribute = self.chaSpinBox.value()
                strST = ((attribute - 10)/2) + int(pb)
                if(strST < 0):
                        strST = 0
                strSTs = " +"
                strSTs += str(int(strST))
                skills += strSTs
            else:
                skills += ", "
                skills += self.intimidationCheckBox.text()
                ###skill bonus
                attribute = self.chaSpinBox.value()
                strST = ((attribute - 10)/2) + int(pb)
                if(strST < 0):
                        strST = 0
                strSTs = " +"
                strSTs += str(int(strST))
                skills += strSTs
        if(self.investigationCheckBox.isChecked()):
            if(skills == ""):
                skills += self.investigationCheckBox.text()
                ###skill bonus
                attribute = self.intSpinBox.value()
                strST = ((attribute - 10)/2) + int(pb)
                if(strST < 0):
                        strST = 0
                strSTs = " +"
                strSTs += str(int(strST))
                skills += strSTs
            else:
                skills += ", "
                skills += self.investigationCheckBox.text()
                ###skill bonus
                attribute = self.intSpinBox.value()
                strST = ((attribute - 10)/2) + int(pb)
                if(strST < 0):
                        strST = 0
                strSTs = " +"
                strSTs += str(int(strST))
                skills += strSTs
        if(self.medicineCheckBox.isChecked()):
            if(skills == ""):
                skills += self.medicineCheckBox.text()
                ###skill bonus
                attribute = self.wisSpinBox.value()
                strST = ((attribute - 10)/2) + int(pb)
                if(strST < 0):
                        strST = 0
                strSTs = " +"
                strSTs += str(int(strST))
                skills += strSTs
            else:
                skills += ", "
                skills += self.medicineCheckBox.text()
                ###skill bonus
                attribute = self.wisSpinBox.value()
                strST = ((attribute - 10)/2) + int(pb)
                if(strST < 0):
                        strST = 0
                strSTs = " +"
                strSTs += str(int(strST))
                skills += strSTs  
        if(self.natureCheckBox.isChecked()):
            if(skills == ""):
                skills += self.natureCheckBox.text()
                ###skill bonus
                attribute = self.intSpinBox.value()
                strST = ((attribute - 10)/2) + int(pb)
                if(strST < 0):
                        strST = 0
                strSTs = " +"
                strSTs += str(int(strST))
                skills += strSTs
            else:
                skills += ", "
                skills += self.natureCheckBox.text()
                ###skill bonus
                attribute = self.intSpinBox.value()
                strST = ((attribute - 10)/2) + int(pb)
                if(strST < 0):
                        strST = 0
                strSTs = " +"
                strSTs += str(int(strST))
                skills += strSTs
        if(self.perceptionCheckBox.isChecked()):
            if(skills == ""):
                skills += self.perceptionCheckBox.text()
                ###skill bonus
                attribute = self.wisSpinBox.value()
                strST = ((attribute - 10)/2) + int(pb)
                if(strST < 0):
                        strST = 0
                strSTs = " +"
                strSTs += str(int(strST))
                skills += strSTs
            else:
                skills += ", "
                skills += self.perceptionCheckBox.text()
                ###skill bonus
                attribute = self.wisSpinBox.value()
                strST = ((attribute - 10)/2) + int(pb)
                if(strST < 0):
                        strST = 0
                strSTs = " +"
                strSTs += str(int(strST))
                skills += strSTs
        if(self.performanceCheckBox.isChecked()):
            if(skills == ""):
                skills += self.performanceCheckBox.text()
                ###skill bonus
                attribute = self.chaSpinBox.value()
                strST = ((attribute - 10)/2) + int(pb)
                if(strST < 0):
                        strST = 0
                strSTs = " +"
                strSTs += str(int(strST))
                skills += strSTs
            else:
                skills += ", "
                skills += self.performanceCheckBox.text()
                ###skill bonus
                attribute = self.chaSpinBox.value()
                strST = ((attribute - 10)/2) + int(pb)
                if(strST < 0):
                        strST = 0
                strSTs = " +"
                strSTs += str(int(strST))
                skills += strSTs
        if(self.persuasionCheckBox.isChecked()):
            if(skills == ""):
                skills += self.persuasionCheckBox.text()
                ###skill bonus
                attribute = self.chaSpinBox.value()
                strST = ((attribute - 10)/2) + int(pb)
                if(strST < 0):
                        strST = 0
                strSTs = " +"
                strSTs += str(int(strST))
                skills += strSTs
            else:
                skills += ", "
                skills += self.persuasionCheckBox.text()
                ###skill bonus
                attribute = self.chaSpinBox.value()
                strST = ((attribute - 10)/2) + int(pb)
                if(strST < 0):
                        strST = 0
                strSTs = " +"
                strSTs += str(int(strST))
                skills += strSTs
        if(self.religionCheckBox.isChecked()):
            if(skills == ""):
                skills += self.religionCheckBox.text()
                ###skill bonus
                attribute = self.intSpinBox.value()
                strST = ((attribute - 10)/2) + int(pb)
                if(strST < 0):
                        strST = 0
                strSTs = " +"
                strSTs += str(int(strST))
                skills += strSTs
            else:
                skills += ", "
                skills += self.religionCheckBox.text()
                ###skill bonus
                attribute = self.intSpinBox.value()
                strST = ((attribute - 10)/2) + int(pb)
                if(strST < 0):
                        strST = 0
                strSTs = " +"
                strSTs += str(int(strST))
                skills += strSTs
        if(self.slightOfHandCheckBox.isChecked()):
            if(skills == ""):
                skills += self.slightOfHandCheckBox.text()
                ###skill bonus
                attribute = self.dexSpinBox.value()
                strST = ((attribute - 10)/2) + int(pb)
                if(strST < 0):
                        strST = 0
                strSTs = " +"
                strSTs += str(int(strST))
                skills += strSTs
            else:
                skills += ", "
                skills += self.slightOfHandCheckBox.text()
                ###skill bonus
                attribute = self.dexSpinBox.value()
                strST = ((attribute - 10)/2) + int(pb)
                if(strST < 0):
                        strST = 0
                strSTs = " +"
                strSTs += str(int(strST))
                skills += strSTs
        if(self.stealthCheckBox.isChecked()):
            if(skills == ""):
                skills += self.stealthCheckBox.text()
                ###skill bonus
                attribute = self.dexSpinBox.value()
                strST = ((attribute - 10)/2) + int(pb)
                if(strST < 0):
                        strST = 0
                strSTs = " +"
                strSTs += str(int(strST))
                skills += strSTs
            else:
                skills += ", "
                skills += self.stealthCheckBox.text()
                ###skill bonus
                attribute = self.dexSpinBox.value()
                strST = ((attribute - 10)/2) + int(pb)
                if(strST < 0):
                        strST = 0
                strSTs = " +"
                strSTs += str(int(strST))
                skills += strSTs
        if(self.survivalCheckBox.isChecked()):
            if(skills == ""):
                skills += self.survivalCheckBox.text()
                ###skill bonus
                attribute = self.wisSpinBox.value()
                strST = ((attribute - 10)/2) + int(pb)
                if(strST < 0):
                        strST = 0
                strSTs = " +"
                strSTs += str(int(strST))
                skills += strSTs
            else:
                skills += ", "
                skills += self.survivalCheckBox.text()
                ###skill bonus
                attribute = self.wisSpinBox.value()
                strST = ((attribute - 10)/2) + int(pb)
                if(strST < 0):
                        strST = 0
                strSTs = " +"
                strSTs += str(int(strST))
                skills += strSTs
        self.ui.label_34.setText(skills)
                
        #creature = monster(creature_name, str_value,dex_value,con_value,int_value,wis_value,cha_value, hp_value, armor_value, size, sizeofDie, self.dprSpinBox.value(), self.attkBonSpinBox.value(), numAttks, numAttks2, numAttks3, numAttks4, attdie, attdie2,attdie3,attdie4)
        
        self.window.show() 

myFuncs = funcs()