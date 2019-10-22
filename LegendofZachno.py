# Import necessary modules
import pygame
import sys
import random
import os
import math
from pytictoc import TicToc

# Initializing the pygame components i use 
pygame.mixer.pre_init()
pygame.init()
pygame.font.init()

pygame.mixer.init()
myfont = pygame.font.SysFont('Arial', 20)
Time=TicToc()

#Storing color coded in variables so i can use a name when i want to color text
white = ((255,255,255))
blue = ((0,0,255))
green = ((0,255,0))
red = ((255,0,0))
black = ((0,0,0))
orange = ((255,100,10))
yellow = ((255,255,0))
blue_green = ((0,255,170))
marroon = ((115,0,0))
lime = ((180,255,100))
pink = ((255,100,180))
purple = ((240,0,255))
gray = ((127,127,127))
magenta = ((255,0,230))
brown = ((100,40,0))
forest_green = ((0,50,0))
navy_blue = ((0,0,100))
rust = ((210,150,75))
dandilion_yellow = ((255,200,0))
highlighter = ((255,255,100))
sky_blue = ((0,255,255))
light_grey = ((200,200,200))
dark_grey = ((50,50,50))
tan = ((230,220,170))
coffee_brown =((200,190,140))
moon_glow = ((235,245,255))

# Loading soundfiles into RAM in variables so i can use the .play() command
Walk = pygame.mixer.Sound('Walk.ogg')
EnemyWalk = pygame.mixer.Sound('EnemyWalk.ogg')
Bump = pygame.mixer.Sound('Bump.ogg')
StairsUp = pygame.mixer.Sound('Up.ogg')
Ping = pygame.mixer.Sound('Ping.ogg')
OpeningChest = pygame.mixer.Sound('OpeningChest.ogg')
Life = pygame.mixer.Sound('Life.ogg')
Mana = pygame.mixer.Sound('Mana.ogg')
Grab = pygame.mixer.Sound('Grab.ogg')
Clank = pygame.mixer.Sound('Clank.ogg')
Fire = pygame.mixer.Sound('Fire.ogg')
Teleport = pygame.mixer.Sound('Teleport.ogg')
Steal = pygame.mixer.Sound('Steal.ogg')
Lightning = pygame.mixer.Sound('Lightning.ogg')
Fireball = pygame.mixer.Sound('Fireball.ogg')
Punch = pygame.mixer.Sound('Punch.ogg')
Stab = pygame.mixer.Sound('Stab.ogg')
MaceHit = pygame.mixer.Sound('MaceHit.ogg')
SwordHit = pygame.mixer.Sound('SwordHit.ogg')
AxeHit = pygame.mixer.Sound('AxeHit.ogg')
Auch = pygame.mixer.Sound('Auch.ogg')
Applause = pygame.mixer.Sound('Applause.ogg')
Fail = pygame.mixer.Sound('Fail.ogg')
DeathScream = pygame.mixer.Sound('DeathScream.ogg')
Spikes = pygame.mixer.Sound('Spikes.ogg')
Trap = pygame.mixer.Sound('Trap.ogg')
Sizzle = pygame.mixer.Sound('Sizzle.ogg')
Boom = pygame.mixer.Sound('Boom.ogg')
Shatter = pygame.mixer.Sound('Shatter.ogg')
Tinkering = pygame.mixer.Sound('Tinkering.ogg')

# Loading picture files into RAM
Black=pygame.image.load('Black.png')
Loading=pygame.image.load('Loading.png')
Floor=pygame.image.load('newFloor.PNG')
Stairs=pygame.image.load('newStairs.PNG')
Wall=pygame.image.load('newWall.PNG')
Player=pygame.image.load('newMonster.PNG')
TextBar=pygame.image.load('TextBar.png')
Splash=pygame.image.load('Splash.png')
Leather=pygame.image.load('Leather.png')
Skull=pygame.image.load('Skull.png')
Wood=pygame.image.load('Wood.png')
Iron=pygame.image.load('Iron.png')
Steel=pygame.image.load('Steel.png')
Shield=pygame.image.load('Shield.png')
ChestClosed=pygame.image.load('ChestClosed.png')
ChestOpen=pygame.image.load('ChestOpen.png')
Mace=pygame.image.load('Mace.png')
BearTrap=pygame.image.load('BearTrap.png')
Mine=pygame.image.load('Mine.png')
LifePotion=pygame.image.load('Life.png')
ManaPotion=pygame.image.load('Mana.png')
Dagger=pygame.image.load('Dagger.png')
Sword=pygame.image.load('Sword.png')
BattleAxe=pygame.image.load('BattleAxe.png')
DaggerSmall=pygame.image.load('DaggerSmall.png')
SwordSmall=pygame.image.load('SwordSmall.png')
MaceSmall=pygame.image.load('MaceSmall.png')
BattleAxeSmall=pygame.image.load('BattleAxeSmall.png')
ShieldSmall=pygame.image.load('ShieldSmall.png')
WShieldSmall=pygame.image.load('WShieldSmall.png')
TShieldSmall=pygame.image.load('TShieldSmall.png')
WShield=pygame.image.load('WShield.png')
TShield=pygame.image.load('TShield.png')
Dead=pygame.image.load('Dead.png')

SpikeTrap=pygame.image.load('SpikeTrap.png')
AcidTrap=pygame.image.load('AcidTrap.png')
ElectroTrap=pygame.image.load('ElectroTrap.png')
FireScroll=pygame.image.load('FireScroll.png')
TeleportScroll=pygame.image.load('TeleportScroll.png')
LightningScroll=pygame.image.load('LightningScroll.png')
DrainScroll=pygame.image.load('DrainScroll.png')
FireballScroll=pygame.image.load('FireballScroll.png')
Flame=pygame.image.load('Flame.png')
Wormhole=pygame.image.load('Wormhole.png')
Heart=pygame.image.load('Heart.png')
Bolt=pygame.image.load('Bolt.png')
Blast=pygame.image.load('Blast.png')
Gnome=pygame.image.load('Gnome.png')
BloodSpatter=pygame.image.load('BloodSpatter.png')
AcidPuddle=pygame.image.load('AcidPuddle.png')
ElectricSpark=pygame.image.load('ElectricSpark.png')
Explosion=pygame.image.load('Explosion.png')


Soldier=pygame.image.load('Soldier.png')
Rogue=pygame.image.load('Rogue.png')
Amazon=pygame.image.load('Amazon.png')
Wizard=pygame.image.load('Wizard.png')
Knight=pygame.image.load('Knight.png')

Chainmail=pygame.image.load('Chainmail.png')
ChainmailSmall=pygame.image.load('ChainmailSmall.png')
Plate=pygame.image.load('Plate.png')
PlateSmall=pygame.image.load('PlateSmall.png')


# Declaring the main game screen, only do this once, outside of a loop otherwise video-memory will be flooded after extended game-play
pygame.display.set_caption('Legend of Zachno')
Width=int(1200)
Heigth=int(800)
screen = pygame.display.set_mode((Width, Heigth))
Message=''

# Setting intitial player coordinated
PlayerX=0
PlayerY=0

# Declaring arrays
Labyrinth=list()
RoomPos=list()
Room=list()
VisualList=list()
HeroLifeList=list()
Spacebar=False
PlayerPos=[PlayerX, PlayerY]
NextLevel=False
global StairsX
global StairsY
global MapGen

# LevelMax is the highest map level +1
LevelMax=21
StairsX=0
StairsY=-2

# Declaring the map for level zero
Labyrinth=['Wall','-3','3','Wall','-2','3','Wall','-1','3','Wall','0','3','Wall','1','3','Wall','2','3','Wall','3','3','Wall','-3','2','Floor','-2','2','Floor','-1','2','Floor','0','2',
'Floor','1','2','Floor','2','2','Wall','3','2','Wall','-3','1','Floor','-2','1','Floor','-1','1','Floor','0','1','Floor','1','1','Floor','2','1','Wall','3','1',
'Wall','-3','0','Floor','-2','0','Floor','-1','0','Floor','0','0','Floor','1','0','Floor','2','0','Wall','3','0',
'Wall','-3','-1','Floor','-2','-1','Floor','-1','-1','Floor','0','-1','Floor','1','-1','Floor','2','-1','Wall','3','-1',
'Wall','-3','-2','Floor','-2','-2','Floor','-1','-2','Stairs','0','-2','Floor','1','-2','Floor','2','-2','Wall','3','-2',
'Wall','-3','-3','Wall','-2','-3','Wall','-1','-3','Wall','0','-3','Wall','1','-3','Wall','2','-3','Wall','3','-3']


# A pause function
def wait():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
	                		return

# Function that collects items from the game array when they are in screen range, these are stored in the VisualList array which DoScreen uses
# XDiff and YDiff are x/y coordinates relative to the player
def VisualScan(Labyrinth, HeroList):
	del VisualList[:]
	MaxCounter=len(Labyrinth)
	Counter=0
	while Counter<MaxCounter:
		Object=str(Labyrinth[Counter])
		ObjectX=int(Labyrinth[Counter+1])
		ObjectY=int(Labyrinth[Counter+2])
		XDiff=ObjectX-PlayerX
		YDiff=ObjectY-PlayerY
		if (-7 <= XDiff) and ( XDiff <= 7) and (-5 <= YDiff) and (YDiff <= 4):
			VisualList.append(Object)
			VisualList.append(XDiff)
			VisualList.append(YDiff)
		Counter=Counter+3
	MaxCounter=len(HeroList)
	Counter=0
	while Counter<MaxCounter:
		Object=str(HeroList[Counter+1])
		ObjectX=int(HeroList[Counter+13])
		ObjectY=int(HeroList[Counter+14])
		XDiff=ObjectX-PlayerX
		YDiff=ObjectY-PlayerY
		if (-7 <= XDiff) and ( XDiff <= 7) and (-5 <= YDiff) and (YDiff <= 4):
			VisualList.append(Object)
			VisualList.append(XDiff)
			VisualList.append(YDiff)
		Counter=Counter+15
	return(VisualList)

# Translates items in game array to pictures
def GetScreenItem(ObjectImage):
	if ObjectImage=='Wall':
		ScreenItem=Wall
	elif ObjectImage=='Floor':
		ScreenItem=Floor
	elif ObjectImage=='Stairs':
		ScreenItem=Stairs
	elif ObjectImage=='Leather':
		ScreenItem=Leather
	elif ObjectImage=='Skull':
		ScreenItem=Skull
	elif ObjectImage=='Wood':
		ScreenItem=Wood
	elif ObjectImage=='Iron':
		ScreenItem=Iron
	elif ObjectImage=='Steel':
		ScreenItem=Steel
	elif ObjectImage=='Shield':
		ScreenItem=Shield
	elif ObjectImage=='ChestClosed':
		ScreenItem=ChestClosed
	elif ObjectImage=='ChestOpen':
		ScreenItem=ChestOpen
	elif ObjectImage=='Mace':
		ScreenItem=Mace
	elif ObjectImage=='BearTrap':
		ScreenItem=BearTrap
	elif ObjectImage=='ElectroTrap':
		ScreenItem=ElectroTrap
	elif ObjectImage=='Mine':
		ScreenItem=Mine
	elif ObjectImage=='Life':
		ScreenItem=LifePotion
	elif ObjectImage=='Mana':
		ScreenItem=ManaPotion
	elif ObjectImage=='Dagger':
		ScreenItem=Dagger
	elif ObjectImage=='Sword':
		ScreenItem=Sword
	elif ObjectImage=='BattleAxe':
		ScreenItem=BattleAxe
	elif ObjectImage=='SpikeTrap':
		ScreenItem=SpikeTrap
	elif ObjectImage=='AcidTrap':
		ScreenItem=AcidTrap
	elif ObjectImage=='FireScroll':
		ScreenItem=FireScroll
	elif ObjectImage=='TeleportScroll':
		ScreenItem=TeleportScroll
	elif ObjectImage=='DrainScroll':
		ScreenItem=DrainScroll
	elif ObjectImage=='LightningScroll':
		ScreenItem=LightningScroll
	elif ObjectImage=='FireballScroll':
		ScreenItem=FireballScroll
	elif ObjectImage=='WShield':
		ScreenItem=WShield
	elif ObjectImage=='Shield':
		ScreenItem=Shield
	elif ObjectImage=='TShield':
		ScreenItem=TShield
	elif ObjectImage=='Chainmail':
		ScreenItem=Chainmail
	elif ObjectImage=='Plate':
		ScreenItem=Plate
	elif ObjectImage=='Gnome':
		ScreenItem=Gnome
	elif ObjectImage=='Benny':
		ScreenItem=Soldier
	elif ObjectImage=='Dave':
		ScreenItem=Soldier
	elif ObjectImage=='Watch':
		ScreenItem=Soldier
	elif ObjectImage=='Flame Soldier':
		ScreenItem=Soldier
	elif ObjectImage=='Berserker':
		ScreenItem=Knight
	elif ObjectImage=='Trapper':
		ScreenItem=Rogue
	elif ObjectImage=='Guard':
		ScreenItem=Soldier
	elif ObjectImage=='Grenadier':
		ScreenItem=Soldier
	elif ObjectImage=='Knight':
		ScreenItem=Knight
	elif ObjectImage=='Amazon':
		ScreenItem=Amazon
	elif ObjectImage=='Heavy Guard':
		ScreenItem=Soldier
	elif ObjectImage=='Warlock':
		ScreenItem=Wizard
	elif ObjectImage=='Hell Knight':
		ScreenItem=Knight
	elif ObjectImage=='Paladin':
		ScreenItem=Knight
	elif ObjectImage=='Rogue':
		ScreenItem=Rogue
	elif ObjectImage=='Blink Rogue':
		ScreenItem=Rogue
	elif ObjectImage=='Defender':
		ScreenItem=Knight
	elif ObjectImage=='Shield Maiden':
		ScreenItem=Amazon
	elif ObjectImage=='Greater Knight':
		ScreenItem=Knight
	elif ObjectImage=='Thunder Wizard':
		ScreenItem=Wizard
	elif ObjectImage=='Pyromancer Knight':
		ScreenItem=Knight
	elif ObjectImage=='Warlord':
		ScreenItem=Knight
	elif ObjectImage=='Vampire Queen':
		ScreenItem=Amazon
	elif ObjectImage=='Storm Mage':
		ScreenItem=Wizard
	elif ObjectImage=='Destroyer':
		ScreenItem=Knight
	elif ObjectImage=='Annihilator Knight':
		ScreenItem=Knight
	elif ObjectImage=='Lancelot':
		ScreenItem=Knight
	elif ObjectImage=='King Arthur':
		ScreenItem=Knight
	return(ScreenItem)

def DoInventoryList():
	if len(InvList) > 0:
		ItemText='1> '+InvList[0].rstrip()
		ItemTextSurf=myfont.render(ItemText, False, sky_blue)		
		screen.blit(ItemTextSurf,(950,200))
	if len(InvList) > 1:
		ItemText='2> '+InvList[1].rstrip()
		ItemTextSurf=myfont.render(ItemText, False, sky_blue)		
		screen.blit(ItemTextSurf,(950,220))
	if len(InvList) > 2:
		ItemText='3> '+InvList[2].rstrip()
		ItemTextSurf=myfont.render(ItemText, False, sky_blue)		
		screen.blit(ItemTextSurf,(950,240))
	if len(InvList) > 3:
		ItemText='4> '+InvList[3].rstrip()
		ItemTextSurf=myfont.render(ItemText, False, sky_blue)		
		screen.blit(ItemTextSurf,(950,260))
	if len(InvList) > 4:
		ItemText='5> '+InvList[4].rstrip()
		ItemTextSurf=myfont.render(ItemText, False, sky_blue)		
		screen.blit(ItemTextSurf,(950,280))
	if len(InvList) > 5:
		ItemText='6> '+InvList[5].rstrip()
		ItemTextSurf=myfont.render(ItemText, False, sky_blue)		
		screen.blit(ItemTextSurf,(950,300))
	if len(InvList) > 6:
		ItemText='7> '+InvList[6].rstrip()
		ItemTextSurf=myfont.render(ItemText, False, sky_blue)		
		screen.blit(ItemTextSurf,(950,320))
	if len(InvList) > 7:
		ItemText='8> '+InvList[7].rstrip()
		ItemTextSurf=myfont.render(ItemText, False, sky_blue)		
		screen.blit(ItemTextSurf,(950,340))
	if len(InvList) > 8:
		ItemText='9> '+InvList[8].rstrip()
		ItemTextSurf=myfont.render(ItemText, False, sky_blue)		
		screen.blit(ItemTextSurf,(950,360))
	if len(InvList) > 9:
		ItemText='0> '+InvList[9].rstrip()
		ItemTextSurf=myfont.render(ItemText, False, sky_blue)		
		screen.blit(ItemTextSurf,(950,380))
	return

def HeroScan(Labyrinth, HeroList):
	del HeroLifeList[:]
	MaxCounter=len(HeroList)
	Counter=0
	while Counter<MaxCounter:
		HeroName=str(HeroList[Counter+1])
		HeroLife=int(HeroList[Counter+9])
		HeroWeapon=str(HeroList[Counter+2])
		HeroArmor=str(HeroList[Counter+3])
		HeroSpell=str(HeroList[Counter+4])
		HeroAtt=int(HeroList[Counter+5])
		HeroDef=int(HeroList[Counter+6])
		HeroMana=int(HeroList[Counter+10])
		ObjectX=int(HeroList[Counter+13])
		ObjectY=int(HeroList[Counter+14])
		if HeroWeapon=='Dagger':
			HeroAtt=HeroAtt+4
		elif HeroWeapon=='Mace':
			HeroAtt=HeroAtt+6
		elif HeroWeapon=='Sword':
			HeroAtt=HeroAtt+8
		elif HeroWeapon=='Battleaxe':
			HeroAtt=HeroAtt+10

		if HeroArmor=='WShield':
			HeroDef=HeroDef+1
		elif HeroArmor=='Shield':
			HeroDef=HeroDef+2
		elif HeroArmor=='TShield':
			HeroDef=HeroDef+3
		elif HeroArmor=='Chainmail':
			HeroDef=HeroDef+4
		elif HeroArmor=='Plate':
			HeroDef=HeroDef+5
		XDiff=ObjectX-PlayerX
		YDiff=ObjectY-PlayerY
		if (-7 <= XDiff) and ( XDiff <= 7) and (-5 <= YDiff) and (YDiff <= 4):
			HeroLifeList.append(HeroName)
			HeroLifeList.append(HeroWeapon)
			HeroLifeList.append(HeroArmor)
			HeroLifeList.append(HeroSpell)
			HeroLifeList.append(HeroAtt)
			HeroLifeList.append(HeroDef)
			HeroLifeList.append(HeroLife)
			HeroLifeList.append(HeroMana)
			HeroLifeList.append(XDiff)
			HeroLifeList.append(YDiff)
		Counter=Counter+15
	return(HeroLifeList)

# Display function
def DoScreen (Labyrinth, Level):
	# Calling VisualScan to fill VisualList
	global PlayerLife
	global Spacebar
	VisualScan(Labyrinth, HeroList)
	HeroScan(Labyrinth, HeroList)
	Counter=0
	MaxCounter=len(VisualList)
	screen.blit(Black,(0,0))
	# Looping through VisualList to get an object name and an x and y coordinate
	while Counter < MaxCounter:
		ObjectImage=str(VisualList[Counter])
		ObjectX=int(VisualList[Counter+1])
		ObjectY=int(VisualList[Counter+2])
		# calling GetScreenItem to get the right picture with the object name
		ScreenItem=GetScreenItem(ObjectImage)
		# Translating x and y coordinates from VisualList into actual pixel coordinatesd
		ScreenX=(ObjectX+7)*80
		YConvert=ObjectY*-1
		ScreenY=(YConvert+4)*80
		# Placing the item on screen
		screen.blit(ScreenItem, (ScreenX, ScreenY))
		Counter=Counter+3

	if PlayerWeapon=='Dagger':
		PlayerAtt=PlayerAttack+4
	elif PlayerWeapon=='Mace':
		PlayerAtt=PlayerAttack+6
	elif PlayerWeapon=='Sword':
		PlayerAtt=PlayerAttack+8
	elif PlayerWeapon=='Battleaxe':
		PlayerAtt=PlayerAttack+10
	else:
		PlayerAtt=PlayerAttack

	Counter=0
	MaxCounter=len(HeroLifeList)
	while Counter < MaxCounter:
		HeroName=str(HeroLifeList[Counter])
		HeroWeapon=str(HeroLifeList[Counter+1])
		HeroArmor=str(HeroLifeList[Counter+2])
		HeroSpell=str(HeroLifeList[Counter+3])
		HeroAtt=int(HeroLifeList[Counter+4])
		HeroDef=int(HeroLifeList[Counter+5])
		HeroLife=int(HeroLifeList[Counter+6])
		HeroMana=int(HeroLifeList[Counter+7])
		ObjectX=int(HeroLifeList[Counter+8])
		ObjectY=int(HeroLifeList[Counter+9])
		# calling GetScreenItem to get the right picture with the object name
		ScreenX=((ObjectX+7)*80)
		YConvert=ObjectY*-1
		ScreenY=((YConvert+4)*80)

		if HeroArmor=='Shield':
			screen.blit(ShieldSmall, ((ScreenX+40), (ScreenY+20)))
		elif HeroArmor=='WShield':
			screen.blit(WShieldSmall, ((ScreenX+40), (ScreenY+20)))
		elif HeroArmor=='TShield':
			screen.blit(TShieldSmall, ((ScreenX+40), (ScreenY+20)))
		elif HeroArmor=='Chainmail':
			screen.blit(ChainmailSmall, ((ScreenX+20), (ScreenY+40)))
		elif HeroArmor=='Plate':
			screen.blit(PlateSmall, ((ScreenX+20), (ScreenY+40)))
	
		if HeroWeapon=='Dagger':
			screen.blit(DaggerSmall, (ScreenX, ScreenY))
		elif HeroWeapon=='Sword':
			screen.blit(SwordSmall, (ScreenX, ScreenY))
		elif HeroWeapon=='Mace':
			screen.blit(MaceSmall, (ScreenX, ScreenY))
		elif HeroWeapon=='Battleaxe':
			screen.blit(BattleAxeSmall, (ScreenX, ScreenY))


		if HeroSpell == 'None':
			Namecolor=green
		else:
			Namecolor=sky_blue

		if HeroDef >= PlayerAtt:
			color=red
		else:
			color=green
		HeroNameText=str(HeroName)
		HeroLifeTextSurf=myfont.render(HeroNameText, False, Namecolor)
		HeroText1='Att:'+str(HeroAtt)+' Def:'+str(HeroDef)
		HeroText1Surf=myfont.render(HeroText1, False, color)
		HeroText2='Life:'+str(HeroLife)+' Mana:'+str(HeroMana)
		HeroText2Surf=myfont.render(HeroText2, False, color)

		# Translating x and y coordinates from VisualList into actual pixel coordinatesd
		ScreenX=(ObjectX+7)*80
		YConvert=ObjectY*-1
		ScreenY=((YConvert+4)*80)+60
		# Placing the item on screen
		screen.blit(HeroLifeTextSurf, (ScreenX, ScreenY))
		ScreenY=((YConvert+4)*80)+80
		screen.blit(HeroText1Surf, (ScreenX, ScreenY))
		ScreenY=((YConvert+4)*80)+100
		screen.blit(HeroText2Surf, (ScreenX, ScreenY))
		Counter=Counter+10

	

