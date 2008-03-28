#!/usr/bin/env python

import pyglet

import settings
from sprites import Player

pyglet.resource.path.append('data')
pyglet.resource.reindex()

btc = pyglet.graphics.Batch()

win = pyglet.window.Window(width=settings.WINDOW_WIDTH, height=settings.WINDOW_HEIGHT)
ply = Player(batch=btc)

def update(dt):
    ply.update(dt)
pyglet.clock.schedule_interval(update, float(1)/60)

@win.event
def on_draw():
    win.clear()
    btc.draw()

win.push_handlers(ply)

pyglet.app.run()
