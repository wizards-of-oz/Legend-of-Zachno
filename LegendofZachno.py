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

# Loading picture files into RAM
Black=pygame.image.load('Black.png')
Loading=pygame.image.load('Loading.png')
Floor=pygame.image.load('newFloor.PNG')
Stairs=pygame.image.load('newStairs.PNG')
Wall=pygame.image.load('newWall.PNG')
Player=pygame.image.load('newMonster.PNG')
TextBar=pygame.image.load('TextBar.png')
Splash=pygame.image.load('Splash.png')
Candle=pygame.image.load('Candle.png')
Lantern=pygame.image.load('Lantern.png')
Rubble=pygame.image.load('Rubble.png')
Skull=pygame.image.load('Skull.png')
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

Bully=pygame.image.load('Bully.png')
Peasant=pygame.image.load('Peasant.png')
Soldier=pygame.image.load('Soldier.png')
Trapper=pygame.image.load('Trapper.png')
Apprentice=pygame.image.load('Apprentice.png')
Battlemage=pygame.image.load('Battlemage.png')
Knight=pygame.image.load('Knight.png')
Warlock=pygame.image.load('Warlock.png')
Strongman=pygame.image.load('Strongman.png')
Heavy=pygame.image.load('Heavy.png')
Spacewizard=pygame.image.load('Spacewizard.png')
Tank=pygame.image.load('Tank.png')
Spacemage=pygame.image.load('Spacemage.png')
Heavyguard=pygame.image.load('Heavyguard.png')
Vampirehero=pygame.image.load('Vampirehero.png')
Lightningmage=pygame.image.load('Lightningmage.png')
Stormking=pygame.image.load('Stormking.png')
Berserker=pygame.image.load('Berserker.png')
Rogue=pygame.image.load('Rogue.png')
Paladin=pygame.image.load('Paladin.png')
Archmage=pygame.image.load('Archmage.png')
KingArthur=pygame.image.load('KingArthur.png')


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
	elif ObjectImage=='Lantern':
		ScreenItem=Lantern
	elif ObjectImage=='Rubble':
		ScreenItem=Rubble
	elif ObjectImage=='Skull':
		ScreenItem=Skull
	elif ObjectImage=='Shield':
		ScreenItem=Shield
	elif ObjectImage=='Candle':
		ScreenItem=Candle
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
	elif ObjectImage=='Bully':
		ScreenItem=Bully
	elif ObjectImage=='Peasant':
		ScreenItem=Peasant
	elif ObjectImage=='Soldier':
		ScreenItem=Soldier
	elif ObjectImage=='Trapper':
		ScreenItem=Trapper
	elif ObjectImage=='Apprentice':
		ScreenItem=Apprentice
	elif ObjectImage=='Battlemage':
		ScreenItem=Battlemage
	elif ObjectImage=='Knight':
		ScreenItem=Knight
	elif ObjectImage=='Warlock':
		ScreenItem=Warlock
	elif ObjectImage=='Strongman':
		ScreenItem=Strongman
	elif ObjectImage=='Heavy':
		ScreenItem=Heavy
	elif ObjectImage=='Spacewizard':
		ScreenItem=Spacewizard
	elif ObjectImage=='Tank':
		ScreenItem=Tank
	elif ObjectImage=='Spacemage':
		ScreenItem=Spacemage
	elif ObjectImage=='Heavyguard':
		ScreenItem=Heavyguard
	elif ObjectImage=='Vampirehero':
		ScreenItem=Vampirehero
	elif ObjectImage=='Lightningmage':
		ScreenItem=Lightningmage
	elif ObjectImage=='Stormking':
		ScreenItem=Stormking
	elif ObjectImage=='Berserker':
		ScreenItem=Berserker
	elif ObjectImage=='Rogue':
		ScreenItem=Rogue
	elif ObjectImage=='Paladin':
		ScreenItem=Paladin
	elif ObjectImage=='Archmage':
		ScreenItem=Archmage
	elif ObjectImage=='KingArthur':
		ScreenItem=KingArthur
	return(ScreenItem)

