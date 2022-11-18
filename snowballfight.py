# [게임 목표]
# 1. player는 위,아래로 이동가능 ㅇ 11/07
# 2. 각각 ctrl를 누르면 눈이 날라감 ㅇ 11/08
# 3. 눈이 상대방에게 맞으면 모양이 바뀐 후 사라짐 o 11/08 가능하면 효과음도 넣고 싶음
# 4. 눈에 맞으면 체력이 깎임 가능하면 약간 멈추게 하고 싶음 (x), 체력은 아래 표시 o 11/09
# 5. 아이템은 눈을 맞춰 얻음, 아이템은 특정 시간이 지났을 때 생성 , 얻은 아이템은 체력 위에 표시 , 아이템은 3개까지만 가질 수 있음 11/10 o
# 6. 아이템은 각 shift키를 눌러 사용 가능 (하트-체력 1 회복, 방어-방어막 생성, 독약-상대방의 속도 느려짐 회복약-속도 회복) 11/11 o
# 7. 체력이 0이 되면 게임 종료 o 11/09
# 8. 게임 시작전에 게임 화면을 만들고 싶음 (설명, 게임시작 버튼) 11/12 o
# 9. 게임이 종료되면 player1 win! , player2 win! 메세지 화면에 띄우기 11/12 o
# 10. 캐릭터 선택 (직업마다 속도가 다르다던지, 던질 수 있는 눈 개수가 다르다던지, 눈 속도가 다르다던지...)

import pygame
import numpy as np
import random
import sys

pygame.init()

white = (255,255,255)
green = (0,200,0)
blue = (0,0,255)
black = (0,0,0)
screen_width = 1024
screen_height = 512
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('snowball fight')

running = True
clock = pygame.time.Clock()

itemtime = pygame.USEREVENT + 1 # 아이템 생성을 위한 이벤트
pygame.time.set_timer(itemtime, 10000) # 10초마다 이벤트 발생

game_font = pygame.font.Font(None, 40)
game_result = "game over"  # 게임 종료 메시지

player_1 = pygame.image.load("C:/Users/82107/OneDrive - 서울과학기술대학교/바탕 화면/오픈소스소프트웨어/image/player1.png")
player_1 = pygame.transform.scale(player_1, (60, 70))

player_2 = pygame.image.load("C:/Users/82107/OneDrive - 서울과학기술대학교/바탕 화면/오픈소스소프트웨어/image/player2.png")
player_2 = pygame.transform.scale(player_2, (60, 70))

snowball = pygame.image.load("C:/Users/82107/OneDrive - 서울과학기술대학교/바탕 화면/오픈소스소프트웨어/image/snowball.png")
snowball = pygame.transform.scale(snowball, (20, 20))

snow = pygame.image.load("C:/Users/82107/OneDrive - 서울과학기술대학교/바탕 화면/오픈소스소프트웨어/image/snow.png")
snow = pygame.transform.scale(snow, (20, 20))

heart = pygame.image.load("C:/Users/82107/OneDrive - 서울과학기술대학교/바탕 화면/오픈소스소프트웨어/image/heart.png")
heart = pygame.transform.scale(heart, (20, 20))

i_heart = pygame.image.load("C:/Users/82107/OneDrive - 서울과학기술대학교/바탕 화면/오픈소스소프트웨어/image/heart.png")
i_heart = pygame.transform.scale(i_heart, (20, 20))

i_shield = pygame.image.load("C:/Users/82107/OneDrive - 서울과학기술대학교/바탕 화면/오픈소스소프트웨어/image/shield.png")
i_shield = pygame.transform.scale(i_shield, (20, 20))

i_poison = pygame.image.load("C:/Users/82107/OneDrive - 서울과학기술대학교/바탕 화면/오픈소스소프트웨어/image/poison.png")
i_poison = pygame.transform.scale(i_poison, (20, 20))

i_medicine = pygame.image.load("C:/Users/82107/OneDrive - 서울과학기술대학교/바탕 화면/오픈소스소프트웨어/image/medicine.png")
i_medicine = pygame.transform.scale(i_medicine, (20, 20))

shield = pygame.image.load("C:/Users/82107/OneDrive - 서울과학기술대학교/바탕 화면/오픈소스소프트웨어/image/sshield.png")