#	Xdiff=StairsX-PlayerX
#	Ydiff=StairsY-PlayerY

#	if (Xdiff==0) and (Ydiff==0):
#		StairDistance=0
#	else:
#		StairDistance=int(math.sqrt((Xdiff**2+Ydiff**2)))


	# Preparing and 'blitting' text on the game screen
	MapGen=int(Level/2)+1
	if Level==0:
		Size=7
	else:
		Size=(MapGen*2*9)+9

	LevelText = 'Level: '+str(Level)
	PlayerPosText = 'Position: '+str(PlayerX)+' '+str(PlayerY)
	LabyrinthText='Size of map: '+str(Size)+' by '+str(Size)
	GoldText='Player gold: '+str(Gold)

	LeatherText='Leather: '+str(LeatherAmount)
	BoneText='Bone: '+str(BoneAmount)
	WoodText='Wood: '+str(WoodAmount)
	IronText='Iron: '+str(IronAmount)
	SteelText='Steel: '+str(SteelAmount)
	CraftText='Press <c> to craft items'

	SlotText='Saveslot: '+str(int((SaveSlot+19)/19))
	NumberOfEnemiesText='Enemies: '+str(int(len(HeroList)/15))
	EscapeText='Press <esc> to quit game'

	PlayerAttackText='Attack: '
	PlayerDefenceText='Defence:'
	PlayerLifeLevelText='Health: '
	PlayerMagicText='Magic: '
	PlayerLifeText='Life: '
	PlayerManaText='Mana: '

	PlayerAttackTextSurf=myfont.render(PlayerAttackText, False, green)
	PlayerDefenceTextSurf=myfont.render(PlayerDefenceText, False, green)
	PlayerLifeLevelTextSurf=myfont.render(PlayerLifeLevelText, False, green)
	PlayerMagicTextSurf=myfont.render(PlayerMagicText, False, green)
	PlayerLifeTextSurf=myfont.render(PlayerLifeText, False, green)
	PlayerManaTextSurf=myfont.render(PlayerManaText, False, green)

	screen.blit(PlayerAttackTextSurf,(950,0))
	screen.blit(PlayerDefenceTextSurf,(950,20))
	screen.blit(PlayerLifeLevelTextSurf,(950,40))
	screen.blit(PlayerMagicTextSurf,(950,60))
	screen.blit(PlayerLifeTextSurf,(950,80))
	screen.blit(PlayerManaTextSurf,(950,100))
	Att=''
	Arm=''
	if PlayerWeapon=='Dagger':
		Att='+4'
	elif PlayerWeapon=='Mace':
		Att='+6'
	elif PlayerWeapon=='Sword':
		Att='+8'
	elif PlayerWeapon=='Battleaxe':
		Att='+10'

	if PlayerArmor=='WShield':
		Arm='+1'
	elif PlayerArmor=='Shield':
		Arm='+2'
	elif PlayerArmor=='TShield':
		Arm='+3'
	elif PlayerArmor=='Chainmail':
		Arm='+4'
	elif PlayerArmor=='Plate':
		Arm='+5'


	PlayerAttackNo=str(PlayerAttack)+Att
	PlayerDefenceNo=str(PlayerDefence)+Arm
	PlayerLifeLevelNo=str(PlayerLifeLevel)
	PlayerMagicNo=str(PlayerMagic)
	PlayerLifeNo=str(PlayerLife)+'/'+str(PlayerLifeLevel*10)
	PlayerManaNo=str(PlayerMana)+'/'+str(PlayerMagic*5)

	PlayerAttackNoSurf=myfont.render(PlayerAttackNo, False, green)
	PlayerDefenceNoSurf=myfont.render(PlayerDefenceNo, False, green)
	PlayerLifeLevelNoSurf=myfont.render(PlayerLifeLevelNo, False, green)
	PlayerMagicNoSurf=myfont.render(PlayerMagicNo, False, green)
	PlayerLifeNoSurf=myfont.render(PlayerLifeNo, False, green)
	PlayerManaNoSurf=myfont.render(PlayerManaNo, False, green)

	screen.blit(PlayerAttackNoSurf,(1100,0))
	screen.blit(PlayerDefenceNoSurf,(1100,20))
	screen.blit(PlayerLifeLevelNoSurf,(1100,40))
	screen.blit(PlayerMagicNoSurf,(1100,60))
	screen.blit(PlayerLifeNoSurf,(1100,80))
	screen.blit(PlayerManaNoSurf,(1100,100))

	DoInventoryList()

	WeaponText='Weapon:'
	ArmorText='Armor:'
	WeaponTextSurf=myfont.render(WeaponText, False, green)
	ArmorTextSurf=myfont.render(ArmorText, False, green)

	screen.blit(WeaponTextSurf,(950,140))
	screen.blit(ArmorTextSurf,(950,160))

	PlayerWeaponText=PlayerWeapon
	PlayerArmorText=PlayerArmor
	PlayerWeaponTextSurf=myfont.render(PlayerWeaponText, False, green)
	PlayerArmorTextSurf=myfont.render(PlayerArmorText, False, green)

	screen.blit(PlayerWeaponTextSurf,(1100,140))
	screen.blit(PlayerArmorTextSurf,(1100,160))

	LevelTextSurf=myfont.render(LevelText, 1, green)
	PlayerPosTextSurf = myfont.render(PlayerPosText, False, green)
	LabyrinthTextSurf = myfont.render(LabyrinthText, False, green)
	GoldTextSurf = myfont.render(GoldText, False, green)

	LeatherTextSurf = myfont.render(LeatherText, False, green)
	BoneTextSurf = myfont.render(BoneText, False, green)
	WoodTextSurf = myfont.render(WoodText, False, green)
	IronTextSurf = myfont.render(IronText, False, green)
	SteelTextSurf = myfont.render(SteelText, False, green)
	CraftTextSurf = myfont.render(CraftText, False, green)

	SlotTextSurf=myfont.render(SlotText, False, green)
	NumberOfEnemiesTextSurf=myfont.render(NumberOfEnemiesText, False, green)
	EscapeTextSurf=myfont.render(EscapeText, False, green)

	screen.blit(LevelTextSurf,(0,0))
	screen.blit(PlayerPosTextSurf,(0,20))
	screen.blit(LabyrinthTextSurf,(0,40))
	screen.blit(GoldTextSurf,(0,60))
	screen.blit(LeatherTextSurf,(0,100))
	screen.blit(BoneTextSurf,(0,120))
	screen.blit(WoodTextSurf,(0,140))
	screen.blit(IronTextSurf,(0,160))
	screen.blit(SteelTextSurf,(0,180))
	if len(InvList) < 10:
		screen.blit(CraftTextSurf,(0,220))

	screen.blit(SlotTextSurf,(550,0))
	screen.blit(NumberOfEnemiesTextSurf,(550,20))
	screen.blit(EscapeTextSurf,(550,40))

	#screen.blit(StairsPosTextSurf,(0,20))
	# Placing the player picture in the middle of the screen

	screen.blit(Player, (560, 320))
	screen.blit(PlayerLifeNoSurf,(560,400))
	if PlayerArmor=='Shield':
		screen.blit(ShieldSmall, (600, 340))
	elif PlayerArmor=='WShield':
		screen.blit(WShieldSmall, (600, 340))
	elif PlayerArmor=='TShield':
		screen.blit(TShieldSmall, (600, 340))
	elif PlayerArmor=='Chainmail':
		screen.blit(ChainmailSmall, (580, 360))
	elif PlayerArmor=='Plate':
		screen.blit(PlateSmall, (580, 360))

	if PlayerWeapon=='Dagger':
		screen.blit(DaggerSmall, (560, 320))
	elif PlayerWeapon=='Sword':
		screen.blit(SwordSmall, (560, 320))
	elif PlayerWeapon=='Mace':
		screen.blit(MaceSmall, (560, 320))
	elif PlayerWeapon=='Battleaxe':
		screen.blit(BattleAxeSmall, (560, 320))

	SpellXDiff=SpellX-PlayerX
	SpellYDiff=SpellY-PlayerY
	ScreenX=(SpellXDiff+7)*80
	YConvert=SpellYDiff*-1
	ScreenY=(YConvert+4)*80
	if Spell=='Fire':
		ScreenItem=Flame
	elif Spell=='Teleport':
		ScreenItem=Wormhole
	elif Spell=='Drain':
		ScreenItem=Heart
	elif Spell=='Lightning':
		ScreenItem=Bolt
	elif Spell=='Fireball':
		ScreenItem=Blast
	elif Spell=='BloodSpatter':
		ScreenItem=BloodSpatter
	elif Spell=='AcidPuddle':
		ScreenItem=AcidPuddle
	elif Spell=='ElectricSpark':
		ScreenItem=ElectricSpark
	elif Spell=='Explosion':
		ScreenItem=Explosion

	screen.blit(ScreenItem, (ScreenX, ScreenY))


	if Spacebar:
		screen.blit(TextBar,(0,780))
		Text='Game paused, press inventory number or SPACE to unpause...'
		TextSurf = myfont.render(Text, False, green)
		screen.blit(TextSurf,(0,780))

	# Writing all previous draw commands into the game-screen at once
	pygame.display.flip()
	return

# Player movement
def DoMovePlayer(PlayerX, PlayerY, Dir):
	PlayerPos[0]=PlayerX
	PlayerPos[1]=PlayerY
	if Dir==8:
		NewX=PlayerPos[0]
		NewY=PlayerPos[1]+1
	if Dir==6:
		NewX=PlayerPos[0]+1
		NewY=PlayerPos[1]
	if Dir==2:
		NewX=PlayerPos[0]
		NewY=PlayerPos[1]-1
	if Dir==4:
		NewX=PlayerPos[0]-1
		NewY=PlayerPos[1]
	# Before the x and y coordinates of the player are updated DoPlayerCollisionDetection() checks what's in the next space
	Collision=DoPlayerCollisionDetection(NewX, NewY, Labyrinth, HeroList)
	# If DoPlayerCollisionDetection() returns True only the Bump sound will be played and the player x and y will not update
	if not Collision:
		PlayerPos[0]=NewX
		PlayerPos[1]=NewY
		Walk.play()
	return(PlayerPos)

def DoGetItem():
	global Gold
	ItemNo=random.randint(1,26)
	if ItemNo==1:
		Item='Dagger'
		InvList.append(Item)
	if ItemNo==2:
		Item='Dagger'
		InvList.append(Item)
	if ItemNo==3:
		Item='Mace'
		InvList.append(Item)
	if ItemNo==4:
		Item='Sword'
		InvList.append(Item)
	if ItemNo==5:
		Item='Battleaxe'
		InvList.append(Item)
	if ItemNo==6:
		Item='Beartrap'
		InvList.append(Item)
	if ItemNo==7:
		Item='Spiketrap'
		InvList.append(Item)
	if ItemNo==8:
		Item='Acidtrap'
		InvList.append(Item)
	if ItemNo==9:
		Item='Electrotrap'
		InvList.append(Item)
	if ItemNo==10:
		Item='Mine'
		InvList.append(Item)
	if ItemNo>=11 and ItemNo<=13:
		Item='Lifepotion'
		InvList.append(Item)
	if ItemNo>=14 and ItemNo<=15:
		Item='Manapotion'
		InvList.append(Item)
	if ItemNo==16:
		Item='Fire'
		InvList.append(Item)
	if ItemNo==17:
		Item='Teleport'
		InvList.append(Item)
	if ItemNo==18:
		Item='Drain'
		InvList.append(Item)
	if ItemNo==19:
		Item='Lightning'
		InvList.append(Item)
	if ItemNo==20:
		Item='Fireball'
		InvList.append(Item)
	if ItemNo==21:
		Item='Shield'
		InvList.append(Item)
	if ItemNo==22:
		Item='WShield'
		InvList.append(Item)
	if ItemNo==23:
		Item='TShield'
		InvList.append(Item)
	if ItemNo==24:
		Item='Chainmail'
		InvList.append(Item)
	if ItemNo==25:
		Item='Plate'
		InvList.append(Item)
	if ItemNo==26:
		Item='bag of 10 gold'
		Gold=Gold+10



	ChestText='You received a '+Item+', press enter...'
	ChestTextSurf = myfont.render(ChestText, False, green)

	screen.blit(TextBar,(0,370))
	screen.blit(TextBar,(0,390))
	screen.blit(TextBar,(0,410))

	screen.blit(ChestTextSurf,(0,390))
	pygame.display.flip()
	wait()
	return

def DoChest(NewX, NewY):
	ChestText='Open chest? <y/n>...'
	ChestTextSurf = myfont.render(ChestText, False, green)

	screen.blit(TextBar,(0,370))
	screen.blit(TextBar,(0,390))
	screen.blit(TextBar,(0,410))

	screen.blit(ChestTextSurf,(0,390))
	pygame.display.flip()
	MakingAChoice=True
	while MakingAChoice:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_y:
					DoGetItem()
					Counter=0
					MaxCounter=len(Labyrinth)
					while Counter < MaxCounter:
						Object=Labyrinth[Counter]
						ObjectX=Labyrinth[Counter+1]
						ObjectY=Labyrinth[Counter+2]
						if ObjectX==NewX and ObjectY==NewY:
							if Object=='ChestClosed':
								Labyrinth[Counter]='ChestOpen'
								OpeningChest.play()
						Counter=Counter+3
					MakingAChoice=False
				if event.key == pygame.K_n:
					MakingAChoice=False
	return

def BuyItem():
	global Gold
	pygame.key.set_repeat()
	MakingaChoice=True
	while MakingaChoice:
		Text1='Press item number to buy or <enter> to cancel... Your gold: '+str(Gold)
		Text1Surf = myfont.render(Text1, False, green)
		Text2='1> 12 gold: Lifepotion'
		Text2Surf = myfont.render(Text2, False, green)
		Text3='2> 16 gold: Manapotion'
		Text3Surf = myfont.render(Text3, False, green)
		Text4='3> 10 gold: Fire'
		Text4Surf = myfont.render(Text4, False, green)
		Text5='4> 12 gold: Teleport'
		Text5Surf = myfont.render(Text5, False, green)
		Text6='5> 14 gold: Drain'
		Text6Surf = myfont.render(Text6, False, green)
		Text7='6> 16 gold: Lightning'
		Text7Surf = myfont.render(Text7, False, green)
		Text8='7> 18 gold: Fireball'
		Text8Surf = myfont.render(Text8, False, green)

		screen.blit(TextBar,(0,620))
		screen.blit(TextBar,(0,640))
		screen.blit(TextBar,(0,660))
		screen.blit(TextBar,(0,680))
		screen.blit(TextBar,(0,700))
		screen.blit(TextBar,(0,720))
		screen.blit(TextBar,(0,740))
		screen.blit(TextBar,(0,760))

		screen.blit(Text1Surf,(0,620))
		screen.blit(Text2Surf,(0,640))
		screen.blit(Text3Surf,(0,660))
		screen.blit(Text4Surf,(0,680))
		screen.blit(Text5Surf,(0,700))
		screen.blit(Text6Surf,(0,720))
		screen.blit(Text7Surf,(0,740))
		screen.blit(Text8Surf,(0,760))

		pygame.display.flip()

		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if (event.key == pygame.K_1 or event.key == pygame.K_KP1) and len(InvList) < 10:
					if Gold >= 12:
						Gold=Gold-12
						InvList.append('Lifepotion')
				if (event.key == pygame.K_2 or event.key == pygame.K_KP2) and len(InvList) < 10:
					if Gold >= 16:
						Gold=Gold-16
						InvList.append('Manapotion')
				if (event.key == pygame.K_3 or event.key == pygame.K_KP3) and len(InvList) < 10:
					if Gold >= 10:
						Gold=Gold-10
						InvList.append('Fire')
				if (event.key == pygame.K_4 or event.key == pygame.K_KP4) and len(InvList) < 10:
					if Gold >= 12:
						Gold=Gold-12
						InvList.append('Teleport')
				if (event.key == pygame.K_5 or event.key == pygame.K_KP5) and len(InvList) < 10:
					if Gold >= 14:
						Gold=Gold-14
						InvList.append('Drain')
				if (event.key == pygame.K_6 or event.key == pygame.K_KP6) and len(InvList) < 10:
					if Gold >= 16:
						Gold=Gold-16
						InvList.append('Lightning')
				if (event.key == pygame.K_7 or event.key == pygame.K_KP7) and len(InvList) < 10:
					if Gold >= 18:
						Gold=Gold-18
						InvList.append('Fireball')
				if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
					MakingaChoice=False
			DoScreen(Labyrinth, Level)
	pygame.key.set_repeat(30,50)

	return

def GetGold(ItemCounter):
	global Gold
	if InvList[ItemCounter].rstrip()=='Mace':
		Gold=Gold+3
		del InvList[ItemCounter]
	elif InvList[ItemCounter].rstrip()=='Dagger':
		Gold=Gold+2
		del InvList[ItemCounter]
	elif InvList[ItemCounter].rstrip()=='Sword':
		Gold=Gold+4
		del InvList[ItemCounter]
	elif InvList[ItemCounter].rstrip()=='Battleaxe':
		Gold=Gold+5
		del InvList[ItemCounter]
	elif InvList[ItemCounter].rstrip()=='Shield':
		Gold=Gold+10
		del InvList[ItemCounter]
	elif InvList[ItemCounter].rstrip()=='WShield':
		Gold=Gold+5
		del InvList[ItemCounter]
	elif InvList[ItemCounter].rstrip()=='TShield':
		Gold=Gold+15
		del InvList[ItemCounter]
	elif InvList[ItemCounter].rstrip()=='Chainmail':
		Gold=Gold+20
		del InvList[ItemCounter]
	elif InvList[ItemCounter].rstrip()=='Plate':
		Gold=Gold+25
		del InvList[ItemCounter]
	elif InvList[ItemCounter].rstrip()=='Beartrap':
		Gold=Gold+4
		del InvList[ItemCounter]
	elif InvList[ItemCounter].rstrip()=='Spiketrap':
		Gold=Gold+2
		del InvList[ItemCounter]
	elif InvList[ItemCounter].rstrip()=='Acidtrap':
		Gold=Gold+6
		del InvList[ItemCounter]
	elif InvList[ItemCounter].rstrip()=='Electrotrap':
		Gold=Gold+8
		del InvList[ItemCounter]
	elif InvList[ItemCounter].rstrip()=='Mine':
		Gold=Gold+10
		del InvList[ItemCounter]
	elif InvList[ItemCounter].rstrip()=='Lifepotion':
		Gold=Gold+9
		del InvList[ItemCounter]
	elif InvList[ItemCounter].rstrip()=='Manapotion':
		Gold=Gold+15
		del InvList[ItemCounter]
	elif InvList[ItemCounter].rstrip()=='Fire':
		Gold=Gold+4
		del InvList[ItemCounter]
	elif InvList[ItemCounter].rstrip()=='Teleport':
		Gold=Gold+8
		del InvList[ItemCounter]
	elif InvList[ItemCounter].rstrip()=='Drain':
		Gold=Gold+12
		del InvList[ItemCounter]
	elif InvList[ItemCounter].rstrip()=='Lightning':
		Gold=Gold+16
		del InvList[ItemCounter]
	elif InvList[ItemCounter].rstrip()=='Fireball':
		Gold=Gold+20
		del InvList[ItemCounter]
	DoScreen(Labyrinth, Level)
	return