def DoInventoryList():
	if len(InvList) > 0:
		ItemText='1> '+InvList[0].rstrip()
		ItemTextSurf=myfont.render(ItemText, False, red)		
		screen.blit(ItemTextSurf,(950,200))
	if len(InvList) > 1:
		ItemText='2> '+InvList[1].rstrip()
		ItemTextSurf=myfont.render(ItemText, False, red)		
		screen.blit(ItemTextSurf,(950,220))
	if len(InvList) > 2:
		ItemText='3> '+InvList[2].rstrip()
		ItemTextSurf=myfont.render(ItemText, False, red)		
		screen.blit(ItemTextSurf,(950,240))
	if len(InvList) > 3:
		ItemText='4> '+InvList[3].rstrip()
		ItemTextSurf=myfont.render(ItemText, False, red)		
		screen.blit(ItemTextSurf,(950,260))
	if len(InvList) > 4:
		ItemText='5> '+InvList[4].rstrip()
		ItemTextSurf=myfont.render(ItemText, False, red)		
		screen.blit(ItemTextSurf,(950,280))
	if len(InvList) > 5:
		ItemText='6> '+InvList[5].rstrip()
		ItemTextSurf=myfont.render(ItemText, False, red)		
		screen.blit(ItemTextSurf,(950,300))
	if len(InvList) > 6:
		ItemText='7> '+InvList[6].rstrip()
		ItemTextSurf=myfont.render(ItemText, False, red)		
		screen.blit(ItemTextSurf,(950,320))
	if len(InvList) > 7:
		ItemText='8> '+InvList[7].rstrip()
		ItemTextSurf=myfont.render(ItemText, False, red)		
		screen.blit(ItemTextSurf,(950,340))
	if len(InvList) > 8:
		ItemText='9> '+InvList[8].rstrip()
		ItemTextSurf=myfont.render(ItemText, False, red)		
		screen.blit(ItemTextSurf,(950,360))
	if len(InvList) > 9:
		ItemText='0> '+InvList[9].rstrip()
		ItemTextSurf=myfont.render(ItemText, False, red)		
		screen.blit(ItemTextSurf,(950,380))
	return

