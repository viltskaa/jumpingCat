import pygame


class Background:
    def __init__(self):
        self.bgimage = pygame.image.load('assets/bg1.png')
        self.rectBGimg = self.bgimage.get_rect()

        self.__bgY1 = 0
        self.__bgX1 = 0

        self.__bgY2 = self.rectBGimg.height
        self.__bgX2 = self.rectBGimg.width

        self.__movingYSpeed = 0
        self.__movingXSpeed = 0

    def set_speed(self, speed_x, speed_y):
        self.__movingYSpeed = int(speed_y)
        self.__movingXSpeed = int(speed_x)

    def update(self, speed_x=0, speed_y=0):
        self.set_speed(speed_x, speed_y)

        self.__bgY1 -= self.__movingYSpeed
        self.__bgY2 -= self.__movingYSpeed

        self.__bgX1 -= self.__movingXSpeed
        self.__bgX2 -= self.__movingXSpeed

        if abs(self.__bgY1) <= -(self.rectBGimg.height):
            self.__bgY1 = self.rectBGimg.height
        if abs(self.__bgY2) <= -(self.rectBGimg.height):
            self.__bgY2 = self.rectBGimg.height
        if abs(self.__bgX1) <= -(self.rectBGimg.width):
            self.__bgX1 = self.rectBGimg.width
        if abs(self.__bgX2) <= -(self.rectBGimg.width):
            self.__bgX2 = self.rectBGimg.width

    def render(self, screen: pygame.Surface):
        screen.blit(self.bgimage, (self.__bgX1, self.__bgY1))
        screen.blit(self.bgimage, (self.__bgX2, self.__bgY2))
