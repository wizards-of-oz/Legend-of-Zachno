# Import necessary modules
import pygame
import sys
import random
import os
import math
 
pygame.mixer.pre_init()
pygame.init()
pygame.font.init()

pygame.mixer.init()
myfont = pygame.font.SysFont('Arial', 20)

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

Walk = pygame.mixer.Sound('Walk.ogg')
Bump = pygame.mixer.Sound('Bump.ogg')
StairsUp = pygame.mixer.Sound('Up.ogg')
Ping = pygame.mixer.Sound('Ping.ogg')

Black=pygame.image.load('Black.png')
Loading=pygame.image.load('Loading.png')
Floor=pygame.image.load('newFloor.PNG')
Stairs=pygame.image.load('newStairs.PNG')
Wall=pygame.image.load('newWall.PNG')
Player=pygame.image.load('newMonster.PNG')
TextBar=pygame.image.load('TextBar.png')

#pygame.display.set_icon()
pygame.display.set_caption('Legend of Zachno')
Width=int(1200)
Heigth=int(800)
screen = pygame.display.set_mode((Width, Heigth))
Message=''

PlayerX=0
PlayerY=0
PlayerWeapon='Fists'
PlayerMove=1
PlayerLifeMax=20
PlayerLife=20
PlayerMagic=2
PlayerMagicMax=2

Labyrinth=list()
RoomPos=list()
Room=list()
VisualList=list()
PlayerPos=[PlayerX, PlayerY]
NextLevel=False
global StairsX
global StairsY
global MapGen

LevelMax=20
StairsX=0
StairsY=-2

# Declaring the map for level zero
Labyrinth=['Wall','-3','3','Wall','-2','3','Wall','-1','3','Wall','0','3','Wall','1','3','Wall','2','3','Wall','3','3','Wall','-3','2','Floor','-2','2','Floor','-1','2','Floor','0','2',
'Floor','1','2','Floor','2','2','Wall','3','2','Wall','-3','1','Floor','-2','1','Floor','-1','1','Floor','0','1','Floor','1','1','Floor','2','1','Wall','3','1',
'Wall','-3','0','Floor','-2','0','Floor','-1','0','Floor','0','0','Floor','1','0','Floor','2','0','Wall','3','0',
'Wall','-3','-1','Floor','-2','-1','Floor','-1','-1','Floor','0','-1','Floor','1','-1','Floor','2','-1','Wall','3','-1',
'Wall','-3','-2','Floor','-2','-2','Floor','-1','-2','Stairs','0','-2','Floor','1','-2','Floor','2','-2','Wall','3','-2',
'Wall','-3','-3','Wall','-2','-3','Wall','-1','-3','Wall','0','-3','Wall','1','-3','Wall','2','-3','Wall','3','-3']

Load=open('Zachno.sav', 'r')
LoadList=list(Load)
Load.close()


# A pause function
def wait():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
	                		return

#Function that collects items from the game array when they are in screen range
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
	
	return(ScreenItem)

