# ItsyBitsy_M4_Oled_Eyes
Driving Oled Animations in CircuitPython

To set the project up, the following hardware is needed:
1. 1x https://www.adafruit.com/product/3800 
2. 2 x https://www.adafruit.com/product/938

For the sound effects a piezo buzzer is nedded (optional)...
1. 1x https://www.adafruit.com/product/1740

Follow the wiring diagram, and make sure to flash the two display firmware to the board!

Just double click the reset button and drag and drop the ItsyBitsyM4_2Display.uf2 inside the folder that will pop up...

For more info or in case something goes wrong, here is some more detailed information on how to do this...

https://learn.adafruit.com/introducing-adafruit-itsybitsy-m4/uf2-bootloader-details

Also you will need to drag and drop:
1. main.py 
2. spritesheet.bmp
3. spritesheet_look_left.bmp
4. spritesheet_look_right.bmp
5. spritesheet_look_left_low.bmp
6. spritesheet_look_right_low.bmp
7. spritesheet_happy.bmp
8. spritesheet_sad.bmp
9. spritesheet_center.bmp

Once you did this a sequence of all animations should be played back...

You can play individual animations by just sending the animations number to the serial port!

e.g "4" will play spritesheet_look_left_low.bmp

In this section of the code, you modifiy which images are being loaded and their corresponding playback commands:

```
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
```

The code is a bit messy, but it should work fine...

You can connect via Serial USB or UART...

Have fun!! :)

![alt text](https://github.com/SwannSchilling/ItsyBitsy_M4_Oled_Eyes/blob/main/OledsAndBuzzer.JPG)

