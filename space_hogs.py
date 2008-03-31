#!/usr/bin/env python

import pyglet
import settings
from sprites import Player, Bullet, BULLETS

class SpaceHogs(pyglet.window.Window):
    def __init__(self):
        super(SpaceHogs, self).__init__(caption='Space Hogs', width=settings.WINDOW_WIDTH, height=settings.WINDOW_HEIGHT)
        
        pyglet.resource.path.append('data')
        pyglet.resource.reindex()
        
        self.batch = pyglet.graphics.Batch()
        
        self.player = Player(batch=self.batch)
        self.push_handlers(self.player)
        
        pyglet.clock.schedule_interval(self.update, float(1)/60)
    
    def run(self):
        pyglet.app.run()
    
    def update(self, dt):
        self.player.update(dt)
        for bullet in BULLETS[:]:
            bullet.update(dt)
    
    def on_draw(self):
        self.clear()
        self.batch.draw()

if __name__ == '__main__':
    SpaceHogs().run()
