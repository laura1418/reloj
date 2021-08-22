vertical_position = 0

def setup():
    
    size(250, 500)
    
        
        
def draw():
    
    global vertical_position
    
    background(180)
    
    ellipse(width/2, vertical_position, 50, 50)
    fill(23)
    
    if vertical_position > height:
        vertical_position = 0
    else:
        vertical_position = map(second(), 0, 59, 0, height) 
        
        
        
    ellipse(width/2, vertical_position, 50, 50)
    fill(53,21,188)
    
    if vertical_position > height:
        vertical_position = 0
    else:
        vertical_position = map(minute(), 0, 60, 0, height) 
     
        
              
        ellipse(width/2, vertical_position, 50, 50)
    fill(19,50,260)
    
    if vertical_position > height:
        vertical_position = 0
    else:
        vertical_position = map(hour(), 0, 24, 0, height)
