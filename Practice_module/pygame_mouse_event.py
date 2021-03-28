from pygame.locals import *
import pygame
import sys

def main():
    pygame.init()    # Pygameを初期化
    screen = pygame.display.set_mode((400, 330))    # 画面を作成
    pygame.display.set_caption("mouse event")    # タイトルを作成
    
    while True:        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # マウスクリック時の動作
            if event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                print("mouse clicked -> (" + str(x) + ", " + str(y) + ")")
                
            # マウスポインタが移動したときの動作
            if event.type == MOUSEMOTION:
                x, y = event.pos
                #print("mouse moved   -> (" + str(x) + ", " + str(y) + ")")

        pygame.display.update()
               
if __name__=="__main__":
    main()