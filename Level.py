import pygame
import json
from Object import Object
from Player import Player

scroll_speed = 3

class Level:
    
    def __init__(self):
        self.Objects = pygame.sprite.Group()
        #self.Player = Player

    def load_level(self, image_path):
        json_file = json.load(open('Test.json', 'r', encoding="utf-8"))
        for object in json_file["objects"]:
            temp_object = Object(object.get("object_name"),object.get("object_width"), object.get("object_height"), object.get("object_x"), object.get("object_y"), object.get("image_path"))
            if (temp_object.name == "player"):
                self.player_object = Player(object.get("object_name"),object.get("object_width"), object.get("object_height"), object.get("object_x"), object.get("object_y"), object.get("image_path"))
                self.Objects.add(self.player_object)
                #the commented out sections are for when the player class gets implemented. It's supposed to follow the same format as the object class since it inherits from it.
                #pass
            else:
                self.Objects.add(temp_object)
       
    def add_obj(self, object):
        self.Objects.add(object)
    
    def draw(self, screen):
        self.Objects.draw(screen)
        for object in self.Objects:
            if object.name != "player" and self.player_object.in_middle == True:
                object.move_x(-scroll_speed)
        self.Objects.update()