def HeroScan(Labyrinth, HeroList):
	del HeroLifeList[:]
	MaxCounter=len(HeroList)
	Counter=0
	while Counter<MaxCounter:
		HeroName=str(HeroList[Counter+1])
		HeroLife=int(HeroList[Counter+9])
		ObjectX=int(HeroList[Counter+13])
		ObjectY=int(HeroList[Counter+14])
		XDiff=ObjectX-PlayerX
		YDiff=ObjectY-PlayerY
		if (-7 <= XDiff) and ( XDiff <= 7) and (-5 <= YDiff) and (YDiff <= 4):
			HeroLifeList.append(HeroName)
			HeroLifeList.append(HeroLife)
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

	Counter=0
	MaxCounter=len(HeroLifeList)
	while Counter < MaxCounter:
		HeroName=str(HeroLifeList[Counter])
		HeroLife=str(HeroLifeList[Counter+1])
		ObjectX=int(HeroLifeList[Counter+2])
		ObjectY=int(HeroLifeList[Counter+3])
		# calling GetScreenItem to get the right picture with the object name
		HeroLifeText=str(HeroName)+':'+str(HeroLife)
		HeroLifeTextSurf=myfont.render(HeroLifeText, False, green)
		# Translating x and y coordinates from VisualList into actual pixel coordinatesd
		ScreenX=(ObjectX+7)*80
		YConvert=ObjectY*-1
		ScreenY=((YConvert+4)*80)+60
		# Placing the item on screen
		screen.blit(HeroLifeTextSurf, (ScreenX, ScreenY))
		Counter=Counter+4

	

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
		Att='+2'
	elif PlayerWeapon=='Mace':
		Att='+3'
	elif PlayerWeapon=='Sword':
		Att='+4'
	elif PlayerWeapon=='Battleaxe':
		Att='+5'

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
	PlayerLifeNo=str(PlayerLife)
	PlayerManaNo=str(PlayerMana)

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
	screen.blit(LevelTextSurf,(0,0))
	screen.blit(PlayerPosTextSurf,(0,20))
	screen.blit(LabyrinthTextSurf,(0,40))
	screen.blit(GoldTextSurf,(0,60))
	#screen.blit(StairsPosTextSurf,(0,20))
	# Placing the player picture in the middle of the screen

	screen.blit(Player, (560, 320))
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
				if event.key == pygame.K_1 and len(InvList) < 10:
					if Gold >= 12:
						Gold=Gold-12
						InvList.append('Lifepotion')
				if event.key == pygame.K_2 and len(InvList) < 10:
					if Gold >= 16:
						Gold=Gold-16
						InvList.append('Manapotion')
				if event.key == pygame.K_3 and len(InvList) < 10:
					if Gold >= 10:
						Gold=Gold-10
						InvList.append('Fire')
				if event.key == pygame.K_4 and len(InvList) < 10:
					if Gold >= 12:
						Gold=Gold-12
						InvList.append('Teleport')
				if event.key == pygame.K_5 and len(InvList) < 10:
					if Gold >= 14:
						Gold=Gold-14
						InvList.append('Drain')
				if event.key == pygame.K_6 and len(InvList) < 10:
					if Gold >= 16:
						Gold=Gold-16
						InvList.append('Lightning')
				if event.key == pygame.K_7 and len(InvList) < 10:
					if Gold >= 18:
						Gold=Gold-18
						InvList.append('Fireball')
				if event.key == pygame.K_RETURN:
					MakingaChoice=False
		DoScreen(Labyrinth, Level)
	pygame.key.set_repeat(30,30)

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
				if event.key == pygame.K_1 and len(InvList) > 0:
					ItemCounter=0
					GetGold(ItemCounter)
				if event.key == pygame.K_2 and len(InvList) > 1:
					ItemCounter=1
					GetGold(ItemCounter)
				if event.key == pygame.K_3 and len(InvList) > 2:
					ItemCounter=2
					GetGold(ItemCounter)
				if event.key == pygame.K_4 and len(InvList) > 3:
					ItemCounter=3
					GetGold(ItemCounter)
				if event.key == pygame.K_5 and len(InvList) > 4:
					ItemCounter=4
					GetGold(ItemCounter)
				if event.key == pygame.K_6 and len(InvList) > 5:
					ItemCounter=5
					GetGold(ItemCounter)
				if event.key == pygame.K_7 and len(InvList) > 6:
					ItemCounter=6
					GetGold(ItemCounter)
				if event.key == pygame.K_8 and len(InvList) > 7:
					ItemCounter=7
					GetGold(ItemCounter)
				if event.key == pygame.K_9 and len(InvList) > 8:
					ItemCounter=8
					GetGold(ItemCounter)
				if event.key == pygame.K_0 and len(InvList) > 9:
					ItemCounter=9
					GetGold(ItemCounter)
				if event.key == pygame.K_RETURN:
					MakingaChoice=False
			DoScreen(Labyrinth, Level)
	pygame.key.set_repeat(30,30)
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
				if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
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

	if HeroArmor=='WShield':
		HeroDefence=HeroDefence+1
	elif HeroArmor=='Shield':
		HeroDefence=HeroDefence+2
	elif HeroArmor=='TShield':
		HeroDefence=HeroDefence+3
	elif HeroArmor=='Chainmail':
		HeroDefence=HeroDefence+4
	elif HeroArmor=='Plate':
		HeroDefence=HeroDefence+5

	ZachnoAttack=PlayerAttack
	if PlayerWeapon=='Fists':
		ZachnoAttack=PlayerAttack+1
	elif PlayerWeapon=='Dagger':
		ZachnoAttack=PlayerAttack+2
	elif PlayerWeapon=='Mace':
		ZachnoAttack=PlayerAttack+3
	elif PlayerWeapon=='Sword':
		ZachnoAttack=PlayerAttack+4
	elif PlayerWeapon=='Battleaxe':
		ZachnoAttack=PlayerAttack+5

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
	NumberofGnomes=int(Level/4)
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
	LoadingText='Placing decorations...'
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
		LoadingText='Placing decoration '+str(DecMin)+' of '+str(DecMax)+'...'
		LoadingTextSurf = myfont.render(LoadingText, False, green)
		screen.blit(TextBar,(0,780))
		screen.blit(LoadingTextSurf,(0,780))
		pygame.display.flip()
		DecNo=random.randint(1,5)
		if DecNo==1:
			Decoration='Candle'
		if DecNo==2:
			Decoration='Lantern'
		if DecNo==3:
			Decoration='Rubble'
		if DecNo==4:
			Decoration='Skull'
		if DecNo==5:
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

