import pygame as pg
import os, random
pg.init()

class Menu:
    
    #Initializes the Menu
    def __init__(self):
        #Load assets
        win_w, win_h = win.get_size()
        self.play = pg.image.load(os.path.join('Assets', 'Play.png'))
        self.play = pg.transform.scale(self.play, (int(self.play.get_width()/7), int(self.play.get_height()/7)))
        self.font = pg.font.Font(None, 32)
        self.size = "Insert how many rows, you would like"
        self.New = True
        self.Clicked = False
          
        self.button_x = int((win_w/2)-self.play.get_width()/2)
        self.button_y = int(win_h/5*3)

    def NumInput(self, win):
        win_w, win_h = win.get_size()
        self.text = self.font.render(self.size, True, (0,0,0))
        win.blit(self.text, (int((win_w/2)-self.text.get_width()/2),int(win_h/5*2)))

    #Sets the Buttons
    def Buttons(self, win):
        win.blit(self.play, (self.button_x, self.button_y))
        
class Grid: 
    def __init__(self, win):
        self.win = win
        self.header_h = 70
        self.paused = True
        self.back = pg.image.load(os.path.join("Assets", "Back.png"))
        self.back = pg.transform.scale(self.back, (int(self.back.get_width()/8), int(self.back.get_height()/8)))
        self.play = pg.image.load(os.path.join('Assets', 'Play.png'))
        self.play = pg.transform.scale(self.play, (int(self.play.get_width()/15), int(self.play.get_height()/15)))
        self.play_x, self.play_y = int((self.win.get_width()/2)-(self.play.get_width()/2)), int((self.header_h-self.play.get_height())/2)
        self.pause = pg.image.load(os.path.join("Assets", "Pause.png"))
        self.pause = pg.transform.scale(self.pause, (int(self.pause.get_width()/15), int(self.pause.get_height()/15)))
        self.font = pg.font.Font(None, 60)
        self.Clicked_A = False
        self.Blocked_A = False
        self.Clicked_B = False
        self.Blocked_B = False
        self.Clicked_Block = False
        self.Clicked_Erase = False

    def Set(self, menu):
        self.Cells = [[0 for x in range(int(menu.size))] for x in range(int(menu.size))]
        self.Cells_size = int(min(self.win.get_width(),self.win.get_height() - self.header_h)/int(menu.size))
        self.Cells_x = int((max(self.win.get_width(),self.win.get_height() - self.header_h)- self.Cells_size*int(menu.size))/2)

    def Draw(self):
        pg.draw.rect(self.win,(220,220,220), (0,0,self.win.get_width(),self.header_h))
        self.Rect_A = pg.draw.rect(self.win, (93,178,212), (100,10,50,50))
        self.Rect_B = pg.draw.rect(self.win, (227, 60, 57), (170,10,50,50))
        self.Rect_Block = pg.draw.rect(self.win, (65, 65, 65), (240, 10, 50,50))
        self.Rect_Erase = pg.draw.rect(self.win, (227, 60, 57), (310,10,50,50))
        self.win.blit(self.back, (0,0))
        self.win.blit(self.font.render("A", True, (0,0,0)), (110,15))
        self.win.blit(self.font.render("B", True, (0,0,0)), (180, 15))
        self.win.blit(self.font.render("ø".upper(), True, (255,255,255)), (250, 15))
        self.win.blit(self.font.render("X", True, (0,0,0)), (320, 15))
        if not self.paused:
            self.win.blit(self.pause, (self.play_x, self.play_y))
        else:
            self.win.blit(self.play, (self.play_x, self.play_y))
        
        for x, row in enumerate(self.Cells):
            for y, cell in enumerate(row):
                #  0      = Nothing
                # "A"     = Point A
                # "B"     = Point B
                # "Block" = Block

                pg.draw.rect(self.win, (220,220,220),
                (x*self.Cells_size+self.Cells_x-1,y*self.Cells_size+self.header_h-1,self.Cells_size,self.Cells_size))
                if self.Cells[x][y] == 0:
                    pg.draw.rect(self.win, (250,250,250),
                    (x*self.Cells_size+self.Cells_x+5, y*self.Cells_size+self.header_h+5, self.Cells_size-10,self.Cells_size-10))
                elif self.Cells[x][y] == "A":
                    pg.draw.rect(self.win, (93,178,212),
                    (x*self.Cells_size+self.Cells_x+5, y*self.Cells_size+self.header_h+5, self.Cells_size-10,self.Cells_size-10))

                elif self.Cells[x][y] == "B":
                    pg.draw.rect(self.win, (227, 60, 57),
                    (x*self.Cells_size+self.Cells_x+5, y*self.Cells_size+self.header_h+5, self.Cells_size-10,self.Cells_size-10))
                
                elif self.Cells[x][y] == "Block":
                    pg.draw.rect(self.win, (65,65,65),
                    (x*self.Cells_size+self.Cells_x+5, y*self.Cells_size+self.header_h+5, self.Cells_size-10,self.Cells_size-10))