# Display function
def DoScreen (Labyrinth, Level):
	VisualScan(Labyrinth)
	Counter=0
	MaxCounter=len(VisualList)
	screen.blit(Black,(0,0))
	while Counter < MaxCounter:
		ObjectImage=str(VisualList[Counter])
		ObjectX=int(VisualList[Counter+1])
		ObjectY=int(VisualList[Counter+2])
		ScreenItem=GetScreenItem(ObjectImage)
		ScreenX=(ObjectX+7)*80
		YConvert=ObjectY*-1
		ScreenY=(YConvert+4)*80
		screen.blit(ScreenItem, (ScreenX, ScreenY))
		Counter=Counter+3
	SDiffX=StairsX-PlayerX
	SDiffY=StairsY-PlayerY
	LevelText = 'Level: '+str(Level)
	PlayerPosText = 'Position: '+str(PlayerX)+' '+str(PlayerY)
	StairsPosText = 'Stairs: '+str(SDiffX)+' '+str(SDiffY)

	WeaponText='Weapon:'
	MoveText='Speed:'
	LifeText='Life:'
	MagicText='Magic:'

	PlayerWeaponText=PlayerWeapon
	PlayerMoveText=str(PlayerMove)
	PlayerLifeText=str(PlayerLife)+'/'+str(PlayerLifeMax)
	PlayerMagicText=str(PlayerMagic)+'/'+str(PlayerMagicMax)

	WeaponTextSurf= myfont.render(WeaponText, False, green)
	MoveTextSurf= myfont.render(MoveText, False, green)
	LifeTextSurf= myfont.render(LifeText, False, green)
	MagicTextSurf= myfont.render(MagicText, False, green)

	screen.blit(WeaponTextSurf,(1000,0))
	screen.blit(MoveTextSurf,(1000,20))
	screen.blit(LifeTextSurf,(1000,40))
	screen.blit(MagicTextSurf,(1000,60))

	PlayerWeaponTextSurf= myfont.render(PlayerWeaponText, False, green)
	PlayerMoveTextSurf= myfont.render(PlayerMoveText, False, green)
	PlayerLifeTextSurf= myfont.render(PlayerLifeText, False, green)
	PlayerMagicTextSurf= myfont.render(PlayerMagicText, False, green)

	screen.blit(PlayerWeaponTextSurf,(1100,0))
	screen.blit(PlayerMoveTextSurf,(1100,20))
	screen.blit(PlayerLifeTextSurf,(1100,40))
	screen.blit(PlayerMagicTextSurf,(1100,60))

	LevelTextSurf=myfont.render(LevelText, 1, green)
	PlayerPosTextSurf = myfont.render(PlayerPosText, False, green)
	StairsPosTextSurf = myfont.render(StairsPosText, 1, green)
	screen.blit(LevelTextSurf,(0,0))
	#screen.blit(PlayerPosTextSurf,(0,20))
	screen.blit(StairsPosTextSurf,(0,20))
	screen.blit(Player, (560, 320))
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
	Collision=DoPlayerCollisionDetection(NewX, NewY, Labyrinth)
	if Collision:
		Bump.play()
	else:
		PlayerPos[0]=NewX
		PlayerPos[1]=NewY
		Walk.play()
	return(PlayerPos)

# Checks next position in movement and makes game decisions
def DoPlayerCollisionDetection(NewX, NewY, Labyrinth):
	global PlayerX
	global PlayerY
	global NextLevel
	Collision=False
	Counter=0
	MaxCounter=len(Labyrinth)
	while Counter < MaxCounter:
		Object=str(Labyrinth[Counter])
		ObjectX=int(Labyrinth[Counter+1])
		ObjectY=int(Labyrinth[Counter+2])
		if (ObjectX == NewX) and (ObjectY == NewY):
			if Object == 'Floor':
				Collision=False
			elif Object == 'Stairs':
				PlayerX=NewX
				PlayerY=NewY
				DoScreen(Labyrinth, Level)
				StairsUp.play()
				NextLevel=True
			else:
				Collision=True
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
	del RoomPos[:]
	MapGen=int(Level/2)+1
	XCounterMin=-1*MapGen
	XCounterMax=MapGen
	YCounterMin=-1*MapGen
	YCounterMax=Level
	MaxRooms=0
	while YCounterMin <= YCounterMax:
		while XCounterMin <= XCounterMax:
			MaxRooms=MaxRooms+2
			RoomSize=random.randint(1, 4)
			RoomX=XCounterMin*9
			RoomY=YCounterMin*9
			RoomPos.append(RoomSize)
			RoomPos.append(RoomX)
			RoomPos.append(RoomY)
			XCounterMin=XCounterMin+1
		XCounterMin=-1*MapGen
		YCounterMin=YCounterMin+1
	return(MaxRooms)

