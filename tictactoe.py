def minimax(marked,move):
    #if move==1 then minimises
    wn,winner=win(marked)
    if wn:
        if winner==0:
            return 1
        else:
            return -1
    elif wn==-1 and len(marked)==9:
        return 0

    scores=[]
    for i in range(3):
        for j in range(3):
            if (i,j) not in marked:
                marked[(i,j)]=move
                scores.append(minimax(marked,abs(move-1)))
                del marked[(i,j)]
    #print(scores)

    if len(scores)==0:
        return 0
    return min(scores) if move else max(scores)

def ai(marked):
    best_score=-10
    for i in range(3):
        for j in range(3):
            if (i,j) not in marked:
                marked[(i,j)]=0
                score=minimax(marked,1)
                if score>best_score:
                    best_score=score
                    move=(i,j)
                del marked[(i,j)]
    return move

def win(marked):
    #check rows
    for i in range(3):
        if (i,0) in marked and (i,1) in marked and (i,2) in marked and marked[(i,0)]==marked[(i,1)]==marked[(i,2)]:
            return 1,marked[(i,0)]
    #check columns
    for i in range(3):
        if (0,i) in marked and (1,i) in marked and (2,i) in marked and marked[(0,i)]==marked[(1,i)]==marked[(2,i)]:
            return 1,marked[(0,i)]
    #chech left diagnal
    i=0
    if (0,0) in marked and (1,1) in marked and(2,2) in marked and marked[(i,i)]==marked[(i+1,i+1)]==marked[(i+2,i+2)]:
        return 1,marked[(i,i)]
    #check right diagnal
    if (2,0) in marked and (1,1) in marked and(0,2) in marked and marked[(2,0)]==marked[(1,1)]==marked[(0,2)]:
        return 1,marked[(1,1)]
    return 0,-1

import pygame as pg
pg.init()
dis = pg.display.set_mode((600, 300))
pg.display.update()
pg.display.set_caption('TicTacToe')
game_over = False
def setup():
    dis.fill((0,0,0))
    pg.draw.line(dis, (255, 255, 255), (200, 0), (200, 300), 2)
    pg.draw.line(dis, (255, 255, 255), (400, 0), (400, 300), 2)
    pg.draw.line(dis, (255, 255, 255), (0, 100), (600, 100), 2)
    pg.draw.line(dis, (255, 255, 255), (0, 200), (600,200), 2)
    pg.display.update()

font = pg.font.SysFont("comicsansms", 72)
text = font.render("X", True, (255, 0, 0))
text1 = font.render("O", True, (255, 0, 0))
new_game=1
while not game_over:
    if new_game:
        setup()
        new_game=0
        marked={}
    for x in pg.event.get():
        if x.type == pg.QUIT:
            game_over = True
            break
        if x.type==pg.MOUSEBUTTONUP:
            pos0,pos1=pg.mouse.get_pos()
            idx=(pos0//200,pos1//100)
            if idx not in marked:
                marked[idx]=1
                dis.blit(text1,(idx[0]*200+70,idx[1]*100))
            else:
                continue
            if len(marked)==9:
                new_game=1
                break
            check,winner=win(marked)
            if check:
                pg.time.wait(1000)
                text2=font.render("Winner"+" "+str(winner),True,(255,0,0))
                dis.fill((0,0,0))
                dis.blit(text2,(150,100))
                pg.display.update()
                new_game=1
                pg.time.wait(2000)
                break
            move=ai(marked)
            marked[move]=0
            dis.blit(text,(move[0]*200+70,move[1]*100))
            pg.display.update()
            if len(marked)==9:
                new_game=1
                break
            check,winner=win(marked)
            if check:
                pg.time.wait(1000)
                text2=font.render("Winner"+" "+str(winner),True,(255,0,0))
                dis.fill((0,0,0))
                dis.blit(text2,(150,100))
                pg.display.update()
                new_game=1
                pg.time.wait(2000)
                break
        pg.display.update()
pg.quit()
quit()
