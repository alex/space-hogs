import pyglet

import settings

BULLETS = []

def center_anchor(img):
    img.anchor_x = img.width // 2
    img.anchor_y = img.height // 2

class MovingSprite(pyglet.sprite.Sprite):
    dx = 0
    dy = 0
    
    def __init__(self, *args, **kwargs):
        super(MovingSprite, self).__init__(*args, **kwargs)
        center_anchor(self.image)
    
    def update(self, dt):
        self.x = self.x + self.dx * dt
        self.y = self.y + self.dy * dt
    
    def _get_top(self):
        return self.y + self.image.height // 2
    
    def _set_top(self, val):
        self.y = val - self.image.height //2
    top = property(_get_top, _set_top)
    
    def _get_bottom(self):
        return self.y - self.image.height // 2
    
    def _set_bottom(self, val):
        self.y = val + self.image.height // 2
    bottom = property(_get_bottom, _set_bottom)
    
    def _get_right(self):
        return self.x + self.image.width // 2
    
    def _set_right(self, val):
        self.x = val - self.image.width //2
    right = property(_get_right, _set_right)
    
    def _get_left(self):
        return self.x - self.image.width // 2
    
    def _set_left(self, val):
        self.x = val + self.image.width //2
    left = property(_get_left, _set_left)

class Player(MovingSprite, pyglet.window.key.KeyStateHandler):
    def __init__(self, x=settings.WINDOW_WIDTH // 2, y=settings.WINDOW_HEIGHT // 2, batch=None):
        super(Player, self).__init__(img=pyglet.resource.image('player.bmp'), x=x, y=y, batch=batch)
        self.reset()
    
    def reset(self):
        self.x = settings.WINDOW_WIDTH // 2
        self.y = settings.WINDOW_HEIGHT // 2
        self.dx = 0
        self.dy = 0
        
        self.fire_timeout = 0
    
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
        
        if self.right >= settings.WINDOW_WIDTH:
            self.right = settings.WINDOW_WIDTH
        elif self.left <= 0:
            self.left = 0
        
        if self.top >= settings.WINDOW_HEIGHT:
            self.top = settings.WINDOW_HEIGHT
        elif self.bottom <= 0:
            self.bottom = 0
        
        self.fire_timeout -= dt
        if self[pyglet.window.key.SPACE] and self.fire_timeout <= 0:
            BULLETS.append(Bullet(x=self.right, y=self.y, batch=self.batch))
            self.fire_timeout = settings.PLAYER_FIRE_LIMIT

class Bullet(MovingSprite):
    def __init__(self, x, y, batch):
        super(MovingSprite, self).__init__(img=pyglet.resource.image('bullet.png'), x=x, y=y, batch=batch)
        self.dx = 150
        self.dy = 0
    
    def update(self, dt):
        super(Bullet, self).update(dt)
        if self.x > settings.WINDOW_WIDTH:
            self.delete()
            BULLETS.remove(self)
