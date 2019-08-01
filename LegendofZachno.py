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
	LevelText = 'Level: '+str(Level)
	PlayerPosText = 'Position: '+str(PlayerX)+' '+str(PlayerY)
	LevelTextSurf = myfont.render(LevelText, False, green)
	PlayerPosTextSurf = myfont.render(PlayerPosText, False, green)
	screen.blit(LevelTextSurf,(0,0))
	screen.blit(PlayerPosTextSurf,(0,20))
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
	print('GenerateRoomPos')
	del RoomPos[:]
	XCounterMin=-1*Level
	XCounterMax=Level
	YCounterMin=-1*Level
	YCounterMax=Level
	while YCounterMin <= YCounterMax:
		while XCounterMin <= XCounterMax:
			RoomX=XCounterMin*8
			RoomY=YCounterMin*8
			RoomPos.append(RoomX)
			RoomPos.append(RoomY)
			XCounterMin=XCounterMin+1
		XCounterMin=-1*Level
		YCounterMin=YCounterMin+1
	return

# Creates a tunnel in the up directioon from a room
def BuildTunnelUp(RoomCenterX, RoomCenterY, RoomSize):
	print('Building tunnel up')
	Counter=RoomSize
	MaxCounter=8
	while Counter < MaxCounter:
		ObjectX=RoomCenterX
		ObjectY=RoomCenterY+Counter
		CheckX=ObjectX
		CheckY=ObjectY+1
		FoundSomething=CheckSpace(Labyrinth, CheckX, CheckY)
		Labyrinth.append('Floor')
		Labyrinth.append(ObjectX)
		Labyrinth.append(ObjectY)
		if FoundSomething:
			break
		Counter=Counter+1
	Counter=RoomSize
	MaxCounter=8
	while Counter < MaxCounter:
		ObjectX=RoomCenterX-1
		ObjectY=RoomCenterY+Counter
		CheckX=ObjectX
		CheckY=ObjectY+1
		FoundSomething=CheckSpace(Labyrinth, CheckX, CheckY)
		Labyrinth.append('Wall')
		Labyrinth.append(ObjectX)
		Labyrinth.append(ObjectY)
		if FoundSomething:
			break
		Counter=Counter+1
	Counter=RoomSize
	MaxCounter=8
	while Counter < MaxCounter:
		ObjectX=RoomCenterX+1
		ObjectY=RoomCenterY+Counter
		CheckX=ObjectX
		CheckY=ObjectY+1
		FoundSomething=CheckSpace(Labyrinth, CheckX, CheckY)
		Labyrinth.append('Wall')
		Labyrinth.append(ObjectX)
		Labyrinth.append(ObjectY)
		if FoundSomething:
			break
		Counter=Counter+1
	return

