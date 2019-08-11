# Import necessary modules
import pygame
import sys
import random
import os
import math

# Initializing the pygame components i use 
pygame.mixer.pre_init()
pygame.init()
pygame.font.init()

pygame.mixer.init()
myfont = pygame.font.SysFont('Arial', 20)

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
def VisualScan(Labyrinth):
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
	return(ScreenItem)

def DoInventoryList():
	if len(InvList) > 0:
		ItemText='1> '+InvList[0].rstrip()
		ItemTextSurf=myfont.render(ItemText, False, green)		
		screen.blit(ItemTextSurf,(950,200))
	if len(InvList) > 1:
		ItemText='2> '+InvList[1].rstrip()
		ItemTextSurf=myfont.render(ItemText, False, green)		
		screen.blit(ItemTextSurf,(950,220))
	if len(InvList) > 2:
		ItemText='3> '+InvList[2].rstrip()
		ItemTextSurf=myfont.render(ItemText, False, green)		
		screen.blit(ItemTextSurf,(950,240))
	if len(InvList) > 3:
		ItemText='4> '+InvList[3].rstrip()
		ItemTextSurf=myfont.render(ItemText, False, green)		
		screen.blit(ItemTextSurf,(950,260))
	if len(InvList) > 4:
		ItemText='5> '+InvList[4].rstrip()
		ItemTextSurf=myfont.render(ItemText, False, green)		
		screen.blit(ItemTextSurf,(950,280))
	if len(InvList) > 5:
		ItemText='6> '+InvList[5].rstrip()
		ItemTextSurf=myfont.render(ItemText, False, green)		
		screen.blit(ItemTextSurf,(950,300))
	if len(InvList) > 6:
		ItemText='7> '+InvList[6].rstrip()
		ItemTextSurf=myfont.render(ItemText, False, green)		
		screen.blit(ItemTextSurf,(950,320))
	if len(InvList) > 7:
		ItemText='8> '+InvList[7].rstrip()
		ItemTextSurf=myfont.render(ItemText, False, green)		
		screen.blit(ItemTextSurf,(950,340))
	if len(InvList) > 8:
		ItemText='9> '+InvList[8].rstrip()
		ItemTextSurf=myfont.render(ItemText, False, green)		
		screen.blit(ItemTextSurf,(950,360))
	if len(InvList) > 9:
		ItemText='0> '+InvList[9].rstrip()
		ItemTextSurf=myfont.render(ItemText, False, green)		
		screen.blit(ItemTextSurf,(950,380))
	return

# Display function
def DoScreen (Labyrinth, Level):
	# Calling VisualScan to fill VisualList
	VisualScan(Labyrinth)
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

	PlayerAttackText='Attack: '
	PlayerSpeedText='Speed:'
	PlayerLifeLevelText='Health: '
	PlayerMagicText='Magic: '
	PlayerLifeText='Life: '
	PlayerManaText='Mana: '

	PlayerAttackTextSurf=myfont.render(PlayerAttackText, False, green)
	PlayerSpeedTextSurf=myfont.render(PlayerSpeedText, False, green)
	PlayerLifeLevelTextSurf=myfont.render(PlayerLifeLevelText, False, green)
	PlayerMagicTextSurf=myfont.render(PlayerMagicText, False, green)
	PlayerLifeTextSurf=myfont.render(PlayerLifeText, False, green)
	PlayerManaTextSurf=myfont.render(PlayerManaText, False, green)

	screen.blit(PlayerAttackTextSurf,(950,0))
	screen.blit(PlayerSpeedTextSurf,(950,20))
	screen.blit(PlayerLifeLevelTextSurf,(950,40))
	screen.blit(PlayerMagicTextSurf,(950,60))
	screen.blit(PlayerLifeTextSurf,(950,80))
	screen.blit(PlayerManaTextSurf,(950,100))

	PlayerAttackNo=str(PlayerAttack)
	PlayerSpeedNo=str(PlayerSpeed)
	PlayerLifeLevelNo=str(PlayerLifeLevel)
	PlayerMagicNo=str(PlayerMagic)
	PlayerLifeNo=str(PlayerLife)
	PlayerManaNo=str(PlayerMana)

	PlayerAttackNoSurf=myfont.render(PlayerAttackNo, False, green)
	PlayerSpeedNoSurf=myfont.render(PlayerSpeedNo, False, green)
	PlayerLifeLevelNoSurf=myfont.render(PlayerLifeLevelNo, False, green)
	PlayerMagicNoSurf=myfont.render(PlayerMagicNo, False, green)
	PlayerLifeNoSurf=myfont.render(PlayerLifeNo, False, green)
	PlayerManaNoSurf=myfont.render(PlayerManaNo, False, green)

	screen.blit(PlayerAttackNoSurf,(1100,0))
	screen.blit(PlayerSpeedNoSurf,(1100,20))
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
	screen.blit(LevelTextSurf,(0,0))
	screen.blit(PlayerPosTextSurf,(0,20))
	screen.blit(LabyrinthTextSurf,(0,40))
	#screen.blit(StairsPosTextSurf,(0,20))
	# Placing the player picture in the middle of the screen
	screen.blit(Player, (560, 320))
	if PlayerWeapon=='Dagger':
			screen.blit(DaggerSmall, (560, 320))
	elif PlayerWeapon=='Sword':
			screen.blit(SwordSmall, (560, 320))
	elif PlayerWeapon=='Mace':
			screen.blit(MaceSmall, (560, 320))
	elif PlayerWeapon=='Battleaxe':
			screen.blit(BattleAxeSmall, (560, 320))

	if PlayerArmor=='Shield':
			screen.blit(ShieldSmall, (600, 340))
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
	Collision=DoPlayerCollisionDetection(NewX, NewY, Labyrinth)
	# If DoPlayerCollisionDetection() returns True only the Bump sound will be played and the player x and y will not update
	if Collision:
		Bump.play()
	else:
	# If false the walking sound will be played and x and y will be updated
		PlayerPos[0]=NewX
		PlayerPos[1]=NewY
		Walk.play()
	return(PlayerPos)

