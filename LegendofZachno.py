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

Black=pygame.image.load('Black.png')
Floor=pygame.image.load('newFloor.PNG')
Stairs=pygame.image.load('newStairs.PNG')
Wall=pygame.image.load('newWall.PNG')
Player=pygame.image.load('newMonster.PNG')

#pygame.display.set_icon()
pygame.display.set_caption('Legend of Zachno')
Width=int(1200)
Heigth=int(800)
screen = pygame.display.set_mode((Width, Heigth))

PlayerX=0
PlayerY=0

Labyrinth=list()
RoomPos=list()
Room=list()
VisualList=list()
PlayerPos=[PlayerX, PlayerY]
NextLevel=False

Labyrinth=['Wall','-3','3','Wall','-2','3','Wall','-1','3','Wall','0','3','Wall','1','3','Wall','2','3','Wall','3','3','Wall','-3','2','Floor','-2','2','Floor','-1','2','Floor','0','2',
'Floor','1','2','Floor','2','2','Wall','3','2','Wall','-3','1','Floor','-2','1','Floor','-1','1','Floor','0','1','Floor','1','1','Floor','2','1','Wall','3','1',
'Wall','-3','0','Floor','-2','0','Floor','-1','0','Floor','0','0','Floor','1','0','Floor','2','0','Wall','3','0',
'Wall','-3','-1','Floor','-2','-1','Floor','-1','-1','Floor','0','-1','Floor','1','-1','Floor','2','-1','Wall','3','-1',
'Wall','-3','-2','Floor','-2','-2','Floor','-1','-2','Stairs','0','-2','Floor','1','-2','Floor','2','-2','Wall','3','-2',
'Wall','-3','-3','Wall','-2','-3','Wall','-1','-3','Wall','0','-3','Wall','1','-3','Wall','2','-3','Wall','3','-3']

def wait():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
	                		return

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
		if (-7 <= XDiff) and ( XDiff <= 7) and (-4 <= YDiff) and (YDiff <= 4):
			VisualList.append(Object)
			VisualList.append(XDiff)
			VisualList.append(YDiff)
		Counter=Counter+3
	return(VisualList)

def GetScreenItem(ObjectImage):
	if ObjectImage=='Wall':
		ScreenItem=Wall
	elif ObjectImage=='Floor':
		ScreenItem=Floor
	elif ObjectImage=='Stairs':
		ScreenItem=Stairs
	
	return(ScreenItem)

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
	LevelText = 'Level: '+str(Level)
	LevelTextSurf = myfont.render(LevelText, False, green)
	screen.blit(LevelTextSurf,(0,0))
	screen.blit(Player, (560, 320))
	pygame.display.flip()
	return

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

def GenerateRoomPos(Level):
	del RoomPos[:]
	XCounterMin=-1*Level
	XCounterMax=Level
	YCounterMin=-1*Level
	YCounterMax=Level
	while YCounterMin <= YCounterMax:
		while XCounterMin <= XCounterMax:
			RoomX=XCounterMin*7
			RoomY=YCounterMin*7
			RoomPos.append(RoomX)
			RoomPos.append(RoomY)
			XCounterMin=XCounterMin+1
		XCounterMin=-1*Level
		YCounterMin=YCounterMin+1
	return

def BuildTunnelUp(RoomCenterX, RoomCenterY):
	Counter=1
	MaxCounter=7
	while Counter < MaxCounter:
		ObjectX=RoomCenterX
		ObjectY=RoomCenterY+Counter
		Labyrinth.append('Floor')
		Labyrinth.append(ObjectX)
		Labyrinth.append(ObjectY)
		Counter=Counter+1
	Counter=1
	MaxCounter=7
	while Counter < MaxCounter:
		ObjectX=RoomCenterX-1
		ObjectY=RoomCenterY+Counter
		Labyrinth.append('Wall')
		Labyrinth.append(ObjectX)
		Labyrinth.append(ObjectY)
		Counter=Counter+1
	Counter=1
	MaxCounter=7
	while Counter < MaxCounter:
		ObjectX=RoomCenterX+1
		ObjectY=RoomCenterY+Counter
		Labyrinth.append('Wall')
		Labyrinth.append(ObjectX)
		Labyrinth.append(ObjectY)
		Counter=Counter+1
	return

def BuildTunnelRight(RoomCenterX, RoomCenterY):
	Counter=1
	MaxCounter=7
	while Counter < MaxCounter:
		ObjectX=RoomCenterX+Counter
		ObjectY=RoomCenterY
		Labyrinth.append('Floor')
		Labyrinth.append(ObjectX)
		Labyrinth.append(ObjectY)
		Counter=Counter+1
	Counter=1
	MaxCounter=7
	while Counter < MaxCounter:
		ObjectX=RoomCenterX+Counter
		ObjectY=RoomCenterY+1
		Labyrinth.append('Wall')
		Labyrinth.append(ObjectX)
		Labyrinth.append(ObjectY)
		Counter=Counter+1
	Counter=1
	MaxCounter=7
	while Counter < MaxCounter:
		ObjectX=RoomCenterX+Counter
		ObjectY=RoomCenterY-1
		Labyrinth.append('Wall')
		Labyrinth.append(ObjectX)
		Labyrinth.append(ObjectY)
		Counter=Counter+1
	return