# Creates a tunnel in the up directioon from a room
def BuildTunnelUp(RoomCenterX, RoomCenterY, RoomSize, TunnelWidth):
	LoadingText='Building tunnel up...'
	LoadingTextSurf = myfont.render(LoadingText, False, green)
	screen.blit(TextBar,(0,780))
	screen.blit(LoadingTextSurf,(0,780))
	pygame.display.flip()
	OffsetMin=-1*TunnelWidth
	OffsetMax=TunnelWidth
	Counter=RoomSize
	MaxCounter=9
	while OffsetMin <= OffsetMax:
		Counter=RoomSize
		MaxCounter=9
		FoundSomething=False
		while Counter < MaxCounter:
			ObjectX=RoomCenterX+OffsetMin
			ObjectY=RoomCenterY+Counter
			Labyrinth.append('Floor')
			Labyrinth.append(ObjectX)
			Labyrinth.append(ObjectY)
			CheckX=ObjectX
			CheckY=ObjectY+1
			FoundSomething=CheckSpace(Labyrinth, CheckX, CheckY)
			if FoundSomething:
				break
			Counter=Counter+1
		OffsetMin=OffsetMin+1
	OffsetMin=-1*TunnelWidth
	OffsetMax=TunnelWidth
	Counter=RoomSize
	MaxCounter=9
	while Counter < MaxCounter:
		FoundSomething=False
		ObjectX=RoomCenterX-1-OffsetMax
		ObjectY=RoomCenterY+Counter
		Labyrinth.append('Wall')
		Labyrinth.append(ObjectX)
		Labyrinth.append(ObjectY)
		CheckX=ObjectX
		CheckY=ObjectY+1
		FoundSomething=CheckSpace(Labyrinth, CheckX, CheckY)
		if FoundSomething:
			break
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
		CheckX=ObjectX
		CheckY=ObjectY+1
		FoundSomething=CheckSpace(Labyrinth, CheckX, CheckY)
		if FoundSomething:
			break
		Counter=Counter+1
	return

# Creates a tunnel in the right directioon from a room
def BuildTunnelRight(RoomCenterX, RoomCenterY, RoomSize, TunnelWidth):
	LoadingText='Building tunnel right...'
	LoadingTextSurf = myfont.render(LoadingText, False, green)
	screen.blit(TextBar,(0,780))
	screen.blit(LoadingTextSurf,(0,780))
	pygame.display.flip()
	Counter=RoomSize
	MaxCounter=9
	OffsetMin=-1*TunnelWidth
	OffsetMax=TunnelWidth
	while OffsetMin <= OffsetMax:
		Counter=RoomSize
		MaxCounter=9
		FoundSomething=False
		while Counter < MaxCounter:
			FoundSomething=False
			ObjectX=RoomCenterX+Counter
			ObjectY=RoomCenterY+OffsetMin
			Labyrinth.append('Floor')
			Labyrinth.append(ObjectX)
			Labyrinth.append(ObjectY)
			CheckX=ObjectX+1
			CheckY=ObjectY
			FoundSomething=CheckSpace(Labyrinth, CheckX, CheckY)
			if FoundSomething:
				break
			Counter=Counter+1
		OffsetMin=OffsetMin+1
	OffsetMin=-1*TunnelWidth
	Counter=RoomSize
	MaxCounter=9
	while Counter < MaxCounter:
		FoundSomething=False
		ObjectX=RoomCenterX+Counter
		ObjectY=RoomCenterY+1+OffsetMax
		CheckX=ObjectX+1
		CheckY=ObjectY
		FoundSomething=CheckSpace(Labyrinth, CheckX, CheckY)
		Labyrinth.append('Wall')
		Labyrinth.append(ObjectX)
		Labyrinth.append(ObjectY)
		if FoundSomething:
			break
		Counter=Counter+1
	OffsetMin=-1*TunnelWidth
	Counter=RoomSize
	MaxCounter=9
	while Counter < MaxCounter:
		FoundSomething=False
		ObjectX=RoomCenterX+Counter
		ObjectY=RoomCenterY-1-OffsetMax
		CheckX=ObjectX+1
		CheckY=ObjectY
		FoundSomething=CheckSpace(Labyrinth, CheckX, CheckY)
		Labyrinth.append('Wall')
		Labyrinth.append(ObjectX)
		Labyrinth.append(ObjectY)
		if FoundSomething:
			break
		Counter=Counter+1
	return

