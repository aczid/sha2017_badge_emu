#import ugfx
import random, time
ugfx.clear(ugfx.BLACK)
while True:
    for i in range(6):
	badge.led_set(i, '#%03x' % random.randint(0, 0xfff))
    badge.display_picture(random.randint(0,4),-1)
    time.sleep(0.5)

ugfx.clear(ugfx.BLACK)
ugfx.rounded_box(20, 20, 200, 80, 30, ugfx.WHITE)
ugfx.arc(40, 40, 40, 30, 70, ugfx.WHITE)
ugfx.fill_circle(200, 80, 20, ugfx.WHITE)
ugfx.ellipse(200, 20, 40, 80, ugfx.WHITE)
ugfx.flush()

