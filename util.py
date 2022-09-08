import time

WIDTH = 100
HEIGHT = 100

class RateLimiter:
    def __init__(self):
        self.lastShot = 0

    def shoot(self, cooldown):
        if time.time() - self.lastShot > cooldown:
            self.lastShot = time.time()
            return True
        return False