# Creates a tunnel in the down directioon from a room
def BuildTunnelDown(RoomCenterX, RoomCenterY, RoomSize, TunnelWidth):
	LoadingText='Building tunnel up down...'
	LoadingTextSurf = myfont.render(LoadingText, False, green)
	screen.blit(TextBar,(0,780))
	screen.blit(LoadingTextSurf,(0,780))
	pygame.display.flip()
	Counter=-1*RoomSize
	MaxCounter=-9
	OffsetMin=-1*TunnelWidth
	OffsetMax=TunnelWidth
	while OffsetMin <= OffsetMax:
		Counter=-1*RoomSize
		MaxCounter=-9
		FoundSomething=False
		while Counter > MaxCounter:
			ObjectX=RoomCenterX+OffsetMin
			ObjectY=RoomCenterY+Counter
			Labyrinth.append('Floor')
			Labyrinth.append(ObjectX)
			Labyrinth.append(ObjectY)
			CheckX=ObjectX
			CheckY=ObjectY-1
			FoundSomething=CheckSpace(Labyrinth, CheckX, CheckY)
			if FoundSomething:
				break
			Counter=Counter-1
		OffsetMin=OffsetMin+1
	OffsetMin=-1*TunnelWidth
	Counter=-1*RoomSize
	MaxCounter=-9
	while Counter > MaxCounter:
		FoundSomething=False
		ObjectX=RoomCenterX-1-OffsetMax
		ObjectY=RoomCenterY+Counter
		CheckX=ObjectX
		CheckY=ObjectY-1
		FoundSomething=CheckSpace(Labyrinth, CheckX, CheckY)
		Labyrinth.append('Wall')
		Labyrinth.append(ObjectX)
		Labyrinth.append(ObjectY)
		if FoundSomething:
			break
		Counter=Counter-1
	OffsetMin=-1*TunnelWidth
	Counter=-1*RoomSize
	MaxCounter=-9
	while Counter > MaxCounter:
		FoundSomething=False
		ObjectX=RoomCenterX+1+OffsetMax
		ObjectY=RoomCenterY+Counter
		CheckX=ObjectX
		CheckY=ObjectY-1
		FoundSomething=CheckSpace(Labyrinth, CheckX, CheckY)
		Labyrinth.append('Wall')
		Labyrinth.append(ObjectX)
		Labyrinth.append(ObjectY)
		if FoundSomething:
			break
		Counter=Counter-1
	return

# Creates a tunnel in the left directioon from a room
def BuildTunnelLeft(RoomCenterX, RoomCenterY, RoomSize, TunnelWidth):
	LoadingText='Building tunnel up left...'
	LoadingTextSurf = myfont.render(LoadingText, False, green)
	screen.blit(TextBar,(0,780))
	screen.blit(LoadingTextSurf,(0,780))
	pygame.display.flip()
	Counter=-1*RoomSize
	MaxCounter=-9
	OffsetMin=-1*TunnelWidth
	OffsetMax=TunnelWidth
	while OffsetMin <= OffsetMax:
		Counter=-1*RoomSize
		MaxCounter=-9
		FoundSomething=False
		while Counter > MaxCounter:
			ObjectX=RoomCenterX+Counter
			ObjectY=RoomCenterY+OffsetMin
			CheckX=ObjectX-1
			CheckY=ObjectY
			FoundSomething=CheckSpace(Labyrinth, CheckX, CheckY)
			Labyrinth.append('Floor')
			Labyrinth.append(ObjectX)
			Labyrinth.append(ObjectY)
			if FoundSomething:
				break
			Counter=Counter-1
		OffsetMin=OffsetMin+1
	OffsetMin=-1*TunnelWidth
	Counter=-1*RoomSize
	MaxCounter=-9
	while Counter > MaxCounter:
		FoundSomething=False
		ObjectX=RoomCenterX+Counter
		ObjectY=RoomCenterY-1-OffsetMax
		CheckX=ObjectX-1
		CheckY=ObjectY
		FoundSomething=CheckSpace(Labyrinth, CheckX, CheckY)
		Labyrinth.append('Wall')
		Labyrinth.append(ObjectX)
		Labyrinth.append(ObjectY)
		if FoundSomething:
			break
		Counter=Counter-1
	OffsetMin=-1*TunnelWidth
	Counter=-1*RoomSize
	MaxCounter=-9
	while Counter > MaxCounter:
		FoundSomething=False
		ObjectX=RoomCenterX+Counter
		ObjectY=RoomCenterY+1+OffsetMax
		CheckX=ObjectX-1
		CheckY=ObjectY
		FoundSomething=CheckSpace(Labyrinth, CheckX, CheckY)
		Labyrinth.append('Wall')
		Labyrinth.append(ObjectX)
		Labyrinth.append(ObjectY)
		if FoundSomething:
			break
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
		if Object=='Floor':
			FloorFound=True
		if Object=='Wall':
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
def CheckRoomUp(Labyrinth, RoomCenterX, RoomCenterY):
	LoadingText='Checking for room up '+str(RoomCenterX)+' '+str(RoomCenterY)+'...'
	LoadingTextSurf = myfont.render(LoadingText, False, green)
	screen.blit(TextBar,(0,780))
	screen.blit(LoadingTextSurf,(0,780))
	pygame.display.flip()

	OffSetY=1
	while OffSetY < 9:
		LabCounter=0
		LabCounterMax=len(Labyrinth)
		while LabCounter < LabCounterMax:
			Object=Labyrinth[LabCounter]
			ObjectX=Labyrinth[LabCounter+1]
			ObjectY=Labyrinth[LabCounter+2]
			if ObjectX==RoomCenterX and ObjectY==(RoomCenterY+OffSetY):
				if Object=='Wall':
					OffSetY=OffSetY+1
					CheckX=RoomCenterX
					CheckY=RoomCenterY+OffSetY
					CheckCounter=0
					CheckCounterMax=len(Labyrinth)
					FoundSomething=CheckSpace(Labyrinth, CheckX, CheckY)
					if FoundSomething:
						while CheckCounter < CheckCounterMax:
							CheckObject=Labyrinth[CheckCounter]
							CheckObjectX=Labyrinth[CheckCounter+1]
							CheckObjectY=Labyrinth[CheckCounter+2]
							if CheckObjectX==CheckX and CheckObjectY==CheckY: 
								if CheckObject=='Floor':
									Labyrinth[LabCounter]='Floor'
							CheckCounter=CheckCounter+3
					else:
						return
					
			LabCounter=LabCounter+3
		OffSetY=OffSetY+1
	return