def DoSplash():
	screen.blit(Black,(0,0))
	screen.blit(Splash,(480,280))
	screen.blit(TextBar,(0,780))
	Text='Entering level '+str(Level)+'...'
	TextSurf = myfont.render(Text, False, green)
	LoadingText='Welcome to Legend of Zachno, press enter...'
	LoadingTextSurf = myfont.render(LoadingText, False, green)
	screen.blit(TextSurf,(0,0))
	screen.blit(LoadingTextSurf,(0,780))
	pygame.display.flip()
	wait()
	return

def DoExit():
	screen.blit(Black,(0,0))
	screen.blit(Splash,(480,280))
	screen.blit(TextBar,(0,780))
	LoadingText='Game state saved next session will be in level '+str(Level)+' , press enter...'
	LoadingTextSurf = myfont.render(LoadingText, False, green)
	screen.blit(LoadingTextSurf,(0,780))
	pygame.display.flip()
	wait()
	return

def DoVictory():
	screen.blit(Black,(0,0))
	screen.blit(Splash,(480,280))
	screen.blit(TextBar,(0,780))
	LoadingText='Congratulations on beating Legend of Zachno, keep current save (k) or reset save (r)...'
	LoadingTextSurf = myfont.render(LoadingText, False, green)
	screen.blit(LoadingTextSurf,(0,780))
	pygame.display.flip()
	MakingAChoice=True
	while MakingAChoice:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_k:
					os.system('rm Zachno.sav')
					Save=open('Zachno.sav', 'a')
					LevelSave='20\n'
					Save.write('0\n')
					Save.write(LevelSave)
					AttackSave=str(PlayerAttack)+'\n'
					DefenceSave=str(PlayerDefence)+'\n'
					HealthSave=str(PlayerLifeLevel)+'\n'
					MagicSave=str(PlayerMagic)+'\n'
					LifeSave=str(PlayerLife)+'\n'
					ManaSave=str(PlayerMana)+'\n'
					Save.write(AttackSave)
					Save.write(DefenceSave)
					Save.write(HealthSave)
					Save.write(MagicSave)
					Save.write(LifeSave)
					Save.write(ManaSave)
					Save.write('0\n')
					Save.write('0')
					Save.close()
					sys.exit()
				if event.key == pygame.K_r:
					os.system('rm Zachno.sav')
					Save=open('Zachno.sav', 'a')
					Save.write('0\n')
					Save.write('0\n')
					Save.write('1\n')
					Save.write('1\n')
					Save.write('1\n')
					Save.write('1\n')
					Save.write('10\n')
					Save.write('10\n')
					Save.write('0\n')
					Save.write('0')
					Save.close()
					sys.exit()
	wait()
	return

def DoItem(ItemCounter):
	Item=InvList[ItemCounter].rstrip()
	ChestText='Use '+Item+' <u> or drop '+Item+' <d>...'
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
				if event.key == pygame.K_u:
					UseItem(ItemCounter)
					MakingAChoice=False
				if event.key == pygame.K_d:
					DropItem(ItemCounter)
					MakingAChoice=False

	return