def SellItem():
	pygame.key.set_repeat()
	MakingaChoice=True
	while MakingaChoice:
		ChestText='Press inventory number to sell or <enter> to cancel...'
		ChestTextSurf = myfont.render(ChestText, False, green)

		screen.blit(TextBar,(0,500))
		screen.blit(TextBar,(0,520))
		screen.blit(TextBar,(0,540))

		screen.blit(ChestTextSurf,(0,520))
		pygame.display.flip()

		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if (event.key == pygame.K_1 or event.key == pygame.K_KP1) and len(InvList) > 0:
					ItemCounter=0
					GetGold(ItemCounter)
				if (event.key == pygame.K_2 or event.key == pygame.K_KP2) and len(InvList) > 1:
					ItemCounter=1
					GetGold(ItemCounter)
				if (event.key == pygame.K_3 or event.key == pygame.K_KP3) and len(InvList) > 2:
					ItemCounter=2
					GetGold(ItemCounter)
				if (event.key == pygame.K_4 or event.key == pygame.K_KP4) and len(InvList) > 3:
					ItemCounter=3
					GetGold(ItemCounter)
				if (event.key == pygame.K_5 or event.key == pygame.K_KP5) and len(InvList) > 4:
					ItemCounter=4
					GetGold(ItemCounter)
				if (event.key == pygame.K_6 or event.key == pygame.K_KP6) and len(InvList) > 5:
					ItemCounter=5
					GetGold(ItemCounter)
				if (event.key == pygame.K_7 or event.key == pygame.K_KP7) and len(InvList) > 6:
					ItemCounter=6
					GetGold(ItemCounter)
				if (event.key == pygame.K_8 or event.key == pygame.K_KP8) and len(InvList) > 7:
					ItemCounter=7
					GetGold(ItemCounter)
				if (event.key == pygame.K_9 or event.key == pygame.K_KP9) and len(InvList) > 8:
					ItemCounter=8
					GetGold(ItemCounter)
				if (event.key == pygame.K_0 or event.key == pygame.K_KP0) and len(InvList) > 9:
					ItemCounter=9
					GetGold(ItemCounter)
				if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
					MakingaChoice=False
			DoScreen(Labyrinth, Level)
	pygame.key.set_repeat(30,50)
	return

def DoGnome():
	MakingAChoice=True
	while MakingAChoice:
		DoScreen(Labyrinth, Level)
		ChestText='Buy <b> Sell <s> Ignore <enter>...'
		ChestTextSurf = myfont.render(ChestText, False, green)

		screen.blit(TextBar,(0,370))
		screen.blit(TextBar,(0,390))
		screen.blit(TextBar,(0,410))

		screen.blit(ChestTextSurf,(0,390))
		pygame.display.flip()

		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_b:
					BuyItem()
				if event.key == pygame.K_s:
					SellItem()
				if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
					MakingAChoice=False
	return

def DoPlayerCombat(Counter):
	global PlayerAttack
	global PlayerDefence
	global PlayerLifeLevel
	global PlayerMagic
	global PlayerLife
	global PlayerMana
	global PlayerLevel
	global PlayerXP
	global PlayerWeapon
	global HeroList
	global Spell
	global SpellX
	global SpellY

	HeroLevel=int(HeroList[Counter])
	HeroArmor=str(HeroList[Counter+3])
	HeroDefence=int(HeroList[Counter+6])
	HeroLife=int(HeroList[Counter+9])
	DropItemOne=str(HeroList[Counter+11])
	DropItemTwo=str(HeroList[Counter+12])
	HeroX=int(HeroList[Counter+13])
	HeroY=int(HeroList[Counter+14])

	BreakChance=0
	if HeroArmor=='WShield':
		HeroDefence=HeroDefence+1
		BreakChance=1
	elif HeroArmor=='Shield':
		HeroDefence=HeroDefence+2
		BreakChance=2
	elif HeroArmor=='TShield':
		HeroDefence=HeroDefence+3
		BreakChance=3
	elif HeroArmor=='Chainmail':
		HeroDefence=HeroDefence+4
		BreakChance=4
	elif HeroArmor=='Plate':
		HeroDefence=HeroDefence+5
		BreakChance=5

	ZachnoAttack=PlayerAttack
	if PlayerWeapon=='Fists':
		ZachnoAttack=PlayerAttack+1
	elif PlayerWeapon=='Dagger':
		ZachnoAttack=PlayerAttack+4
	elif PlayerWeapon=='Mace':
		ZachnoAttack=PlayerAttack+6
	elif PlayerWeapon=='Sword':
		ZachnoAttack=PlayerAttack+8
	elif PlayerWeapon=='Battleaxe':
		ZachnoAttack=PlayerAttack+10

	ZachnoAttack=ZachnoAttack-HeroDefence
	if ZachnoAttack > 0:
		if PlayerWeapon=='Fists':
			Punch.play()
		elif PlayerWeapon=='Dagger':
			Stab.play()
		elif PlayerWeapon=='Mace':
			MaceHit.play()
		elif PlayerWeapon=='Sword':
			SwordHit.play()
		elif PlayerWeapon=='Battleaxe':
			AxeHit.play()
		HeroLife=HeroLife-ZachnoAttack
		Spell='BloodSpatter'
		SpellX=HeroX
		SpellY=HeroY
		if BreakChance >= random.randint(1,40):
			Shatter.play()
			PlayerWeapon='Fists'
	else:
		Bump.play()

	if HeroLife < 1:
		DeathScream.play()
		PlayerXP=PlayerXP+HeroLevel
		Chance=random.randint(1,2)
		if Chance==1:
			if DropItemOne != 'None':
				Labyrinth.append(DropItemOne)
				Labyrinth.append(HeroX)
				Labyrinth.append(HeroY)
		if Chance==2:
			if DropItemTwo != 'None':
				Labyrinth.append(DropItemTwo)
				Labyrinth.append(HeroX)
				Labyrinth.append(HeroY)
		del HeroList[Counter]
		del HeroList[Counter]
		del HeroList[Counter]
		del HeroList[Counter]
		del HeroList[Counter]
		del HeroList[Counter]
		del HeroList[Counter]
		del HeroList[Counter]
		del HeroList[Counter]
		del HeroList[Counter]
		del HeroList[Counter]
		del HeroList[Counter]
		del HeroList[Counter]
		del HeroList[Counter]
		del HeroList[Counter]
	else:
		HeroList[Counter+9]=HeroLife
	return

# Checks next position in movement and makes game decisions
def DoPlayerCollisionDetection(NewX, NewY, Labyrinth, HeroList):
	global PlayerX
	global PlayerY
	global NextLevel
	global LeatherAmount
	global BoneAmount
	global WoodAmount
	global IronAmount
	global SteelAmount

	Collision=False
	Counter=0
	MaxCounter=len(Labyrinth)
	# Looping through the Labyrinth array where all inanimate objects are stored
	while Counter < MaxCounter:
		Object=str(Labyrinth[Counter])
		ObjectX=int(Labyrinth[Counter+1])
		ObjectY=int(Labyrinth[Counter+2])
		if (ObjectX == NewX) and (ObjectY == NewY):
			# If the object is a Floor, the player can freely move on
			if Object == 'Wall':
				Collision=True
				Bump.play()
				break
			# If the object is a stair the stairwalking sound will be played and NextLevel will be set to True
			if Object == 'Stairs':
				PlayerX=NewX
				PlayerY=NewY
				DoScreen(Labyrinth, Level)
				StairsUp.play()
				NextLevel=True
				Collision=False
			if Object == 'Floor':
				Collision=False
			if Object == 'ChestClosed':
				if len(InvList) < 10:
					DoChest(NewX, NewY)
				else:
					ChestText='Inventory full, press enter...'
					ChestTextSurf = myfont.render(ChestText, False, green)

					screen.blit(TextBar,(0,370))
					screen.blit(TextBar,(0,390))
					screen.blit(TextBar,(0,410))

					screen.blit(ChestTextSurf,(0,390))
					pygame.display.flip()
					wait()
				Collision=True
			if Object == 'Gnome':
				DoGnome()
				Collision=True

			if Object == 'Dagger':
				Collision=False
				if len(InvList) < 10:
					InvList.append('Dagger')
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					MaxCounter=len(Labyrinth)
					Grab.play()
			if Object == 'Mace':
				Collision=False
				if len(InvList) < 10:
					InvList.append('Mace')
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					MaxCounter=len(Labyrinth)
					Grab.play()
			if Object == 'Sword':
				Collision=False
				if len(InvList) < 10:
					InvList.append('Sword')
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					MaxCounter=len(Labyrinth)
					Grab.play()
			if Object == 'BattleAxe':
				Collision=False
				if len(InvList) < 10:
					InvList.append('Battleaxe')
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					MaxCounter=len(Labyrinth)
					Grab.play()
			if Object == 'Life':
				Collision=False
				if len(InvList) < 10:
					InvList.append('Lifepotion')
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					MaxCounter=len(Labyrinth)
					Grab.play()
			if Object == 'Mana':
				Collision=False
				if len(InvList) < 10:
					InvList.append('Manapotion')
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					MaxCounter=len(Labyrinth)
					Grab.play()
			if Object == 'SpikeTrap':
				Collision=False
				if len(InvList) < 10:
					InvList.append('Spiketrap')
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					MaxCounter=len(Labyrinth)
					Grab.play()
			if Object == 'BearTrap':
				Collision=False
				if len(InvList) < 10:
					InvList.append('Beartrap')
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					MaxCounter=len(Labyrinth)
					Grab.play()
			if Object == 'AcidTrap':
				Collision=False
				if len(InvList) < 10:
					InvList.append('Acidtrap')
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					MaxCounter=len(Labyrinth)
					Grab.play()
			if Object == 'ElectroTrap':
				Collision=False
				if len(InvList) < 10:
					InvList.append('Electrotrap')
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					MaxCounter=len(Labyrinth)
					Grab.play()
			if Object == 'Mine':
				Collision=False
				if len(InvList) < 10:
					InvList.append('Mine')
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					MaxCounter=len(Labyrinth)
					Grab.play()
			if Object == 'FireScroll':
				Collision=False
				if len(InvList) < 10:
					InvList.append('Fire')
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					MaxCounter=len(Labyrinth)
					Grab.play()
			if Object == 'TeleportScroll':
				Collision=False
				if len(InvList) < 10:
					InvList.append('Teleport')
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					MaxCounter=len(Labyrinth)
					Grab.play()
			if Object == 'DrainScroll':
				Collision=False
				if len(InvList) < 10:
					InvList.append('Drain')
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					MaxCounter=len(Labyrinth)
					Grab.play()
			if Object == 'LightningScroll':
				Collision=False
				if len(InvList) < 10:
					InvList.append('Lightning')
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					MaxCounter=len(Labyrinth)
					Grab.play()
			if Object == 'FireballScroll':
				Collision=False
				if len(InvList) < 10:
					InvList.append('Fireball')
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					MaxCounter=len(Labyrinth)
					Grab.play()
			if Object == 'WShield':
				Collision=False
				if len(InvList) < 10:
					InvList.append('WShield')
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					MaxCounter=len(Labyrinth)
					Grab.play()
			if Object == 'Shield':
				Collision=False
				if len(InvList) < 10:
					InvList.append('Shield')
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					MaxCounter=len(Labyrinth)
					Grab.play()
			if Object == 'TShield':
				Collision=False
				if len(InvList) < 10:
					InvList.append('TShield')
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					MaxCounter=len(Labyrinth)
					Grab.play()
			if Object == 'Chainmail':
				Collision=False
				if len(InvList) < 10:
					InvList.append('Chainmail')
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					MaxCounter=len(Labyrinth)
					Grab.play()
			if Object == 'Plate':
				Collision=False
				if len(InvList) < 10:
					InvList.append('Plate')
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					MaxCounter=len(Labyrinth)
					Grab.play()
			if Object == 'Leather':
				Collision=False
				if LeatherAmount < 10:
					LeatherAmount=LeatherAmount+1
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					MaxCounter=len(Labyrinth)
					Grab.play()
			if Object == 'Skull':
				Collision=False
				if BoneAmount < 10:
					BoneAmount=BoneAmount+1
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					MaxCounter=len(Labyrinth)
					Grab.play()
			if Object == 'Wood':
				Collision=False
				if WoodAmount < 10:
					WoodAmount=WoodAmount+1
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					MaxCounter=len(Labyrinth)
					Grab.play()
			if Object == 'Iron':
				Collision=False
				if IronAmount < 10:
					IronAmount=IronAmount+1
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					MaxCounter=len(Labyrinth)
					Grab.play()
			if Object == 'Steel':
				Collision=False
				if SteelAmount < 10:
					SteelAmount=SteelAmount+1
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					del Labyrinth[Counter]
					MaxCounter=len(Labyrinth)
					Grab.play()
		Counter=Counter+3
	Counter=0
	MaxCounter=len(HeroList)
	while Counter < MaxCounter:
		HeroX=int(HeroList[Counter+13])
		HeroY=int(HeroList[Counter+14])
		if HeroX == NewX and HeroY == NewY:
			DoPlayerCombat(Counter)
			MaxCounter=len(HeroList)
			Collision=True
		Counter=Counter+15
	return(Collision)

# Creates a list of all room positions in current level
def GenerateRoomPos(Level):
	global MaxRooms
	global MapGen
	LoadingText='Generating room positions...'
	LoadingTextSurf = myfont.render(LoadingText, False, green)
	screen.blit(TextBar,(0,780))
	screen.blit(LoadingTextSurf,(0,780))
	pygame.display.flip()
	# Empyting the previous RoomPos array
	del RoomPos[:]
	MapGen=int(Level/2)+1
	# Setting up the maximum distances from the center of the current map
	XCounterMin=-1*MapGen
	XCounterMax=MapGen
	YCounterMin=-1*MapGen
	YCounterMax=MapGen
	MaxRooms=0
	# Loop that fills RoomPos with all the center positions of the rooms in this level
	while YCounterMin <= YCounterMax:
		while XCounterMin <= XCounterMax:
			TunnelSwitch=0
			MaxRooms=MaxRooms+2
			RoomSize=random.randint(1, 4)
			RoomX=XCounterMin*9
			RoomY=YCounterMin*9
			RoomPos.append(RoomSize)
			RoomPos.append(TunnelSwitch)
			RoomPos.append(TunnelSwitch)
			RoomPos.append(TunnelSwitch)
			RoomPos.append(TunnelSwitch)
			RoomPos.append(RoomX)
			RoomPos.append(RoomY)
			XCounterMin=XCounterMin+1
		XCounterMin=-1*MapGen
		YCounterMin=YCounterMin+1
	return(MaxRooms)

# Creates a tunnel in the up directioon from a room
def BuildTunnelUp(RoomCenterX, RoomCenterY,TargetX, TargetY, RoomSize, TunnelWidth, RoomPos):
	LoadingText='Building tunnel up room '+str(RoomCenterX)+' '+str(RoomCenterY)+'...'
	LoadingTextSurf = myfont.render(LoadingText, False, green)
	screen.blit(TextBar,(0,780))
	screen.blit(LoadingTextSurf,(0,780))
	pygame.display.flip()
	RoomCounter=0
	MaxRoomCounter=len(RoomPos)
	while RoomCounter < MaxRoomCounter:
		TargetRoomSize=RoomPos[RoomCounter]
		TargetRoomX=RoomPos[RoomCounter+5]
		TargetRoomY=RoomPos[RoomCounter+6]
		if TargetX==TargetRoomX and TargetY==TargetRoomY:
			MaxCounter=9-TargetRoomSize
		RoomCounter=RoomCounter+7
	Counter=RoomSize
	OffsetMin=-1*TunnelWidth
	OffsetMax=TunnelWidth
	while OffsetMin <= OffsetMax:
		Counter=RoomSize
		while Counter < MaxCounter:
			ObjectX=RoomCenterX+OffsetMin
			ObjectY=RoomCenterY+Counter
			CheckX=ObjectX
			CheckY=ObjectY
			FoundSomething=False
			FoundSomething=CheckSpace(Labyrinth, CheckX, CheckY)
			if FoundSomething==False:
				Labyrinth.append('Floor')
				Labyrinth.append(ObjectX)
				Labyrinth.append(ObjectY)
			Counter=Counter+1
		OffsetMin=OffsetMin+1
	OffsetMin=-1*TunnelWidth
	OffsetMax=TunnelWidth
	Counter=RoomSize
	while Counter < MaxCounter:
		FoundSomething=False
		ObjectX=RoomCenterX-1-OffsetMax
		ObjectY=RoomCenterY+Counter
		Labyrinth.append('Wall')
		Labyrinth.append(ObjectX)
		Labyrinth.append(ObjectY)
		Counter=Counter+1
	OffsetMin=-1*TunnelWidth
	OffsetMax=TunnelWidth
	Counter=RoomSize
	MaxCounter=9
	while Counter < MaxCounter:
		FoundSomething=False
		ObjectX=RoomCenterX+1+OffsetMax
		ObjectY=RoomCenterY+Counter
		Labyrinth.append('Wall')
		Labyrinth.append(ObjectX)
		Labyrinth.append(ObjectY)
		Counter=Counter+1
	return

# Creates a tunnel in the right directioon from a room
def BuildTunnelRight(RoomCenterX, RoomCenterY,TargetX, TargetY, RoomSize, TunnelWidth, RoomPos):
	LoadingText='Building tunnel right room '+str(RoomCenterX)+' '+str(RoomCenterY)+'...'
	LoadingTextSurf = myfont.render(LoadingText, False, green)
	screen.blit(TextBar,(0,780))
	screen.blit(LoadingTextSurf,(0,780))
	pygame.display.flip()
	RoomCounter=0
	MaxRoomCounter=len(RoomPos)
	while RoomCounter < MaxRoomCounter:
		TargetRoomSize=RoomPos[RoomCounter]
		TargetRoomX=RoomPos[RoomCounter+5]
		TargetRoomY=RoomPos[RoomCounter+6]
		if TargetX==TargetRoomX and TargetY==TargetRoomY:
			MaxCounter=9-TargetRoomSize
		RoomCounter=RoomCounter+7
	Counter=RoomSize
	OffsetMin=-1*TunnelWidth
	OffsetMax=TunnelWidth
	while OffsetMin <= OffsetMax:
		Counter=RoomSize
		FoundSomething=False
		while Counter < MaxCounter:
			ObjectX=RoomCenterX+Counter
			ObjectY=RoomCenterY+OffsetMin
			CheckX=ObjectX
			CheckY=ObjectY
			FoundSomething=False
			FoundSomething=CheckSpace(Labyrinth, CheckX, CheckY)
			if FoundSomething==False:
				Labyrinth.append('Floor')
				Labyrinth.append(ObjectX)
				Labyrinth.append(ObjectY)
			Counter=Counter+1
		OffsetMin=OffsetMin+1
	OffsetMin=-1*TunnelWidth
	Counter=RoomSize
	while Counter < MaxCounter:
		FoundSomething=False
		ObjectX=RoomCenterX+Counter
		ObjectY=RoomCenterY+1+OffsetMax
		Labyrinth.append('Wall')
		Labyrinth.append(ObjectX)
		Labyrinth.append(ObjectY)
		Counter=Counter+1
	OffsetMin=-1*TunnelWidth
	Counter=RoomSize
	while Counter < MaxCounter:
		FoundSomething=False
		ObjectX=RoomCenterX+Counter
		ObjectY=RoomCenterY-1-OffsetMax
		Labyrinth.append('Wall')
		Labyrinth.append(ObjectX)
		Labyrinth.append(ObjectY)
		Counter=Counter+1
	return

# Creates a tunnel in the down directioon from a room
def BuildTunnelDown(RoomCenterX, RoomCenterY,TargetX, TargetY, RoomSize, TunnelWidth, RoomPos):
	LoadingText='Building tunnel down room '+str(RoomCenterX)+' '+str(RoomCenterY)+'...'
	LoadingTextSurf = myfont.render(LoadingText, False, green)
	screen.blit(TextBar,(0,780))
	screen.blit(LoadingTextSurf,(0,780))
	pygame.display.flip()
	RoomCounter=0
	MaxRoomCounter=len(RoomPos)
	while RoomCounter < MaxRoomCounter:
		TargetRoomSize=RoomPos[RoomCounter]
		TargetRoomX=RoomPos[RoomCounter+5]
		TargetRoomY=RoomPos[RoomCounter+6]
		if TargetX==TargetRoomX and TargetY==TargetRoomY:
			MaxCounter=-1*(9-TargetRoomSize)
		RoomCounter=RoomCounter+7
	Counter=-1*RoomSize
	OffsetMin=-1*TunnelWidth
	OffsetMax=TunnelWidth
	while OffsetMin <= OffsetMax:
		Counter=-1*RoomSize
		FoundSomething=False
		while Counter > MaxCounter:
			ObjectX=RoomCenterX+OffsetMin
			ObjectY=RoomCenterY+Counter
			CheckX=ObjectX
			CheckY=ObjectY
			FoundSomething=False
			FoundSomething=CheckSpace(Labyrinth, CheckX, CheckY)
			if FoundSomething==False:
				Labyrinth.append('Floor')
				Labyrinth.append(ObjectX)
				Labyrinth.append(ObjectY)
			Counter=Counter-1
		OffsetMin=OffsetMin+1
	OffsetMin=-1*TunnelWidth
	Counter=-1*RoomSize
	while Counter > MaxCounter:
		FoundSomething=False
		ObjectX=RoomCenterX-1-OffsetMax
		ObjectY=RoomCenterY+Counter
		Labyrinth.append('Wall')
		Labyrinth.append(ObjectX)
		Labyrinth.append(ObjectY)
		Counter=Counter-1
	OffsetMin=-1*TunnelWidth
	Counter=-1*RoomSize
	while Counter > MaxCounter:
		FoundSomething=False
		ObjectX=RoomCenterX+1+OffsetMax
		ObjectY=RoomCenterY+Counter
		Labyrinth.append('Wall')
		Labyrinth.append(ObjectX)
		Labyrinth.append(ObjectY)
		Counter=Counter-1
	return