# Creates a tunnel in the right directioon from a room
def BuildTunnelRight(RoomCenterX, RoomCenterY, RoomSize):
	print('Building tunnel right')
	Counter=RoomSize
	MaxCounter=8
	while Counter < MaxCounter:
		ObjectX=RoomCenterX+Counter
		ObjectY=RoomCenterY
		CheckX=ObjectX+1
		CheckY=ObjectY
		FoundSomething=CheckSpace(Labyrinth, CheckX, CheckY)
		Labyrinth.append('Floor')
		Labyrinth.append(ObjectX)
		Labyrinth.append(ObjectY)
		if FoundSomething:
			break
		Counter=Counter+1
	Counter=RoomSize
	MaxCounter=8
	while Counter < MaxCounter:
		ObjectX=RoomCenterX+Counter
		ObjectY=RoomCenterY+1
		CheckX=ObjectX+1
		CheckY=ObjectY
		FoundSomething=CheckSpace(Labyrinth, CheckX, CheckY)
		Labyrinth.append('Wall')
		Labyrinth.append(ObjectX)
		Labyrinth.append(ObjectY)
		if FoundSomething:
			break
		Counter=Counter+1
	Counter=RoomSize
	MaxCounter=8
	while Counter < MaxCounter:
		ObjectX=RoomCenterX+Counter
		ObjectY=RoomCenterY-1
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
def BuildTunnelDown(RoomCenterX, RoomCenterY, RoomSize):
	print('Building tunnel down')
	Counter=-1*RoomSize
	MaxCounter=-8
	while Counter > MaxCounter:
		ObjectX=RoomCenterX
		ObjectY=RoomCenterY+Counter
		CheckX=ObjectX
		CheckY=ObjectY-1
		FoundSomething=CheckSpace(Labyrinth, CheckX, CheckY)
		Labyrinth.append('Floor')
		Labyrinth.append(ObjectX)
		Labyrinth.append(ObjectY)
		if FoundSomething:
			break
		Counter=Counter-1
	Counter=-1*RoomSize
	MaxCounter=-8
	while Counter > MaxCounter:
		ObjectX=RoomCenterX-1
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
	Counter=-1*RoomSize
	MaxCounter=-8
	while Counter > MaxCounter:
		ObjectX=RoomCenterX+1
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
def BuildTunnelLeft(RoomCenterX, RoomCenterY, RoomSize):
	print('Building tunnel left')
	Counter=-1*RoomSize
	MaxCounter=-8
	while Counter > MaxCounter:
		ObjectX=RoomCenterX+Counter
		ObjectY=RoomCenterY
		CheckX=ObjectX-1
		CheckY=ObjectY
		FoundSomething=CheckSpace(Labyrinth, CheckX, CheckY)
		Labyrinth.append('Floor')
		Labyrinth.append(ObjectX)
		Labyrinth.append(ObjectY)
		if FoundSomething:
			break
		Counter=Counter-1
	Counter=-1*RoomSize
	MaxCounter=-8
	while Counter > MaxCounter:
		ObjectX=RoomCenterX+Counter
		ObjectY=RoomCenterY-1
		CheckX=ObjectX-1
		CheckY=ObjectY
		FoundSomething=CheckSpace(Labyrinth, CheckX, CheckY)
		Labyrinth.append('Wall')
		Labyrinth.append(ObjectX)
		Labyrinth.append(ObjectY)
		if FoundSomething:
			break
		Counter=Counter-1
	Counter=-1*RoomSize
	MaxCounter=-8
	while Counter > MaxCounter:
		ObjectX=RoomCenterX+Counter
		ObjectY=RoomCenterY+1
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
	print('CheckRoomUp ', RoomCenterX, RoomCenterY)
	OffSetY=1
	while OffSetY < 8:
		LabCounter=0
		LabCounterMax=len(Labyrinth)
		while LabCounter < LabCounterMax:
			Object=Labyrinth[LabCounter]
			ObjectX=Labyrinth[LabCounter+1]
			ObjectY=Labyrinth[LabCounter+2]
			if ObjectX==RoomCenterX and ObjectY==(RoomCenterY+OffSetY):
				if Object=='Wall':
					print('Wall')
					OffSetY=OffSetY+1
					CheckX=RoomCenterX
					CheckY=RoomCenterY+OffSetY
					CheckCounter=0
					CheckCounterMax=len(Labyrinth)
					FoundSomething=CheckSpace(Labyrinth, CheckX, CheckY)
					if FoundSomething:
						print('Found Something')
						while CheckCounter < CheckCounterMax:
							CheckObject=Labyrinth[CheckCounter]
							CheckObjectX=Labyrinth[CheckCounter+1]
							CheckObjectY=Labyrinth[CheckCounter+2]
							if CheckObjectX==CheckX and CheckObjectY==CheckY: 
								if CheckObject=='Floor':
									Labyrinth[LabCounter]='Floor'
									print('Floor')
							CheckCounter=CheckCounter+3
					else:
						return
					
			LabCounter=LabCounter+3
		OffSetY=OffSetY+1
	return

# Looks wether another room wants to make an opening in the current room
def CheckRoomRight(Labyrinth, RoomCenterX, RoomCenterY):
	print('CheckRoomRight', RoomCenterX, RoomCenterY)
	OffSetX=1
	while OffSetX < 8:
		LabCounter=0
		LabCounterMax=len(Labyrinth)
		while LabCounter < LabCounterMax:
			Object=Labyrinth[LabCounter]
			ObjectX=Labyrinth[LabCounter+1]
			ObjectY=Labyrinth[LabCounter+2]
			if ObjectX==(RoomCenterX+OffSetX) and ObjectY==RoomCenterY:
				if Object=='Wall':
					print('Wall')
					OffSetX=OffSetX+1
					CheckX=RoomCenterX+OffSetX
					CheckY=RoomCenterY
					CheckCounter=0
					CheckCounterMax=len(Labyrinth)
					FoundSomething=CheckSpace(Labyrinth, CheckX, CheckY)
					if FoundSomething:
						print('Found Something')
						while CheckCounter < CheckCounterMax:
							CheckObject=Labyrinth[CheckCounter]
							CheckObjectX=Labyrinth[CheckCounter+1]
							CheckObjectY=Labyrinth[CheckCounter+2]
							if CheckObjectX==CheckX and CheckObjectY==CheckY:
								if CheckObject=='Floor':
									Labyrinth[LabCounter]='Floor'
									print('Floor')
							CheckCounter=CheckCounter+3
					else:
						return
					
			LabCounter=LabCounter+3
		OffSetX=OffSetX+1
	return