def DoSpell():
	global PlayerX
	global PlayerY
	global PlayerLifeLevel
	global PlayerLife
	global PlayerXP
	global Spell
	global SpellX
	global SpellY
	global HeroList
	DoScreen(Labyrinth, Level)
	MapGen=int(Level/2)+1
	SpellText='Press direction for '+Spell+' spell...'
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
						HeroAttack=HeroAttack-1
						if HeroAttack < 0:
							HeroAttack=0
						HeroLife=HeroLife-4
					if Spell=='Teleport':
						HeroDefence=HeroDefence-2
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
						HeroMana=HeroMana-4
					if Spell=='Fireball':
						Fireball.play()
						HeroLife=HeroLife-20

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
	if InvList[ItemCounter].rstrip()=='Mace':
		PlayerWeapon='Mace'
		del InvList[ItemCounter]
	elif InvList[ItemCounter].rstrip()=='Dagger':
		PlayerWeapon='Dagger'
		del InvList[ItemCounter]
	elif InvList[ItemCounter].rstrip()=='Sword':
		PlayerWeapon='Sword'
		del InvList[ItemCounter]
	elif InvList[ItemCounter].rstrip()=='Battleaxe':
		PlayerWeapon='Battleaxe'
		del InvList[ItemCounter]
	elif InvList[ItemCounter].rstrip()=='Shield':
		PlayerArmor='Shield'
		del InvList[ItemCounter]
	elif InvList[ItemCounter].rstrip()=='WShield':
		PlayerArmor='WShield'
		del InvList[ItemCounter]
	elif InvList[ItemCounter].rstrip()=='TShield':
		PlayerArmor='TShield'
		del InvList[ItemCounter]
	elif InvList[ItemCounter].rstrip()=='Chainmail':
		PlayerArmor='Chainmail'
		del InvList[ItemCounter]
	elif InvList[ItemCounter].rstrip()=='Plate':
		PlayerArmor='Plate'
		del InvList[ItemCounter]
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
	elif InvList[ItemCounter].rstrip()=='Fire':
		if PlayerMana >= 1:
			PlayerMana=PlayerMana-1
			Spell='Fire'
			DoSpell()
			del InvList[ItemCounter]
		else:
			Fail.play()
	elif InvList[ItemCounter].rstrip()=='Teleport':
		if PlayerMana >= 2:
			PlayerMana=PlayerMana-2
			Spell='Teleport'
			DoSpell()
			del InvList[ItemCounter]
		else:
			Fail.play()
	elif InvList[ItemCounter].rstrip()=='Drain':
		if PlayerMana >= 3:
			PlayerMana=PlayerMana-3
			Spell='Drain'
			DoSpell()
			del InvList[ItemCounter]
		else:
			Fail.play()
	elif InvList[ItemCounter].rstrip()=='Lightning':
		if PlayerMana >= 4:
			PlayerMana=PlayerMana-4
			Spell='Lightning'
			DoSpell()
			del InvList[ItemCounter]
		else:
			Fail.play()
	elif InvList[ItemCounter].rstrip()=='Fireball':
		if PlayerMana >= 5:
			PlayerMana=PlayerMana-5
			Spell='Fireball'
			DoSpell()
			del InvList[ItemCounter]
		else:
			Fail.play()
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
		Object='Shield'
	if InvList[ItemCounter].rstrip()=='TShield':
		Object='Shield'
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
				if event.key == pygame.K_1:
					PlayerAttack=PlayerAttack+1
					PlayerXP=PlayerXP-(PlayerLevel*2)
					MakingaChoice=False
				if event.key == pygame.K_2:
					PlayerDefence=PlayerDefence+1
					PlayerXP=PlayerXP-(PlayerLevel*2)
					MakingaChoice=False
				if event.key == pygame.K_3:
					PlayerLifeLevel=PlayerLifeLevel+1
					PlayerLife=PlayerLifeLevel*10
					PlayerXP=PlayerXP-(PlayerLevel*2)
					MakingaChoice=False
				if event.key == pygame.K_4:
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

	if HeroWeapon=='Fists':
		HeroAt=HeroAttack+1
	elif HeroWeapon=='Dagger':
		HeroAt=HeroAttack+2
	elif HeroWeapon=='Mace':
		HeroAt=HeroAttack+3
	elif HeroWeapon=='Sword':
		HeroAt=HeroAttack+4
	elif HeroWeapon=='Battleaxe':
		HeroAt=HeroAttack+5

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
	else:
		Bump.play()


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
					HeroAttack=HeroAttack-1
					if HeroAttack < 0:
						HeroAttack=0
					HeroLife=HeroLife-2
					SpellX=NewHeroX
					SpellY=NewHeroY
					Spell='BloodSpatter'
					Spikes.play()
				if Object=='BearTrap':
					del Labyrinth[LabNum]
					del Labyrinth[LabNum]
					del Labyrinth[LabNum]
					LabNumMax=len(Labyrinth)
					HeroDefence=HeroDefence-2
					if HeroDefence < 0:
						HeroDefence=0
					HeroLife=HeroLife-4
					SpellX=NewHeroX
					SpellY=NewHeroY
					Spell='BloodSpatter'
					Trap.play()
				if Object=='AcidTrap':
					del Labyrinth[LabNum]
					del Labyrinth[LabNum]
					del Labyrinth[LabNum]
					LabNumMax=len(Labyrinth)
					HeroLife=HeroLife-6
					SpellX=NewHeroX
					SpellY=NewHeroY
					Spell='AcidPuddle'
					Sizzle.play()
				if Object=='ElectroTrap':
					del Labyrinth[LabNum]
					del Labyrinth[LabNum]
					del Labyrinth[LabNum]
					LabNumMax=len(Labyrinth)
					HeroMana=HeroMana-4
					HeroLife=HeroLife-8
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
					HeroMagic=HeroMagic-5
					HeroLife=HeroLife-10
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
PlayerX=0
PlayerY=0
PlayerXP=0