# Creates a tunnel in the left directioon from a room
def BuildTunnelLeft(RoomCenterX, RoomCenterY,TargetX, TargetY, RoomSize, TunnelWidth, RoomPos):
	LoadingText='Building tunnel left room '+str(RoomCenterX)+' '+str(RoomCenterY)+'...'
	LoadingTextSurf = myfont.render(LoadingText, False, green)
	screen.blit(TextBar,(0,780))
	screen.blit(LoadingTextSurf,(0,780))
	pygame.display.flip()
	RoomCounter=0
	MaxRoomCounter=len(RoomPos)
	while RoomCounter < MaxRoomCounter:
		TargetRoomSize=RoomPos[RoomCounter]
		TargetRoomX=RoomPos[RoomCounter+5]
		TargetRoomY=RoomPos[RoomCounter+6]
		if TargetX==TargetRoomX and TargetY==TargetRoomY:
			MaxCounter=-1*(9-TargetRoomSize)
		RoomCounter=RoomCounter+7
	Counter=-1*RoomSize
	OffsetMin=-1*TunnelWidth
	OffsetMax=TunnelWidth
	while OffsetMin <= OffsetMax:
		Counter=-1*RoomSize
		while Counter > MaxCounter:
			ObjectX=RoomCenterX+Counter
			ObjectY=RoomCenterY+OffsetMin
			CheckX=ObjectX
			CheckY=ObjectY
			FoundSomething=False
			FoundSomething=CheckSpace(Labyrinth, CheckX, CheckY)
			if FoundSomething==False:
				Labyrinth.append('Floor')
				Labyrinth.append(ObjectX)
				Labyrinth.append(ObjectY)
			Counter=Counter-1
		OffsetMin=OffsetMin+1
	OffsetMin=-1*TunnelWidth
	Counter=-1*RoomSize
	while Counter > MaxCounter:
		ObjectX=RoomCenterX+Counter
		ObjectY=RoomCenterY-1-OffsetMax
		Labyrinth.append('Wall')
		Labyrinth.append(ObjectX)
		Labyrinth.append(ObjectY)
		Counter=Counter-1
	OffsetMin=-1*TunnelWidth
	Counter=-1*RoomSize
	while Counter > MaxCounter:
		ObjectX=RoomCenterX+Counter
		ObjectY=RoomCenterY+1+OffsetMax
		Labyrinth.append('Wall')
		Labyrinth.append(ObjectX)
		Labyrinth.append(ObjectY)
		Counter=Counter-1
	return

def CheckFloor(Labyrinth, CheckX, CheckY):
	FloorFound=False
	Counter=0
	MaxCounter=len(Labyrinth)
	while Counter < MaxCounter:
		Object=''
		Object=Labyrinth[Counter]
		ObjectX=Labyrinth[Counter+1]
		ObjectY=Labyrinth[Counter+2]
		if CheckX==ObjectX and CheckY==ObjectY:
			if not Object=='Floor':
				FloorFound=False
				return(FloorFound)
			if Object=='':
				FloorFound=False
				return(FloorFound)
			if Object=='Floor':
				FloorFound=True
		Counter=Counter+3
	return(FloorFound)

# Function for checking wether there is Labyrinth in the CheckX and CheckY position
def CheckSpace(Labyrinth, CheckX, CheckY):
	FoundSomething=False
	Counter=0
	MaxCounter=len(Labyrinth)
	while Counter < MaxCounter:
		LabX=Labyrinth[Counter+1]
		LabY=Labyrinth[Counter+2]
		if CheckX==LabX and CheckY==LabY:
			FoundSomething=True
		Counter=Counter+3
	return(FoundSomething)

# Looks wether another room wants to make an opening in the current room
def CheckRoomUp(Labyrinth, RoomCenterX, RoomCenterY, RoomSize, RoomPos):
	LoadingText='Checking for room up '+str(RoomCenterX)+' '+str(RoomCenterY)+'...'
	LoadingTextSurf = myfont.render(LoadingText, False, green)
	screen.blit(TextBar,(0,780))
	screen.blit(LoadingTextSurf,(0,780))
	pygame.display.flip()

	TargetX=RoomCenterX
	TargetY=RoomCenterY+9
	RoomCounter=0
	MaxRoomCounter=len(RoomPos)
	while RoomCounter < MaxRoomCounter:
		Incoming=RoomPos[RoomCounter+3]
		RoomX=RoomPos[RoomCounter+5]
		RoomY=RoomPos[RoomCounter+6]
		if RoomX==TargetX and RoomY==TargetY:
			if Incoming==1:
				TargetX=RoomCenterX
				TargetY=RoomCenterY+RoomSize
				Counter=0
				MaxCounter=len(Labyrinth)
				while Counter < MaxCounter:
					LabX=Labyrinth[Counter+1]
					LabY=Labyrinth[Counter+2]
					if LabX==TargetX and LabY==TargetY:
						Labyrinth[Counter]='Floor'
					Counter=Counter+3
		RoomCounter=RoomCounter+7
	return

# Looks wether another room wants to make an opening in the current room
def CheckRoomRight(Labyrinth, RoomCenterX, RoomCenterY, RoomSize, RoomPos):
	LoadingText='Checking for room to the right '+str(RoomCenterX)+' '+str(RoomCenterY)+'...'
	LoadingTextSurf = myfont.render(LoadingText, False, green)
	screen.blit(TextBar,(0,780))
	screen.blit(LoadingTextSurf,(0,780))
	pygame.display.flip()

	Opening=False
	TargetX=RoomCenterX+9
	TargetY=RoomCenterY
	RoomCounter=0
	MaxRoomCounter=len(RoomPos)
	while RoomCounter < MaxRoomCounter:
		Incoming=RoomPos[RoomCounter+4]
		RoomX=RoomPos[RoomCounter+5]
		RoomY=RoomPos[RoomCounter+6]
		if RoomX==TargetX and RoomY==TargetY:
			if Incoming==1:
				TargetX=RoomCenterX+RoomSize
				TargetY=RoomCenterY
				Counter=0
				MaxCounter=len(Labyrinth)
				while Counter < MaxCounter:
					LabX=Labyrinth[Counter+1]
					LabY=Labyrinth[Counter+2]
					if LabX==TargetX and LabY==TargetY:
						Labyrinth[Counter]='Floor'
					Counter=Counter+3
		RoomCounter=RoomCounter+7
	return

# Looks wether another room wants to make an opening in the current room
def CheckRoomDown(Labyrinth, RoomCenterX, RoomCenterY, RoomSize, RoomPos):
	LoadingText='Checking for room down '+str(RoomCenterX)+' '+str(RoomCenterY)+'...'
	LoadingTextSurf = myfont.render(LoadingText, False, green)
	screen.blit(TextBar,(0,780))
	screen.blit(LoadingTextSurf,(0,780))
	pygame.display.flip()

	Opening=False
	TargetX=RoomCenterX
	TargetY=RoomCenterY-9
	RoomCounter=0
	MaxRoomCounter=len(RoomPos)
	while RoomCounter < MaxRoomCounter:
		Incoming=RoomPos[RoomCounter+1]
		RoomX=RoomPos[RoomCounter+5]
		RoomY=RoomPos[RoomCounter+6]
		if RoomX==TargetX and RoomY==TargetY:
			if Incoming==1:
				TargetX=RoomCenterX
				TargetY=RoomCenterY-RoomSize
				Counter=0
				MaxCounter=len(Labyrinth)
				while Counter < MaxCounter:
					LabX=Labyrinth[Counter+1]
					LabY=Labyrinth[Counter+2]
					if LabX==TargetX and LabY==TargetY:
						Labyrinth[Counter]='Floor'
					Counter=Counter+3
		RoomCounter=RoomCounter+7
	return

# Looks wether another room wants to make an opening in the current room
def CheckRoomLeft(Labyrinth, RoomCenterX, RoomCenterY, RoomSize, RoomPos):
	LoadingText='Checking for room to the left '+str(RoomCenterX)+' '+str(RoomCenterY)+'...'
	LoadingTextSurf = myfont.render(LoadingText, False, green)
	screen.blit(TextBar,(0,780))
	screen.blit(LoadingTextSurf,(0,780))
	pygame.display.flip()

	Opening=False
	TargetX=RoomCenterX-9
	TargetY=RoomCenterY
	RoomCounter=0
	MaxRoomCounter=len(RoomPos)
	while RoomCounter < MaxRoomCounter:
		Incoming=RoomPos[RoomCounter+2]
		RoomX=RoomPos[RoomCounter+5]
		RoomY=RoomPos[RoomCounter+6]
		if RoomX==TargetX and RoomY==TargetY:
			if Incoming==1:
				TargetX=RoomCenterX-RoomSize
				TargetY=RoomCenterY
				Counter=0
				MaxCounter=len(Labyrinth)
				while Counter < MaxCounter:
					LabX=Labyrinth[Counter+1]
					LabY=Labyrinth[Counter+2]
					if LabX==TargetX and LabY==TargetY:
						Labyrinth[Counter]='Floor'
					Counter=Counter+3
		RoomCounter=RoomCounter+7
	return

# Function that checks for surrounding rooms
def CheckNextRoom(Labyrinth, RoomPos):
	global Rooms
	global MaxRooms
	global MapGen
	Counter=0
	MaxCounter=len(RoomPos)
	while Counter < MaxCounter:
		RoomUp=True
		RoomRight=True
		RoomDown=True
		RoomLeft=True

		Rooms=Rooms+1
		Percentage=GetPercentage(Rooms, MaxRooms)
		PercentageText='Generating level '+str(Level)+' '+str(Percentage)+'%'
		PercentageTextSurf = myfont.render(PercentageText, False, green)
		screen.blit(TextBar,(0,780))
		screen.blit(TextBar,(0,0))
		screen.blit(PercentageTextSurf,(0,0))
		pygame.display.flip()

		RoomSize=RoomPos[Counter]
		RoomCenterX=RoomPos[Counter+5]
		RoomCenterY=RoomPos[Counter+6]
		if RoomCenterY==(MapGen*9):
			RoomUp=False
		if RoomCenterX==(MapGen*9):
			RoomRight=False
		if RoomCenterY==(MapGen*-9):
			RoomDown=False
		if RoomCenterX==(MapGen*-9):
			RoomLeft=False

		if RoomUp:
			CheckRoomUp(Labyrinth, RoomCenterX, RoomCenterY, RoomSize, RoomPos)
		if RoomRight:
			CheckRoomRight(Labyrinth, RoomCenterX, RoomCenterY, RoomSize, RoomPos)
		if RoomDown:
			CheckRoomDown(Labyrinth, RoomCenterX, RoomCenterY, RoomSize, RoomPos)
		if RoomLeft:
			CheckRoomLeft(Labyrinth, RoomCenterX, RoomCenterY, RoomSize, RoomPos)
		Counter=Counter+7
	return(Labyrinth)

def GetPercentage(Rooms, MaxRooms):
	Percentage=int((Rooms/MaxRooms)*100)
	return(Percentage)

def CheckTargetRoom(TargetX, TargetY, RoomSize, RoomPos):
	TunnelWidth=random.randint(0,1)
	if RoomSize==1:
		TunnelWidth=0
	Counter=0
	MaxCounter=len(RoomPos)
	while Counter < MaxCounter:
		TargetRoomSize=RoomPos[Counter]
		TargetRoomX=RoomPos[Counter+5]
		TargetRoomY=RoomPos[Counter+6]
		if TargetX==TargetRoomX and TargetY==TargetRoomY:
			if TargetRoomSize==1:
				TunnelWidth=0
		Counter=Counter+7
	return(TunnelWidth)

# Generates a room per room positions found in the RoomPos array
def GenerateRooms(RoomPos):
	global Rooms
	global MaxRooms
	Counter=0
	MaxCounter=len(RoomPos)
	while Counter < MaxCounter:
		Rooms=Rooms+1
		RoomSize=RoomPos[Counter]
		RoomCenterX=RoomPos[Counter+5]
		RoomCenterY=RoomPos[Counter+6]
		LoadingText='Generating room '+str(RoomCenterX)+str(RoomCenterY)+'...'
		Percentage=GetPercentage(Rooms, MaxRooms)
		PercentageText='Generating level '+str(Level)+' '+str(Percentage)+'%'
		PercentageTextSurf = myfont.render(PercentageText, False, green)
		LoadingTextSurf = myfont.render(LoadingText, False, green)
		screen.blit(TextBar,(0,780))
		screen.blit(TextBar,(0,0))
		screen.blit(LoadingTextSurf,(0,780))
		screen.blit(PercentageTextSurf,(0,0))
		pygame.display.flip()
		NumberofExits=random.randint(1, 4)
		ExitCounter=0
		ExitUp=False
		ExitRight=False
		ExitDown=False
		ExitLeft=False
		while ExitCounter < NumberofExits:
			ExitDir=random.randint(1, 4)
			if ExitDir==1:
				if RoomCenterY < (MapGen*9):
					if ExitUp==False:
						RoomPos[Counter+1]=1
						ExitUp=True
						TargetX=RoomCenterX
						TargetY=RoomCenterY+9
						TunnelWidth=CheckTargetRoom(TargetX, TargetY, RoomSize, RoomPos)
						TunnelUp=TunnelWidth
						BuildTunnelUp(RoomCenterX, RoomCenterY,TargetX, TargetY, RoomSize, TunnelWidth, RoomPos)
						ExitCounter=ExitCounter+1
				else:
					if RoomCenterY > (MapGen*-9):
						RoomPos[Counter+3]=1
						ExitDown=True
						TargetX=RoomCenterX
						TargetY=RoomCenterY-9
						TunnelWidth=CheckTargetRoom(TargetX, TargetY, RoomSize, RoomPos)
						TunnelDown=TunnelWidth
						BuildTunnelDown(RoomCenterX, RoomCenterY,TargetX, TargetY, RoomSize, TunnelWidth, RoomPos)
						ExitCounter=ExitCounter+1
			if ExitDir==2:
				if RoomCenterX < (MapGen*9):
					if ExitRight==False:
						RoomPos[Counter+2]=1
						ExitRight=True
						TargetX=RoomCenterX+9
						TargetY=RoomCenterY
						TunnelWidth=CheckTargetRoom(TargetX, TargetY, RoomSize, RoomPos)
						TunnelRight=TunnelWidth
						BuildTunnelRight(RoomCenterX, RoomCenterY,TargetX, TargetY, RoomSize, TunnelWidth, RoomPos)
						ExitCounter=ExitCounter+1
				else:
					if RoomCenterX > (MapGen*-9):
						RoomPos[Counter+4]=1
						ExitLeft=True
						TargetX=RoomCenterX-9
						TargetY=RoomCenterY
						TunnelWidth=CheckTargetRoom(TargetX, TargetY, RoomSize, RoomPos)
						TunnelLeft=TunnelWidth
						BuildTunnelLeft(RoomCenterX, RoomCenterY,TargetX, TargetY, RoomSize, TunnelWidth, RoomPos)
						ExitCounter=ExitCounter+1
			if ExitDir==3:
				if RoomCenterY > (MapGen*-9):
					if ExitDown==False:
						RoomPos[Counter+3]=1
						ExitDown=True
						TargetX=RoomCenterX
						TargetY=RoomCenterY-9
						TunnelWidth=CheckTargetRoom(TargetX, TargetY, RoomSize, RoomPos)
						TunnelDown=TunnelWidth
						BuildTunnelDown(RoomCenterX, RoomCenterY,TargetX, TargetY, RoomSize, TunnelWidth, RoomPos)
						ExitCounter=ExitCounter+1
				else:
					if RoomCenterY < (MapGen*9):
						ExitUp=True
						RoomPos[Counter+1]=1
						TargetX=RoomCenterX
						TargetY=RoomCenterY+9
						TunnelWidth=CheckTargetRoom(TargetX, TargetY, RoomSize, RoomPos)
						TunnelUp=TunnelWidth
						BuildTunnelUp(RoomCenterX, RoomCenterY,TargetX, TargetY, RoomSize, TunnelWidth, RoomPos)
						ExitCounter=ExitCounter+1
			if ExitDir==4:
				if RoomCenterX > (MapGen*-9):
					if ExitLeft==False:
						RoomPos[Counter+4]=1
						ExitLeft=True
						TargetX=RoomCenterX-9
						TargetY=RoomCenterY
						TunnelWidth=CheckTargetRoom(TargetX, TargetY, RoomSize, RoomPos)
						TunnelLeft=TunnelWidth
						ExitLeft=True
						BuildTunnelLeft(RoomCenterX, RoomCenterY,TargetX, TargetY, RoomSize, TunnelWidth, RoomPos)
						ExitCounter=ExitCounter+1
				else:
					if RoomCenterX < (MapGen*9):
						RoomPos[Counter+2]=1
						ExitRight=True
						TargetX=RoomCenterX+9
						TargetY=RoomCenterY
						TunnelWidth=CheckTargetRoom(TargetX, TargetY, RoomSize, RoomPos)
						TunnelRight=TunnelWidth
						BuildTunnelRight(RoomCenterX, RoomCenterY,TargetX, TargetY, RoomSize, TunnelWidth, RoomPos)
						ExitCounter=ExitCounter+1
		FloorMinX=-1*RoomSize
		FloorMaxX=RoomSize
		FloorMinY=-1*RoomSize
		FloorMaxY=RoomSize
		while FloorMinY <= FloorMaxY:
			while FloorMinX <= FloorMaxX:
				ObjectX=RoomCenterX+FloorMinX
				ObjectY=RoomCenterY+FloorMinY
				FloorDone=False
				LabCounter=0
				LabMaxCounter=len(Labyrinth)
				while LabCounter < LabMaxCounter:
					LabX=Labyrinth[LabCounter+1]
					LabY=Labyrinth[LabCounter+2]
					if (LabX==ObjectX) and (LabY==ObjectY):
						Labyrinth[LabCounter]='Floor'
						FloorDone=True
					LabCounter=LabCounter+3
				if FloorDone==False:
					Labyrinth.append('Floor')
					Labyrinth.append(ObjectX)
					Labyrinth.append(ObjectY)
				FloorMinX=FloorMinX+1
			FloorMinX=-1*RoomSize
			FloorMinY=FloorMinY+1

		YTop=RoomCenterY+RoomSize
		Xleft=RoomCenterX-RoomSize
		XRight=RoomCenterX+RoomSize
		while Xleft <= XRight:
			if ExitUp:
				if Xleft==RoomCenterX:
					Labyrinth.append('Floor')
				elif Xleft==RoomCenterX-TunnelUp:
					Labyrinth.append('Floor')
				elif Xleft==RoomCenterX+TunnelUp:
					Labyrinth.append('Floor')
				else:
					Labyrinth.append('Wall')
			else:
				Labyrinth.append('Wall')
			Labyrinth.append(Xleft)
			Labyrinth.append(YTop)
			Xleft=Xleft+1
		YTop=RoomCenterY+RoomSize
		YBottom=RoomCenterY-RoomSize
		XRight=RoomCenterX+RoomSize
		while YTop >= YBottom:
			if ExitRight:
				if YTop==RoomCenterY:
					Labyrinth.append('Floor')
				elif YTop==RoomCenterY-TunnelRight:
					Labyrinth.append('Floor')
				elif YTop==RoomCenterY+TunnelRight:
					Labyrinth.append('Floor')
				else:
					Labyrinth.append('Wall')
			else:
				Labyrinth.append('Wall')
			Labyrinth.append(XRight)
			Labyrinth.append(YTop)
			YTop=YTop-1
		YBottom=RoomCenterY-RoomSize
		Xleft=RoomCenterX-RoomSize
		XRight=RoomCenterX+RoomSize
		while XRight >= Xleft:
			if ExitDown:
				if XRight==RoomCenterX:
					Labyrinth.append('Floor')
				elif XRight==RoomCenterX-TunnelDown:
					Labyrinth.append('Floor')
				elif XRight==RoomCenterX+TunnelDown:
					Labyrinth.append('Floor')
				else:
					Labyrinth.append('Wall')
			else:
				Labyrinth.append('Wall')
			Labyrinth.append(XRight)
			Labyrinth.append(YBottom)
			XRight=XRight-1
		YBottom=RoomCenterY-RoomSize
		Xleft=RoomCenterX-RoomSize
		YTop=RoomCenterY+RoomSize
		while YBottom <= YTop:
			if ExitLeft:
				if YBottom==RoomCenterY:
					Labyrinth.append('Floor')
				elif YBottom==RoomCenterY-TunnelLeft:
					Labyrinth.append('Floor')
				elif YBottom==RoomCenterY+TunnelLeft:
					Labyrinth.append('Floor')
				else:
					Labyrinth.append('Wall')
			else:
				Labyrinth.append('Wall')
			Labyrinth.append(Xleft)
			Labyrinth.append(YBottom)
			YBottom=YBottom+1

		Counter=Counter+7
	return(Rooms)

# Sticks stairs to the next level in a random room
def PlaceStairs(Labyrinth):
	LoadingText='Placing stairs to next level...'
	LoadingTextSurf = myfont.render(LoadingText, False, green)
	screen.blit(TextBar,(0,780))
	screen.blit(LoadingTextSurf,(0,780))
	pygame.display.flip()

	global StairsX
	global StairsY
	StairsXMin=-1*MapGen*9
	StairsXMax=MapGen*9
	StairsYMin=-1*MapGen*9
	StairsYMax=MapGen*9
	LookingForASpot=True
	while LookingForASpot:
		NoBlock=True
		StairsX=random.randint(StairsXMin, StairsXMax)
		StairsY=random.randint(StairsYMin, StairsYMax)

		if (StairsX/9)==int(StairsX/9):
			NoBlock=False
		if (StairsY/9)==int(StairsY/9):
			NoBlock=False

		if NoBlock:
			FloorFound=False
			CheckX=StairsX
			CheckY=StairsY
			FloorFound=CheckFloor(Labyrinth, CheckX, CheckY)
			if FloorFound:
				Counter=0
				MaxCounter=len(Labyrinth)
				LookingForASpot=False
				Counter=0
				MaxCounter=len(Labyrinth)
				while Counter < MaxCounter:
					Object=Labyrinth[Counter]
					ObjectX=Labyrinth[Counter+1]
					ObjectY=Labyrinth[Counter+2]
					if ObjectX==StairsX and ObjectY==StairsY:
						Labyrinth[Counter]='Stairs'
					Counter=Counter+3
	return