# Looks wether another room wants to make an opening in the current room
def CheckRoomDown(Labyrinth, RoomCenterX, RoomCenterY):
	print('CheckRoomDown', RoomCenterX, RoomCenterY)
	OffSetY=-1
	while OffSetY > -8:
		LabCounter=0
		LabCounterMax=len(Labyrinth)
		while LabCounter < LabCounterMax:
			Object=Labyrinth[LabCounter]
			ObjectX=Labyrinth[LabCounter+1]
			ObjectY=Labyrinth[LabCounter+2]
			if ObjectX==RoomCenterX and ObjectY==(RoomCenterY+OffSetY):
				if Object=='Wall':
					print('Wall')
					OffSetY=OffSetY-1
					CheckX=RoomCenterX
					CheckY=RoomCenterY+OffSetY
					CheckCounter=0
					CheckCounterMax=len(Labyrinth)
					FoundSomething=CheckSpace(Labyrinth, CheckX, CheckY)
					if FoundSomething:
						print('Found Something')
						while CheckCounter < CheckCounterMax:
							CheckObject=Labyrinth[CheckCounter]
							CheckObjectX=Labyrinth[CheckCounter+1]
							CheckObjectY=Labyrinth[CheckCounter+2]
							if CheckObjectX==CheckX and CheckObjectY==CheckY:
								if CheckObject=='Floor':
									Labyrinth[LabCounter]='Floor'
									print('Floor')
							CheckCounter=CheckCounter+3
					else:
						return
					
			LabCounter=LabCounter+3
		OffSetY=OffSetY-1
	return

# Looks wether another room wants to make an opening in the current room
def CheckRoomLeft(Labyrinth, RoomCenterX, RoomCenterY):
	print('CheckRoomLeft', RoomCenterX, RoomCenterY)
	OffSetX=-1
	while OffSetX > -8:
		LabCounter=0
		LabCounterMax=len(Labyrinth)
		while LabCounter < LabCounterMax:
			Object=Labyrinth[LabCounter]
			ObjectX=Labyrinth[LabCounter+1]
			ObjectY=Labyrinth[LabCounter+2]
			if ObjectX==(RoomCenterX+OffSetX) and ObjectY==RoomCenterY:
				if Object=='Wall':
					print('Wall')
					OffSetX=OffSetX-1
					CheckX=RoomCenterX+OffSetX
					CheckY=RoomCenterY
					CheckCounter=0
					CheckCounterMax=len(Labyrinth)
					FoundSomething=CheckSpace(Labyrinth, CheckX, CheckY)
					if FoundSomething:
						print('Found Something')
						while CheckCounter < CheckCounterMax:
							CheckObject=Labyrinth[CheckCounter]
							CheckObjectX=Labyrinth[CheckCounter+1]
							CheckObjectY=Labyrinth[CheckCounter+2]
							if CheckObjectX==CheckX and CheckObjectY==CheckY:
								if CheckObject=='Floor':
									Labyrinth[LabCounter]='Floor'
									print('Floor')
							CheckCounter=CheckCounter+3
					else:
						return
					
			LabCounter=LabCounter+3
		OffSetX=OffSetX-1
	return

# Function that checks for surrounding rooms
def CheckNextRoom(Labyrinth, RoomPos):
	print('CheckNextRoom')
	Counter=0
	MaxCounter=len(RoomPos)
	while Counter < MaxCounter:
		RoomCenterX=RoomPos[Counter]
		RoomCenterY=RoomPos[Counter+1]
		CheckRoomUp(Labyrinth, RoomCenterX, RoomCenterY)
		CheckRoomRight(Labyrinth, RoomCenterX, RoomCenterY)
		CheckRoomDown(Labyrinth, RoomCenterX, RoomCenterY)
		CheckRoomLeft(Labyrinth, RoomCenterX, RoomCenterY)
		Counter=Counter+2
	return(Labyrinth)

