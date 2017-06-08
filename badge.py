from Tkinter import *
import tkFont
from PIL import ImageTk, Image

class Badge:

    BLACK = 0
    WHITE = 1

    pictures = [
        'pic_1.png',
        'pic_2.png',
        'pic_3.png',
        'pic_4.png',
        'pic_5.png',
    ]
    leds = []

    BADGE_EINK_WIDTH = 296
    BADGE_EINK_HEIGHT = 128

    def init(self):
        pass

    def eink_init(self):
        eink.place(x=27, y=32, width=self.BADGE_EINK_WIDTH, height=self.BADGE_EINK_HEIGHT)

    def display_picture(self, a, b):
        photoimage = ImageTk.PhotoImage(file=self.pictures[a])
        eink.create_image(148, 64, image=photoimage)
        slow_eink_update()

    def power_init(self):
        pass

    def battery_charge_status(self):
        pass

    def battery_volt_sense(self):
        pass

    def usb_volt_sense(self):
        pass

    def leds_init(self):
        x = 45
        y = 5
        for i in range(6):
            self.leds.append(canvas.create_rectangle(x, y, x+18, y+18, fill='grey'))
            x+=48
        pass

    def led_set(self, led, hexcolor):
        canvas.itemconfig(self.leds[led], fill=hexcolor)
        t.update()

    def run(self):
        t.mainloop()

    def button_one_callback(self):
        print "Button 1 pressed!"

    def buttons_init(self):
        button_a = Button(canvas, text="A", command=self.button_one_callback)
        button_a.place(x=298, y=192)
        button_b = Button(canvas, text="B", command=self.button_one_callback)
        button_b.place(x=258, y=226)

        button_select = Button(canvas, text="select", command=self.button_one_callback)
        button_select.place(x=140, y=270)

        button_select = Button(canvas, text="start", command=self.button_one_callback)
        button_select.place(x=210, y=270)

        button_up = Button(canvas, text="^", command=self.button_one_callback)
        button_up.place(x=60, y=190)

        button_down = Button(canvas, text="v", command=self.button_one_callback)
        button_down.place(x=60, y=260)

        button_left = Button(canvas, text="<", command=self.button_one_callback)
        button_left.place(x=20, y=225)

        button_right = Button(canvas, text=">", command=self.button_one_callback)
        button_right.place(x=90, y=225)

    def __init__(self):
        self.leds_init()
        self.buttons_init()

import time

def slow_eink_update():
    time.sleep(0.5)
    t.update()

def color2string(color):
    if color == 0:
	return "black"
    else:
	return "white"

def native_font_lookup(font):
    lut = {'Roboto_BlackItalic24': ('Roboto', 24, 'italic'),
           'PermanentMarker22':    ('Permanent Marker', 22, 'bold')
            }
    return lut[font]

def polygonpoints(x1, y1, x2, y2, radius):
    # https://stackoverflow.com/questions/44099594/how-to-make-a-tkinter-canvas-rectangle-with-rounded-corners
    points = [x1+radius, y1,
          x1+radius, y1,
          x2-radius, y1,
          x2-radius, y1,
          x2, y1,
          x2, y1+radius,
          x2, y1+radius,
          x2, y2-radius,
          x2, y2-radius,
          x2, y2,
          x2-radius, y2,
          x2-radius, y2,
          x1+radius, y2,
          x1+radius, y2,
          x1, y2,
          x1, y2-radius,
          x1, y2-radius,
          x1, y1+radius,
          x1, y1+radius,
          x1, y1,]
    return points