def PlaceGnome(Labyrinth):
	global Level
	LoadingText='Placing Gome...'
	LoadingTextSurf = myfont.render(LoadingText, False, green)
	screen.blit(TextBar,(0,780))
	screen.blit(LoadingTextSurf,(0,780))
	pygame.display.flip()

	GnomeXMin=-1*MapGen*9
	GnomeXMax=MapGen*9
	GnomeYMin=-1*MapGen*9
	GnomeYMax=MapGen*9
	Number=0
	NumberofGnomes=int(Level/4)+1
	while Number < NumberofGnomes: 
		LookingForASpot=True
		while LookingForASpot:
			NoBlock=True
			GnomeX=random.randint(GnomeXMin, GnomeXMax)
			GnomeY=random.randint(GnomeYMin, GnomeYMax)

			if (GnomeX/9)==int(GnomeX/9):
				NoBlock=False
			if (GnomeY/9)==int(GnomeY/9):
				NoBlock=False

			if NoBlock:
				FloorFound=False
				CheckX=GnomeX
				CheckY=GnomeY
				FloorFound=CheckFloor(Labyrinth, CheckX, CheckY)
				if FloorFound:
					Labyrinth.append('Gnome')
					Labyrinth.append(GnomeX)
					Labyrinth.append(GnomeY)
					LookingForASpot=False
		Number=Number+1
	return


def PlaceDecorations():
	LoadingText='Placing items...'
	LoadingTextSurf = myfont.render(LoadingText, False, green)
	screen.blit(TextBar,(0,780))
	screen.blit(LoadingTextSurf,(0,780))
	pygame.display.flip()

	global StairsX
	global StairsY
	Chests=0
	MaxChests=Level
	DecMin=0
	DecMax=int(len(RoomPos)/14)
	while DecMin < DecMax:
		LoadingText='Placing item '+str(DecMin)+' of '+str(DecMax)+'...'
		LoadingTextSurf = myfont.render(LoadingText, False, green)
		screen.blit(TextBar,(0,780))
		screen.blit(LoadingTextSurf,(0,780))
		pygame.display.flip()
		DecNo=random.randint(1,6)
		if DecNo==1:
			Decoration='Leather'
		if DecNo==2:
			Decoration='Skull'
		if DecNo==3:
			Decoration='Wood'
		if DecNo==4:
			Decoration='Iron'
		if DecNo==5:
			Decoration='Steel'
		if DecNo==6:
			Chests=Chests+1
			if Chests <= MaxChests:
				Decoration='ChestClosed'
			else:
				Decoration='Skull'

		DecXMin=-1*MapGen*9
		DecXMax=MapGen*9
		DecYMin=-1*MapGen*9
		DecYMax=MapGen*9
		LookingForASpot=True
		while LookingForASpot:
			NoBlock=True
			DecX=random.randint(DecXMin, DecXMax)
			DecY=random.randint(DecYMin, DecYMax)

			if (DecX/9)==int(DecX/9):
				NoBlock=False
			if (DecY/9)==int(DecY/9):
				NoBlock=False
	
			if NoBlock:
				FloorFound=False
				CheckX=DecX
				CheckY=DecY
				FloorFound=CheckFloor(Labyrinth, CheckX, CheckY)
				if FloorFound:
					LookingForASpot=False
					Counter=0
					MaxCounter=len(Labyrinth)
					while Counter < MaxCounter:
						Object=Labyrinth[Counter]
						ObjectX=Labyrinth[Counter+1]
						ObjectY=Labyrinth[Counter+2]
						if ObjectX==DecX and ObjectY==DecY:
							Labyrinth.append(Decoration)
							Labyrinth.append(DecX)
							Labyrinth.append(DecY)
						Counter=Counter+3
		DecMin=DecMin+1
	return


# Container Function for all the functions that generate a new level
def GenerateLabyrinth():
	global MapGen
	LoadingText='Cooking level '+str(Level)+'...'
	LoadingTextSurf = myfont.render(LoadingText, False, green)
	screen.blit(TextBar,(0,780))
	screen.blit(LoadingTextSurf,(0,780))
	pygame.display.flip()
	#DoOuterWall(Level)
	GenerateRoomPos(Level)
	GenerateRooms(RoomPos)
	return()

def DoSplash(LoadList):
	pygame.key.set_repeat()
	screen.blit(Black,(0,0))
	screen.blit(Splash,(480,280))
	screen.blit(TextBar,(0,780))
	Text='Select a save slot...'
	LevelSave1=int(LoadList[1].rstrip())
	LevelSave2=int(LoadList[20].rstrip())
	LevelSave3=int(LoadList[39].rstrip())
	LevelSave4=int(LoadList[58].rstrip())
	LevelSave5=int(LoadList[77].rstrip())
	LevelSave6=int(LoadList[96].rstrip())

	SLevelSave1=str(LevelSave1)
	SLevelSave2=str(LevelSave2)
	SLevelSave3=str(LevelSave3)
	SLevelSave4=str(LevelSave4)
	SLevelSave5=str(LevelSave5)
	SLevelSave6=str(LevelSave6)

	if LevelSave1==0:
		Save1Status='Save slot 1, new game'
	else:
		Save1Status='Save slot 1, level: '+SLevelSave1+' Att: '+str(LoadList[5]).rstrip()+' Def: '+str(LoadList[6]).rstrip()+' Lif: '+str(LoadList[7]).rstrip()+' Mag: '+str(LoadList[8]).rstrip()
	if LevelSave2==0:
		Save2Status='Save slot 2, new game'
	else:
		Save2Status='Save slot 2, level: '+SLevelSave2+' Att: '+str(LoadList[24]).rstrip()+' Def: '+str(LoadList[25]).rstrip()+' Lif: '+str(LoadList[26]).rstrip()+' Mag: '+str(LoadList[27]).rstrip()
	if LevelSave3==0:
		Save3Status='Save slot 3, new game'
	else:
		Save3Status='Save slot 3, level: '+SLevelSave3+' Att: '+str(LoadList[43]).rstrip()+' Def: '+str(LoadList[44]).rstrip()+' Lif: '+str(LoadList[45]).rstrip()+' Mag: '+str(LoadList[46]).rstrip()
	if LevelSave4==0:
		Save4Status='Save slot 4, new game'
	else:
		Save4Status='Save slot 4, level: '+SLevelSave4+' Att: '+str(LoadList[62]).rstrip()+' Def: '+str(LoadList[63]).rstrip()+' Lif: '+str(LoadList[64]).rstrip()+' Mag: '+str(LoadList[65]).rstrip()
	if LevelSave5==0:
		Save5Status='Save slot 5, new game'
	else:
		Save5Status='Save slot 5, level: '+SLevelSave5+' Att: '+str(LoadList[81]).rstrip()+' Def: '+str(LoadList[82]).rstrip()+' Lif: '+str(LoadList[83]).rstrip()+' Mag: '+str(LoadList[84]).rstrip()
	if LevelSave6==0:
		Save6Status='Save slot 6, new game'
	else:
		Save6Status='Save slot 6, level: '+SLevelSave6+' Att: '+str(LoadList[100]).rstrip()+' Def: '+str(LoadList[101]).rstrip()+' Lif: '+str(LoadList[102]).rstrip()+' Mag: '+str(LoadList[103]).rstrip()

	Save1Text = myfont.render(Save1Status, False, green)
	Save2Text = myfont.render(Save2Status, False, green)
	Save3Text = myfont.render(Save3Status, False, green)
	Save4Text = myfont.render(Save4Status, False, green)
	Save5Text = myfont.render(Save5Status, False, green)
	Save6Text = myfont.render(Save6Status, False, green)
	Status = myfont.render('Select a save slot or press ESC to quit', False, yellow)

	screen.blit(Save1Text,(0,50))
	screen.blit(Save2Text,(0,100))
	screen.blit(Save3Text,(0,150))
	screen.blit(Save4Text,(0,200))
	screen.blit(Save5Text,(0,250))
	screen.blit(Save6Text,(0,300))
	TextSurf = myfont.render(Text, False, green)
	LoadingText='Welcome to Legend of Zachno, press enter...'
	LoadingTextSurf = myfont.render(LoadingText, False, green)
	screen.blit(TextSurf,(0,0))
	screen.blit(LoadingTextSurf,(0,780))
	pygame.display.flip()
	
	Selection=True
	while Selection:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_KP1 or event.key == pygame.K_1:
					SaveSlot=0
					Selection=False
				if event.key == pygame.K_KP2 or event.key == pygame.K_2:
					SaveSlot=19
					Selection=False
				if event.key == pygame.K_KP3 or event.key == pygame.K_3:
					SaveSlot=38
					Selection=False
				if event.key == pygame.K_KP4 or event.key == pygame.K_4:
					SaveSlot=57
					Selection=False
				if event.key == pygame.K_KP5 or event.key == pygame.K_5:
					SaveSlot=76
					Selection=False
				if event.key == pygame.K_KP6 or event.key == pygame.K_6:
					SaveSlot=95
					Selection=False
	pygame.key.set_repeat(30,50)
	return(SaveSlot)

def DoExit():
	screen.blit(Black,(0,0))
	screen.blit(Splash,(480,280))
	screen.blit(TextBar,(0,780))
	LoadingText='Game state saved next session will be in level '+str(Level)+' , press <enter> to return to game or <esc> to quit...'
	LoadingTextSurf = myfont.render(LoadingText, False, green)
	screen.blit(LoadingTextSurf,(0,780))
	pygame.display.flip()
	MakingAChoice=True
	while MakingAChoice:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
					return
				if event.key == pygame.K_ESCAPE:
					sys.exit()
	return

def DoVictory():
	screen.blit(Black,(0,0))
	screen.blit(Splash,(480,280))
	screen.blit(TextBar,(0,780))
	LoadingText='Congratulations on beating Legend of Zachno, press <enter> to keep the save, press <del> to reset...'
	LoadingTextSurf = myfont.render(LoadingText, False, green)
	screen.blit(LoadingTextSurf,(0,780))
	pygame.display.flip()
	MakingAChoice=True
	while MakingAChoice:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
					MakingAChoice=False
				if event.key == pygame.K_DELETE:
					LoadList[SaveSlot]=0
					LoadList[SaveSlot+1]=0
					LoadList[SaveSlot+2]='Fist'
					LoadList[SaveSlot+3]='None'
					LoadList[SaveSlot+4]=0
					LoadList[SaveSlot+5]=2
					LoadList[SaveSlot+6]=2
					LoadList[SaveSlot+7]=2
					LoadList[SaveSlot+8]=2
					LoadList[SaveSlot+9]=20
					LoadList[SaveSlot+10]=10
					LoadList[SaveSlot+11]=0
					LoadList[SaveSlot+12]=0
					LoadList[SaveSlot+13]=0
					LoadList[SaveSlot+14]=0
					LoadList[SaveSlot+15]=0
					LoadList[SaveSlot+16]=0
					LoadList[SaveSlot+17]=0
					LoadList[SaveSlot+18]=0
					os.system('rm Zachno.sav')
					Save=open('Zachno.sav', 'a')
					PlayerCounter=0
					MaxPlayerCounter=len(LoadList)
					while PlayerCounter < MaxPlayerCounter:
						SaveLine=str(LoadList[PlayerCounter]).rstrip()
						Save.write(SaveLine)
						if not PlayerCounter==MaxPlayerCounter-1:
							Save.write('\n')
						PlayerCounter=PlayerCounter+1
					Save.close()
					MakingAChoice=False
	sys.exit()
	return

def DoItem(ItemCounter):
	global Spell
	Item=InvList[ItemCounter].rstrip()
	if Item=='Fire' or Item=='Teleport' or Item=='Drain' or Item=='Lightning' or Item=='Fireball':
		Spell=Item
		DoSpell(ItemCounter)
		return
	ChestText='Press <enter> to use '+Item+' or <del> to drop...'
	ChestTextSurf = myfont.render(ChestText, False, green)

	screen.blit(TextBar,(0,370))
	screen.blit(TextBar,(0,390))
	screen.blit(TextBar,(0,410))

	screen.blit(ChestTextSurf,(0,390))
	pygame.display.flip()
	MakingAChoice=True
	while MakingAChoice:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
					UseItem(ItemCounter)
					MakingAChoice=False
				if event.key == pygame.K_DELETE:
					DropItem(ItemCounter)
					MakingAChoice=False

	return

def DoSpell(ItemCounter):
	global PlayerX
	global PlayerY
	global PlayerLifeLevel
	global PlayerLife
	global PlayerMana
	global PlayerXP
	global Spell
	global SpellX
	global SpellY
	global HeroList
	DoScreen(Labyrinth, Level)
	MapGen=int(Level/2)+1
	SpellText='Press direction for '+Spell+' spell or <del> to drop...'
	SpellTextSurf = myfont.render(SpellText, False, green)

	screen.blit(TextBar,(0,740))
	screen.blit(TextBar,(0,760))
	screen.blit(TextBar,(0,780))

	screen.blit(SpellTextSurf,(0,760))
	pygame.display.flip()
	MakingAChoice=True
	while MakingAChoice:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					SpellDir=1
					MakingAChoice=False
				if event.key == pygame.K_RIGHT:
					SpellDir=2
					MakingAChoice=False
				if event.key == pygame.K_DOWN:
					SpellDir=3
					MakingAChoice=False
				if event.key == pygame.K_LEFT:
					SpellDir=4
					MakingAChoice=False
				if event.key == pygame.K_DELETE:
					DropItem(ItemCounter)
					return
					MakingAChoice=False

	if Spell=='Fire':
		if PlayerMana >= 1:
			PlayerMana=PlayerMana-1
			del InvList[ItemCounter]
		else:
			Fail.play()
			return
	elif Spell=='Teleport':
		if PlayerMana >= 2:
			PlayerMana=PlayerMana-2
			del InvList[ItemCounter]
		else:
			Fail.play()
			return
	elif Spell=='Drain':
		if PlayerMana >= 3:
			PlayerMana=PlayerMana-3
			del InvList[ItemCounter]
		else:
			Fail.play()
			return
	elif Spell=='Lightning':
		if PlayerMana >= 4:
			PlayerMana=PlayerMana-4
			del InvList[ItemCounter]
		else:
			Fail.play()
			return
	elif Spell=='Fireball':
		if PlayerMana >= 5:
			PlayerMana=PlayerMana-5
			del InvList[ItemCounter]
		else:
			Fail.play()
			return

	SpellX=PlayerX
	SpellY=PlayerY
	FreeFlight=True
	while FreeFlight:
		if SpellDir==1:
			SpellY=SpellY+1
		elif SpellDir==2:
			SpellX=SpellX+1
		elif SpellDir==3:
			SpellY=SpellY-1
		elif SpellDir==4:
			SpellX=SpellX-1
		
		DoScreen(Labyrinth, Level)

		CheckX=SpellX
		CheckY=SpellY
		FloorFound=CheckFloor(Labyrinth, CheckX, CheckY)
		if FloorFound:
			HeroCounter=0
			HeroCounterMax=len(HeroList)
			while HeroCounter < HeroCounterMax:
				HeroLevel=int(HeroList[HeroCounter])
				HeroArmor=str(HeroList[HeroCounter+3])
				HeroAttack=int(HeroList[HeroCounter+5])
				HeroDefence=int(HeroList[HeroCounter+6])
				HeroLife=int(HeroList[HeroCounter+9])
				HeroMana=int(HeroList[HeroCounter+10])
				DropItemOne=str(HeroList[HeroCounter+11])
				DropItemTwo=str(HeroList[HeroCounter+12])
				HeroX=int(HeroList[HeroCounter+13])
				HeroY=int(HeroList[HeroCounter+14])
				if HeroX==SpellX and HeroY==SpellY:
					FreeFlight=False
					if Spell=='Fire':
						Fire.play()
						HeroAttack=HeroAttack-2
						if HeroAttack < 0:
							HeroAttack=0
						HeroList[HeroCounter+5]=HeroAttack
						HeroLife=HeroLife-4
					if Spell=='Teleport':
						HeroDefence=HeroDefence-4
						if HeroDefence < 0:
							HeroDefence=0
						HeroList[HeroCounter+6]=HeroDefence
						Teleport.play()
						TeleportXMin=-1*MapGen*9
						TeleportXMax=MapGen*9
						TeleportYMin=-1*MapGen*9
						TeleportYMax=MapGen*9
						LookingForASpot=True
						while LookingForASpot:
							NoBlock=True
							TeleportX=random.randint(TeleportXMin, TeleportXMax)
							TeleportY=random.randint(TeleportYMin, TeleportYMax)
			
							if (TeleportX/9)==int(TeleportX/9):
								NoBlock=False
							if (TeleportY/9)==int(TeleportY/9):
								NoBlock=False

							if NoBlock:
								FloorFound=False
								CheckX=TeleportX
								CheckY=TeleportY
								FloorFound=CheckFloor(Labyrinth, CheckX, CheckY)
								if FloorFound:
									HeroList[HeroCounter+13]=TeleportX
									HeroList[HeroCounter+14]=TeleportY
									LookingForASpot=False
					if Spell=='Drain':
						Steal.play()
						PlayerLife=PlayerLife+12
						if PlayerLife > (PlayerLifeLevel*10):
							PlayerLife = (PlayerLifeLevel*10)
						HeroLife=HeroLife-12
					if Spell=='Lightning':
						Lightning.play()
						HeroLife=HeroLife-16
						HeroMana=HeroMana-8
						HeroList[HeroCounter+10]=HeroMana
					if Spell=='Fireball':
						Fireball.play()
						HeroLife=HeroLife-20
						HeroDefence=HeroDefence-10
						if HeroDefence < 0:
							HeroDefence=0
						HeroList[HeroCounter+6]=HeroDefence
					if HeroLife < 1:
						DeathScream.play()
						PlayerXP=PlayerXP+HeroLevel
						Chance=random.randint(1,2)
						if Chance==1:
							if DropItemOne != 'None':
								Labyrinth.append(DropItemOne)
								Labyrinth.append(HeroX)
								Labyrinth.append(HeroY)
						if Chance==2:
							if DropItemTwo != 'None':
								Labyrinth.append(DropItemTwo)
								Labyrinth.append(HeroX)
								Labyrinth.append(HeroY)
						del HeroList[HeroCounter]
						del HeroList[HeroCounter]
						del HeroList[HeroCounter]
						del HeroList[HeroCounter]
						del HeroList[HeroCounter]
						del HeroList[HeroCounter]
						del HeroList[HeroCounter]
						del HeroList[HeroCounter]
						del HeroList[HeroCounter]
						del HeroList[HeroCounter]
						del HeroList[HeroCounter]
						del HeroList[HeroCounter]
						del HeroList[HeroCounter]
						del HeroList[HeroCounter]
						del HeroList[HeroCounter]
						HeroCounterMax=len(HeroList)
					else:
						HeroList[HeroCounter+9]=HeroLife
				HeroCounter=HeroCounter+15
		else:
			FreeFlight=False
	SpellX=-200
	SpellY=-200
	return

def UseItem(ItemCounter):
	global PlayerWeapon
	global PlayerArmor
	global PlayerLifeLevel
	global PlayerLife
	global PlayerMagic
	global PlayerMana
	global Spell
	OldWeapon=PlayerWeapon
	OldArmor=PlayerArmor
	if InvList[ItemCounter].rstrip()=='Mace':
		PlayerWeapon='Mace'
		del InvList[ItemCounter]
		if not OldWeapon=='Fists':
			InvList.append(OldWeapon)
	elif InvList[ItemCounter].rstrip()=='Dagger':
		PlayerWeapon='Dagger'
		del InvList[ItemCounter]
		if not OldWeapon=='Fists':
			InvList.append(OldWeapon)
	elif InvList[ItemCounter].rstrip()=='Sword':
		PlayerWeapon='Sword'
		del InvList[ItemCounter]
		if not OldWeapon=='Fists':
			InvList.append(OldWeapon)
	elif InvList[ItemCounter].rstrip()=='Battleaxe':
		PlayerWeapon='Battleaxe'
		del InvList[ItemCounter]
		if not OldWeapon=='Fists':
			InvList.append(OldWeapon)
	elif InvList[ItemCounter].rstrip()=='Shield':
		PlayerArmor='Shield'
		del InvList[ItemCounter]
		if not OldArmor=='None':
			InvList.append(OldArmor)
	elif InvList[ItemCounter].rstrip()=='WShield':
		PlayerArmor='WShield'
		del InvList[ItemCounter]
		if not OldArmor=='None':
			InvList.append(OldArmor)
	elif InvList[ItemCounter].rstrip()=='TShield':
		PlayerArmor='TShield'
		del InvList[ItemCounter]
		if not OldArmor=='None':
			InvList.append(OldArmor)
	elif InvList[ItemCounter].rstrip()=='Chainmail':
		PlayerArmor='Chainmail'
		del InvList[ItemCounter]
		if not OldArmor=='None':
			InvList.append(OldArmor)
	elif InvList[ItemCounter].rstrip()=='Plate':
		PlayerArmor='Plate'
		del InvList[ItemCounter]
		if not OldArmor=='None':
			InvList.append(OldArmor)
	elif InvList[ItemCounter].rstrip()=='Beartrap':
		DropItem(ItemCounter)
	elif InvList[ItemCounter].rstrip()=='Spiketrap':
		Clank.play()
		DropItem(ItemCounter)
	elif InvList[ItemCounter].rstrip()=='Acidtrap':
		Clank.play()
		DropItem(ItemCounter)
	elif InvList[ItemCounter].rstrip()=='Electrotrap':
		Clank.play()
		DropItem(ItemCounter)
	elif InvList[ItemCounter].rstrip()=='Mine':
		Clank.play()
		DropItem(ItemCounter)
	elif InvList[ItemCounter].rstrip()=='Lifepotion':
		PlayerLife=PlayerLife+10
		if PlayerLife > PlayerLifeLevel*10:
			PlayerLife=PlayerLifeLevel*10
		Life.play()
		del InvList[ItemCounter]
	elif InvList[ItemCounter].rstrip()=='Manapotion':
		PlayerMana=PlayerMana+10
		if PlayerMana > PlayerMagic*5:
			PlayerMana=PlayerMagic*5
		Mana.play()
		del InvList[ItemCounter]
	return


