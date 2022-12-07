import pygame
import numpy as np
import random
import sys

pygame.init()

white = (255,255,255)
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



player_1 = pygame.image.load("image/player1.png")
player_1 = pygame.transform.scale(player_1, (60, 70))

player_2 = pygame.image.load("image/player2.png")
player_2 = pygame.transform.scale(player_2, (60, 70))

snowball = pygame.image.load("image/snowball.png")
snowball = pygame.transform.scale(snowball, (20, 20))

snow = pygame.image.load("image/snow.png")
snow = pygame.transform.scale(snow, (20, 20))

heart = pygame.image.load("image/heart.png")
heart = pygame.transform.scale(heart, (20, 20))

i_heart = pygame.image.load("image/heart.png")
i_heart = pygame.transform.scale(i_heart, (20, 20))

i_shield = pygame.image.load("image/shield.png")
i_shield = pygame.transform.scale(i_shield, (20, 20))

i_poison = pygame.image.load("image/poison.png")
i_poison = pygame.transform.scale(i_poison, (20, 20))

i_medicine = pygame.image.load("image/medicine.png")
i_medicine = pygame.transform.scale(i_medicine, (20, 20))

shield = pygame.image.load("image/sshield.png")


title = pygame.image.load("image/title.png")
explanation = pygame.image.load("image/explanation.png")
explanation1 = pygame.image.load("image/explanation1.png")
gamestart = pygame.image.load("image/gamestart.png")
gamestart1 = pygame.image.load("image/gamestart1.png")
gamestart1 = pygame.transform.scale(gamestart1,(200,80))
ex_text = pygame.image.load("image/ex_text.png")
winex = pygame.image.load("image/winex.png")

btup = pygame.image.load("image/btup.png")
btup = pygame.transform.scale(btup, (70, 40))
btdown = pygame.image.load("image/btdown.png")
btdown = pygame.transform.scale(btdown, (70, 40))
p1_text = pygame.image.load("image/p1_text.png")
p2_text = pygame.image.load("image/p2_text.png")
p1_text = pygame.transform.scale(p1_text, (100, 40))
p2_text = pygame.transform.scale(p2_text, (102, 42))
stat_title = pygame.image.load("image/stat_title.png")
speed = pygame.image.load("image/speed.png")
snowmax = pygame.image.load("image/snowmax.png")
snowspeed = pygame.image.load("image/snowspeed.png")
stat_text = pygame.image.load("image/stat.png")
# 시작 화면 
def StartScreen():    

    # 제목 
    title_rect = title.get_rect(center=(screen_width/2,screen_height/3))
    screen.blit(title,title_rect)

    # 버튼
    bt_width = 200
    bt_height = 80 
    btst_xy = [screen_width/6, 2 * screen_height / 3 + 25]
    btex_xy = [3*screen_width/4 - 100, 2 * screen_height / 3 + 25]

    # 게임 시작 버튼, 게임 설명 버튼 
    gamestart_rect = gamestart.get_rect(center=(btst_xy[0]+(bt_width/2),btst_xy[1]+(bt_height/2)))
    explanation_rect = explanation.get_rect(center=(btex_xy[0]+(bt_width/2),btex_xy[1]+(bt_height/2)))

    while True:
        
        screen.fill(white)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # 게임 시작 버튼을 누르면 스텟 분배 화면으로 전환
        if (btst_xy[0] + bt_width > mouse[0]) and (mouse[0] >btst_xy[0] ) and (btst_xy[1] + bt_height > mouse[1] ) and (mouse[1] > btst_xy[1]):
            if click[0] == 1 : 
                stat()

        # 게임 설명 버튼을 누르면 게임 설명 화면으로 전환 
        if (btex_xy[0] + bt_width > mouse[0]) and (mouse[0] >btex_xy[0] ) and (btex_xy[1] + bt_height > mouse[1] ) and (mouse[1] > btex_xy[1]):
            if click[0] == 1 : 
                explainGame()
        
        screen.blit(title,title_rect)
        screen.blit(gamestart,gamestart_rect)
        screen.blit(explanation,explanation_rect)
        
        pygame.display.update()

