from App import App
from Object import Object
from Level import Level

App = App("Shotformer", 640, 480)

Object1 = Object(25, 25, 150, 200, "blue_square.png")
Object2 = Object(10, 10, 100, 100, "red_square.png")
Level1 = Level()
Level1.add_obj(Object1)
Level1.add_obj(Object2)

App.app_add_level(Level1)
#App.app_add_obj(Object1)
App.app_running()