class Ugfx:

    justifyLeft = 0
    justifyCenter = 1
    justifyRight = 2

    def init(self):
        pass

    def deinit(self):
        pass

    def clear(self, color):
	eink.delete("all")
        eink.configure(bg=color2string(color))
        slow_eink_update()
    
    def flush(self):
	eink.delete("all")
        slow_eink_update()

    def get_char_width(self, char, font):
        return self.get_string_width(char, font)

    def get_string_width(self, string, font):
        # https://stackoverflow.com/questions/7193798/how-can-i-measure-the-width-of-a-string-rendering-via-tkfont-without-creating-a
        font, size, weight = native_font_lookup(font)
        if weight == 'italic':
            # weird tkinter quirk
            weight = 'normal'
        font = tkFont.Font(family=font, size=size, weight=weight)
        return font.measure(string)

    def char(self, x, y, char, font, color):
        self.string(x,y,char,font,color)

    def string(self, x, y, string, font, color):
        font, size, weight = native_font_lookup(font)
        canvas_id = eink.create_text(x, y, anchor="nw")
        eink.itemconfig(canvas_id, text=string, font=(font, size, weight), fill=color2string(color), width=780)
        slow_eink_update()

    def string_box(self, x0, y0, x1, y1, string, font, color, justify):
        #self.box(x0, y0, x1-x0, y1-y0, color)
	eink.create_rectangle(x0, y0, x1-x0, y1-y0, outline=color2string(color))
        if justify == self.justifyLeft:
            self.string(x0, y0, string, font, color)
        elif justify == self.justifyCenter:
            length = self.get_string_width(string, font)
            center = (x0+length)/2
            self.string(center, y0, string, font, color)
        elif justify == self.justifyRight:
            length = self.get_string_width(string, font)
            begin = x1-length
            self.string(begin, y0, string, font, color)

    def pixel(self, x, y, color):
	eink.create_line(x, y, x + 1, y)
        slow_eink_update()

    def line(self, x0, y0, x1, y1, color):
	eink.create_line(x0, y0, x1, y1, fill=color2string(color))
        slow_eink_update()

    def thickline(self, x0, y0, x1, y1, color, width, rnd):
	eink.create_line(x0, y0, x1, y1, fill=color2string(color), width=width)
        slow_eink_update()

    def arc(self, x0, y0, r, a1, a2, color):
	eink.create_arc(x0-r, y0-r, x0+r, y0+r, outline=color2string(color), start=a1, extent=a2)
        slow_eink_update()

    def fill_arc(self, x0, y0, r, color, a1, a2):
	eink.create_arc(x0-r, y0-r, x0+r, y0+r, fill=color2string(color), start=a1, extent=a2)
        slow_eink_update()

    def circle(self, x0, y0, r, color):
	eink.create_oval(x0-r, y0-r, x0+r, y0+r, outline=color2string(color))
        slow_eink_update()

    def fill_circle(self, x0, y0, r, color):
	eink.create_oval(x0-r, y0-r, x0+r, y0+r, fill=color2string(color))
        slow_eink_update()

    def ellipse(self, x0, y0, a, b, color):
	eink.create_oval(x0, y0, a, b, outline=color2string(color))
        slow_eink_update()

    def fill_ellipse(self, x0, y0, a, b, color):
	eink.create_oval(x0, y0, a, b, fill=color2string(color))
        slow_eink_update()

    def polygon(self, x0, y0, color, points):
	points = [(x+x0, y+y0) for x,y in points]
	eink.create_polygon(points, fill=fill, outline=outline, smooth=True)
        slow_eink_update()

    def area(self, x0, y0, a, b, color):
	eink.create_rectangle(x0, y0, a, b, fill=color2string(color))
        slow_eink_update()

    def box(self, x0, y0, a, b, color):
	eink.create_rectangle(x0, y0, a, b, outline=color2string(color))
        slow_eink_update()

    def rounded_box(self, x0, y0, a, b, r, color):
	eink.create_polygon(polygonpoints(x0, y0, x0+a, y0+b, r), outline=color2string(color), smooth=True)
        slow_eink_update()

    def fill_rounded_box(self, x0, y0, a, b, r, color):
	eink.create_polygon(polygonpoints(x0, y0, x0+a, y0+b, r), fill=color2string(color), smooth=True)
        slow_eink_update()

    def demo(self, string):
        self.clear(badge.WHITE)
        self.string(150,25,"STILL","Roboto_BlackItalic24",badge.BLACK)
        self.string(130,50,string,"PermanentMarker22",badge.BLACK)
        length = ugfx.get_string_width("Hacking","PermanentMarker22")
        self.line(127+3,50+22,127+3+length+14, 50+22, badge.BLACK)
        self.line(127+3+length+10,50+2,127+3+length+10, 50+22, badge.BLACK)
        self.string(140,75,"Anyway","Roboto_BlackItalic24",badge.BLACK)
        self.fill_circle(60, 60, 50, badge.BLACK)
        self.fill_circle(60, 60, 40, badge.WHITE)
        self.fill_circle(60, 60, 30, badge.BLACK)
        self.fill_circle(60, 60, 20, badge.WHITE)
        self.fill_circle(60, 60, 10, badge.BLACK)
        self.flush()

class esp:
    def flash_read(self, offset_in):
        pass

    def flash_read(self, offset_in, buf_in):
        pass

    def flash_erase(self, sector_in):
        pass

    def flash_size(self):
        return 0x1000000 # 16 MB

    def flash_user_start(self):
        pass

    def neopixel_write(self, pin, buf, timing):
        pass

    def rtcmem_write(self, pos, val):
        pass

    def rtcmem_write(self, pos):
        pass

    def rtcmem_get_reset_reason(self, cpu):
        pass

    def start_sleeping(self, duration):
        pass

    pass

class machine:
    pass

class network:
    def WLAN(self, mode):
        pass

    def initialize(self):
        pass

    def active(self, active):
        pass

    def connect(self, ssid, password):
        pass

    def disconnect(self):
        pass

    def status(self):
        pass

    def scan(self):
        pass

    def isconnected(self):
        pass

    def ifconfig(self):
        pass

    def config(self):
        pass

if __name__ == "__main__":

    t = Tk()
    t.title("SHA2017 badge")

    frame = Frame(t)
    frame.pack(fill=BOTH, expand=YES)
    canvas = Canvas(frame, width=350, height=322, bg="black", highlightthickness=0)
    background_image = ImageTk.PhotoImage(file="badge_background.png")
    canvas.create_image(175, 161, image=background_image)
    canvas.pack(fill=BOTH, expand=YES)

    eink = Canvas(frame)

    badge = Badge()
    ugfx = Ugfx()

    def run(argv):
        with file(argv[1],'r') as f:
            script = f.read()
            exec(script)
            badge.run()

    sys.exit(run(sys.argv))

