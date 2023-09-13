# Payton Lutterman
# Alarms for Clock
# Last Updated 9-11



from winsound import *

import pygame as pg

# Mario Theme Song
"""
 def alarm1():
    for i in range(5):
        Beep(480, 200);

        Beep(1568, 200);

        Beep(1568, 200);

        Beep(1568, 200);

        Beep(739, 200);

        Beep(783, 200);

        Beep(783, 200);

        Beep(783, 200);

        Beep(369, 200);

        Beep(392, 200);

        Beep(369, 200);

        Beep(392, 200);

        Beep(392, 400);

        Beep(196, 400);

        Beep(739, 200);

        Beep(783, 200);

        Beep(783, 200);

        Beep(739, 200);

        Beep(783, 200);

        Beep(783, 200);

        Beep(739, 200);

        Beep(83, 200);

        Beep(880, 200);

        Beep(830, 200);

        Beep(880, 200);

        Beep(987, 400);

        Beep(880, 200);

        Beep(783, 200);

        Beep(698, 200);

        Beep(739, 200);

        Beep(783, 200);

        Beep(783, 200);

        Beep(739, 200);

        Beep(783, 200);

        Beep(783, 200);

        Beep(739, 200);

        Beep(783, 200);

        Beep(880, 200);

        Beep(830, 200);

        Beep(880, 200);

        Beep(987, 400);



    Beep(1108, 10);
    Beep(1174, 200);
    Beep(1480, 10);
    Beep(1568, 200);


    Beep(739, 200);

    Beep(783, 200);

    Beep(783, 200);

    Beep(739, 200);

    Beep(783, 200);

    Beep(783, 200);

    Beep(739, 200);

    Beep(783, 200);

    Beep(880, 200);

    Beep(830, 200);

    Beep(880, 200);

    Beep(987, 400);

    Beep(880, 200);

    Beep(783, 200);

    Beep(698, 200);

    Beep(659, 200);

    Beep(698, 200);

    Beep(784, 200);

    Beep(880, 400);

    Beep(784, 200);

    Beep(698, 200);

    Beep(659, 200);

    Beep(587, 200);

    Beep(659, 200);

    Beep(698, 200);

    Beep(784, 400);

    Beep(698, 200);

    Beep(659, 200);

    Beep(587, 200);

    Beep(523, 200);

    Beep(587, 200);

    Beep(659, 200);

    Beep(698, 400);

    Beep(659, 200);

    Beep(587, 200);

    Beep(493, 200);

    Beep(523, 200);


    Beep(349, 400);

    Beep(392, 200);

    Beep(329, 200);

    Beep(523, 200);

    Beep(493, 200);

    Beep(466, 200);

    Beep(440, 200);

    Beep(493, 200);

    Beep(523, 200);

    Beep(880, 200);

    Beep(493, 200);

    Beep(880, 200);

    Beep(1760, 200);

    Beep(440, 200);

    Beep(392, 200);

    Beep(440, 200);

    Beep(493, 200);

    Beep(783, 200);

    Beep(440, 200);

    Beep(783, 200);

    Beep(1568, 200);

    Beep(392, 200);

    Beep(349, 200);

    Beep(392, 200);

    Beep(440, 200);

    Beep(698, 200);

    Beep(415, 200);

    Beep(698, 200);

    Beep(139, 200);



    Beep(329, 200);

    Beep(311, 200);

    Beep(329, 200);

    Beep(659, 200);

    Beep(698, 400);

    Beep(783, 400);

    Beep(440, 200);

    Beep(493, 200);

    Beep(523, 200);

    Beep(880, 200);

    Beep(493, 200);

    Beep(880, 200);

    Beep(1760, 200);

    Beep(440, 200);

    Beep(392, 200);

    Beep(440, 200);

    Beep(493, 200);

    Beep(783, 200);

    Beep(440, 200);

    Beep(783, 200);

    Beep(1568, 200);

    Beep(392, 200);

    Beep(349, 200);

    Beep(392, 200);

    Beep(440, 00);

    Beep(698, 200);

    Beep(659, 200);

    Beep(698, 200);

    Beep(739, 200);

    Beep(783, 200);

    Beep(392, 200);

    Beep(392, 200);

    Beep(392, 200);

    Beep(392, 200);

    Beep(196, 200);

    Beep(196, 200);

    Beep(196, 200);

    Beep(185, 200);

    Beep(196, 200);

    Beep(185, 200);

    Beep(196, 200);

    Beep(207, 200);

    Beep(220, 200);

    Beep(233, 200);

    Beep(246, 200); 
"""

def alarm2():
    pg.mixer.music.load("assets/sound/Monkey Screeches 1 - QuickSounds.com.mp3")
    pg.mixer.music.play(loops=-1, fade_ms=200)

def alarm3():
    pg.mixer.music.load("assets/sound/Monkeys in The Zoo - QuickSounds.com.mp3")
    pg.mixer.music.play(loops=-1, fade_ms=200)