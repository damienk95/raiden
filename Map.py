import util

class Map:
    def __init__(self):
        self.sprite = util.bushSprite
        self.bushes = [(50, 50, 3, 4), (20, 20, 5, 1)]

    def draw(self, screen, screenHeight, offsetY):
        for bush in self.bushes:
            if (bush[1] - offsetY) < screenHeight:
                for i in range(bush[2]):
                    for j in range(bush[3]):
                        x = bush[0] + 8 * i
                        y = bush[1] + 8 * j
                        screen.blit(self.sprite, (x, y))
