badge.eink_init()
ugfx.clear(badge.BLACK)
import random, time
while True:
    for i in range(6):
	badge.led_set(i, '#%03x' % random.randint(0, 0xfff))
    badge.display_picture(random.randint(0,4),-1)
    time.sleep(0.5)

ugfx.clear(badge.BLACK)
ugfx.rounded_box(20, 20, 200, 80, 30, badge.WHITE)
ugfx.arc(40, 40, 40, 30, 70, badge.WHITE)
ugfx.fill_circle(200, 80, 20, badge.WHITE)
ugfx.ellipse(200, 20, 40, 80, badge.WHITE)