# Looks wether another room wants to make an opening in the current room
def CheckRoomRight(Labyrinth, RoomCenterX, RoomCenterY):
	LoadingText='Checking for room to the right '+str(RoomCenterX)+' '+str(RoomCenterY)+'...'
	LoadingTextSurf = myfont.render(LoadingText, False, green)
	screen.blit(TextBar,(0,780))
	screen.blit(LoadingTextSurf,(0,780))
	pygame.display.flip()

	OffSetX=1
	while OffSetX < 9:
		LabCounter=0
		LabCounterMax=len(Labyrinth)
		while LabCounter < LabCounterMax:
			Object=Labyrinth[LabCounter]
			ObjectX=Labyrinth[LabCounter+1]
			ObjectY=Labyrinth[LabCounter+2]
			if ObjectX==(RoomCenterX+OffSetX) and ObjectY==RoomCenterY:
				if Object=='Wall':
					OffSetX=OffSetX+1
					CheckX=RoomCenterX+OffSetX
					CheckY=RoomCenterY
					CheckCounter=0
					CheckCounterMax=len(Labyrinth)
					FoundSomething=CheckSpace(Labyrinth, CheckX, CheckY)
					if FoundSomething:
						while CheckCounter < CheckCounterMax:
							CheckObject=Labyrinth[CheckCounter]
							CheckObjectX=Labyrinth[CheckCounter+1]
							CheckObjectY=Labyrinth[CheckCounter+2]
							if CheckObjectX==CheckX and CheckObjectY==CheckY:
								if CheckObject=='Floor':
									Labyrinth[LabCounter]='Floor'
							CheckCounter=CheckCounter+3
					else:
						return
					
			LabCounter=LabCounter+3
		OffSetX=OffSetX+1
	return

# Looks wether another room wants to make an opening in the current room
def CheckRoomDown(Labyrinth, RoomCenterX, RoomCenterY):
	LoadingText='Checking for room down '+str(RoomCenterX)+' '+str(RoomCenterY)+'...'
	LoadingTextSurf = myfont.render(LoadingText, False, green)
	screen.blit(TextBar,(0,780))
	screen.blit(LoadingTextSurf,(0,780))
	pygame.display.flip()

	OffSetY=-1
	while OffSetY > -9:
		LabCounter=0
		LabCounterMax=len(Labyrinth)
		while LabCounter < LabCounterMax:
			Object=Labyrinth[LabCounter]
			ObjectX=Labyrinth[LabCounter+1]
			ObjectY=Labyrinth[LabCounter+2]
			if ObjectX==RoomCenterX and ObjectY==(RoomCenterY+OffSetY):
				if Object=='Wall':
					OffSetY=OffSetY-1
					CheckX=RoomCenterX
					CheckY=RoomCenterY+OffSetY
					CheckCounter=0
					CheckCounterMax=len(Labyrinth)
					FoundSomething=CheckSpace(Labyrinth, CheckX, CheckY)
					if FoundSomething:
						while CheckCounter < CheckCounterMax:
							CheckObject=Labyrinth[CheckCounter]
							CheckObjectX=Labyrinth[CheckCounter+1]
							CheckObjectY=Labyrinth[CheckCounter+2]
							if CheckObjectX==CheckX and CheckObjectY==CheckY:
								if CheckObject=='Floor':
									Labyrinth[LabCounter]='Floor'
							CheckCounter=CheckCounter+3
					else:
						return
					
			LabCounter=LabCounter+3
		OffSetY=OffSetY-1
	return