def DropItem(ItemCounter):
	if InvList[ItemCounter].rstrip()=='Mace':
		Object='Mace'
	if InvList[ItemCounter].rstrip()=='Beartrap':
		Object='BearTrap'
	if InvList[ItemCounter].rstrip()=='Spiketrap':
		Object='SpikeTrap'
	if InvList[ItemCounter].rstrip()=='Electrotrap':
		Object='ElectroTrap'
	if InvList[ItemCounter].rstrip()=='Acidtrap':
		Object='AcidTrap'
	if InvList[ItemCounter].rstrip()=='Mine':
		Object='Mine'
	if InvList[ItemCounter].rstrip()=='Lifepotion':
		Object='Life'
	if InvList[ItemCounter].rstrip()=='Manapotion':
		Object='Mana'
	if InvList[ItemCounter].rstrip()=='Dagger':
		Object='Dagger'
	if InvList[ItemCounter].rstrip()=='Sword':
		Object='Sword'
	if InvList[ItemCounter].rstrip()=='Battleaxe':
		Object='BattleAxe'
	if InvList[ItemCounter].rstrip()=='Shield':
		Object='Shield'
	if InvList[ItemCounter].rstrip()=='WShield':
		Object='WShield'
	if InvList[ItemCounter].rstrip()=='TShield':
		Object='TShield'
	if InvList[ItemCounter].rstrip()=='Chainmail':
		Object='Chainmail'
	if InvList[ItemCounter].rstrip()=='Plate':
		Object='Plate'
	if InvList[ItemCounter].rstrip()=='Fire':
		Object='FireScroll'
	if InvList[ItemCounter].rstrip()=='Teleport':
		Object='TeleportScroll'
	if InvList[ItemCounter].rstrip()=='Drain':
		Object='DrainScroll'
	if InvList[ItemCounter].rstrip()=='Lightning':
		Object='LightningScroll'
	if InvList[ItemCounter].rstrip()=='Fireball':
		Object='FireballScroll'
	Clank.play()
	Labyrinth.append(Object)
	Labyrinth.append(PlayerX)
	Labyrinth.append(PlayerY)
	del InvList[ItemCounter]
	return

def PlaceHeroes(Labyrinth, Level):
	global HeroList
	del HeroList[:]
	HeroFile=open('Heroes', 'r')
	ListofHeroes=list(HeroFile)
	HeroFile.close()
	MapGen=int(Level/2)+1
	Counter=0
	MaxCounter=len(ListofHeroes)
	while Counter < MaxCounter:
		HeroLevel=int(ListofHeroes[Counter])
		HeroName=ListofHeroes[Counter+1].rstrip()
		HeroWeapon=ListofHeroes[Counter+2].rstrip()
		HeroArmor=ListofHeroes[Counter+3].rstrip()
		HeroSpell=ListofHeroes[Counter+4].rstrip()
		HeroAttack=int(ListofHeroes[Counter+5])
		HeroDefence=int(ListofHeroes[Counter+6])
		HeroLifeLevel=int(ListofHeroes[Counter+7])
		HeroMagic=int(ListofHeroes[Counter+8])
		HeroLife=int(ListofHeroes[Counter+9])
		HeroMana=int(ListofHeroes[Counter+10])
		HeroDropItemOne=ListofHeroes[Counter+11].rstrip()
		HeroDropItemTwo=ListofHeroes[Counter+12].rstrip()
		Number=1
		MaxNumber=int(Level/HeroLevel)
		while Number <= MaxNumber:
			HeroXMin=-1*MapGen*9
			HeroXMax=MapGen*9
			HeroYMin=-1*MapGen*9
			HeroYMax=MapGen*9
			LookingForASpot=True
			while LookingForASpot:
				NoBlock=True
				HeroX=random.randint(HeroXMin, HeroXMax)
				HeroY=random.randint(HeroYMin, HeroYMax)

				if (HeroX/9)==int(HeroX/9):
					NoBlock=False
				if (HeroY/9)==int(HeroY/9):
					NoBlock=False

				if NoBlock:
					FloorFound=False
					CheckX=HeroX
					CheckY=HeroY
					FloorFound=CheckFloor(Labyrinth, CheckX, CheckY)
					if FloorFound:
						HeroList.append(HeroLevel)
						HeroList.append(HeroName)
						HeroList.append(HeroWeapon)
						HeroList.append(HeroArmor)
						HeroList.append(HeroSpell)
						HeroList.append(HeroAttack)
						HeroList.append(HeroDefence)
						HeroList.append(HeroLifeLevel)
						HeroList.append(HeroMagic)
						HeroList.append(HeroLife)
						HeroList.append(HeroMana)
						HeroList.append(HeroDropItemOne)
						HeroList.append(HeroDropItemTwo)
						HeroList.append(HeroX)
						HeroList.append(HeroY)
						LookingForASpot=False
			LoadingText='Placing '+str(HeroName)+'...'
			LoadingTextSurf = myfont.render(LoadingText, False, green)
			screen.blit(TextBar,(0,780))
			screen.blit(LoadingTextSurf,(0,780))
			pygame.display.flip()

			Number=Number+1
		Counter=Counter+13
	return

def DoLevelUp():
	global PlayerAttack
	global PlayerDefence
	global PlayerLifeLevel
	global PlayerMagic
	global PlayerLife
	global PlayerMana
	global PlayerXP
	PlayerLevel=PlayerAttack+PlayerDefence+PlayerLifeLevel+PlayerMagic
	Applause.play()
	MakingaChoice=True
	while MakingaChoice:
		Text1='Press number to level attribute...'
		Text1Surf = myfont.render(Text1, False, green)
		Text2='1> Attack: '+str(PlayerAttack)
		Text2Surf = myfont.render(Text2, False, green)
		Text3='2> Defence: '+str(PlayerDefence)
		Text3Surf = myfont.render(Text3, False, green)
		Text4='3> Health:'+str(PlayerLifeLevel)
		Text4Surf = myfont.render(Text4, False, green)
		Text5='4> Magic:'+str(PlayerMagic)
		Text5Surf = myfont.render(Text5, False, green)

		screen.blit(TextBar,(0,620))
		screen.blit(TextBar,(0,640))
		screen.blit(TextBar,(0,660))
		screen.blit(TextBar,(0,680))
		screen.blit(TextBar,(0,700))

		screen.blit(Text1Surf,(0,620))
		screen.blit(Text2Surf,(0,640))
		screen.blit(Text3Surf,(0,660))
		screen.blit(Text4Surf,(0,680))
		screen.blit(Text5Surf,(0,700))

		pygame.display.flip()

		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_1 or event.key == pygame.K_KP1:
					PlayerAttack=PlayerAttack+1
					PlayerXP=PlayerXP-(PlayerLevel*2)
					MakingaChoice=False
				if event.key == pygame.K_2 or event.key == pygame.K_KP2:
					PlayerDefence=PlayerDefence+1
					PlayerXP=PlayerXP-(PlayerLevel*2)
					MakingaChoice=False
				if event.key == pygame.K_3 or event.key == pygame.K_KP3:
					PlayerLifeLevel=PlayerLifeLevel+1
					PlayerLife=PlayerLifeLevel*10
					PlayerXP=PlayerXP-(PlayerLevel*2)
					MakingaChoice=False
				if event.key == pygame.K_4 or event.key == pygame.K_KP4:
					PlayerMagic=PlayerMagic+1
					PlayerMana=PlayerMagic*5
					PlayerXP=PlayerXP-(PlayerLevel*2)
					MakingaChoice=False
		DoScreen(Labyrinth, Level)
	return

def DoHeroSpell(HeroX, HeroY, HeroSpell, Counter):
	global PlayerX
	global PlayerY
	global PlayerLifeLevel
	global PlayerLife
	global PlayerXP
	global Spell
	global SpellX
	global SpellY
	global HeroList
	MapGen=int(Level/2)+1
	if HeroY < PlayerY:
		SpellDir=1
	if HeroX < PlayerX:
		SpellDir=2
	if HeroY > PlayerY:
		SpellDir=3
	if HeroX > PlayerX:
		SpellDir=4

	Spell=HeroSpell
	SpellX=HeroX
	SpellY=HeroY
	FreeFlight=True
	if Spell=='Fire':
		HeroMana=int(HeroList[Counter+10])
		HeroMana=HeroMana-1
		HeroList[Counter+10]=HeroMana
		Fire.play()
	if Spell=='Teleport':
		HeroMana=int(HeroList[Counter+10])
		HeroMana=HeroMana-2
		HeroList[Counter+10]=HeroMana
		Teleport.play()
	if Spell=='Drain':
		HeroMana=int(HeroList[Counter+10])
		HeroMana=HeroMana-3
		HeroList[Counter+10]=HeroMana
		Steal.play()
	if Spell=='Lightning':
		HeroMana=int(HeroList[Counter+10])
		HeroMana=HeroMana-4
		HeroList[Counter+10]=HeroMana
		Lightning.play()
	if Spell=='Fireball':
		HeroMana=int(HeroList[Counter+10])
		HeroMana=HeroMana-5
		HeroList[Counter+10]=HeroMana
		Fireball.play()
	while FreeFlight:
		if SpellDir==1:
			SpellY=SpellY+1
		elif SpellDir==2:
			SpellX=SpellX+1
		elif SpellDir==3:
			SpellY=SpellY-1
		elif SpellDir==4:
			SpellX=SpellX-1
		
		DoScreen(Labyrinth, Level)

		CheckX=SpellX
		CheckY=SpellY
		FloorFound=CheckFloor(Labyrinth, CheckX, CheckY)
		if FloorFound:
			if SpellX==PlayerX and SpellY==PlayerY:
				FreeFlight=False
				if Spell=='Fire':
					PlayerLife=PlayerLife-4
				if Spell=='Teleport':
					TeleportXMin=-1*MapGen*9
					TeleportXMax=MapGen*9
					TeleportYMin=-1*MapGen*9
					TeleportYMax=MapGen*9
					LookingForASpot=True
					while LookingForASpot:
						TeleportX=random.randint(TeleportXMin, TeleportXMax)
						TeleportY=random.randint(TeleportYMin, TeleportYMax)
		
						FloorFound=False
						CheckX=TeleportX
						CheckY=TeleportY
						FloorFound=CheckFloor(Labyrinth, CheckX, CheckY)
						if FloorFound:
							PlayerX=TeleportX
							PlayerY=TeleportY
							LookingForASpot=False
				if Spell=='Drain':
					HeroLife=int(HeroList[Counter+9])
					HeroLife=HeroLife+12
					HeroList[Counter+9]=HeroLife
					PlayerLife=PlayerLife-12
				if Spell=='Lightning':
					PlayerLife=PlayerLife-16
				if Spell=='Fireball':
					PlayerLife=PlayerLife-20

				if PlayerLife < 1:
					DeathScream.play()
					screen.blit(Dead, (560, 320))
					pygame.display.flip()
					wait()
					sys.exit()
		else:
			FreeFlight=False
	SpellX=-200
	SpellY=-200
	return

def DoHeroCombat(Counter):
	global PlayerX
	global PlayerY
	global PlayerArmor
	global PlayerDefence
	global PlayerLifeLevel
	global PlayerLife
	global PlayerXP
	global Spell
	global SpellX
	global SpellY
	global HeroList
	PlayerDef=PlayerDefence
	HeroWeapon=str(HeroList[Counter+2])
	HeroAttack=int(HeroList[Counter+5])
	if PlayerArmor=='WShield':
		PlayerDef=PlayerDefence+1
	elif PlayerArmor=='Shield':
		PlayerDef=PlayerDefence+2
	elif PlayerArmor=='TShield':
		PlayerDef=PlayerDefence+3
	elif PlayerArmor=='Chainmail':
		PlayerDef=PlayerDefence+4
	elif PlayerArmor=='Plate':
		PlayerDef=PlayerDefence+5

	BreakChance=0
	if HeroWeapon=='Fists':
		HeroAt=HeroAttack+1
		BreakChance=1
	elif HeroWeapon=='Dagger':
		HeroAt=HeroAttack+4
		BreakChance=2
	elif HeroWeapon=='Mace':
		HeroAt=HeroAttack+6
		BreakChance=3
	elif HeroWeapon=='Sword':
		HeroAt=HeroAttack+8
		BreakChance=4
	elif HeroWeapon=='Battleaxe':
		HeroAt=HeroAttack+10
		BreakChance=5

	HeroAt=HeroAt-PlayerDef
	if HeroAt > 0:
		if HeroWeapon=='Fists':
			Punch.play()
		elif HeroWeapon=='Dagger':
			Stab.play()
		elif HeroWeapon=='Mace':
			MaceHit.play()
		elif HeroWeapon=='Sword':
			SwordHit.play()
		elif HeroWeapon=='Battleaxe':
			AxeHit.play()
		PlayerLife=PlayerLife-HeroAt
		Spell='BloodSpatter'
		SpellX=PlayerX
		SpellY=PlayerY
		if PlayerLife < 1:
			DeathScream.play()
			screen.blit(Dead, (560, 320))
			pygame.display.flip()
			wait()
			sys.exit()
		pygame.display.flip()
	else:
		Bump.play()
	if BreakChance >= random.randint(1,20):
		Shatter.play()
		PlayerArmor='None'
	return

def EnemyMove(EnemyDir, Counter):
	global PlayerX
	global PlayerY
	global Labyrinth
	global HeroList
	global Spell
	global SpellX
	global SpellY

	Blocked=False
	HeroLevel=int(HeroList[Counter])
	HeroName=HeroList[Counter+1].rstrip()
	HeroWeapon=HeroList[Counter+2].rstrip()
	HeroArmor=HeroList[Counter+3].rstrip()
	HeroSpell=HeroList[Counter+4].rstrip()
	HeroAttack=int(HeroList[Counter+5])
	HeroDefence=int(HeroList[Counter+6])
	HeroLifeLevel=int(HeroList[Counter+7])
	HeroMagic=int(HeroList[Counter+8])
	HeroLife=int(HeroList[Counter+9])
	HeroMana=int(HeroList[Counter+10])
	HeroDropItemOne=HeroList[Counter+11].rstrip()
	HeroDropItemTwo=HeroList[Counter+12].rstrip()
	HeroX=HeroList[Counter+13]
	HeroY=HeroList[Counter+14]

	if EnemyDir==8:
		NewHeroX=HeroX
		NewHeroY=HeroY+1
	elif EnemyDir==6:
		NewHeroX=HeroX+1
		NewHeroY=HeroY
	elif EnemyDir==2:
		NewHeroX=HeroX
		NewHeroY=HeroY-1
	elif EnemyDir==4:
		NewHeroX=HeroX-1
		NewHeroY=HeroY
	if NewHeroX==PlayerX and NewHeroY==PlayerY:
		DoHeroCombat(Counter)
	else:
		LabNum=0
		LabNumMax=len(Labyrinth)
		while LabNum < LabNumMax:
			Object=Labyrinth[LabNum]
			ObjectX=int(Labyrinth[LabNum+1])
			ObjectY=int(Labyrinth[LabNum+2])
			if NewHeroX==ObjectX and NewHeroY==ObjectY:
				if Object=='SpikeTrap':
					del Labyrinth[LabNum]
					del Labyrinth[LabNum]
					del Labyrinth[LabNum]
					LabNumMax=len(Labyrinth)
					HeroAttack=HeroAttack-2
					if HeroAttack < 0:
						HeroAttack=0
					HeroLife=HeroLife-3
					SpellX=NewHeroX
					SpellY=NewHeroY
					Spell='BloodSpatter'
					Spikes.play()
				if Object=='BearTrap':
					del Labyrinth[LabNum]
					del Labyrinth[LabNum]
					del Labyrinth[LabNum]
					LabNumMax=len(Labyrinth)
					HeroDefence=HeroDefence-3
					if HeroDefence < 0:
						HeroDefence=0
					HeroLife=HeroLife-6
					SpellX=NewHeroX
					SpellY=NewHeroY
					Spell='BloodSpatter'
					Trap.play()
				if Object=='AcidTrap':
					del Labyrinth[LabNum]
					del Labyrinth[LabNum]
					del Labyrinth[LabNum]
					LabNumMax=len(Labyrinth)
					HeroLife=HeroLife-9
					HeroLifeLevel=HeroLifeLevel+5
					HeroList[Counter+7]=HeroLifeLevel
					SpellX=NewHeroX
					SpellY=NewHeroY
					Spell='AcidPuddle'
					Sizzle.play()
				if Object=='ElectroTrap':
					del Labyrinth[LabNum]
					del Labyrinth[LabNum]
					del Labyrinth[LabNum]
					LabNumMax=len(Labyrinth)
					HeroMana=HeroMana-6
					HeroLife=HeroLife-12
					SpellX=NewHeroX
					SpellY=NewHeroY
					Spell='ElectricSpark'
					Lightning.play()
				if Object=='Mine':
					del Labyrinth[LabNum]
					del Labyrinth[LabNum]
					del Labyrinth[LabNum]
					LabNumMax=len(Labyrinth)
					HeroAttack=HeroAttack-5
					HeroDefence=HeroDefence-5
					HeroMana=HeroMana-5
					HeroLife=HeroLife-15
					SpellX=NewHeroX
					SpellY=NewHeroY
					Spell='Explosion'
					Boom.play()
			LabNum=LabNum+3
		if HeroLife < 1:
			Chance=random.randint(1,2)
			if Chance==1:
				if not HeroDropItemOne=='None':
					Labyrinth.append(HeroDropItemOne)
					Labyrinth.append(HeroX)
					Labyrinth.append(HeroY)
			else:
				if not HeroDropItemTwo=='None':
					Labyrinth.append(HeroDropItemTwo)
					Labyrinth.append(HeroX)
					Labyrinth.append(HeroY)
			del HeroList[Counter]
			del HeroList[Counter]
			del HeroList[Counter]
			del HeroList[Counter]
			del HeroList[Counter]
			del HeroList[Counter]
			del HeroList[Counter]
			del HeroList[Counter]
			del HeroList[Counter]
			del HeroList[Counter]
			del HeroList[Counter]
			del HeroList[Counter]
			del HeroList[Counter]
			del HeroList[Counter]
			del HeroList[Counter]
			DeathScream.play()
			return(Blocked)
		else:
			HeroList[Counter+5]=HeroAttack
			HeroList[Counter+6]=HeroDefence
			HeroList[Counter+9]=HeroLife
			HeroList[Counter+10]=HeroMana
		CheckX=NewHeroX
		CheckY=NewHeroY
		FoundFloor=False
		FoundFloor=CheckFloor(Labyrinth, CheckX, CheckY)
		NoEnemy=True
		NoEnemy=CheckEnemy(HeroList, CheckX, CheckY)
		if FoundFloor and NoEnemy:
			HeroList[Counter+13]=NewHeroX
			HeroList[Counter+14]=NewHeroY
			EnemyWalk.play()
		else:
			Blocked=True
	return(Blocked)

def HeroHunts(Counter):
	global PlayerX
	global PlayerY
	HeroX=HeroList[Counter+13]
	HeroY=HeroList[Counter+14]
	XDist=(HeroX-PlayerX)**2
	YDist=(HeroY-PlayerY)**2
	Blocked=False
	Horizontal=False
	Vertical=False
	if XDist >= YDist:
		Horizontal=True
	else:
		Vertical=True

	if HeroX <= PlayerX:
		EnemyDirHRZ=6
	else:
		EnemyDirHRZ=4

	if HeroY <= PlayerY:
		EnemyDirVRT=8
	else:
		EnemyDirVRT=2

	if Horizontal:
		EnemyDir=EnemyDirHRZ
		Blocked=EnemyMove(EnemyDir, Counter)
		if Blocked:
			EnemyDir=EnemyDirVRT
			EnemyMove(EnemyDir, Counter)
	else:
		EnemyDir=EnemyDirVRT
		Blocked=EnemyMove(EnemyDir, Counter)
		if Blocked:
			EnemyDir=EnemyDirHRZ
			EnemyMove(EnemyDir, Counter)
	return

def HeroFlees(Counter):
	global PlayerX
	global PlayerY
	HeroX=HeroList[Counter+13]
	HeroY=HeroList[Counter+14]
	XDist=(HeroX-PlayerX)**2
	YDist=(HeroY-PlayerY)**2
	Blocked=False
	Horizontal=False
	Vertical=False
	if XDist >= YDist:
		Horizontal=True
	else:
		Vertical=True

	if HeroX <= PlayerX:
		EnemyDirHRZ=4
	else:
		EnemyDirHRZ=6

	if HeroY <= PlayerY:
		EnemyDirVRT=2
	else:
		EnemyDirVRT=8

	if Horizontal:
		EnemyDir=EnemyDirHRZ
		Blocked=EnemyMove(EnemyDir, Counter)
		if Blocked:
			EnemyDir=EnemyDirVRT
			EnemyMove(EnemyDir, Counter)
	else:
		EnemyDir=EnemyDirVRT
		Blocked=EnemyMove(EnemyDir, Counter)
		if Blocked:
			EnemyDir=EnemyDirHRZ
			EnemyMove(EnemyDir, Counter)

	return