def DoGetItem():
	ItemNo=random.randint(1,9)
	if ItemNo==1:
		Item='Mace'
	if ItemNo==2:
		Item='Beartrap'
	if ItemNo==3:
		Item='Mine'
	if ItemNo==4:
		Item='Lifepotion'
	if ItemNo==5:
		Item='Manapotion'
	if ItemNo==6:
		Item='Dagger'
	if ItemNo==7:
		Item='Sword'
	if ItemNo==8:
		Item='Battleaxe'
	if ItemNo==9:
		Item='Shield'

	InvList.append(Item)
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

# Checks next position in movement and makes game decisions
def DoPlayerCollisionDetection(NewX, NewY, Labyrinth):
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
		Counter=Counter+3
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
			FoundSomething=False
			ObjectX=RoomCenterX+Counter
			ObjectY=RoomCenterY+OffsetMin
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
		Object=Labyrinth[Counter]
		ObjectX=Labyrinth[Counter+1]
		ObjectY=Labyrinth[Counter+2]
		if CheckX==ObjectX and CheckY==ObjectY:
			if Object=='Floor':
				FloorFound=True
			if Object!='Floor':
				FloorFound=False
				break
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

def PlaceDecorations():
	LoadingText='Placing decorations...'
	LoadingTextSurf = myfont.render(LoadingText, False, green)
	screen.blit(TextBar,(0,780))
	screen.blit(LoadingTextSurf,(0,780))
	pygame.display.flip()

	global StairsX
	global StairsY
	Chests=0
	MaxChests=int(Level/2)
	DecMin=0
	DecMax=int(len(RoomPos)/14)
	while DecMin < DecMax:
		DecNo=random.randint(1,6)
		if DecNo==1:
			Decoration='Candle'
		if DecNo==2:
			Decoration='Lantern'
		if DecNo==3:
			Decoration='Rubble'
		if DecNo==4:
			Decoration='Skull'
		if DecNo==5:
			Decoration='Shield'
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
					Counter=0
					MaxCounter=len(Labyrinth)
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
					SpeedSave=str(PlayerSpeed)+'\n'
					HealthSave=str(PlayerLifeLevel)+'\n'
					MagicSave=str(PlayerMagic)+'\n'
					LifeSave=str(PlayerLife)+'\n'
					ManaSave=str(PlayerMana)+'\n'
					Save.write(AttackSave)
					Save.write(SpeedSave)
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
					Save.write('1\n')
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

def UseItem(ItemCounter):
	global PlayerWeapon
	global PlayerArmor
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
	elif InvList[ItemCounter].rstrip()=='Beartrap':
		DropItem(ItemCounter)
	elif InvList[ItemCounter].rstrip()=='Mine':
		DropItem(ItemCounter)
	elif InvList[ItemCounter].rstrip()=='Lifepotion':
		Life.play()
		del InvList[ItemCounter]
	elif InvList[ItemCounter].rstrip()=='Manapotion':
		Mana.play()
		del InvList[ItemCounter]
	return


def DropItem(ItemCounter):
	if InvList[ItemCounter].rstrip()=='Mace':
		Object='Mace'
	if InvList[ItemCounter].rstrip()=='Beartrap':
		Object='Beartrap'
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
	Labyrinth.append(Object)
	Labyrinth.append(PlayerX)
	Labyrinth.append(PlayerY)
	del InvList[ItemCounter]
	return

# Main loop
PlayerWeapon='Fists'
PlayerArmor='None'

PlayerAttack=1
PlayerSpeed=1
PlayerLifeLevel=1
PlayerMagic=1
PlayerLife=PlayerLifeLevel*10
PlayerMana=1
PlayerX=0
PlayerY=0

Load=open('Zachno.sav', 'r')
LoadList=list(Load)
Load.close()

LoadCounter=0
LoadCounterMax=len(LoadList)
ConSwitch=int(LoadList[0])
Level=int(LoadList[1])