ex_key = pygame.image.load("C:/Users/82107/OneDrive - 서울과학기술대학교/바탕 화면/오픈소스소프트웨어/image/keyex.png")
ex_item = pygame.image.load("C:/Users/82107/OneDrive - 서울과학기술대학교/바탕 화면/오픈소스소프트웨어/image/itemex.png")

    
# 시작 화면 
def StartScreen():    

    # 제목 
    titleFont = pygame.font.SysFont("malgungothic", 100)
    title = titleFont.render('눈싸움 게임',True,black,white)
    title_rect = title.get_rect(center=(screen_width/2,screen_height/3))
    screen.blit(title,title_rect)

    # 버튼
    bt_width = 100
    bt_height = 50 
    btst_xy = [screen_width/4, 2 * screen_height / 3 + 25]
    btex_xy = [3*screen_width/4 - 100, 2 * screen_height / 3 + 25]

    bottonFont = pygame.font.SysFont("malgungothic", 50)
    btst = bottonFont.render('게임 시작',True,white,green)
    btst_rect = btst.get_rect(center=(btst_xy[0]+(bt_width/2),btst_xy[1]+(bt_height/2)))

    btex = bottonFont.render('게임 설명',True,white,blue)
    btex_rect = btex.get_rect(center=(btex_xy[0]+(bt_width/2),btex_xy[1]+(bt_height/2)))

    while True:
        
        screen.fill(white)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # 게임 시작 버튼을 누르면 게임 시작
        if (btst_xy[0] + bt_width > mouse[0]) and (mouse[0] >btst_xy[0] ) and (btst_xy[1] + bt_height > mouse[1] ) and (mouse[1] > btst_xy[1]):
            if click[0] == 1 : 
                runGame()

        # 게임 설명 버튼을 누르면 게임 설명 화면으로 전환 
        if (btex_xy[0] + bt_width > mouse[0]) and (mouse[0] >btex_xy[0] ) and (btex_xy[1] + bt_height > mouse[1] ) and (mouse[1] > btex_xy[1]):
            if click[0] == 1 : 
                explainGame()
        
        screen.blit(title,title_rect)
        screen.blit(btst,btst_rect)
        screen.blit(btex,btex_rect)
        
        pygame.display.update()

# 게임 설명 화면 
def explainGame():

    # 게임 시작 버튼
    bt_width = 100
    bt_height = 50 
    btst_xy = [7.5 * screen_width / 9,  8 * screen_height / 9]
    
    bottonFont = pygame.font.SysFont("malgungothic", 30)
    btst = bottonFont.render('게임 시작',True,white,green)
    btst_rect = btst.get_rect(center=(btst_xy[0]+(bt_width/2),btst_xy[1]+(bt_height/2)))

    # 제목
    titleFont = pygame.font.SysFont("malgungothic", 45)
    title = titleFont.render('[게임 설명]',True,black,white)
    title_rect = title.get_rect(center=(screen_width/2,screen_height/12)) 
    
    # 승리 조건 문장
    textFont = pygame.font.SysFont("malgungothic", 30)
    text = textFont.render('상대방의 체력을 0으로 만들면 승리!',True,black)

    while True:
        global ex_key, ex_item

        screen.fill(white)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # 시작 버튼 클릭
        if (btst_xy[0] + bt_width > mouse[0]) and (mouse[0] >btst_xy[0] ) and (btst_xy[1] + bt_height > mouse[1] ) and (mouse[1] > btst_xy[1]):
            if click[0] == 1 : 
                runGame()
        
        screen.blit(btst,btst_rect)
        screen.blit(title,title_rect)
        screen.blit(ex_key,(50,screen_height/9 + 30))
        screen.blit(ex_item,(600,screen_height/9 + 30))
        screen.blit(text,(270,screen_height/9 + 403))
        pygame.display.update()

        