# Looks wether another room wants to make an opening in the current room
def CheckRoomLeft(Labyrinth, RoomCenterX, RoomCenterY):
	LoadingText='Checking for room to the left '+str(RoomCenterX)+' '+str(RoomCenterY)+'...'
	LoadingTextSurf = myfont.render(LoadingText, False, green)
	screen.blit(TextBar,(0,780))
	screen.blit(LoadingTextSurf,(0,780))
	pygame.display.flip()

	OffSetX=-1
	while OffSetX > -9:
		LabCounter=0
		LabCounterMax=len(Labyrinth)
		while LabCounter < LabCounterMax:
			Object=Labyrinth[LabCounter]
			ObjectX=Labyrinth[LabCounter+1]
			ObjectY=Labyrinth[LabCounter+2]
			if ObjectX==(RoomCenterX+OffSetX) and ObjectY==RoomCenterY:
				if Object=='Wall':
					OffSetX=OffSetX-1
					CheckX=RoomCenterX+OffSetX
					CheckY=RoomCenterY
					CheckCounter=0
					CheckCounterMax=len(Labyrinth)
					FoundSomething=CheckSpace(Labyrinth, CheckX, CheckY)
					if FoundSomething:
						while CheckCounter < CheckCounterMax:
							CheckObject=Labyrinth[CheckCounter]
							CheckObjectX=Labyrinth[CheckCounter+1]
							CheckObjectY=Labyrinth[CheckCounter+2]
							if CheckObjectX==CheckX and CheckObjectY==CheckY:
								if CheckObject=='Floor':
									Labyrinth[LabCounter]='Floor'
							CheckCounter=CheckCounter+3
					else:
						return
					
			LabCounter=LabCounter+3
		OffSetX=OffSetX-1
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
		PercentageText='Loading level '+str(Level)+' '+str(Percentage)+'%'
		PercentageTextSurf = myfont.render(PercentageText, False, green)
		screen.blit(TextBar,(0,780))
		screen.blit(TextBar,(0,0))
		screen.blit(PercentageTextSurf,(0,0))
		pygame.display.flip()

		RoomSize=RoomPos[Counter]
		RoomCenterX=RoomPos[Counter+1]
		RoomCenterY=RoomPos[Counter+2]
		if RoomCenterY==(MapGen*9):
			RoomUp=False
		if RoomCenterX==(MapGen*9):
			RoomRight=False
		if RoomCenterY==(MapGen*-9):
			RoomDown=False
		if RoomCenterX==(MapGen*-9):
			RoomLeft=False

		if RoomUp:
			CheckRoomUp(Labyrinth, RoomCenterX, RoomCenterY)
		if RoomRight:
			CheckRoomRight(Labyrinth, RoomCenterX, RoomCenterY)
		if RoomDown:
			CheckRoomDown(Labyrinth, RoomCenterX, RoomCenterY)
		if RoomLeft:
			CheckRoomLeft(Labyrinth, RoomCenterX, RoomCenterY)
		Counter=Counter+3
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
		TargetRoomX=RoomPos[Counter+1]
		TargetRoomY=RoomPos[Counter+2]
		if TargetX==TargetRoomX and TargetY==TargetRoomY:
			if TargetRoomSize==1:
				TunnelWidth=0
		Counter=Counter+3
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
		RoomCenterX=RoomPos[Counter+1]
		RoomCenterY=RoomPos[Counter+2]
		LoadingText='Generating room '+str(RoomCenterX)+str(RoomCenterY)+'...'
		Percentage=GetPercentage(Rooms, MaxRooms)
		PercentageText='Loading level '+str(Level)+' '+str(Percentage)+'%'
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
						ExitUp=True
						TargetX=RoomCenterX
						TargetY=RoomCenterY+9
						TunnelWidth=CheckTargetRoom(TargetX, TargetY, RoomSize, RoomPos)
						TunnelUp=TunnelWidth
						BuildTunnelUp(RoomCenterX, RoomCenterY, RoomSize, TunnelWidth)
						ExitCounter=ExitCounter+1
				else:
					if RoomCenterY > (MapGen*-9):
						ExitDown=True
						TargetX=RoomCenterX
						TargetY=RoomCenterY-9
						TunnelWidth=CheckTargetRoom(TargetX, TargetY, RoomSize, RoomPos)
						TunnelDown=TunnelWidth
						BuildTunnelDown(RoomCenterX, RoomCenterY, RoomSize, TunnelWidth)
						ExitCounter=ExitCounter+1
			if ExitDir==2:
				if RoomCenterX < (MapGen*9):
					if ExitRight==False:
						ExitRight=True
						TargetX=RoomCenterX+9
						TargetY=RoomCenterY
						TunnelWidth=CheckTargetRoom(TargetX, TargetY, RoomSize, RoomPos)
						TunnelRight=TunnelWidth
						BuildTunnelRight(RoomCenterX, RoomCenterY, RoomSize, TunnelWidth)
						ExitCounter=ExitCounter+1
				else:
					if RoomCenterX > (MapGen*-9):
						ExitLeft=True
						TargetX=RoomCenterX-9
						TargetY=RoomCenterY
						TunnelWidth=CheckTargetRoom(TargetX, TargetY, RoomSize, RoomPos)
						TunnelLeft=TunnelWidth
						BuildTunnelLeft(RoomCenterX, RoomCenterY, RoomSize, TunnelWidth)
						ExitCounter=ExitCounter+1
			if ExitDir==3:
				if RoomCenterY > (MapGen*-9):
					if ExitDown==False:
						ExitDown=True
						TargetX=RoomCenterX
						TargetY=RoomCenterY-9
						TunnelWidth=CheckTargetRoom(TargetX, TargetY, RoomSize, RoomPos)
						TunnelDown=TunnelWidth
						BuildTunnelDown(RoomCenterX, RoomCenterY, RoomSize, TunnelWidth)
						ExitCounter=ExitCounter+1
				else:
					if RoomCenterY < (MapGen*9):
						ExitUp=True
						TargetX=RoomCenterX
						TargetY=RoomCenterY+9
						TunnelWidth=CheckTargetRoom(TargetX, TargetY, RoomSize, RoomPos)
						TunnelUp=TunnelWidth
						BuildTunnelUp(RoomCenterX, RoomCenterY, RoomSize, TunnelWidth)
						ExitCounter=ExitCounter+1
			if ExitDir==4:
				if RoomCenterX > (MapGen*-9):
					if ExitLeft==False:
						ExitLeft=True
						TargetX=RoomCenterX-9
						TargetY=RoomCenterY
						TunnelWidth=CheckTargetRoom(TargetX, TargetY, RoomSize, RoomPos)
						TunnelLeft=TunnelWidth
						ExitLeft=True
						BuildTunnelLeft(RoomCenterX, RoomCenterY, RoomSize, TunnelWidth)
						ExitCounter=ExitCounter+1
				else:
					if RoomCenterX < (MapGen*9):
						ExitRight=True
						TargetX=RoomCenterX+9
						TargetY=RoomCenterY
						TunnelWidth=CheckTargetRoom(TargetX, TargetY, RoomSize, RoomPos)
						TunnelRight=TunnelWidth
						BuildTunnelRight(RoomCenterX, RoomCenterY, RoomSize, TunnelWidth)
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

		Counter=Counter+3
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
	StairsXMin=-1*Level*9
	StairsXMax=Level*9
	StairsYMin=-1*Level*9
	StairsYMax=Level*9
	LookingForASpot=True
	while LookingForASpot:
		StairsX=random.randint(StairsXMin, StairsXMax)
		StairsY=random.randint(StairsYMin, StairsYMax)
		FoundASpot=False
		Counter=0
		MaxCounter=len(Labyrinth)
		while Counter < MaxCounter:
			Object=Labyrinth[Counter]
			ObjectX=Labyrinth[Counter+1]
			ObjectY=Labyrinth[Counter+2]
			if ObjectX==StairsX and ObjectY==StairsY:
				if Object=='Wall':
					FoundASpot=False
					break
				if Object=='Floor':
					FoundASpot=True
			Counter=Counter+3
		if FoundASpot:
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

