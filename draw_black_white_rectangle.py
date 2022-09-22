"""
The following code attempts to draw a black-filled outer rectangle with a white-filled inner circle inside it.
However, the graphical output does not display the white inner circle. Modify the code so it will look as intended.
"""
def draw_black_white_rectangle():
  panel = DrawingPanel(200, 100)

  panel.set_fill_color("black")
  panel.fill_rect(10, 10, 50, 50)
  panel.set_fill_color("white")
  panel.fill_oval(10, 10, 50, 50)
