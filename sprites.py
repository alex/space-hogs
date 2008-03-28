import pyglet

import settings

class MovingSprite(pyglet.sprite.Sprite):
    dx = 0
    dy = 0
    
    def __init__(self, *args, **kwargs):
        super(MovingSprite, self).__init__(*args, **kwargs)
    
    def update(self, dt):
        self.x = self.x + self.dx * dt
        self.y = self.y + self.dy * dt

class Player(MovingSprite, pyglet.window.key.KeyStateHandler):
    def __init__(self, x=settings.WINDOW_WIDTH // 2, y=settings.WINDOW_HEIGHT // 2, batch=None):
        super(Player, self).__init__(img=pyglet.resource.image('player.bmp'), x=x, y=y, batch=batch)
        self.reset()
    
    def reset(self):
        self.x = settings.WINDOW_WIDTH // 2
        self.y = settings.WINDOW_HEIGHT // 2
        self.dx = 0
        self.dy = 0
    
    def update(self, dt):
        if self[pyglet.window.key.UP]:
            self.dy = 50
        elif self[pyglet.window.key.DOWN]:
            self.dy = -50
        
        if self[pyglet.window.key.RIGHT]:
            self.dx = 50
        elif self[pyglet.window.key.LEFT]:
            self.dx = -50
        
        super(Player, self).update(dt)
        
        self.dx = 0
        self.dy = 0