InvList=list()
pygame.key.set_repeat(30,30)
DoSplash()
if Level > 0:
	if ConSwitch==0:
		if Level > 0 and Level < LevelMax:
			PlayerWeapon=LoadList[2].rstrip()
			PlayerArmor=LoadList[3].rstrip()
			PlayerAttack=int(LoadList[4])
			PlayerSpeed=int(LoadList[5])
			PlayerLifeLevel=int(LoadList[6])
			PlayerMagic=int(LoadList[7])
			PlayerLife=int(LoadList[8])
			PlayerMana=int(LoadList[9])
			PlayerX=0
			PlayerY=0
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
			Ping.play()
	else:
		del Labyrinth[:]
		PlayerWeapon=LoadList[2].rstrip()
		PlayerArmor=LoadList[3].rstrip()
		PlayerAttack=int(LoadList[4])
		PlayerSpeed=int(LoadList[5])
		PlayerLifeLevel=int(LoadList[6])
		PlayerMagic=int(LoadList[7])
		PlayerLife=int(LoadList[8])
		PlayerMana=int(LoadList[9])
		PlayerX=int(LoadList[10])
		PlayerY=int(LoadList[11])
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

while Level < LevelMax:
	DoScreen(Labyrinth, Level)
	Running=True
	while Running:
		for event in pygame.event.get():
			if pygame.key.get_pressed()[pygame.K_UP]:
				Dir=8
				DoMovePlayer(PlayerX, PlayerY, Dir)
				PlayerX=PlayerPos[0]
				PlayerY=PlayerPos[1]
			if pygame.key.get_pressed()[pygame.K_RIGHT]:
				Dir=6
				DoMovePlayer(PlayerX, PlayerY, Dir)
				PlayerX=PlayerPos[0]
				PlayerY=PlayerPos[1]
			if pygame.key.get_pressed()[pygame.K_DOWN]:
				Dir=2
				DoMovePlayer(PlayerX, PlayerY, Dir)
				PlayerX=PlayerPos[0]
				PlayerY=PlayerPos[1]
			if pygame.key.get_pressed()[pygame.K_LEFT]:
				Dir=4
				DoMovePlayer(PlayerX, PlayerY, Dir)
				PlayerX=PlayerPos[0]
				PlayerY=PlayerPos[1]
			if pygame.key.get_pressed()[pygame.K_1] and len(InvList) > 0:
				ItemCounter=0
				DoItem(ItemCounter)
			if pygame.key.get_pressed()[pygame.K_2] and len(InvList) > 1:
				ItemCounter=1
				DoItem(ItemCounter)
			if pygame.key.get_pressed()[pygame.K_3] and len(InvList) > 2:
				ItemCounter=2
				DoItem(ItemCounter)
			if pygame.key.get_pressed()[pygame.K_4] and len(InvList) > 3:
				ItemCounter=3
				DoItem(ItemCounter)
			if pygame.key.get_pressed()[pygame.K_5] and len(InvList) > 4:
				ItemCounter=4
				DoItem(ItemCounter)
			if pygame.key.get_pressed()[pygame.K_6] and len(InvList) > 5:
				ItemCounter=5
				DoItem(ItemCounter)
			if pygame.key.get_pressed()[pygame.K_7] and len(InvList) > 6:
				ItemCounter=6
				DoItem(ItemCounter)
			if pygame.key.get_pressed()[pygame.K_8] and len(InvList) > 7:
				ItemCounter=7
				DoItem(ItemCounter)
			if pygame.key.get_pressed()[pygame.K_9] and len(InvList) > 8:
				ItemCounter=8
				DoItem(ItemCounter)
			if pygame.key.get_pressed()[pygame.K_0] and len(InvList) > 9:
				ItemCounter=9
				DoItem(ItemCounter)
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
					AttackSave=str(PlayerAttack)+'\n'
					SpeedSave=str(PlayerSpeed)+'\n'
					HealthSave=str(PlayerLifeLevel)+'\n'
					MagicSave=str(PlayerMagic)+'\n'
					LifeSave=str(PlayerLife)+'\n'
					ManaSave=str(PlayerMana)+'\n'

					Save.write(WeaponSave)
					Save.write(ArmorSave)
					Save.write(AttackSave)
					Save.write(SpeedSave)
					Save.write(HealthSave)
					Save.write(MagicSave)
					Save.write(LifeSave)
					Save.write(ManaSave)

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
		pygame.event.pump()
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
				AttackSave=str(PlayerAttack)+'\n'
				SpeedSave=str(PlayerSpeed)+'\n'
				HealthSave=str(PlayerLifeLevel)+'\n'
				MagicSave=str(PlayerMagic)+'\n'
				LifeSave=str(PlayerLife)+'\n'
				ManaSave=str(PlayerMana)+'\n'

				Save.write(WeaponSave)
				Save.write(ArmorSave)
				Save.write(AttackSave)
				Save.write(SpeedSave)
				Save.write(HealthSave)
				Save.write(MagicSave)
				Save.write(LifeSave)
				Save.write(ManaSave)
		
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
				Ping.play()
			else:
				DoVictory()

wait()
sys.exit()
