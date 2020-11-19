import gc
from time import sleep
import board
import displayio
import adafruit_displayio_ssd1306
import adafruit_imageload
import simpleio
import supervisor
import busio
gc.collect()

def note(name):
    octave = int(name[-1])
    PITCHES = "c,c#,d,d#,e,f,f#,g,g#,a,a#,b".split(",")
    pitch = PITCHES.index(name[:-1].lower())
    return 440 * 2 ** ((octave - 4) + (pitch - 9) / 12.)

start_sound = [
  ("e5", 1),("e5", 1),(None, 1),("e5", 1),(None, 1),("c5", 1),("e5", 1),
  ("g5", 2),(None, 2),("g4", 1),(None, 1)]
no_sound =[(None,1)]
blink_sound = [("g5", 1),("g4", 1)]
center_sound = [("e5", 1)]
happy_sound = [("g5", 1),("g5", 1)]
sad_sound = [("g4", 4),("g4", 4),("g4", 4),("g4", 1),(None, 1),("e5", 1)]
def play_sound(name):
    for (notename, eigths) in name:
        length = eigths * 0.1
        if notename:
            simpleio.tone(board.A0,note(notename), length)
        else:
            sleep(length)

uart = busio.UART(board.TX, board.RX, baudrate=115200)

if supervisor.runtime.serial_connected:
    print("Hello World!")

def serial_read():
   if supervisor.runtime.serial_bytes_available:
        value = int(input())
        print_serial(value)

displayio.release_displays()
spi = board.SPI()
oled_reset_left = board.D9      
oled_cs_left = board.D10
oled_dc_left = board.D7
display_bus_left = displayio.FourWire(spi, command=oled_dc_left, chip_select=oled_cs_left,
                                reset=oled_reset_left, baudrate=1000000)

oled_reset_right = board.D12  
oled_cs_right  = board.D13
oled_dc_right = board.D11
display_bus_right = displayio.FourWire(spi, command=oled_dc_right, chip_select=oled_cs_right,
                                reset=oled_reset_right, baudrate=1000000)


WIDTH = 128
HEIGHT = 64     
BORDER = 5

display_left = adafruit_displayio_ssd1306.SSD1306(display_bus_left, width=WIDTH, height=HEIGHT)
display_right = adafruit_displayio_ssd1306.SSD1306(display_bus_right, width=WIDTH, height=HEIGHT)

group_left = displayio.Group(scale=2)
group_right = displayio.Group(scale=2)
group_left.y = 5
group_right.y = 5
display_left.show(group_left)
display_right.show(group_right)

name = ("/idle.bmp")
odb, palette = adafruit_imageload.load(name,
                                            bitmap=displayio.Bitmap,
                                            palette=displayio.Palette)
image_left = displayio.TileGrid(odb, pixel_shader=palette)
image_right = displayio.TileGrid(odb, pixel_shader=palette)
image_right.flip_x=True
image_right.flip_y=True
group_left.append(image_left)
group_right.append(image_right)
sleep(1)

def anim_eyes(name,ticks,wait,sound):
    odb, palette = adafruit_imageload.load(name,
                                    bitmap=displayio.Bitmap,
                                    palette=displayio.Palette)
    image_left = displayio.TileGrid(odb, pixel_shader=palette,
                width = 1,
                height = 1,
                tile_width = 64,
                tile_height = 32)
    image_right = displayio.TileGrid(odb, pixel_shader=palette,
                width = 1,
                height = 1,
                tile_width = 64,
                tile_height = 32)
    image_right.flip_x=True
    image_right.flip_y=True
    group_left.append(image_left)
    group_right.append(image_right)
    source_index_left = 0
    source_index_right = 0
    for i in range(1,10):
        image_left[0] = i
        image_right[0] = i
        sleep(ticks)
    play_sound(sound)
    sleep(wait)
    for i in range(1,10):
        image_left[0] = 10-i
        image_right[0] = 10-i
        sleep(ticks)
    group_left.pop()
    group_right.pop()


anim_eyes(("/spritesheet.bmp"),.005,0,start_sound)
sleep(0.5)
anim_eyes(("/spritesheet_look_left.bmp"),.005,0,blink_sound)
sleep(0.5)
anim_eyes(("/spritesheet_look_right.bmp"),.005,0,blink_sound)
sleep(0.5)
anim_eyes(("/spritesheet_look_left_low.bmp"),.05,1,blink_sound)
sleep(0.5)
anim_eyes(("/spritesheet_look_right_low.bmp"),.05,1,blink_sound)
sleep(0.5)
anim_eyes(("/spritesheet_happy.bmp"),.005,1,happy_sound)
sleep(0.5)
anim_eyes(("/spritesheet_sad.bmp"),.005,0,sad_sound)
sleep(0.5)
anim_eyes(("/spritesheet_center.bmp"),.005,0,center_sound)
sleep(1)

def print_serial(data):
    print(data)
    if data ==1:
        anim_eyes(("/spritesheet_look_right_low.bmp"),.05,1,blink_sound)
    elif data ==2:
        anim_eyes(("/spritesheet_sad.bmp"),.005,0,sad_sound)
    elif data ==3:
        anim_eyes(("/spritesheet_happy.bmp"),.005,1,happy_sound)
    elif data ==4:
        anim_eyes(("/spritesheet_look_left_low.bmp"),.05,1,blink_sound)
    elif data ==5:
        anim_eyes(("/spritesheet_center.bmp"),.005,0,center_sound)
    elif data ==6:
         anim_eyes(("/spritesheet.bmp"),.005,0,blink_sound)

while True:
    #This code works with USB serial or UART
    #--------------------------------------------------
    serial_read()
    #--------------------------------------------------
    data = uart.readline()
    print(data)  # this is a bytearray type
    if data is None:
        pass
    else:
        datastr = ''.join([chr(b) for b in data])
        print (datastr)
        try:
            print_serial(int(float(datastr)))
        except ValueError:
            print("Could not convert data to an integer.")
     #--------------------------------------------------
    pass
        