PlayerLevel=PlayerAttack+PlayerDefence+PlayerMagic

Spell='Fire'
SpellX=-200
SpellY=-200

Load=open('Zachno.sav', 'r')
LoadList=list(Load)
Load.close()

LoadCounter=0
LoadCounterMax=len(LoadList)
ConSwitch=int(LoadList[0])
Level=int(LoadList[1])

HeroList=list()
InvList=list()
pygame.key.set_repeat(30,30)
DoSplash()
if Level > 0:
	if ConSwitch==0:
		if Level > 0 and Level < LevelMax:
			PlayerWeapon=LoadList[2].rstrip()
			PlayerArmor=LoadList[3].rstrip()
			Gold=int(LoadList[4])
			PlayerAttack=int(LoadList[5])
			PlayerDefence=int(LoadList[6])
			PlayerLifeLevel=int(LoadList[7])
			PlayerMagic=int(LoadList[8])
			PlayerLife=int(LoadList[9])
			PlayerMana=int(LoadList[10])
			PlayerXP=int(LoadList[11])
			PlayerX=0
			PlayerY=0
			PlayerLevel=PlayerAttack+PlayerDefence+PlayerMagic
			MaxRooms=0
			Rooms=0
			LoadInv=open('Inventory.sav', 'r')
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
		PlayerWeapon=LoadList[2].rstrip()
		PlayerArmor=LoadList[3].rstrip()
		Gold=int(LoadList[4])		
		PlayerAttack=int(LoadList[5])
		PlayerDefence=int(LoadList[6])
		PlayerLifeLevel=int(LoadList[7])
		PlayerMagic=int(LoadList[8])
		PlayerLife=int(LoadList[9])
		PlayerMana=int(LoadList[10])
		PlayerXP=int(LoadList[11])
		PlayerX=int(LoadList[12])
		PlayerY=int(LoadList[13])
		PlayerLevel=PlayerAttack+PlayerDefence+PlayerMagic
		LoadInv=open('Inventory.sav', 'r')
		InvList=list(LoadInv)
		LoadInv.close()
		LoadMap=open('MapState.sav', 'r')
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
		HeroLoad=open('HeroState.sav', 'r')
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
	Spacebar=False
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
			if pygame.key.get_pressed()[pygame.K_1] and len(InvList) > 0:
				ItemCounter=0
				DoItem(ItemCounter)
				Spacebar=False
			if pygame.key.get_pressed()[pygame.K_2] and len(InvList) > 1:
				ItemCounter=1
				DoItem(ItemCounter)
				Spacebar=False
			if pygame.key.get_pressed()[pygame.K_3] and len(InvList) > 2:
				ItemCounter=2
				DoItem(ItemCounter)
				Spacebar=False
			if pygame.key.get_pressed()[pygame.K_4] and len(InvList) > 3:
				ItemCounter=3
				DoItem(ItemCounter)
				Spacebar=False
			if pygame.key.get_pressed()[pygame.K_5] and len(InvList) > 4:
				ItemCounter=4
				DoItem(ItemCounter)
				Spacebar=False
			if pygame.key.get_pressed()[pygame.K_6] and len(InvList) > 5:
				ItemCounter=5
				DoItem(ItemCounter)
				Spacebar=False
			if pygame.key.get_pressed()[pygame.K_7] and len(InvList) > 6:
				ItemCounter=6
				DoItem(ItemCounter)
				Spacebar=False
			if pygame.key.get_pressed()[pygame.K_8] and len(InvList) > 7:
				ItemCounter=7
				DoItem(ItemCounter)
				Spacebar=False
			if pygame.key.get_pressed()[pygame.K_9] and len(InvList) > 8:
				ItemCounter=8
				DoItem(ItemCounter)
				Spacebar=False
			if pygame.key.get_pressed()[pygame.K_0] and len(InvList) > 9:
				ItemCounter=9
				DoItem(ItemCounter)
				Spacebar=False
			if pygame.key.get_pressed()[pygame.K_ESCAPE]:
				if Level > 0:
					LoadingText='Exiting game, save current map <s> start next game with new map <n>...'
					LoadingTextSurf = myfont.render(LoadingText, False, green)

					screen.blit(TextBar,(0,370))
					screen.blit(TextBar,(0,390))
					screen.blit(TextBar,(0,410))

					screen.blit(LoadingTextSurf,(0,390))
					pygame.display.flip()
					MakingAChoice=True
					ConSwitch=0
					while MakingAChoice:
						for event in pygame.event.get():
							if event.type == pygame.KEYDOWN:
								if event.key == pygame.K_s:
									MakingAChoice=False
									ConSwitch=1
								if event.key == pygame.K_n:
									ConSwitch=0
									MakingAChoice=False
					
					SwitchWrite=str(ConSwitch)+'\n'
					os.system('rm Zachno.sav')
					Save=open('Zachno.sav', 'a')
					Save.write(SwitchWrite)
					LevelSave=str(Level)+'\n'
					Save.write(LevelSave)

					WeaponSave=str(PlayerWeapon)+'\n'
					ArmorSave=str(PlayerArmor)+'\n'
					GoldSave=str(Gold)+'\n'
					AttackSave=str(PlayerAttack)+'\n'
					DefenceSave=str(PlayerDefence)+'\n'
					HealthSave=str(PlayerLifeLevel)+'\n'
					MagicSave=str(PlayerMagic)+'\n'
					LifeSave=str(PlayerLife)+'\n'
					ManaSave=str(PlayerMana)+'\n'
					XPSave=str(PlayerXP)+'\n'

					Save.write(WeaponSave)
					Save.write(ArmorSave)
					Save.write(GoldSave)
					Save.write(AttackSave)
					Save.write(DefenceSave)
					Save.write(HealthSave)
					Save.write(MagicSave)
					Save.write(LifeSave)
					Save.write(ManaSave)
					Save.write(XPSave)

					XSave=str(PlayerX)+'\n'
					Save.write(XSave)
					YSave=str(PlayerY)
					Save.write(YSave)
					Save.close()
					os.system('rm MapState.sav')
					MapSave=open('MapState.sav', 'a')
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
					os.system('rm HeroState.sav')
					HeroSave=open('HeroState.sav', 'a')
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

					os.system('rm Inventory.sav')
					InvSave=open('Inventory.sav', 'a')
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
				sys.exit()
		DoScreen(Labyrinth, Level)
		SpellX=-200
		SpellY=-200
		PlayerLevel=PlayerAttack+PlayerDefence+PlayerLifeLevel+PlayerMagic
		if PlayerLevel < 41:
			if PlayerXP >= PlayerLevel*2:
				DoLevelUp()

		SpentTime=Time.tocvalue()
		if SpentTime > 0.65 and Spacebar==False:
			DoEnemies()
			EnemiesMoved=True
			
		if NextLevel:
			Level=Level+1
			if Level < LevelMax:
				PlayerX=0
				PlayerY=0
				os.system('rm Zachno.sav')
				Save=open('Zachno.sav', 'a')
				LevelSave=str(Level)+'\n'
				Save.write('0\n')
				Save.write(LevelSave)
				WeaponSave=str(PlayerWeapon)+'\n'
				ArmorSave=str(PlayerArmor)+'\n'
				GoldSave=str(Gold)+'\n'
				AttackSave=str(PlayerAttack)+'\n'
				DefenceSave=str(PlayerDefence)+'\n'
				HealthSave=str(PlayerLifeLevel)+'\n'
				MagicSave=str(PlayerMagic)+'\n'
				LifeSave=str(PlayerLife)+'\n'
				ManaSave=str(PlayerMana)+'\n'
				XPSave=str(PlayerXP)+'\n'

				Save.write(WeaponSave)
				Save.write(ArmorSave)
				Save.write(GoldSave)
				Save.write(AttackSave)
				Save.write(DefenceSave)
				Save.write(HealthSave)
				Save.write(MagicSave)
				Save.write(LifeSave)
				Save.write(ManaSave)
				Save.write(XPSave)
		
				Save.write('0\n')
				Save.write('0')
				Save.close()
				os.system('rm Inventory.sav')
				InvSave=open('Inventory.sav', 'a')
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