def CheckEnemy(HeroList, CheckX, CheckY):
	Counter=0
	MaxCounter=len(HeroList)
	NoEnemy=True
	while Counter < MaxCounter:
		HeroName=HeroList[Counter+1].rstrip()
		HeroX=HeroList[Counter+13]
		HeroY=HeroList[Counter+14]
		if CheckX==HeroX and CheckY==HeroY:
			if not HeroName=='':
				NoEnemy=False
		Counter = Counter+15
	return(NoEnemy)

def DoEnemies():
	global Labyrinth
	Counter=0
	MaxCounter=len(HeroList)
	while Counter < MaxCounter:
		HeroLevel=int(HeroList[Counter])
		HeroName=HeroList[Counter+1].rstrip()
		HeroWeapon=HeroList[Counter+2].rstrip()
		HeroArmor=HeroList[Counter+3].rstrip()
		HeroSpell=HeroList[Counter+4].rstrip()
		HeroAttack=int(HeroList[Counter+5])
		HeroDefence=int(HeroList[Counter+6])
		HeroLifeLevel=int(HeroList[Counter+7])
		HeroMagic=int(HeroList[Counter+8])
		HeroLife=int(HeroList[Counter+9])
		HeroMana=int(HeroList[Counter+10])
		HeroDropItemOne=HeroList[Counter+11].rstrip()
		HeroDropItemTwo=HeroList[Counter+12].rstrip()
		HeroX=HeroList[Counter+13]
		HeroY=HeroList[Counter+14]
		XDiff=HeroX-PlayerX
		YDiff=HeroY-PlayerY
		TreshHold=10-HeroAttack
		SpellChance=random.randint(1,2)
		EnemyScan=int((HeroLevel+5)/2)
		if (-1*EnemyScan <= XDiff) and ( XDiff <= EnemyScan) and (-1*EnemyScan <= YDiff) and (YDiff <= EnemyScan):
			if HeroLife > (HeroLifeLevel*TreshHold):
				if HeroX==PlayerX or HeroY==PlayerY:
					if HeroY < PlayerY:
						CheckX=HeroX
						CheckY=HeroY+1
					if HeroX < PlayerX:
						CheckX=HeroX+1
						CheckY=HeroY

					if HeroY > PlayerY:
						CheckX=HeroX
						CheckY=HeroY-1

					if HeroX > PlayerX:
						CheckX=HeroX-1
						CheckY=HeroY
					FloorFound=False
					FloorFound=CheckFloor(Labyrinth, CheckX, CheckY)
					if HeroSpell == 'Fire' and HeroMana > 0 and SpellChance==1 and FloorFound:
						DoHeroSpell(HeroX, HeroY, HeroSpell, Counter)
					elif HeroSpell == 'Teleport' and HeroMana > 1 and SpellChance==1 and FloorFound:
						DoHeroSpell(HeroX, HeroY, HeroSpell, Counter)
					elif HeroSpell == 'Drain' and HeroMana > 2 and SpellChance==1 and FloorFound:
						DoHeroSpell(HeroX, HeroY, HeroSpell, Counter)
					elif HeroSpell == 'Lightning' and HeroMana > 3 and SpellChance==1 and FloorFound:
						DoHeroSpell(HeroX, HeroY, HeroSpell, Counter)
					elif HeroSpell == 'Fireball' and HeroMana > 4 and SpellChance==1 and FloorFound:
						DoHeroSpell(HeroX, HeroY, HeroSpell, Counter)
					else:
						HeroHunts(Counter)
						MaxCounter=len(HeroList)
				else:
					HeroHunts(Counter)
					MaxCounter=len(HeroList)
			else:
				HeroFlees(Counter)
				MaxCounter=len(HeroList)
		Counter=Counter+15
	return

def DoCraftItem():
	global LeatherAmount
	global BoneAmount
	global WoodAmount
	global IronAmount
	global SteelAmount
	pygame.key.set_repeat()
	MakingaChoice=True
	while MakingaChoice:
		Text1='Press category number or <enter> to exit...'
		Text1Surf = myfont.render(Text1, False, green)
		Text2='1> Weapons...'
		Text2Surf = myfont.render(Text2, False, green)

		Text3='2> Armor...'
		Text3Surf = myfont.render(Text3, False, green)

		Text4='3> Traps...'
		Text4Surf = myfont.render(Text4, False, green)

		Text5='4> Lifepotion... (3 bone, 2 wood)'
		if BoneAmount > 2 and WoodAmount > 1:
			color=green
		else:
			color=red
		Text5Surf = myfont.render(Text5, False, color)

		screen.blit(TextBar,(0,580))
		screen.blit(TextBar,(0,600))
		screen.blit(TextBar,(0,620))
		screen.blit(TextBar,(0,640))
		screen.blit(TextBar,(0,660))

		screen.blit(Text1Surf,(0,580))
		screen.blit(Text2Surf,(0,600))
		screen.blit(Text3Surf,(0,620))
		screen.blit(Text4Surf,(0,640))
		screen.blit(Text5Surf,(0,660))

		pygame.display.flip()

		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if (event.key == pygame.K_1 or event.key == pygame.K_KP1):
					DoCraftWeapon()
				if (event.key == pygame.K_2 or event.key == pygame.K_KP2):
					DoCraftArmor()
				if (event.key == pygame.K_3 or event.key == pygame.K_KP3):
					DoCraftTrap()
				if (event.key == pygame.K_4 or event.key == pygame.K_KP4) and BoneAmount > 2 and WoodAmount > 1:
					if len(InvList) < 10:
						BoneAmount=BoneAmount-3
						WoodAmount=WoodAmount-2
						InvList.append('Lifepotion')
						Tinkering.play()
				if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
					MakingaChoice=False
			DoScreen(Labyrinth, Level)
	pygame.key.set_repeat(30,50)
	return

def DoCraftWeapon():
	global LeatherAmount
	global BoneAmount
	global WoodAmount
	global IronAmount
	global SteelAmount
	pygame.key.set_repeat()
	DoScreen(Labyrinth, Level)
	MakingaChoice=True
	while MakingaChoice:
		Text1='Press weapon number to craft or <enter> to exit...'
		Text1Surf = myfont.render(Text1, False, green)
		Text2='1> Dagger (2 leather, 1 bone)'
		if LeatherAmount > 1 and BoneAmount > 0:
			color=green
		else:
			color=red
		Text2Surf = myfont.render(Text2, False, color)

		Text3='2> Mace (3 leather, 1 wood)'
		if LeatherAmount > 2 and WoodAmount > 0:
			color=green
		else:
			color=red
		Text3Surf = myfont.render(Text3, False, color)

		Text4='3> Sword (4 leather, 1 iron)'
		if LeatherAmount > 3 and IronAmount > 0:
			color=green
		else:
			color=red
		Text4Surf = myfont.render(Text4, False, color)

		Text5='4> Battleaxe (5 leather, 1 steel)'
		if LeatherAmount > 4 and SteelAmount > 0:
			color=green
		else:
			color=red
		Text5Surf = myfont.render(Text5, False, color)


		screen.blit(TextBar,(0,580))
		screen.blit(TextBar,(0,600))
		screen.blit(TextBar,(0,620))
		screen.blit(TextBar,(0,640))
		screen.blit(TextBar,(0,660))

		screen.blit(Text1Surf,(0,580))
		screen.blit(Text2Surf,(0,600))
		screen.blit(Text3Surf,(0,620))
		screen.blit(Text4Surf,(0,640))
		screen.blit(Text5Surf,(0,660))

		pygame.display.flip()

		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if (event.key == pygame.K_1 or event.key == pygame.K_KP1) and LeatherAmount > 1 and BoneAmount > 0:
					if len(InvList) < 10:
						LeatherAmount=LeatherAmount-2
						BoneAmount=BoneAmount-1
						InvList.append('Dagger')
						Tinkering.play()
				if (event.key == pygame.K_2 or event.key == pygame.K_KP2) and LeatherAmount > 2 and WoodAmount > 0:
					if len(InvList) < 10:
						LeatherAmount=LeatherAmount-3
						WoodAmount=WoodAmount-1
						InvList.append('Mace')
						Tinkering.play()
				if (event.key == pygame.K_3 or event.key == pygame.K_KP3) and LeatherAmount > 3 and IronAmount > 0:
					if len(InvList) < 10:
						LeatherAmount=LeatherAmount-4
						IronAmount=IronAmount-1
						InvList.append('Sword')
						Tinkering.play()
				if (event.key == pygame.K_4 or event.key == pygame.K_KP4) and LeatherAmount > 4 and SteelAmount > 0:
					if len(InvList) < 10:
						LeatherAmount=LeatherAmount-5
						SteelAmount=SteelAmount-1
						InvList.append('Battleaxe')
						Tinkering.play()
				if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
					return
			DoScreen(Labyrinth, Level)
	pygame.key.set_repeat(30,50)
	return

def DoCraftArmor():
	global LeatherAmount
	global BoneAmount
	global WoodAmount
	global IronAmount
	global SteelAmount
	pygame.key.set_repeat()
	DoScreen(Labyrinth, Level)
	MakingaChoice=True
	while MakingaChoice:
		Text1='Press armor number to craft or <enter> to exit...'
		Text1Surf = myfont.render(Text1, False, green)

		Text2='1> WShield (5 leather, 1 steel)'
		if LeatherAmount > 4 and SteelAmount > 0:
			color=green
		else:
			color=red
		Text2Surf = myfont.render(Text2, False, color)

		Text3='2> Shield (5 bone, 2 steel)'
		if BoneAmount > 4 and SteelAmount > 1:
			color=green
		else:
			color=red
		Text3Surf = myfont.render(Text3, False, color)

		Text4='3> TShield (5 wood, 3 steel)'
		if WoodAmount > 4 and SteelAmount > 2:
			color=green
		else:
			color=red
		Text4Surf = myfont.render(Text4, False, color)

		Text5='4> Chainmail (5 iron, 4 steel)'
		if SteelAmount > 3 and IronAmount > 4:
			color=green
		else:
			color=red
		Text5Surf = myfont.render(Text5, False, color)

		Text6='5> Plate (10 steel)'
		if SteelAmount > 9:
			color=green
		else:
			color=red
		Text6Surf = myfont.render(Text6, False, color)


		screen.blit(TextBar,(0,580))
		screen.blit(TextBar,(0,600))
		screen.blit(TextBar,(0,620))
		screen.blit(TextBar,(0,640))
		screen.blit(TextBar,(0,660))
		screen.blit(TextBar,(0,680))

		screen.blit(Text1Surf,(0,580))
		screen.blit(Text2Surf,(0,600))
		screen.blit(Text3Surf,(0,620))
		screen.blit(Text4Surf,(0,640))
		screen.blit(Text5Surf,(0,660))
		screen.blit(Text6Surf,(0,680))

		pygame.display.flip()

		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if (event.key == pygame.K_1 or event.key == pygame.K_KP1) and SteelAmount > 0 and LeatherAmount > 4:
					if len(InvList) < 10:
						SteelAmount=SteelAmount-1
						LeatherAmount=LeatherAmount-5
						InvList.append('WShield')
						Tinkering.play()
				if (event.key == pygame.K_2 or event.key == pygame.K_KP2) and SteelAmount > 1 and BoneAmount > 4:
					if len(InvList) < 10:
						SteelAmount=SteelAmount-2
						BoneAmount=BoneAmount-5
						InvList.append('Shield')
						Tinkering.play()
				if (event.key == pygame.K_3 or event.key == pygame.K_KP3) and SteelAmount > 2 and WoodAmount > 4:
					if len(InvList) < 10:
						SteelAmount=SteelAmount-3
						WoodAmount=WoodAmount-5
						InvList.append('TShield')
						Tinkering.play()
				if (event.key == pygame.K_4 or event.key == pygame.K_KP4) and SteelAmount > 3 and IronAmount > 4:
					if len(InvList) < 10:
						SteelAmount=SteelAmount-4
						IronAmount=IronAmount-5
						InvList.append('Chainmail')
						Tinkering.play()
				if (event.key == pygame.K_5 or event.key == pygame.K_KP5) and SteelAmount > 9:
					if len(InvList) < 10:
						SteelAmount=SteelAmount-10
						InvList.append('Plate')
						Tinkering.play()
				if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
					return
			DoScreen(Labyrinth, Level)
	pygame.key.set_repeat(30,50)
	return

def DoCraftTrap():
	global LeatherAmount
	global BoneAmount
	global WoodAmount
	global IronAmount
	global SteelAmount
	pygame.key.set_repeat()
	DoScreen(Labyrinth, Level)
	MakingaChoice=True
	while MakingaChoice:
		Text1='Press trap number to craft or <enter> to exit...'
		Text1Surf = myfont.render(Text1, False, green)
		Text2='1> Spiketrap (2 leather, 1 bone)'
		if LeatherAmount > 1 and BoneAmount > 0:
			color=green
		else:
			color=red
		Text2Surf = myfont.render(Text2, False, color)

		Text3='2> Beartrap (4 bone)'
		if BoneAmount > 3:
			color=green
		else:
			color=red
		Text3Surf = myfont.render(Text3, False, color)

		Text4='3> Acidtrap (3 bone, 2 wood)'
		if BoneAmount > 2 and WoodAmount > 1:
			color=green
		else:
			color=red
		Text4Surf = myfont.render(Text4, False, color)

		Text5='4> Electrotrap (4 bone, 2 iron)'
		if BoneAmount > 3 and IronAmount > 1:
			color=green
		else:
			color=red
		Text5Surf = myfont.render(Text5, False, color)

		Text6='5> Mine (5 bone, 2 steel)'
		if BoneAmount > 4 and SteelAmount > 1:
			color=green
		else:
			color=red
		Text6Surf = myfont.render(Text6, False, color)


		screen.blit(TextBar,(0,580))
		screen.blit(TextBar,(0,600))
		screen.blit(TextBar,(0,620))
		screen.blit(TextBar,(0,640))
		screen.blit(TextBar,(0,660))
		screen.blit(TextBar,(0,680))

		screen.blit(Text1Surf,(0,580))
		screen.blit(Text2Surf,(0,600))
		screen.blit(Text3Surf,(0,620))
		screen.blit(Text4Surf,(0,640))
		screen.blit(Text5Surf,(0,660))
		screen.blit(Text6Surf,(0,680))

		pygame.display.flip()

		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if (event.key == pygame.K_1 or event.key == pygame.K_KP1) and BoneAmount > 0 and LeatherAmount > 1:
					if len(InvList) < 10:
						BoneAmount=BoneAmount-1
						LeatherAmount=LeatherAmount-2
						InvList.append('Spiketrap')
						Tinkering.play()
				if (event.key == pygame.K_2 or event.key == pygame.K_KP2) and BoneAmount > 3:
					if len(InvList) < 10:
						BoneAmount=BoneAmount-3
						InvList.append('Beartrap')
						Tinkering.play()
				if (event.key == pygame.K_3 or event.key == pygame.K_KP3) and BoneAmount > 2 and WoodAmount > 1:
					if len(InvList) < 10:
						BoneAmount=BoneAmount-3
						WoodAmount=WoodAmount-2
						InvList.append('Acidtrap')
						Tinkering.play()
				if (event.key == pygame.K_4 or event.key == pygame.K_KP4) and BoneAmount > 3 and IronAmount > 1:
					if len(InvList) < 10:
						BoneAmount=BoneAmount-4
						IronAmount=IronAmount-2
						InvList.append('Electrotrap')
						Tinkering.play()
				if (event.key == pygame.K_5 or event.key == pygame.K_KP5) and BoneAmount > 4 and SteelAmount > 1:
					if len(InvList) < 10:
						BoneAmount=BoneAmount-5
						SteelAmount=SteelAmount-2
						InvList.append('Mine')
						Tinkering.play()
				if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
					return
			DoScreen(Labyrinth, Level)
	pygame.key.set_repeat(30,50)
	return

# Main loop
PlayerWeapon='Fists'
PlayerArmor='None'
Gold=0

PlayerAttack=2
PlayerDefence=2
PlayerLifeLevel=2
PlayerMagic=2
PlayerLife=PlayerLifeLevel*10
PlayerMana=PlayerMagic*5
LeatherAmount=0
BoneAmount=0
WoodAmount=0
IronAmount=0
SteelAmount=0
PlayerX=0
PlayerY=0
PlayerXP=0

PlayerLevel=PlayerAttack+PlayerDefence+PlayerLifeLevel+PlayerMagic

Spell='Fire'
SpellX=-200
SpellY=-200

Load=open('Zachno.sav', 'r')
LoadList=list(Load)
Load.close()

HeroList=list()
InvList=list()
pygame.key.set_repeat(30,50)
LoadFile=open('Zachno.sav', 'r')
LoadList=list(LoadFile)
LoadFile.close()

SaveSlot=DoSplash(LoadList)
Level=int(LoadList[SaveSlot+1])
ConSwitch=int(LoadList[SaveSlot])
if Level > 0:
	if ConSwitch==0:
		if Level > 0 and Level < LevelMax:
			PlayerWeapon=LoadList[SaveSlot+2].rstrip()
			PlayerArmor=LoadList[SaveSlot+3].rstrip()
			Gold=int(LoadList[SaveSlot+4])
			PlayerAttack=int(LoadList[SaveSlot+5])
			PlayerDefence=int(LoadList[SaveSlot+6])
			PlayerLifeLevel=int(LoadList[SaveSlot+7])
			PlayerMagic=int(LoadList[SaveSlot+8])
			PlayerLife=int(LoadList[SaveSlot+9])
			PlayerMana=int(LoadList[SaveSlot+10])
			PlayerXP=int(LoadList[SaveSlot+11])
			LeatherAmount=int(LoadList[SaveSlot+12])
			BoneAmount=int(LoadList[SaveSlot+13])
			WoodAmount=int(LoadList[SaveSlot+14])
			IronAmount=int(LoadList[SaveSlot+15])
			SteelAmount=int(LoadList[SaveSlot+16])
			PlayerX=0
			PlayerY=0
			PlayerLevel=PlayerAttack+PlayerDefence+PlayerLifeLevel+PlayerMagic
			MaxRooms=0
			Rooms=0
			if SaveSlot==0:
				LoadInv=open('Inventory1.sav', 'r')
			elif SaveSlot==19:
				LoadInv=open('Inventory2.sav', 'r')
			elif SaveSlot==38:
				LoadInv=open('Inventory3.sav', 'r')
			elif SaveSlot==57:
				LoadInv=open('Inventory4.sav', 'r')
			elif SaveSlot==76:
				LoadInv=open('Inventory5.sav', 'r')
			elif SaveSlot==95:
				LoadInv=open('Inventory6.sav', 'r')

			InvList=list(LoadInv)
			LoadInv.close()
			screen.blit(Loading,(0,0))
			pygame.display.flip()
			del Labyrinth[:]
			GenerateLabyrinth()
			CheckNextRoom(Labyrinth, RoomPos)
			PlaceStairs(Labyrinth)
			PlaceDecorations()
			PlaceGnome(Labyrinth)
			PlaceHeroes(Labyrinth, Level)
			Ping.play()
	else:
		del Labyrinth[:]
		PlayerWeapon=LoadList[SaveSlot+2].rstrip()
		PlayerArmor=LoadList[SaveSlot+3].rstrip()
		Gold=int(LoadList[SaveSlot+4])		
		PlayerAttack=int(LoadList[SaveSlot+5])
		PlayerDefence=int(LoadList[SaveSlot+6])
		PlayerLifeLevel=int(LoadList[SaveSlot+7])
		PlayerMagic=int(LoadList[SaveSlot+8])
		PlayerLife=int(LoadList[SaveSlot+9])
		PlayerMana=int(LoadList[SaveSlot+10])
		PlayerXP=int(LoadList[SaveSlot+11])
		LeatherAmount=int(LoadList[SaveSlot+12])
		BoneAmount=int(LoadList[SaveSlot+13])
		WoodAmount=int(LoadList[SaveSlot+14])
		IronAmount=int(LoadList[SaveSlot+15])
		SteelAmount=int(LoadList[SaveSlot+16])
		PlayerX=int(LoadList[SaveSlot+17])
		PlayerY=int(LoadList[SaveSlot+18])
		PlayerLevel=PlayerAttack+PlayerDefence+PlayerLifeLevel+PlayerMagic
		if SaveSlot==0:
			LoadInv=open('Inventory1.sav', 'r')
		elif SaveSlot==19:
			LoadInv=open('Inventory2.sav', 'r')
		elif SaveSlot==38:
			LoadInv=open('Inventory3.sav', 'r')
		elif SaveSlot==57:
			LoadInv=open('Inventory4.sav', 'r')
		elif SaveSlot==76:
			LoadInv=open('Inventory5.sav', 'r')
		elif SaveSlot==95:
			LoadInv=open('Inventory6.sav', 'r')

		InvList=list(LoadInv)
		LoadInv.close()
		if SaveSlot==0:
			LoadMap=open('MapState1.sav', 'r')
		elif SaveSlot==19:
			LoadMap=open('MapState2.sav', 'r')
		elif SaveSlot==38:
			LoadMap=open('MapState3.sav', 'r')
		elif SaveSlot==57:
			LoadMap=open('MapState4.sav', 'r')
		elif SaveSlot==76:
			LoadMap=open('MapState5.sav', 'r')
		elif SaveSlot==95:
			LoadMap=open('MapState6.sav', 'r')

		LabyrinthState=list(LoadMap)
		LoadMap.close()
		Counter=0
		maxCounter=len(LabyrinthState)
		while Counter < maxCounter:
			Object=str(LabyrinthState[Counter]).rstrip()
			ObjectX=int(LabyrinthState[Counter+1])
			ObjectY=int(LabyrinthState[Counter+2])
			if Object=='Stairs':
				StairsX=ObjectX
				StairsY=ObjectY
			Labyrinth.append(Object)
			Labyrinth.append(ObjectX)
			Labyrinth.append(ObjectY)
			Counter=Counter+3

		if SaveSlot==0:
			HeroLoad=open('HeroState1.sav', 'r')
		elif SaveSlot==19:
			HeroLoad=open('HeroState2.sav', 'r')
		elif SaveSlot==38:
			HeroLoad=open('HeroState3.sav', 'r')
		elif SaveSlot==57:
			HeroLoad=open('HeroState4.sav', 'r')
		elif SaveSlot==76:
			HeroLoad=open('HeroState5.sav', 'r')
		elif SaveSlot==95:
			HeroLoad=open('HeroState6.sav', 'r')

		HeroSave=list(HeroLoad)
		HeroLoad.close()
		HeroCounter=0
		HeroCounterMax=len(HeroSave)
		while HeroCounter < HeroCounterMax:
			HeroLevel=str(HeroSave[HeroCounter]).rstrip()
			HeroName=str(HeroSave[HeroCounter+1]).rstrip()
			HeroWeapon=str(HeroSave[HeroCounter+2]).rstrip()
			HeroArmor=str(HeroSave[HeroCounter+3]).rstrip()
			HeroSpell=str(HeroSave[HeroCounter+4]).rstrip()
			HeroAttack=int(HeroSave[HeroCounter+5])
			HeroDefence=int(HeroSave[HeroCounter+6])
			HeroLifeLevel=int(HeroSave[HeroCounter+7])
			HeroMagic=int(HeroSave[HeroCounter+8])
			HeroLife=int(HeroSave[HeroCounter+9])
			HeroMana=int(HeroSave[HeroCounter+10])
			HeroDropItemOne=str(HeroSave[HeroCounter+11]).rstrip()
			HeroDropItemTwo=str(HeroSave[HeroCounter+12]).rstrip()
			HeroX=int(HeroSave[HeroCounter+13])
			HeroY=int(HeroSave[HeroCounter+14])
			HeroList.append(HeroLevel)
			HeroList.append(HeroName)
			HeroList.append(HeroWeapon)
			HeroList.append(HeroArmor)
			HeroList.append(HeroSpell)
			HeroList.append(HeroAttack)
			HeroList.append(HeroDefence)
			HeroList.append(HeroLifeLevel)
			HeroList.append(HeroMagic)
			HeroList.append(HeroLife)
			HeroList.append(HeroMana)
			HeroList.append(HeroDropItemOne)
			HeroList.append(HeroDropItemTwo)
			HeroList.append(HeroX)
			HeroList.append(HeroY)
			HeroCounter=HeroCounter+15