class PathFind():

    def __init__(self, grid):
        pass

def ButtonClick(cursor, rect):
    return rect.collidepoint(cursor)
    
    

#Main Loop
if __name__ == "__main__":
    win_w, win_h = (1280, 720)

    win = pg.display.set_mode([win_w, win_h])
    pg.display.set_caption("Path Finding")
    win.fill((250,250,250))
    menu = Menu()
    Grid = Grid(win)

    clock = pg.time.Clock()
    while True:

        for event in pg.event.get():
            click = False

            #Checks if the window have been closed
            if event.type == pg.QUIT:
                pg.quit()
                quit()
                
            if event.type == pg.KEYDOWN:
                if not menu.Clicked:
                    if event.key == pg.K_BACKSPACE and not menu.New:
                        menu.size = menu.size[:-1]
                    if event.unicode in ("1","2","3","4","5","6","7","8","9","0"):
                        if menu.New:
                            menu.New = False
                            menu.size = ""
                        menu.size += event.unicode
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:

                    if not menu.Clicked:
                        if ButtonClick(event.pos,pg.Rect(menu.button_x, menu.button_y,menu.play.get_width(),menu.play.get_height())):
                            if len(menu.size) > 0 and menu.size != "Insert how many rows, you would like":
                                if int(menu.size) > 2: 
                                    menu.Clicked = True
                                    Grid.Set(menu)

                    else:
                        if ButtonClick(event.pos, pg.Rect(0,0, Grid.back.get_width(), Grid.back.get_height())):
                            menu.__init__()
                            Grid.__init__(win)
                        
                        if ButtonClick(event.pos, pg.Rect(Grid.play_x, Grid.play_y, Grid.play.get_width(), Grid.play.get_height())):
                            Grid.paused = not Grid.paused
                        
                        if ButtonClick(event.pos, Grid.Rect_A):
                            Grid.Clicked_Block = False
                            Grid.Clicked_A = True
                            Grid.Clicked_B = False
                            Grid.Clicked_Erase = False

                        if ButtonClick(event.pos, Grid.Rect_B):
                            Grid.Clicked_Block = False
                            Grid.Clicked_A = False
                            Grid.Clicked_B = True
                            Grid.Clicked_Erase = False

                        if ButtonClick(event.pos, Grid.Rect_Block):
                            Grid.Clicked_Block = not Grid.Clicked_Block
                            Grid.Clicked_A = False
                            Grid.Clicked_B = False
                            Grid.Clicked_Erase = False

                        if ButtonClick(event.pos, Grid.Rect_Erase):
                            Grid.Clicked_Block = False
                            Grid.Clicked_A = False
                            Grid.Clicked_B = False
                            Grid.Clicked_Erase = not Grid.Clicked_Erase

                        for x, row in enumerate(Grid.Cells):
                            for y, cell in enumerate(row):
                                if ButtonClick(event.pos, pg.Rect(x*Grid.Cells_size+Grid.Cells_x-1,y*Grid.Cells_size+Grid.header_h-1,Grid.Cells_size,Grid.Cells_size)) and Grid.Clicked_A and not Grid.Blocked_A:
                                    Grid.Cells[x][y] = "A"
                                    Grid.Clicked_A = False
                                    Grid.Blocked_A = True

                                if ButtonClick(event.pos, pg.Rect(x*Grid.Cells_size+Grid.Cells_x-1,y*Grid.Cells_size+Grid.header_h-1,Grid.Cells_size,Grid.Cells_size)) and Grid.Clicked_B and not Grid.Blocked_B:
                                    Grid.Cells[x][y] = "B"
                                    Grid.Clicked_B = False
                                    Grid.Blocked_B = True

                                if ButtonClick(event.pos, pg.Rect(x*Grid.Cells_size+Grid.Cells_x-1,y*Grid.Cells_size+Grid.header_h-1,Grid.Cells_size,Grid.Cells_size)) and Grid.Clicked_Block:
                                    Grid.Cells[x][y] = "Block"
                                
                                if ButtonClick(event.pos, pg.Rect(x*Grid.Cells_size+Grid.Cells_x-1,y*Grid.Cells_size+Grid.header_h-1,Grid.Cells_size,Grid.Cells_size)) and Grid.Clicked_Erase:
                                    Grid.Cells[x][y] = 0

        win.fill((250,250,250))
        if not menu.Clicked:
            menu.Buttons(win)
            menu.NumInput(win)

        else:
            Grid.Draw()

        pg.display.update()
        clock.tick(30)