# I don't use this function anymore, my code has evolved!
def DoOuterWall(Level):
	YTop=(Level*7)+7
	Xleft=(Level*-7)-7
	XRight=(Level*7)+7
	while Xleft <= XRight:
		Labyrinth.append('Wall')
		Labyrinth.append(Xleft)
		Labyrinth.append(YTop)
		Xleft=Xleft+1
	YTop=(Level*7)+7
	YBottom=(Level*-7)-7
	XRight=(Level*7)+7
	while YTop >= YBottom:
		Labyrinth.append('Wall')
		Labyrinth.append(XRight)
		Labyrinth.append(YTop)
		YTop=YTop-1
	YBottom=(Level*-7)-7
	Xleft=(Level*-7)-7
	XRight=(Level*7)+7
	while XRight >= Xleft:
		Labyrinth.append('Wall')
		Labyrinth.append(XRight)
		Labyrinth.append(YBottom)
		XRight=XRight-1
	YBottom=(Level*-7)-7
	Xleft=(Level*-7)-7
	YTop=(Level*7)+7
	while YBottom <= YTop:
		Labyrinth.append('Wall')
		Labyrinth.append(Xleft)
		Labyrinth.append(YBottom)
		YBottom=YBottom+1
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

# Main loop
Level=int(LoadList[0])
if Level > 0:
	MaxRooms=0
	Rooms=0
	screen.blit(Loading,(0,0))
	pygame.display.flip()
	del Labyrinth[:]
	GenerateLabyrinth()
	CheckNextRoom(Labyrinth, RoomPos)
	PlaceStairs(Labyrinth)
	Ping.play()

