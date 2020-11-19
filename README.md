# ItsyBitsy_M4_Oled_Eyes
Driving Oled Animations in CircuitPython

To set the project up, the following hardware is needed:
⋅⋅*. 1x https://www.adafruit.com/product/3800 >
⋅⋅*. 2 x https://www.adafruit.com/product/938

for the sound effects a piezo buzzer is nedded (optional)...
⋅⋅*. 1x https://www.adafruit.com/product/1740

Follow the wiring diagram, and make sure to flash the two display firmware to the board!
Just double click the reset button and drag and drop the ItsyBitsyM4_2Display.uf2 inside the folder that will pop up...

For more info or in case something goes wrong, here is some more detailed information on how to do this...
https://learn.adafruit.com/introducing-adafruit-itsybitsy-m4/uf2-bootloader-details

Also you will need to drag and drop:
main.py 
spritesheet.bmp
spritesheet_look_left.bmp
spritesheet_look_right.bmp
spritesheet_look_left_low.bmp
spritesheet_look_right_low.bmp
spritesheet_happy.bmp
spritesheet_sad.bmp
spritesheet_center.bmp

Once you did this a sequence of all animations should be played back...
You can play individual animations by just sending the animations number to the serial port!
e.g "4" will play spritesheet_look_left_low.bmp

In this section of the code, you modifiy which images are being loaded and their corresponding playback commands:

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

Have fun!! :)

![alt text](https://github.com/SwannSchilling/ItsyBitsy_M4_Oled_Eyes/blob/main/OledsAndBuzzer.JPG)