# 게임 실행
def runGame():
    global running, player_1, player_2, snowball, heart, i_heart, i_shield, shield, i_poison, i_medicine, game_result

    x1 = screen_width * 0.05
    y1 = screen_height * 0.08

    x2 = screen_width * 0.9
    y2 = screen_height * 0.08

    p1_speed = 10 # player1의 이동 속도
    p2_speed = 10 # player2의 이동 속도

    sb1_xy=[]
    sb2_xy=[]

    hit1 = False
    hit2 = False

    heart1 = 3 # 기본 체력
    heart2 = 3
    heart1_xy = [[i*30+10,490] for i in range(heart1)]
    heart2_xy = [[1000-30*i,490] for i in range(heart2)]

    items = [i_heart, i_shield, i_poison, i_medicine] 
    prob_items = [10/100,50/100,20/100,20/100] 
    item_xy = [] 
    item = [] 

    p1_item = [] # player1의 아이템 목록
    p2_item = [] # player2의 아이템 목록

    p1_shield = False
    p2_shield = False

    while running:
        clock.tick(60)
        screen.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == itemtime: # 5초마다 아이템 생성
                if len(item) == 0 : # 생성되어 있는 아이템이 없어야 아이템 생성
                    item.append(np.random.choice(items,p=prob_items)) # 확률에 따라 아이템 생성
                    item_xy.append([1024*0.46+20,random.randint(1,440)]) # 아이템 좌표 랜덤 설정
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w: # player1의 이동
                    if y1 >= 0: # player가 화면 바깥으로 벗어나지 않도록 하기 위함
                        y1 -= p1_speed
                elif event.key == pygame.K_s:
                    if y1 <= 420: 
                        y1 += p1_speed
                elif event.key == pygame.K_UP: # player2의 이동
                    if y2 >= 0: # player가 화면 바깥으로 벗어나지 않도록 하기 위함
                        y2 -= p2_speed
                elif event.key == pygame.K_DOWN:
                    if y2 <= 420:
                        y2 += p2_speed

                elif event.key == pygame.K_LCTRL: # player1의 눈 던지기
                    x_s = x1 + 30
                    y_s = y1 + 25
                    sb1_xy.append([x_s,y_s])
                elif event.key == pygame.K_RCTRL: # player2의 눈 던지기
                    x_s = x2 + 30
                    y_s = y2 + 25
                    sb2_xy.append([x_s,y_s])

                elif event.key == pygame.K_LSHIFT: # player1의 아이템 사용
                    if len(p1_item) != 0 :
                        if p1_item[0] == i_heart : # 사용한 아이템이 하트일때 체력 회복
                            if heart1 < 3 :
                                heart1 = heart1 + 1
                                heart1_xy.append([(heart1-1)*30+10,490])
                        elif p1_item[0] == i_shield : # 사용한 아이템이 방패일때 방패 생성
                            p1_shield = True
                        elif p1_item[0] == i_poison: # 사용한 아이템이 독일때 player2의 속도 낮춤 
                            if p2_speed == 10:
                                p2_speed = p2_speed - 5
                        else : # 사용한 아이템이 회복약일때 player1의 속도 회복
                            if p1_speed == 5:
                                p1_speed = p1_speed + 5       
                        p1_item.remove(p1_item[0]) # 사용한 아이템 삭제

                elif event.key == pygame.K_RSHIFT: # player2의 아이템 사용
                    if len(p2_item) != 0 :
                        if p2_item[0] == i_heart : # 사용한 아이템이 하트일때 체력 회복
                            if heart2 < 3 :
                                heart2 = heart2 + 1
                                heart2_xy.append([1000-30*(heart2-1),490])
                        elif p2_item[0] == i_shield : # 사용한 아이템이 방패일때 방패 생성
                            p2_shield = True
                        elif p2_item[0] == i_poison: # 사용한 아이템이 독일때 player1의 속도 낮춤 
                            if p1_speed == 10:
                                p1_speed = p1_speed - 5
                        else : # 사용한 아이템이 회복약일때 player2의 속도 회복
                            if p2_speed == 5:
                                p2_speed = p2_speed + 5       
                        p2_item.remove(p2_item[0])
            
                     
        # player1의 눈이 충돌했을 경우 
        if len(sb1_xy) != 0:
            for i,xy in enumerate(sb1_xy): # 날라가는 눈 표현
                xy[0] += 15
                sb1_xy[i][0] = xy[0]
                if xy[0] >= 1024: # 눈이 화면에 닿을때
                    sb1_xy.remove(xy)
                if xy[0] > x2: # player1의 눈이 player2에게 맞았을때
                    if xy[1] >= y2 and xy[1] <= y2 + 60: 
                        sb1_xy.remove(xy) 
                        hit2 = True
                if len(item_xy) != 0 : 
                    if xy[0] >= item_xy[0][0]: # player1이 아이템을 맞췄을때
                        if xy[1] >= item_xy[0][1] -10 and xy[1] <= item_xy[0][1] + 15:
                            if len(p1_item) < 3 : # player1이 가지고 있는 아이템이 3개 이하일때 player1 아이템 목록에 추가
                                p1_item.append(item[0])
                            item.remove(item[0])
                            item_xy.remove(item_xy[0])
                            sb1_xy.remove(xy)
                if p2_shield: # 상대방의 방어막을 맞췄을때 
                    if xy[0] > x2 -20:
                        if xy[1] >= y2 + 5 and xy[1] <= y2 + 45:
                            screen.blit(snow,(x2-20,y2))
                            sb1_xy.remove(xy)
                            p2_shield = False
 
        # player2의 눈이 충돌했을 경우
        if len(sb2_xy) != 0:
            for i,xy in enumerate(sb2_xy): # 날라가는 눈 표현
                xy[0] -= 15
                sb2_xy[i][0] = xy[0]
                if xy[0] <= 0: # 눈이 화면에 닿을때
                    sb2_xy.remove(xy)
                if xy[0] < x1:  # player2의 눈이 player1에게 맞았을때
                    if xy[1] >= y1 and xy[1] <= y1 + 60:
                        sb2_xy.remove(xy)
                        hit1 = True
                if len(item_xy) != 0 : 
                    if xy[0] <= item_xy[0][0]: # player2가 아이템을 맞췄을때
                        if xy[1] >= item_xy[0][1] - 10 and xy[1] <= item_xy[0][1] + 15:
                            if len(p2_item) < 3 : # player2이 가지고 있는 아이템이 3개 이하일때 player2 아이템 목록에 추가
                                p2_item.append(item[0])
                            item.remove(item[0])
                            item_xy.remove(item_xy[0])
                            sb2_xy.remove(xy)
                if p1_shield: # 상대방의 방어막을 맞췄을때 
                    if xy[0] < x1 + 70:
                        if xy[1] >= y1 + 5 and xy[1] <= y1 + 45:
                            screen.blit(snow,(x1+60,y1))
                            sb2_xy.remove(xy)
                            p1_shield = False
                            
        if len(sb1_xy) != 0: # player1의 눈 표시
            for x_s,y_s in sb1_xy:
                screen.blit(snowball,(x_s,y_s))

        if len(sb2_xy) != 0: # player2의 눈 표시
            for x_s,y_s in sb2_xy:
                screen.blit(snowball,(x_s,y_s))
        
        if hit1: # player1이 눈에 맞았을 때
            screen.blit(snow,(x1+60,y1))
            heart1_xy.remove(heart1_xy[heart1-1]) # 체력 하나 차감
            heart1 = heart1 - 1
            hit1 = False
        
        if hit2: # player2가 눈에 맞았을 때
            screen.blit(snow,(x2-20,y2))
            heart2_xy.remove(heart2_xy[heart2-1]) # 체력 하나 차감
            heart2 = heart2 - 1
            hit2 = False

        if len(heart1_xy) == 0: # player1의 체력이 0이면 게임 종료
                game_result = "player2 win!" # 게임 결과 : player2의 승리
                running = False

        if len(heart2_xy) == 0: # player2의 체력이 0이면 게임 종료
                game_result = "player1 win!" # 게임 결과 : player1의 승리
                running = False

        for x,y in heart1_xy: # player1의 체력 표시
            screen.blit(heart,(x,y))

        for x,y in heart2_xy: # player2의 체력 표시
            screen.blit(heart,(x,y))

        if len(item) != 0:  # 랜덤 아이템 표시
            screen.blit(item[0],(item_xy[0]))


        if len(p1_item) != 0 : # player1의 아이템 표시
            for x in range(len(p1_item)):
                screen.blit(p1_item[x],(x*30+10,460))

        if len(p2_item) != 0 : # player2의 아이템 표시
            for x in range(len(p2_item)):
                screen.blit(p2_item[x],(1000-30*x,460))
       

        if len(item) != 0:  # 아이템 표시
            screen.blit(item[0],(item_xy[0]))

        if p1_shield: # player1 방어막 표시
            screen.blit(shield,(x1+70,y1+15))
 
        if p2_shield: # player2 방어막 표시
            screen.blit(shield,(x2-20,y2+15))
        
        screen.blit(player_1,(x1,y1)) 
        screen.blit(player_2,(x2,y2))
        pygame.display.update()

    if not running: # 게임이 종료 되면 결과 메시지 출력 후 종료
        msg = game_font.render(game_result, True, (0,0,0))
        msg_rect = msg.get_rect(center=(512,256))
        screen.blit(msg, msg_rect)
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()

StartScreen() # 시작 화면
    