while Level < LevelMax:
	DoScreen(Labyrinth, Level)
	Running=True
	PlayerX=0
	PlayerY=0
	while Running:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					Dir=8
					DoMovePlayer(PlayerX, PlayerY, Dir)
					PlayerX=PlayerPos[0]
					PlayerY=PlayerPos[1]
				if event.key == pygame.K_RIGHT:
					Dir=6
					DoMovePlayer(PlayerX, PlayerY, Dir)
					PlayerX=PlayerPos[0]
					PlayerY=PlayerPos[1]
				if event.key == pygame.K_DOWN:
					Dir=2
					DoMovePlayer(PlayerX, PlayerY, Dir)
					PlayerX=PlayerPos[0]
					PlayerY=PlayerPos[1]
				if event.key == pygame.K_LEFT:
					Dir=4
					DoMovePlayer(PlayerX, PlayerY, Dir)
					PlayerX=PlayerPos[0]
					PlayerY=PlayerPos[1]
				if event.key == pygame.K_ESCAPE:
					sys.exit()
		DoScreen(Labyrinth, Level)
		if NextLevel:
			Level=Level+1
			LoadList[0]=Level
			os.system('rm Zachno.sav')
			Save=open('Zachno.sav', 'a')
			Line=str(LoadList[0]).strip()
			SLine=Line+'\n'
			Save.write(SLine)
			Save.close()
			LoadingText='Continue to next level? [j/n]...'
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
						if event.key == pygame.K_j:
							MakingAChoice=False
						if event.key == pygame.K_n:
							sys.exit()

			LoadingText='Cooking level '+str(Level)+'...'
			LoadingTextSurf = myfont.render(LoadingText, False, green)
			screen.blit(Black,(0,0))
			screen.blit(Loading,(0,0))
			screen.blit(LoadingTextSurf,(0,780))
			pygame.display.flip()
			NextLevel=False
			Running=False

			if Level < LevelMax:
				Rooms=0
				MaxRooms=0
				del Labyrinth[:]
				GenerateLabyrinth()
				CheckNextRoom(Labyrinth, RoomPos)
				PlaceStairs(Labyrinth)
			Ping.play()

wait()
sys.exit()