# 게임 설명 화면 
def explainGame():

    # 게임 시작 버튼 위치
    bt_width = 200
    bt_height = 80 
    btst_xy = [7 * screen_width / 9,  5 * screen_height / 6]
    
    # 게임 시작 버튼 
    gamestart1_rect = gamestart1.get_rect(center=(btst_xy[0]+(bt_width/2),btst_xy[1]+(bt_height/2)))

    # 제목 (게임설명)
    explanation1_rect = explanation.get_rect(center=(screen_width/2+20,screen_height/6))
    

    while True:

        screen.fill(white)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # 시작 버튼 클릭하면 스텟 분배 화면으로 전환
        if (btst_xy[0] + bt_width > mouse[0]) and (mouse[0] >btst_xy[0] ) and (btst_xy[1] + bt_height > mouse[1] ) and (mouse[1] > btst_xy[1]):
            if click[0] == 1 : 
                stat()
        
        screen.blit(gamestart1,gamestart1_rect)
        screen.blit(explanation1,explanation1_rect)
        screen.blit(ex_text,(30,screen_height/9 + 50))
        pygame.display.update()
    

# 스텟 분배 화면
def stat():
    global p1_speed, p2_speed, snowmax_1, snowmax_2, snspeed_1, snspeed_2
  
    # 제목 
    stat_rect = stat_title.get_rect(center=(screen_width/2,screen_height/10))

    # 게임 시작 버튼
    btst_width = 200
    btst_height = 80 
    btst_xy = [7*screen_width/9,screen_height/30]
    gamestart1_rect = gamestart1.get_rect(center=(btst_xy[0]+(btst_width/2),btst_xy[1]+(btst_height/2)))

    # 버튼 크기  
    bt_width = 70
    bt_height = 40 

    # 버튼 좌표
    btup1_xy = [[270*i+140, 240] for i in range(0,3)]
    btdown1_xy = [[270*i+210, 238] for i in range(0,3)]
    btup2_xy = [[270*i+140, 440] for i in range(0,3)]
    btdown2_xy = [[270*i+210, 438] for i in range(0,3)]

    # player1 버튼 
    btup11_rect = btup.get_rect(center=(btup1_xy[0][0]+(bt_width/2),btup1_xy[0][1]+(bt_height/2)))
    btup12_rect = btup.get_rect(center=(btup1_xy[1][0]+(bt_width/2),btup1_xy[1][1]+(bt_height/2)))
    btup13_rect = btup.get_rect(center=(btup1_xy[2][0]+(bt_width/2),btup1_xy[2][1]+(bt_height/2)))
    btdown11_rect = btdown.get_rect(center=(btdown1_xy[0][0]+(bt_width/2),btdown1_xy[0][1]+(bt_height/2)))
    btdown12_rect = btdown.get_rect(center=(btdown1_xy[1][0]+(bt_width/2),btdown1_xy[1][1]+(bt_height/2)))
    btdown13_rect = btdown.get_rect(center=(btdown1_xy[2][0]+(bt_width/2),btdown1_xy[2][1]+(bt_height/2)))
    #player2 버튼 
    btup21_rect = btup.get_rect(center=(btup2_xy[0][0]+(bt_width/2),btup2_xy[0][1]+(bt_height/2)))
    btup22_rect = btup.get_rect(center=(btup2_xy[1][0]+(bt_width/2),btup2_xy[1][1]+(bt_height/2)))
    btup23_rect = btup.get_rect(center=(btup2_xy[2][0]+(bt_width/2),btup2_xy[2][1]+(bt_height/2)))
    btdown21_rect = btdown.get_rect(center=(btdown2_xy[0][0]+(bt_width/2),btdown2_xy[0][1]+(bt_height/2)))
    btdown22_rect = btdown.get_rect(center=(btdown2_xy[1][0]+(bt_width/2),btdown2_xy[1][1]+(bt_height/2)))
    btdown23_rect = btdown.get_rect(center=(btdown2_xy[2][0]+(bt_width/2),btdown2_xy[2][1]+(bt_height/2)))

    # 기본 스텟 
    p1_speed = 1 # player1의 기본 이동 속도
    p2_speed = 1 # player2의 기본 이동 속도
    snowmax_1 = 0 # player1의 기본 눈 최대 개수
    snowmax_2 = 0 # player2의 기본 눈 최대 개수
    snspeed_1 = 8 # player1의 기본 눈 속력
    snspeed_2 = 8 # player2의 기본 눈 속력

    # 스텟 분배량
    stat_speed1 = 0
    stat_snowmax1 = 0
    stat_snspeed1 = 0
    stat_speed2 = 0
    stat_snowmax2 = 0
    stat_snspeed2 = 0
    
    # 남은 스텟 
    stat1 = 10 
    stat2 = 10

    # 글자 폰트 설정 
    game_font = pygame.font.SysFont("Monospace", 40)

    
    while True:

        screen.fill(white)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # 마우스를 클릭했을때 
            if event.type == pygame.MOUSEBUTTONUP:
                mouse = pygame.mouse.get_pos()
                # player1의 이동 속도 스텟 증가 버튼 클릭 
                if (btup1_xy[0][0] + bt_width > mouse[0]) and (mouse[0] >btup1_xy[0][0] ) and (btup1_xy[0][1] + bt_height > mouse[1] ) and (mouse[1] > btup1_xy[0][1]):
                    if stat_speed1 < 10 and stat1 > 0 :
                        stat_speed1 = stat_speed1 + 1
                        stat1 = stat1 - 1
                # player1의 이동 속도 스텟 감소 버튼 클릭 
                if (btdown1_xy[0][0] + bt_width > mouse[0]) and (mouse[0] >btdown1_xy[0][0] ) and (btdown1_xy[0][1] + bt_height > mouse[1] ) and (mouse[1] > btdown1_xy[0][1]):
                    if stat_speed1 > 0 and stat1 < 10:
                        stat_speed1 = stat_speed1 - 1
                        stat1 = stat1 + 1
                # player1의 눈 최대 개수 스텟 증가 버튼 클릭 
                if (btup1_xy[1][0] + bt_width > mouse[0]) and (mouse[0] >btup1_xy[1][0] ) and (btup1_xy[1][1] + bt_height > mouse[1] ) and (mouse[1] > btup1_xy[1][1]):
                    if stat_snowmax1 < 10 and stat1 > 0:
                        stat_snowmax1 = stat_snowmax1 + 1
                        stat1 = stat1 - 1
                # player1의 눈 최대 개수 스텟 감소 버튼 클릭 
                if (btdown1_xy[1][0] + bt_width > mouse[0]) and (mouse[0] >btdown1_xy[1][0] ) and (btdown1_xy[1][1] + bt_height > mouse[1] ) and (mouse[1] > btdown1_xy[1][1]):
                    if stat_snowmax1 > 0 and stat1 < 10 :
                        stat_snowmax1 = stat_snowmax1 - 1
                        stat1 = stat1 + 1
                # player1의 눈 속력 스텟 증가 버튼 클릭 
                if (btup1_xy[2][0] + bt_width > mouse[0]) and (mouse[0] >btup1_xy[2][0] ) and (btup1_xy[2][1] + bt_height > mouse[1] ) and (mouse[1] > btup1_xy[2][1]):
                    if stat_snspeed1 < 10 and stat1 > 0:
                        stat_snspeed1 = stat_snspeed1 + 1
                        stat1 = stat1 - 1
                # player1의 눈 속력 스텟 감소 버튼 클릭 
                if (btdown1_xy[2][0] + bt_width > mouse[0]) and (mouse[0] >btdown1_xy[2][0] ) and (btdown1_xy[2][1] + bt_height > mouse[1] ) and (mouse[1] > btdown1_xy[2][1]):
                    if stat_snspeed1 > 0 and stat1 < 10:
                        stat_snspeed1 = stat_snspeed1 - 1
                        stat1 = stat1 + 1
                
                # player2의 이동 속도 스텟 증가 버튼 클릭 
                if (btup2_xy[0][0] + bt_width > mouse[0]) and (mouse[0] >btup2_xy[0][0] ) and (btup2_xy[0][1] + bt_height > mouse[1] ) and (mouse[1] > btup2_xy[0][1]):
                    if stat_speed2 < 10 and stat2 > 0 :
                        stat_speed2 = stat_speed2 + 1
                        stat2 = stat2 - 1
                # player2의 이동 속도 스텟 감소 버튼 클릭 
                if (btdown2_xy[0][0] + bt_width > mouse[0]) and (mouse[0] >btdown2_xy[0][0] ) and (btdown2_xy[0][1] + bt_height > mouse[1] ) and (mouse[1] > btdown2_xy[0][1]):
                    if stat_speed2 > 0 and stat2 < 10:
                        stat_speed2 = stat_speed2 - 1
                        stat2 = stat2 + 1
                # player2의 눈 최대 개수 스텟 증가 버튼 클릭 
                if (btup2_xy[1][0] + bt_width > mouse[0]) and (mouse[0] >btup2_xy[1][0] ) and (btup2_xy[1][1] + bt_height > mouse[1] ) and (mouse[1] > btup2_xy[1][1]):
                    if stat_snowmax2 < 10 and stat2 > 0:
                        stat_snowmax2 = stat_snowmax2 + 1
                        stat2 = stat2 - 1
                # player2의 눈 최대 개수 스텟 감소 버튼 클릭 
                if (btdown2_xy[1][0] + bt_width > mouse[0]) and (mouse[0] >btdown2_xy[1][0] ) and (btdown2_xy[1][1] + bt_height > mouse[1] ) and (mouse[1] > btdown2_xy[1][1]):
                    if stat_snowmax2 > 0 and stat2 < 10:
                        stat_snowmax2 = stat_snowmax2 - 1
                        stat2 = stat2 + 1
                # player2의 눈 속력 스텟 증가 버튼 클릭 
                if (btup2_xy[2][0] + bt_width > mouse[0]) and (mouse[0] >btup2_xy[2][0] ) and (btup2_xy[2][1] + bt_height > mouse[1] ) and (mouse[1] > btup2_xy[2][1]):
                    if stat_snspeed2 < 10 and stat2 > 0:
                        stat_snspeed2 = stat_snspeed2 + 1
                        stat2 = stat2 - 1
                # player2의 눈 속력 스텟 감소 버튼 클릭 
                if (btdown2_xy[2][0] + bt_width > mouse[0]) and (mouse[0] >btdown2_xy[2][0] ) and (btdown2_xy[2][1] + bt_height > mouse[1] ) and (mouse[1] > btdown2_xy[2][1]):
                    if stat_snspeed2 > 0 and stat2 < 10:
                        stat_snspeed2 = stat_snspeed2 - 1
                        stat2 = stat2 + 1
                # 게임 시작 버튼 클릭
                if (btst_xy[0] + btst_width - 10 > mouse[0]) and (mouse[0] > btst_xy[0] + 10 ) and (btst_xy[1] + bt_height + 20 > mouse[1] ) and (mouse[1] > btst_xy[1] + 20):
                    p1_speed = p1_speed + 0.5 * stat_speed1
                    p2_speed = p2_speed + 0.5 * stat_speed2
                    snowmax_1 = snowmax_1 + stat_snowmax1
                    snowmax_2 = snowmax_2 + stat_snowmax2 
                    snspeed_1 = snspeed_1 + stat_snspeed1
                    snspeed_2 = snspeed_2 + stat_snspeed2 
                    runGame()


        stat_sp1 = game_font.render(str(stat_speed1),True,(0,0,0))
        stat_snmax1 = game_font.render(str(stat_snowmax1),True,(0,0,0))
        stat_snsp1 = game_font.render(str(stat_snspeed1),True,(0,0,0))
        stat_stat1 = game_font.render(str(stat1),True,(0,0,0))
        stat_sp2 = game_font.render(str(stat_speed2),True,(0,0,0))
        stat_snmax2 = game_font.render(str(stat_snowmax2),True,(0,0,0))
        stat_snsp2 = game_font.render(str(stat_snspeed2),True,(0,0,0))
        stat_stat2 = game_font.render(str(stat2),True,(0,0,0))
        screen.blit(stat_title,stat_rect)
        screen.blit(gamestart1,gamestart1_rect)
        screen.blit(p1_text,(0,240))
        screen.blit(player_1,(30,160))
        screen.blit(btup,btup11_rect)
        screen.blit(btup,btup12_rect)
        screen.blit(btup,btup13_rect)
        screen.blit(btdown,btdown11_rect)
        screen.blit(btdown,btdown12_rect)
        screen.blit(btdown,btdown13_rect)
        screen.blit(p2_text,(0,440))
        screen.blit(player_2,(25,360))
        screen.blit(btup,btup21_rect)
        screen.blit(btup,btup22_rect)
        screen.blit(btup,btup23_rect)
        screen.blit(btdown,btdown21_rect)
        screen.blit(btdown,btdown22_rect)
        screen.blit(btdown,btdown23_rect)

        screen.blit(stat_sp1,(200,180))
        screen.blit(speed,(150,120))
        screen.blit(stat_snmax1,(470,180))
        screen.blit(snowmax,(390,118))
        screen.blit(stat_snsp1,(740,180))
        screen.blit(snowspeed,(690,118))
        screen.blit(stat_stat1,(900,180))
        screen.blit(stat_text,(850,120))

        screen.blit(stat_sp2,(200,380))
        screen.blit(speed,(150,320))
        screen.blit(stat_snmax2,(470,380))
        screen.blit(snowmax,(390,318))
        screen.blit(stat_snsp2,(740,380))
        screen.blit(snowspeed,(690,318))
        screen.blit(stat_stat2,(900,380))
        screen.blit(stat_text,(850,320))

        pygame.display.update()