while Level < LevelMax:
	DoScreen(Labyrinth, Level)
	Running=True
	Time.tic()
	EnemiesMoved=False
	Spacebar=True
	while Running:
		if EnemiesMoved:
			Time.tic()
			EnemiesMoved=False
		for event in pygame.event.get():
			if pygame.key.get_pressed()[pygame.K_SPACE]:
				if Spacebar:
					Spacebar=False
				else:
					Spacebar=True
#			if pygame.key.get_pressed()[pygame.K_RETURN]:
#				Spacebar=False
			if pygame.key.get_pressed()[pygame.K_UP] and Spacebar==False:
				Dir=8
				DoMovePlayer(PlayerX, PlayerY, Dir)
				PlayerX=PlayerPos[0]
				PlayerY=PlayerPos[1]
			if pygame.key.get_pressed()[pygame.K_RIGHT] and Spacebar==False:
				Dir=6
				DoMovePlayer(PlayerX, PlayerY, Dir)
				PlayerX=PlayerPos[0]
				PlayerY=PlayerPos[1]
			if pygame.key.get_pressed()[pygame.K_DOWN] and Spacebar==False:
				Dir=2
				DoMovePlayer(PlayerX, PlayerY, Dir)
				PlayerX=PlayerPos[0]
				PlayerY=PlayerPos[1]
			if pygame.key.get_pressed()[pygame.K_LEFT] and Spacebar==False:
				Dir=4
				DoMovePlayer(PlayerX, PlayerY, Dir)
				PlayerX=PlayerPos[0]
				PlayerY=PlayerPos[1]
			if (pygame.key.get_pressed()[pygame.K_1] or pygame.key.get_pressed()[pygame.K_KP1]) and len(InvList) > 0:
				ItemCounter=0
				DoItem(ItemCounter)
				Spacebar=False
			if (pygame.key.get_pressed()[pygame.K_2] or pygame.key.get_pressed()[pygame.K_KP2]) and len(InvList) > 1:
				ItemCounter=1
				DoItem(ItemCounter)
				Spacebar=False
			if (pygame.key.get_pressed()[pygame.K_3] or pygame.key.get_pressed()[pygame.K_KP3]) and len(InvList) > 2:
				ItemCounter=2
				DoItem(ItemCounter)
				Spacebar=False
			if (pygame.key.get_pressed()[pygame.K_4] or pygame.key.get_pressed()[pygame.K_KP4]) and len(InvList) > 3:
				ItemCounter=3
				DoItem(ItemCounter)
				Spacebar=False
			if (pygame.key.get_pressed()[pygame.K_5] or pygame.key.get_pressed()[pygame.K_KP5]) and len(InvList) > 4:
				ItemCounter=4
				DoItem(ItemCounter)
				Spacebar=False
			if (pygame.key.get_pressed()[pygame.K_6] or pygame.key.get_pressed()[pygame.K_KP6]) and len(InvList) > 5:
				ItemCounter=5
				DoItem(ItemCounter)
				Spacebar=False
			if (pygame.key.get_pressed()[pygame.K_7] or pygame.key.get_pressed()[pygame.K_KP7]) and len(InvList) > 6:
				ItemCounter=6
				DoItem(ItemCounter)
				Spacebar=False
			if (pygame.key.get_pressed()[pygame.K_8] or pygame.key.get_pressed()[pygame.K_KP8]) and len(InvList) > 7:
				ItemCounter=7
				DoItem(ItemCounter)
				Spacebar=False
			if (pygame.key.get_pressed()[pygame.K_9] or pygame.key.get_pressed()[pygame.K_KP9]) and len(InvList) > 8:
				ItemCounter=8
				DoItem(ItemCounter)
				Spacebar=False
			if (pygame.key.get_pressed()[pygame.K_0] or pygame.key.get_pressed()[pygame.K_KP0]) and len(InvList) > 9:
				ItemCounter=9
				DoItem(ItemCounter)
				Spacebar=False
			if pygame.key.get_pressed()[pygame.K_c] and len(InvList) < 10:
				DoCraftItem()
				Spacebar=False
			if pygame.key.get_pressed()[pygame.K_ESCAPE]:
				if Level > 0:
					pygame.key.set_repeat()
					screen.blit(Black,(0,0))
					screen.blit(Splash,(480,280))
					screen.blit(TextBar,(0,780))
					Text='Select a save slot to save current game, currently playing save slot '+str(int((SaveSlot+14)/14))+'...'
					LevelSave1=int(LoadList[1])
					LevelSave2=int(LoadList[20])
					LevelSave3=int(LoadList[39])
					LevelSave4=int(LoadList[58])
					LevelSave5=int(LoadList[77])
					LevelSave6=int(LoadList[96])

					SLevelSave1=str(LevelSave1)
					SLevelSave2=str(LevelSave2)
					SLevelSave3=str(LevelSave3)
					SLevelSave4=str(LevelSave4)
					SLevelSave5=str(LevelSave5)
					SLevelSave6=str(LevelSave6)

					if LevelSave1==0:
						Save1Status='Save slot 1, new game'
					else:
						Save1Status='Save slot 1, level: '+SLevelSave1
					if LevelSave2==0:
						Save2Status='Save slot 2, new game'
					else:
						Save2Status='Save slot 2, level: '+SLevelSave2
					if LevelSave3==0:
						Save3Status='Save slot 3, new game'
					else:
						Save3Status='Save slot 3, level: '+SLevelSave3
					if LevelSave4==0:
						Save4Status='Save slot 4, new game'
					else:
						Save4Status='Save slot 4, level: '+SLevelSave4
					if LevelSave5==0:
						Save5Status='Save slot 5, new game'
					else:
						Save5Status='Save slot 5, level: '+SLevelSave5
					if LevelSave6==0:
						Save6Status='Save slot 6, new game'
					else:
						Save6Status='Save slot 6, level: '+SLevelSave6

					Save1Text = myfont.render(Save1Status, False, green)
					Save2Text = myfont.render(Save2Status, False, green)
					Save3Text = myfont.render(Save3Status, False, green)
					Save4Text = myfont.render(Save4Status, False, green)
					Save5Text = myfont.render(Save5Status, False, green)
					Save6Text = myfont.render(Save6Status, False, green)
					Status = myfont.render('Select a save slot ...', False, yellow)

					screen.blit(Save1Text,(0,50))
					screen.blit(Save2Text,(0,100))
					screen.blit(Save3Text,(0,150))
					screen.blit(Save4Text,(0,200))
					screen.blit(Save5Text,(0,250))
					screen.blit(Save6Text,(0,300))
					TextSurf = myfont.render(Text, False, green)
					screen.blit(TextSurf,(0,0))
					pygame.display.flip()
	
					Selection=True
					while Selection:
						for event in pygame.event.get():
							if event.type == pygame.KEYDOWN:
								if event.key == pygame.K_KP1 or event.key == pygame.K_1:
									SaveSlot=0
									Selection=False
								if event.key == pygame.K_KP2 or event.key == pygame.K_2:
									SaveSlot=19
									Selection=False
								if event.key == pygame.K_KP3 or event.key == pygame.K_3:
									SaveSlot=38
									Selection=False
								if event.key == pygame.K_KP4 or event.key == pygame.K_4:
									SaveSlot=57
									Selection=False
								if event.key == pygame.K_KP5 or event.key == pygame.K_5:
									SaveSlot=76
									Selection=False
								if event.key == pygame.K_KP6 or event.key == pygame.K_6:
									SaveSlot=95
									Selection=False
					pygame.key.set_repeat(30,50)
																												
					MakingAChoice=True

					LoadList[SaveSlot]=1
					LoadList[SaveSlot+1]=Level
					LoadList[SaveSlot+2]=PlayerWeapon
					LoadList[SaveSlot+3]=PlayerArmor
					LoadList[SaveSlot+4]=Gold
					LoadList[SaveSlot+5]=PlayerAttack
					LoadList[SaveSlot+6]=PlayerDefence
					LoadList[SaveSlot+7]=PlayerLifeLevel
					LoadList[SaveSlot+8]=PlayerMagic
					LoadList[SaveSlot+9]=PlayerLife
					LoadList[SaveSlot+10]=PlayerMana
					LoadList[SaveSlot+11]=PlayerXP
					LoadList[SaveSlot+12]=LeatherAmount
					LoadList[SaveSlot+13]=BoneAmount
					LoadList[SaveSlot+14]=WoodAmount
					LoadList[SaveSlot+15]=IronAmount
					LoadList[SaveSlot+16]=SteelAmount
					LoadList[SaveSlot+17]=PlayerX
					LoadList[SaveSlot+18]=PlayerY
					os.system('rm Zachno.sav')
					Save=open('Zachno.sav', 'a')
					PlayerCounter=0
					MaxPlayerCounter=len(LoadList)
					while PlayerCounter < MaxPlayerCounter:
						SaveLine=str(LoadList[PlayerCounter]).rstrip()
						Save.write(SaveLine)
						if not PlayerCounter==MaxPlayerCounter-1:
							Save.write('\n')
						PlayerCounter=PlayerCounter+1
					Save.close()

					if SaveSlot==0:
						os.system('rm MapState1.sav')
						MapSave=open('MapState1.sav', 'a')
					elif SaveSlot==19:
						os.system('rm MapState2.sav')
						MapSave=open('MapState2.sav', 'a')
					elif SaveSlot==38:
						os.system('rm MapState3.sav')
						MapSave=open('MapState3.sav', 'a')
					elif SaveSlot==57:
						os.system('rm MapState4.sav')
						MapSave=open('MapState4.sav', 'a')
					elif SaveSlot==76:
						os.system('rm MapState5.sav')
						MapSave=open('MapState5.sav', 'a')
					elif SaveSlot==95:
						os.system('rm MapState6.sav')
						MapSave=open('MapState6.sav', 'a')

					LabCounter=0
					LabCounterMax=len(Labyrinth)
					while LabCounter < LabCounterMax:
						Object=str(Labyrinth[LabCounter])+'\n'
						ObjectX=str(Labyrinth[LabCounter+1])+'\n'
						ObjectY=str(Labyrinth[LabCounter+2])+'\n'
						MapSave.write(Object)
						MapSave.write(ObjectX)
						MapSave.write(ObjectY)
						LabCounter=LabCounter+3
					MapSave.close()

					if SaveSlot==0:
						os.system('rm HeroState1.sav')
						HeroSave=open('HeroState1.sav', 'a')
					elif SaveSlot==19:
						os.system('rm HeroState2.sav')
						HeroSave=open('HeroState2.sav', 'a')
					elif SaveSlot==38:
						os.system('rm HeroState3.sav')
						HeroSave=open('HeroState3.sav', 'a')
					elif SaveSlot==57:
						os.system('rm HeroState4.sav')
						HeroSave=open('HeroState4.sav', 'a')
					elif SaveSlot==76:
						os.system('rm HeroState5.sav')
						HeroSave=open('HeroState5.sav', 'a')
					elif SaveSlot==95:
						os.system('rm HeroState6.sav')
						HeroSave=open('HeroState6.sav', 'a')

					HeroCounter=0
					HeroCounterMax=len(HeroList)
					while HeroCounter < HeroCounterMax:
						HeroLevel=str(HeroList[HeroCounter])+'\n'
						HeroName=str(HeroList[HeroCounter+1])+'\n'
						HeroWeapon=str(HeroList[HeroCounter+2])+'\n'
						HeroArmor=str(HeroList[HeroCounter+3])+'\n'
						HeroSpell=str(HeroList[HeroCounter+4])+'\n'
						HeroAttack=str(HeroList[HeroCounter+5])+'\n'
						HeroDefence=str(HeroList[HeroCounter+6])+'\n'
						HeroLifeLevel=str(HeroList[HeroCounter+7])+'\n'
						HeroMagic=str(HeroList[HeroCounter+8])+'\n'
						HeroLife=str(HeroList[HeroCounter+9])+'\n'
						HeroMana=str(HeroList[HeroCounter+10])+'\n'
						HeroDropItemOne=str(HeroList[HeroCounter+11])+'\n'
						HeroDropItemTwo=str(HeroList[HeroCounter+12])+'\n'
						HeroX=str(HeroList[HeroCounter+13])+'\n'
						HeroY=str(HeroList[HeroCounter+14])
						HeroSave.write(HeroLevel)
						HeroSave.write(HeroName)
						HeroSave.write(HeroWeapon)
						HeroSave.write(HeroArmor)
						HeroSave.write(HeroSpell)
						HeroSave.write(HeroAttack)
						HeroSave.write(HeroDefence)
						HeroSave.write(HeroLifeLevel)
						HeroSave.write(HeroMagic)
						HeroSave.write(HeroLife)
						HeroSave.write(HeroMana)
						HeroSave.write(HeroDropItemOne)
						HeroSave.write(HeroDropItemTwo)
						HeroSave.write(HeroX)
						HeroSave.write(HeroY)
						if not HeroCounter==HeroCounterMax-1:
							HeroSave.write('\n')
						HeroCounter=HeroCounter+15
					HeroSave.close()

					if SaveSlot==0:
						os.system('rm Inventory1.sav')
						InvSave=open('Inventory1.sav', 'a')
					elif SaveSlot==19:
						os.system('rm Inventory2.sav')
						InvSave=open('Inventory2.sav', 'a')
					elif SaveSlot==38:
						os.system('rm Inventory3.sav')
						InvSave=open('Inventory3.sav', 'a')
					elif SaveSlot==57:
						os.system('rm Inventory4.sav')
						InvSave=open('Inventory4.sav', 'a')
					elif SaveSlot==76:
						os.system('rm Inventory5.sav')
						InvSave=open('Inventory5.sav', 'a')
					elif SaveSlot==95:
						os.system('rm Inventory6.sav')
						InvSave=open('Inventory6.sav', 'a')

					InvCounter=0
					InvCounterMax=len(InvList)
					while InvCounter < InvCounterMax:
						Object=str(InvList[InvCounter]).rstrip()
						InvSave.write(Object)
						if not InvCounter==InvCounterMax-1:
							InvSave.write('\n')
						InvCounter=InvCounter+1
					InvSave.close()
					DoExit()

		DoScreen(Labyrinth, Level)
		SpellX=-200
		SpellY=-200
		PlayerLevel=PlayerAttack+PlayerDefence+PlayerLifeLevel+PlayerMagic
		if PlayerLevel < 61:
			if PlayerXP >= PlayerLevel*2:
				DoLevelUp()

		SpentTime=Time.tocvalue()
		if SpentTime > 0.65 and Spacebar==False:
			DoEnemies()
			EnemiesMoved=True
			
		if NextLevel:
			PlayerX=0
			PlayerY=0
			Level=Level+1
			if Level < LevelMax:
				LoadList[SaveSlot]=0
				LoadList[SaveSlot+1]=Level
				LoadList[SaveSlot+2]=PlayerWeapon
				LoadList[SaveSlot+3]=PlayerArmor
				LoadList[SaveSlot+4]=Gold
				LoadList[SaveSlot+5]=PlayerAttack
				LoadList[SaveSlot+6]=PlayerDefence
				LoadList[SaveSlot+7]=PlayerLifeLevel
				LoadList[SaveSlot+8]=PlayerMagic
				LoadList[SaveSlot+9]=PlayerLife
				LoadList[SaveSlot+10]=PlayerMana
				LoadList[SaveSlot+11]=PlayerXP
				LoadList[SaveSlot+12]=LeatherAmount
				LoadList[SaveSlot+13]=BoneAmount
				LoadList[SaveSlot+14]=WoodAmount
				LoadList[SaveSlot+15]=IronAmount
				LoadList[SaveSlot+16]=SteelAmount
				LoadList[SaveSlot+17]=0
				LoadList[SaveSlot+18]=0
				os.system('rm Zachno.sav')
				Save=open('Zachno.sav', 'a')
				PlayerCounter=0
				MaxPlayerCounter=len(LoadList)
				while PlayerCounter < MaxPlayerCounter:
					SaveLine=str(LoadList[PlayerCounter]).rstrip()
					Save.write(SaveLine)
					if not PlayerCounter==MaxPlayerCounter-1:
						Save.write('\n')
					PlayerCounter=PlayerCounter+1
				Save.close()
		
				if SaveSlot==0:
					os.system('rm Inventory1.sav')
					InvSave=open('Inventory1.sav', 'a')
				elif SaveSlot==19:
					os.system('rm Inventory2.sav')
					InvSave=open('Inventory2.sav', 'a')
				elif SaveSlot==38:
					os.system('rm Inventory3.sav')
					InvSave=open('Inventory3.sav', 'a')
				elif SaveSlot==57:
					os.system('rm Inventory4.sav')
					InvSave=open('Inventory4.sav', 'a')
				elif SaveSlot==76:
					os.system('rm Inventory5.sav')
					InvSave=open('Inventory5.sav', 'a')
				elif SaveSlot==95:
					os.system('rm Inventory6.sav')
					InvSave=open('Inventory6.sav', 'a')

				InvCounter=0
				InvCounterMax=len(InvList)
				while InvCounter < InvCounterMax:
					Object=str(InvList[InvCounter]).rstrip()
					InvSave.write(Object)
					if not InvCounter==InvCounterMax-1:
						InvSave.write('\n')
					InvCounter=InvCounter+1
				InvSave.close()
				LoadingText='Continue to next level? [y/n]...'
				LoadingTextSurf = myfont.render(LoadingText, False, green)
	
				screen.blit(TextBar,(0,370))
				screen.blit(TextBar,(0,390))
				screen.blit(TextBar,(0,410))
		
				screen.blit(LoadingTextSurf,(0,390))
				pygame.display.flip()
				MakingAChoice=True
				while MakingAChoice:
					for event in pygame.event.get():
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_y:
								MakingAChoice=False
							if event.key == pygame.K_n:
								DoExit()
								sys.exit()

				LoadingText='Cooking level '+str(Level)+'...'
				LoadingTextSurf = myfont.render(LoadingText, False, green)
				screen.blit(Black,(0,0))
				screen.blit(Loading,(0,0))
				screen.blit(LoadingTextSurf,(0,780))
				pygame.display.flip()
				NextLevel=False
				Running=False
			else:
				DoVictory()

			if Level < LevelMax:
				Rooms=0
				MaxRooms=0
				del Labyrinth[:]
				GenerateLabyrinth()
				CheckNextRoom(Labyrinth, RoomPos)
				PlaceStairs(Labyrinth)
				PlaceDecorations()
				PlaceGnome(Labyrinth)
				PlaceHeroes(Labyrinth, Level)
				Ping.play()
			else:
				DoVictory()

wait()
sys.exit()