# Generates a room per room positions found in the RoomPos array
def GenerateRooms(RoomPos):
	print('GenerateRooms')
	Counter=0
	MaxCounter=len(RoomPos)
	while Counter < MaxCounter:
		RoomCenterX=RoomPos[Counter]
		RoomCenterY=RoomPos[Counter+1]
		NumberofExits=random.randint(1, 4)
		print('Generating room', RoomCenterX, RoomCenterY)
		RoomSize=random.randint(1, 4)
		ExitCounter=0
		ExitUp=False
		ExitRight=False
		ExitDown=False
		ExitLeft=False
		while ExitCounter < NumberofExits:
			ExitDir=random.randint(1, 4)
			if ExitDir==1:
				if RoomCenterY != (Level*8):
					ExitUp=True
					BuildTunnelUp(RoomCenterX, RoomCenterY, RoomSize)
				else:
					ExitDown=True
					BuildTunnelDown(RoomCenterX, RoomCenterY, RoomSize)
			if ExitDir==2:
				if RoomCenterX != (Level*8):
					ExitRight=True
					BuildTunnelRight(RoomCenterX, RoomCenterY, RoomSize)
				else:
					ExitLeft=True
					BuildTunnelLeft(RoomCenterX, RoomCenterY, RoomSize)
			if ExitDir==3:
				if RoomCenterY != (Level*-8):
					ExitDown=True
					BuildTunnelDown(RoomCenterX, RoomCenterY, RoomSize)
				else:
					ExitUp=True
					BuildTunnelUp(RoomCenterX, RoomCenterY, RoomSize)
			if ExitDir==4:
				if RoomCenterX != (Level*-8):
					ExitLeft=True
					BuildTunnelLeft(RoomCenterX, RoomCenterY, RoomSize)
				else:
					ExitRight=True
					BuildTunnelRight(RoomCenterX, RoomCenterY, RoomSize)
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
			if Xleft==RoomCenterX and ExitUp:
				Labyrinth.append('Floor')
			else:
				Labyrinth.append('Wall')
			Labyrinth.append(Xleft)
			Labyrinth.append(YTop)
			Xleft=Xleft+1
		YTop=RoomCenterY+RoomSize
		YBottom=RoomCenterY-RoomSize
		XRight=RoomCenterX+RoomSize
		while YTop >= YBottom:
			if YTop==RoomCenterY and ExitRight:
				Labyrinth.append('Floor')
			else:
				Labyrinth.append('Wall')
			Labyrinth.append(XRight)
			Labyrinth.append(YTop)
			YTop=YTop-1
		YBottom=RoomCenterY-RoomSize
		Xleft=RoomCenterX-RoomSize
		XRight=RoomCenterX+RoomSize
		while XRight >= Xleft:
			if XRight==RoomCenterX and ExitDown:
				Labyrinth.append('Floor')
			else:
				Labyrinth.append('Wall')
			Labyrinth.append(XRight)
			Labyrinth.append(YBottom)
			XRight=XRight-1
		YBottom=RoomCenterY-RoomSize
		Xleft=RoomCenterX-RoomSize
		YTop=RoomCenterY+RoomSize
		while YBottom <= YTop:
			if YBottom==RoomCenterY and ExitLeft:
				Labyrinth.append('Floor')
			else:
				Labyrinth.append('Wall')
			Labyrinth.append(Xleft)
			Labyrinth.append(YBottom)
			YBottom=YBottom+1

		Counter=Counter+2
	return

# Sticks stairs to the next level in a random room
def PlaceStairs(Labyrinth):
	print('PlaceStairs')
	StairsXMin=-1*Level
	StairsXMax=Level
	StairsYMin=-1*Level
	StairsYMax=Level
	LookingForASpot=True
	while LookingForASpot:
		StairsX=random.randint(StairsXMin, StairsXMax)*8
		StairsY=random.randint(StairsYMin, StairsYMax)*8
		Counter=0
		MaxCounter=len(Labyrinth)
		while Counter < MaxCounter:
			Object=Labyrinth[Counter]
			ObjectX=Labyrinth[Counter+1]
			ObjectY=Labyrinth[Counter+2]
			if ObjectX==StairsX and ObjectY==StairsY and Object=='Floor':
				Labyrinth[Counter]='Stairs'
				LookingForASpot=False
				break
			Counter=Counter+3
	return

# I don't use this function anymore, my code has evolved!
def DoOuterWall(Level):
	print('DoOuterWall')
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
	print('GenerateLabyrinth')
	#DoOuterWall(Level)
	GenerateRoomPos(Level)
	GenerateRooms(RoomPos)
	return

# Main loop
Level=0
while Level < 11:
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
			LoadingText='Cooking next level...'
			LoadingTextSurf = myfont.render(LoadingText, False, green)
			screen.blit(LoadingTextSurf,(0,780))
			pygame.display.flip()
			Level=Level+1
			NextLevel=False
			Running=False
			if Level < 11:
				del Labyrinth[:]
				GenerateLabyrinth()
				CheckNextRoom(Labyrinth, RoomPos)
				NumberofStairs=int(Level/2)
				if NumberofStairs==0:
					NumberofStairs=1
				StairCounter=0
				while StairCounter < NumberofStairs:
					PlaceStairs(Labyrinth)
					StairCounter=StairCounter+1
			Ping.play()
wait()
sys.exit()
