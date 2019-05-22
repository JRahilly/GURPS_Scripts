# *** Imports *** #
import Functions as F
import os

# *** Classes *** #
class Alien(): # Defines a new alien species
    
    # *** Global Class Vars *** #
    alienNum = 1
    
    # *** Class Functions *** #
    def __init__(self):

        # *** Self Attributes *** #
        self.name = 'SID#{}'.format(Alien.alienNum)
        self.chemicalBasis = Alien.chemicalBasis(self)
        self.dwelling, self.habitat = Alien.habitat(self)
        self.sapience = Alien.sapience(self)
        self.trophicLevel = Alien.trophicLevel(self, 0)
        self.primaryLocomotion, self.secondaryLocomotion, self.tertiaryLocomotion = Alien.locomotion(self)
        self.sizeClass, self.size, self.weight, self.sizeMod, self.strength, self.gravity = Alien.size(self)
        # self.symmetry, self.limbs, self.tails, self.manipulators, self.skeleton = Alien.body(self)

        # *** Class Var Increments *** #
        Alien.alienNum += 1


    def attributes(self):
        print(self.name)

        print('---- Biology ----')
        print('Chemical Basis       : {}'.format(self.chemicalBasis))
        print('Dwelling             : {}'.format(self.dwelling))
        print('Habitat              : {}'.format(self.habitat))
        print('Sapience             : {}'.format(self.sapience))
        print('Trophic Level        : {}'.format(self.trophicLevel))

        print('---- Locomotion ----')
        print('Primary Locomotion   : {}'.format(self.primaryLocomotion))

        if self.secondaryLocomotion != None:
            print('Secondary Locomotion : {}'.format(self.secondaryLocomotion))

        if self.tertiaryLocomotion != None:
            print('Tertiary Locomotion  : {}'.format(self.tertiaryLocomotion))

        print('---- Size ----')
        print('Size Class           : {}'.format(self.sizeClass))
        print('Longest Dimension    : {}'.format(self.size))
        print('Average Earth Weight : {}'.format(self.weight))
        print('Native Gravity       : {}'.format(self.gravity))
        print('Average Native Weight: {:.2f}'.format(self.weight * self.gravity))
        print('Size Modifier        : {}'.format(self.sizeMod))
        print('Average Strength     : {}'.format(self.strength))

        # print('---- Body ----')
        # print('Body Symmetry        : {}'.format(self.symmetry))
        # print('Limb Count           : {}'.format(self.limbs))
        # print('Tail Count           : {}'.format(self.tails))
        # print('Manipulator Count    : {}'.format(self.manipulators))
        # print('Skeleton Type        : {}'.format(self.skeleton))

    
    def body(self):
        
        # *** Tables *** #
        table = {
            'Symmetry' : {
                2  : 'Bilateral',
                3  : 'Bilateral',
                4  : 'Bilateral',
                5  : 'Bilateral',
                6  : 'Bilateral',
                7  : 'Bilateral',
                8  : 'Trilateral',
                9  : 'Radial',
                10 : 'Spherical',
                11 : 'Asymmetric',
                12 : 'Asymmetric',
                13 : 'Asymmetric',
                14 : 'Asymmetric'},
            'Limbs' : {
                1  : 'Limbless',
                2  : 'One Segment (One Limb per Side)',
                3  : 'Two Segments (Two Limbs per Side)',
                4  : 'Segments (Each Segment has One Limb per Side)',
                5  : 'Segments (Each Segment has One Limb per Side)',
                6  : 'Segments (Each Segment has One Limb per Side)'},
            'Tails' : {
                2  : 'No Features',
                3  : 'No Features',
                4  : 'No Features',
                5  : 'No Features',
                6  : 'Striker Tail',
                7  : 'Long Tail',
                8  : 'Constricting Tail',
                9  : 'Barbed Striker Tail',
                10 : 'Gripping Tail',
                11 : 'Branching Tail',
                12 : 'Combination'},
            'Manipulators' : {
                6  : 'No Manipulators',
                7  : '1 Set of Manipulators with Bad Grip',
                8  : 'Prehensile Tail of Trunk',
                9  : '1 Set of Manipulators with Normal DX',
                10 : '2 Sets of Manipulators',
                11 : 'Sets of Manipulators',
                12 : 'Sets of Manipulators',
                13 : 'Sets of Manipulators',
                14 : 'Sets of Manipulators',
                15 : 'Sets of Manipulators',
                16 : 'Sets of Manipulators',
                17 : 'Sets of Manipulators'},
            'Skeleton' : {
                3  : 'No Skeleton',
                4  : 'Hydrostatic Skeleton',
                5  : 'Hydrostatic Skeleton',
                6  : 'External Skeleton',
                7  : 'External Skeleton',
                8  : 'Internal Skeleton',
                9  : 'Internal Skeleton',
                10 : 'Internal Skeleton',
                11 : 'Combination',
                12 : 'Combination',
                13 : 'Combination',
                14 : 'Combination',
                15 : 'Combination',
                16 : 'Combination'},
            'Spherical' : {
                1 : '4 Sides',
                2 : '6 Sides',
                3 : '6 Sides',
                4 : '8 Sides',
                5 : '12 Sides',
                6 : '20 Sides'}}

        # *** Dice Roller *** #
        rollA = F.rollDice(6, 2)
        rollB = F.rollDice(6, 1)
        rollC = F.rollDice(6, 1)
        rollD = F.rollDice(6, 2)
        rollE = F.rollDice(6, 2)
        rollF = F.rollDice(6, 2)

        # *** Symmetry *** #
        if self.habitat == 'Space-Dwelling' or self.primaryLocomotion == 'Immobile':
            rollA += 1
            symmetry = table['Symmetry'][rollA]
        else:
            symmetry = table['Symmetry'][rollA]

        if symmetry == 'Radial':
            symmetry += ' {} Sides'.format(rollDice(6, 1) + 3)
            rollC -= 2
        elif symmetry == 'Spherical':
            symmetry += ' {}'.format(table['Symmetry'][rollB])
        elif symmetry == 'Trilateral':
            rollC -= 1

        # *** Limbs *** #
         
	   	
    
    
    def chemicalBasis(self):
        
        # *** Table **** #
        table = {
            3  : 'Hydrogen-Based Life',
            4  : 'Hydrogen-Based Life',
            5  : 'Hydrogen-Based Life',
            6  : 'Ammonia-Based Life',
            7  : 'Ammonia-Based Life',
            8  : 'Hydrocarbon-Based Life',
            9  : 'Water-Based Life',
            10 : 'Water-Based Life',
            11 : 'Water-Based Life',
            12 : 'Chlorine-Based Life',
            13 : 'Silicon/Sulfuric Acid Life',
            14 : 'Silicon/Liquid Sulfur Life',
            15 : 'Silicon/Liquid Rock Life',
            16 : 'Plasma Life',
            17 : 'Exotica',
            18 : 'Exotica'}
    
        # *** Dice Roller *** #
        rollA = F.rollDice(6, 3)
        rollB = F.rollDice(6, 1)

        chemicalBasis = table[rollA]

        # *** Edge Case *** #
        if chemicalBasis == 'Exotica':
            if rollB == 1:
                chemicalBasis = 'Nebula-Dwelling Life'
            elif rollB == 6:
                chemicalBasis = 'Magnetic Life'
            else:
                chemicalBasis = 'Machine Life'

        return chemicalBasis


    def habitat(self):
        
        # *** Tables *** #
        landHab = {
	    3  : 'Plains',
            4  : 'Plains',
            5  : 'Plains',
            6  : 'Plains',
            7  : 'Plains',
            8  : 'Desert',
            9  : 'Island/Beach',
            10 : 'Woodlands',
            11 : 'Swampland',
            12 : 'Mountain',
            13 : 'Artic',
            14 : 'Jungle',
            15 : 'Jungle',
            16 : 'Jungle',
            17 : 'Jungle',
            18 : 'Jungle'}

        waterHab = {
            3  : 'Banks',
            4  : 'Banks',
            5  : 'Banks',
            6  : 'Banks',
            7  : 'Banks',
            8  : 'Open Ocean',
            9  : 'Fresh-Water Lake',
            10 : 'River/Stream',
            11 : 'Tropical Lagoon',
            12 : 'Deep-Ocean Vents',
            13 : 'Salt-Water Sea',
            14 : 'Reef',
            15 : 'Reef',
            16 : 'Reef',
            17 : 'Reef',
            18 : 'Reef'}

        # *** Dice Roller *** #
        rollA = F.rollDice(6, 1)
        rollB = F.rollDice(6, 1)
        rollC = F.rollDice(6, 3)

        # *** Planetary or Space Based *** #
        dwelling = ''
        habitat = ''

        if self.chemicalBasis == 'Nebula-Dwelling Life':
            dwelling = 'Nebula'
            habitat = 'Space-Dwelling'
        elif rollA >= 5:
            dwelling = 'Gas Giant'
            habitat = waterHab[rollC]
        else:
            if rollB <= 3:
                dwelling = 'Land'
                habitat = landHab[rollC]
            else:
                dwelling = 'Water'
                habitat = waterHab[rollC]

        return dwelling, habitat


    def locomotion(self):

        # *** Table *** #
        primary = {
            'Artic' : {
                2  : 'Immobile',
                3  : 'Slithering',
                4  : 'Slithering',
                5  : 'Swimming',
                6  : 'Swimming',
                7  : 'Digging',
                8  : 'Walking',
                9  : 'Walking',
                10 : 'Winged Flight',
                11 : 'Winged Flight',
                12 : 'Special',
                13 : 'Special'},
            'Banks' : {
                2  : 'Immobile',
                3  : 'Immobile',
                4  : 'Floating',
                5  : 'Sailing',
                6  : 'Swimming',
                7  : 'Swimming',
                8  : 'Swimming',
                9  : 'Winged Flight',
                10 : 'Winged Flight',
                11 : 'Winged Flight',
                12 : 'Special',
                13 : 'Special'},
            'Open Ocean' : {
                2  : 'Immobile',
                3  : 'Immobile',
                4  : 'Floating',
                5  : 'Sailing',
                6  : 'Swimming',
                7  : 'Swimming',
                8  : 'Swimming',
                9  : 'Winged Flight',
                10 : 'Winged Flight',
                11 : 'Winged Flight',
                12 : 'Special',
                13 : 'Special'},
            'Deep-Ocean Vents' : {
                2  : 'Immobile',
                3  : 'Immobile',
                4  : 'Immobile',
                5  : 'Immobile',
                6  : 'Floating',
                7  : 'Digging',
                8  : 'Walking',
                9  : 'Walking',
                10 : 'Swimming',
                11 : 'Swimming',
                12 : 'Swimming',
                13 : 'Swimming'},
            'Reef' : {
                2  : 'Immobile',
                3  : 'Immobile',
                4  : 'Immobile',
                5  : 'Immobile',
                6  : 'Floating',
                7  : 'Digging',
                8  : 'Walking',
                9  : 'Walking',
                10 : 'Swimming',
                11 : 'Swimming',
                12 : 'Swimming',
                13 : 'Swimming'},
            'Desert' : {
                2  : 'Immobile',
                3  : 'Slithering',
                4  : 'Slithering',
                5  : 'Digging',
                6  : 'Walking',
                7  : 'Walking',
                8  : 'Walking',
                9  : 'Winged Flight',
                10 : 'Winged Flight',
                11 : 'Winged Flight',
                12 : 'Special',
                13 : 'Special'},
            'Island/Beach' : {
                2  : 'Immobile',
                3  : 'Slithering',
                4  : 'Slithering',
                5  : 'Digging',
                6  : 'Walking',
                7  : 'Walking',
                8  : 'Climbing',
                9  : 'Swimming',
                10 : 'Winged Flight',
                11 : 'Winged Flight',
                12 : 'Special',
                13 : 'Special'},
            'Tropical Lagoon' : {
                2  : 'Immobile',
                3  : 'Immobile',
                4  : 'Immobile',
                5  : 'Floating',
                6  : 'Slithering',
                7  : 'Walking',
                8  : 'Digging',
                9  : 'Swimming',
                10 : 'Winged Flight',
                11 : 'Winged Flight',
                12 : 'Special',
                13 : 'Special'},
            'Fresh-Water Lake' : {
                2  : 'Immobile',
                3  : 'Immobile',
                4  : 'Floating',
                5  : 'Walking',
                6  : 'Slithering',
                7  : 'Swimming',
                8  : 'Swimming',
                9  : 'Swimming',
                10 : 'Winged Flight',
                11 : 'Winged Flight',
                12 : 'Special',
                13 : 'Special'},
            'Salt-Water Sea' : {
                2  : 'Immobile',
                3  : 'Immobile',
                4  : 'Floating',
                5  : 'Walking',
                6  : 'Slithering',
                7  : 'Swimming',
                8  : 'Swimming',
                9  : 'Swimming',
                10 : 'Winged Flight',
                11 : 'Winged Flight',
                12 : 'Special',
                13 : 'Special'},
            'Mountain' : {
                2  : 'Immobile',
                3  : 'Slithering',
                4  : 'Slithering',
                5  : 'Digging',
                6  : 'Walking',
                7  : 'Walking',
                8  : 'Climbing',
                9  : 'Winged Flight',
                10 : 'Winged Flight',
                11 : 'Winged Flight',
                12 : 'Special',
                13 : 'Special'},
            'Plains' : {
                2  : 'Immobile',
                3  : 'Slithering',
                4  : 'Slithering',
                5  : 'Digging',
                6  : 'Walking',
                7  : 'Walking',
                8  : 'Walking',
                9  : 'Winged Flight',
                10 : 'Winged Flight',
                11 : 'Winged Flight',
                12 : 'Special',
                13 : 'Special'},
            'River/Stream' : {
                2  : 'Immobile',
                3  : 'Immobile',
                4  : 'Floating',
                5  : 'Slithering',
                6  : 'Digging',
                7  : 'Walking',
                8  : 'Swimming',
                9  : 'Swimming',
                10 : 'Winged Flight',
                11 : 'Winged Flight',
                12 : 'Special',
                13 : 'Special'},
            'Swampland' : {
                2  : 'Immobile',
                3  : 'Swimming',
                4  : 'Swimming',
                5  : 'Swimming',
                6  : 'Slithering',
                7  : 'Digging',
                8  : 'Walking',
                9  : 'Climbing',
                10 : 'Winged Flight',
                11 : 'Winged Flight',
                12 : 'Special',
                13 : 'Special'},
            'Woodlands' : {
                2  : 'Immobile',
                3  : 'Slithering',
                4  : 'Slithering',
                5  : 'Digging',
                6  : 'Walking',
                7  : 'Walking',
                8  : 'Climbing',
                9  : 'Climbing',
                10 : 'Winged Flight',
                11 : 'Winged Flight',
                12 : 'Special',
                13 : 'Special'},
            'Jungle' : {
                2  : 'Immobile',
                3  : 'Slithering',
                4  : 'Slithering',
                5  : 'Digging',
                6  : 'Walking',
                7  : 'Walking',
                8  : 'Climbing',
                9  : 'Climbing',
                10 : 'Winged Flight',
                11 : 'Winged Flight',
                12 : 'Special',
                13 : 'Special'},
            'Space-Dwelling' : {
                2  : 'Immobile',
                3  : 'Immobile',
                4  : 'Immobile',
                5  : 'Immobile',
                6  : 'Immobile',
                7  : 'Solar Sail',
                8  : 'Solar Sail',
                9  : 'Solar Sail',
                10 : 'Solar Sail',
                11 : 'Solar Sail',
                12 : 'Rocket',
                13 : 'Rocket'}}

        secondary = {
            'Climbing' : {
                2  : 'Slithering',
                3  : 'Slithering',
                4  : 'Slithering',
                5  : 'Slithering',
                6  : 'Slithering',
                7  : 'Walking',
                8  : 'Walking',
                9  : 'Walking',
                10 : 'Walking',
                11 : 'Walking',
                12 : None},
            'Digging' : {
                'Land' : {
                    2  : 'Slithering',
                    3  : 'Slithering',
                    4  : 'Slithering',
                    5  : 'Slithering',
                    6  : 'Slithering',
                    7  : 'Walking',
                    8  : 'Walking',
                    9  : 'Walking',
                    10 : 'Walking',
                    11 : 'Walking',
                    12 : None},
                'Water' : {
                    2  : 'Slithering',
                    3  : 'Slithering',
                    4  : 'Slithering',
                    5  : 'Slithering',
                    6  : 'Walking',
                    7  : 'Walking',
                    8  : 'Swimming',
                    9  : 'Swimming',
                    10 : 'Swimming',
                    11 : 'Swimming',
                    12 : None}},
            'Slithering' : {
                2  : 'Swimming',
                3  : 'Swimming',
                4  : 'Swimming',
                5  : 'Swimming',
                6  : 'Swimming',
                7  : 'Swimming',
                8  : 'Swimming',
                9  : 'Swimming',
                10 : 'Swimming',
                11 : None,
                12 : None},
            'Swimming' : {
                2  : 'Slithering',
                3  : 'Slithering',
                4  : 'Slithering',
                5  : 'Slithering',
                6  : 'Slithering',
                7  : 'Walking',
                8  : 'Walking',
                9  : 'Walking',
                10 : None,
                11 : None,
                12 : None},
            'Walking' : {
                2  : 'Swimming',
                3  : 'Swimming',
                4  : 'Swimming',
                5  : 'Swimming',
                6  : 'Swimming',
                7  : 'Swimming',
                8  : 'Swimming',
                9  : None,
                10 : None,
                11 : None,
                12 : None},
            'Winged Flight' : {
                2  : 'Climbing',
                3  : 'Climbing',
                4  : 'Climbing',
                5  : 'Climbing',
                6  : 'Swimming',
                7  : 'Swimming',
                8  : 'Walking',
                9  : 'Walking',
                10 : 'Walking',
                11 : 'Slithering',
                12 : None}}

        # *** Dice Roller *** #
        rollA = F.rollDice(6, 2)
        rollB = F.rollDice(6, 2)
        rollC = F.rollDice(6, 2)

        # *** Modifiers *** #
        if self.trophicLevel == 'Pouncing Carnivore' or 'Chasing Carnivore' or 'Omnivore' or 'Gathering Herbivore' or 'Scavenger':
            rollA += 1

        # *** Primary *** #
        primaryL = primary[self.habitat][rollA]
        secondaryL = None
        tertiaryL = None

        # *** Secondary *** #
        try:
            if primaryL == 'Digging':
                secondaryL = secondary[primaryL][self.dwelling][rollB]
            else:
                secondaryL = secondary[primaryL][rollB]
        except:
            secondaryL = None

        # *** Tertiary *** #
        try:
            if primaryL == 'Digging':
                if self.habitat == 'Water':
                    if secondaryL == 'Slithering' or 'Walking':
                        tertiaryL = secondary[secondaryL][rollC]
            elif primaryL == 'Winged Flight':
                if secondaryL == 'Climbing' or 'Swimming' or 'Slithering':
                    tertiaryL = secondary[secondaryL][rollC]
        except:
            tertiaryL = None

        return primaryL, secondaryL, tertiaryL


    def sapience(self):

        # *** Dice Roller *** #
        roll = F.rollDice(100, 1)
	
        # *** Sapience *** #
        sapience = ''
        if roll > 95:
            sapience = 'Sapient'
        else:
            sapience = 'Ordinary'

        return sapience


    def size(self):
         
        # *** Tables *** #
        table = {
            'Small' : {
                1 : [0.05, 0.003, -10],
                2 : [0.07, 0.01, -9],
                3 : [0.1, 0.025, -8],
                4 : [0.15, 0.08, -7],
                5 : [0.2, 0.2, -6],
                6 : [0.3, 1, -5]},
            'Human' : {
                1 : [0.5, 4, -4],
                2 : [0.7, 9, -3],
                3 : [1, 25, -2],
                4 : [1.5, 80, -1],
                5 : [2, 200, 0],
                6 : [3, 600, 1]},
            'Large' : {
                1 : [5, 3000, 2],
                2 : [7, 8000, 3],
                3 : [10, 24000, 4],
                4 : [15, 80000, 5],
                5 : [20, 200000, 6],
                6 : [F.rollDice(6, 2) * 10, 200000, 7]},
            'Gravity' : {
                3  : [5.00, 0.30],
                4  : [3.50, 0.40],
                5  : [2.50, 0.50],
                6  : [2.00, 0.60],
                7  : [1.50, 0.75],
                8  : [1.25, 0.90],
                9  : [1.00, 1.00],
                10 : [0.90, 1.10],
                11 : [0.80, 1.20],
                12 : [0.70, 1.30],
                13 : [0.60, 1.40],
                14 : [0.50, 1.60],
                15 : [0.40, 1.80],
                16 : [0.30, 2.20],
                17 : [0.20, 2.90],
                18 : [0.10, 4.60]}}

        # *** Dice Roller *** #
        rollA = F.rollDice(6, 1)
        rollB = F.rollDice(6, 1)
        rollC = F.rollDice(6, 3)

        # *** Modifiers Size Class *** #
        gravity = table['Gravity'][rollC][0]
        if self.chemicalBasis == 'Magnetic Life':
            rollA -= 4
        if 'Parasite/Symbiont' in self.trophicLevel:
            rollA -= 4
        if self.primaryLocomotion == 'Winged Flight':
            rollA -= 3
        if gravity > 2:
            rollA -= 2
        if 1.5 <= gravity <= 2:
            rollA -= 1
        if self.habitat == 'Tropical Lagoon':
            rollA -= 1
        if self.habitat == 'River/Stream':
            rollA -= 1
        if self.habitat == 'Island/Beach':
            rollA -= 1
        if self.habitat == 'Desert':
            rollA -= 1
        if self.habitat == 'Mountain':
            rollA -= 1
        if 0.5 <= gravity <= 0.75:
            rollA += 1
        if self.habitat == 'Plains':
            rollA += 1
        if self.habitat == 'Open Ocean':
            rollA += 1
        if self.habitat == 'Banks':
            rollA += 1
        if self.trophicLevel == 'Grazing Herbivore':
            rollA += 1
        if self.dwelling == 'Water':
            rollA += 1
        if gravity <= 0.4:
            rollA +=2
        if self.habitat == 'Space-Dwelling':
            rollA += 3

        # *** Size Class *** #
        if rollA <= 2:
            sizeClass = 'Small'
        elif rollA >= 5:
            sizeClass = 'Large'
        else:
            sizeClass = 'Human'

        # *** Size | Weight | Modifier
        size = table[sizeClass][rollB][0]
        weight = table[sizeClass][rollB][1]
        sizeMod = table[sizeClass][rollB][2]

        # *** Size | Weight | Size Mod | Modifiers *** #
        if 'Silicon' in self.chemicalBasis:
            weight *= 2
        if self.chemicalBasis == 'Magnetic Life':
            size /= 1000
        if self.chemicalBasis == 'Hydrogen-Based Life' or self.chemicalBasis == 'Plasma Life':
            weight /= 10
        if self.habitat == 'Space-Dwelling':
            weight /= 5

        # *** Randomize Weight *** #
        start, stop = weight / 2, weight * 2
        if start != 0:
            weight = F.randWeight(start, stop)
        weight = float('{:.2f}'.format(weight))

        # *** Strength *** #
        strength = 2 * (weight ** (1.0/3.0))
        strength = round(strength)

        return sizeClass, size, weight, sizeMod, strength, gravity


    def trophicLevel(self, loop):
        
        # *** Tables *** #
        ordinary = {
            3  : 'Combined',
            4  : 'Autotroph',
            5  : 'Decomposer',
            6  : 'Scavenger',
            7  : 'Omnivore',
            8  : 'Gathering Herbivore',
            9  : 'Gathering Herbivore',
            10 : 'Grazing/Browsing Herbivore',
            11 : 'Grazing/Browsing Herbivore',
            12 : 'Pouncing Carnivore',
            13 : 'Chasing Carnivore',
            14 : 'Trapping Carnivore',
            15 : 'Hijacking Carnivore',
            16 : 'Filter-Feeder',
            17 : 'Parasite/Symbiont',
            18 : 'Parasite/Symbiont'}

        sapient = {
            3  : 'Combined',
            4  : 'Parasite/Symbiont',
            5  : 'Filter-Feeder',
            6  : 'Pouncing Carnivore',
            7  : 'Scavenger',
            8  : 'Gathering Herbivore',
            9  : 'Gathering Herbivore',
            10 : 'Omnivore',
            11 : 'Chasing Carnivore',
            12 : 'Chasing Carnivore',
            13 : 'Grazing Herbivore',
            14 : 'Hijacking Carnivore',
            15 : 'Trapping Carnivore',
            16 : 'Trapping Carnivore',
            17 : 'Decomposer',
            18 : 'Autotroph'}

        autotroph = {
            1 : 'Photosynthesis',
            2 : 'Photosynthesis',
            3 : 'Photosynthesis',
            4 : 'Chemosynthesis',
            5 : 'Chemosynthesis',
            6 : 'Other'}

        # *** Dice Roller *** #
        rollA = F.rollDice(6, 3)
        rollB = F.rollDice(3, 1)
        rollC = F.rollDice(6, 1)

        # *** Trophic Level *** #
        trophicLevel = ''
        if self.sapience == 'Sapient':
            trophicLevel = sapient[rollA]
        else:
            trophicLevel = ordinary[rollA]
        
        # *** Edge Cases *** #
        if trophicLevel == 'Autotroph':
            if self.habitat == 'Deep-Ocean Vents':
                trophicLevel += ': {}'.format(autotroph[3 + rollB])
            else:
                trophicLevel += ': {}'.format(autotroph[rollC])

        if trophicLevel == 'Filter Feeder':
            if self.habitat == 'Artic' or 'Desert':
                trophicLevel = 'Trapping Carnivore'

        if trophicLevel == 'Combined':
            if loop == 0:
                trophicLevelA = Alien.trophicLevel(self, 1)
                trophicLevelB = Alien.trophicLevel(self, 1)
                trophicLevel += ': {} | {}'.format(trophicLevelA, trophicLevelB)
            else:
                trophicLevel = Alien.trophicLevel(self, 1)

        return trophicLevel


# *** Functions *** #
def main():
    entries = 1000
    counter = 0
    print('Starting Alien Creation...')
    for i in range(1, entries + 1, 1):
        alien = Alien()
        # if alien.strength <= 100:
            # counter += 1
        alien.attributes()
        print('\n')
    print('Finished Alien Creation...')
    print('{} Entries Created...'.format(entries))
    # print('{} Entries with Strength >= 100'.format(counter))
    # print('{} Percent of Total Entries'.format(counter / entries * 100))


# *** Main *** #
if __name__ == '__main__':
    main()
