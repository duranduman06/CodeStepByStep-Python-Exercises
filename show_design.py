"""
Write a function named show_design that uses a DrawingPanel to draw the figure below. The window is 200 pixels wide and 200 pixels tall. 
The background is white and the foreground is black. There are 20 pixels between each of the four rectangles, and the rectangles are concentric (their centers are at the same point).
Use a loop to draw the repeated rectangles.
"""
def show_design():
    p=DrawingPanel(200,200,background="white")
    for i in range(0,4):
        p.draw_rect(20+20*i,20+20*i,160-40*i,160-40*i)


show_design()
