
def setup():
    global pg, font
    font = createFont("RobotoMono-Regular.ttf", 600)
    size(800, 800)
    pg=createGraphics(800, 800)
    #frameRate(10)
    
def draw():
    global pg, font
    background(0)
    
    pg.beginDraw()
    pg.background(0)
    pg.fill(255)
    pg.textSize(800)
    pg.pushMatrix() # open matrix
    pg.translate(width/2, height/2-215)
    pg.textAlign(CENTER, CENTER)
    pg.text("a",0,0)
    pg.popMatrix() ## close matrix
    pg.endDraw()
    
    tilesX = 50
    tilesY = 50
    
    tileW = int(width/tilesX)
    tileH = int(height/tilesY) 
    
    for y in range(tilesY) :
        for x in range(tilesX):
            wave = int(sin(frameCount * 0.1 + (x * y)) * 20)
            
            # sx = x * tileW
            # sx = x * tileW + int(random(-100, 100))
            sx = x * tileW + wave
            sy = y * tileH
            sw = tileW
            sh = tileH
            
            dx = x * tileW
            dy = y * tileH
            dw = tileW
            dh = tileH
            
            copy(pg, sx, sy, sw, sh, dx, dy, dw, dh)
    

    
