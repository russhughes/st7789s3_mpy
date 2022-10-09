""" LilyGo T-DISPLAY-S3 170x320 ST7789 display """

from machine import Pin, SPI
import st7789

TFA = 0
BFA = 0

def config(rotation=0, buffer_size=0, options=0):
    LCD_POWER = Pin(15, Pin.OUT)
    LCD_POWER.value(1)

    return st7789.ST7789(
        Pin(48, Pin.OUT),
        Pin(47, Pin.OUT),
        Pin(46, Pin.OUT),
        Pin(45, Pin.OUT),
        Pin(42, Pin.OUT),
        Pin(41, Pin.OUT),
        Pin(40, Pin.OUT),
        Pin(39, Pin.OUT),
        Pin(8, Pin.OUT),
        Pin(9, Pin.OUT),
        170,
        320,
        reset=Pin(5, Pin.OUT),
        cs=Pin(6, Pin.OUT),
        dc=Pin(7, Pin.OUT),
        backlight=Pin(38, Pin.OUT),
        rotation=rotation,
        options=options,
        buffer_size= buffer_size)