# 게임 실행
def runGame():
    global running, player_1, player_2, snowball, heart, i_heart, i_shield, shield, i_poison, i_medicine, game_result , p1_speed, p2_speed, snowmax_1, snowmax_2, snspeed_1, snspeed_2

    x1 = screen_width * 0.05
    y1 = screen_height * 0.08

    x2 = screen_width * 0.9
    y2 = screen_height * 0.08

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

    y1_change = 0
    y2_change = 0

    p1_maxspeed = p1_speed
    p2_maxspeed = p2_speed

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
                    y1_change = y1_change - p1_speed
                elif event.key == pygame.K_s:
                    y1_change = y1_change + p1_speed
                elif event.key == pygame.K_UP: # player2의 이동
                    y2_change = y2_change - p2_speed
                elif event.key == pygame.K_DOWN:
                    y2_change = y2_change + p2_speed

                elif event.key == pygame.K_LCTRL: # player1의 눈 던지기
                    if len(sb1_xy) < snowmax_1:
                        x_s = x1 + 30
                        y_s = y1 + 25
                        sb1_xy.append([x_s,y_s])
                elif event.key == pygame.K_RCTRL:
                    if len(sb2_xy) <= snowmax_2: # player2의 눈 던지기
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
                            if p2_speed <= p2_maxspeed and p2_speed - 1 > 0 :
                                p2_speed = p2_speed - 1
                        else : # 사용한 아이템이 회복약일때 player1의 속도 회복
                            if p1_speed + 1 <= p1_maxspeed:
                                p1_speed = p1_speed + 1       
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
                            if p1_speed <= p1_maxspeed and p1_speed - 1 > 0:
                                p1_speed = p1_speed - 1
                        else : # 사용한 아이템이 회복약일때 player2의 속도 회복
                            if p2_speed + 1 <= p2_maxspeed:
                                p2_speed = p2_speed + 1      
                        p2_item.remove(p2_item[0])
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    y1_change = 0

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y2_change = 0
       
        y1 += y1_change
        y2 += y2_change 

        if y1 <0 : # player1이 화면 바깥으로 나가지 못하게 함 
            y1 = 0
        elif y1 > 400 :
            y1 = 400

        if y2 <0 : # player2이 화면 바깥으로 나가지 못하게 함 
            y2 = 0
        elif y2 > 400 :
            y2 = 400
                     
        # player1의 눈이 충돌했을 경우 
        if len(sb1_xy) != 0:
            for i,xy in enumerate(sb1_xy): # 날라가는 눈 표현
                xy[0] += snspeed_1
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
                xy[0] -= snspeed_2
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