def BuildTunnelDown(RoomCenterX, RoomCenterY):
	Counter=-1
	MaxCounter=-7
	while Counter > MaxCounter:
		ObjectX=RoomCenterX
		ObjectY=RoomCenterY+Counter
		Labyrinth.append('Floor')
		Labyrinth.append(ObjectX)
		Labyrinth.append(ObjectY)
		Counter=Counter-1
	Counter=-1
	MaxCounter=-7
	while Counter > MaxCounter:
		ObjectX=RoomCenterX-1
		ObjectY=RoomCenterY+Counter
		Labyrinth.append('Wall')
		Labyrinth.append(ObjectX)
		Labyrinth.append(ObjectY)
		Counter=Counter-1
	Counter=-1
	MaxCounter=-7
	while Counter > MaxCounter:
		ObjectX=RoomCenterX+1
		ObjectY=RoomCenterY+Counter
		Labyrinth.append('Wall')
		Labyrinth.append(ObjectX)
		Labyrinth.append(ObjectY)
		Counter=Counter-1
	return

def BuildTunnelLeft(RoomCenterX, RoomCenterY):
	Counter=-1
	MaxCounter=-7
	while Counter > MaxCounter:
		ObjectX=RoomCenterX+Counter
		ObjectY=RoomCenterY
		Labyrinth.append('Floor')
		Labyrinth.append(ObjectX)
		Labyrinth.append(ObjectY)
		Counter=Counter-1
	Counter=-1
	MaxCounter=-7
	while Counter > MaxCounter:
		ObjectX=RoomCenterX+Counter
		ObjectY=RoomCenterY-1
		Labyrinth.append('Wall')
		Labyrinth.append(ObjectX)
		Labyrinth.append(ObjectY)
		Counter=Counter-1
	Counter=-1
	MaxCounter=-7
	while Counter > MaxCounter:
		ObjectX=RoomCenterX+Counter
		ObjectY=RoomCenterY+1
		Labyrinth.append('Wall')
		Labyrinth.append(ObjectX)
		Labyrinth.append(ObjectY)
		Counter=Counter-1
	return

def GenerateRooms(RoomPos):
	Counter=0
	MaxCounter=len(RoomPos)
	while Counter < MaxCounter:
		RoomCenterX=RoomPos[Counter]
		RoomCenterY=RoomPos[Counter+1]
		NumberofExits=random.randint(0, 3)
		RoomSize=random.randint(0, 2)
		ExitCounter=0
		ExitUp=False
		ExitRight=False
		ExitDown=False
		ExitLeft=False
		while ExitCounter <= NumberofExits:
			ExitDir=random.randint(1, 4)
			if ExitDir==0:
				ExitUp=True
				BuildTunnelUp(RoomCenterX, RoomCenterY)
			if ExitDir==1:
				ExitRight=True
				BuildTunnelRight(RoomCenterX, RoomCenterY)
			if ExitDir==2:
				ExitDown=True
				BuildTunnelDown(RoomCenterX, RoomCenterY)
			if ExitDir==3:
				ExitLeft=True
				BuildTunnelLeft(RoomCenterX, RoomCenterY)
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
		Counter=Counter+2
	return

def PlaceStairs(Labyrinth):
	StairsXMin=-7*Level
	StairsXMax=7*Level
	StairsYMin=-7*Level
	StairsYMax=7*Level
	LookingForASpot=True
	while LookingForASpot:
		StairsX=random.randint(StairsXMin, StairsXMax)
		StairsY=random.randint(StairsYMin, StairsYMax)
		Counter=0
		MaxCounter=len(Labyrinth)
		while Counter < MaxCounter:
			Object=Labyrinth[Counter]
			ObjectX=Labyrinth[Counter+1]
			ObjectY=Labyrinth[Counter+2]
			if ObjectX==StairsX and ObjectY==StairsY and Object=='Floor':
				Labyrinth[Counter]='Stairs'
				LookingForASpot=False
			Counter=Counter+3
	return

def GenerateLabyrinth():
	GenerateRoomPos(Level)
	GenerateRooms(RoomPos)
	PlaceStairs(Labyrinth)
	return

Level=0
while Level < 21:
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
			NextLevel=False
			Running=False
			del Labyrinth[:]
			GenerateLabyrinth()


sys.exit()
