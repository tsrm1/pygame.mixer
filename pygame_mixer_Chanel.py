# https://www.pygame.org/docs/ref/mixer.html#pygame.mixer.Channel
import pygame
import os
import time                             # импортируем библиотеку time  (time.sleep(3))


def load_all_music(directory, accept=('.wav', '.mp3', '.ogg', '.mdi')):
    playlist = []
    for song in os.listdir(directory):
        name,ext = os.path.splitext(song)
        if ext.lower() in accept:
            playlist.append(os.path.join(directory, song))
    print(playlist)
    return playlist

def spend_time(t):
    for i in range(int(t*8000000)):
        j = i**2


mixer = pygame.mixer.init()
playlist = load_all_music("music")
current_music = pygame.mixer.Sound(playlist[0])


# pygame.mixer.Channel
# Create a Channel object for controlling playback
# Channel(id) -> Channel
channel = pygame.mixer.Channel(1)
print(f'channel = pygame.mixer.Channel(1) -> ', channel)

# pygame.mixer.Channel.play
# play a Sound on a specific Channel
# play(Sound, loops=0, maxtime=0, fade_ms=0) -> None
# # (loops=0, maxtime=0, fade_ms=0) -> Channel
# # loop = -1  - бесконечно
# # loop = 0   - без повтора
# # loop = 1   - повторить 1 раз
# # maxtime = 5000 - максимальное время воспроизведения, ms
# # fade_ms = 3000 - затухание, ms - НЕ РАБОТАЕТ!
print(f'channel.play()          -> ', channel.play(current_music))
spend_time(5)

# pygame.mixer.Channel.pause
# temporarily stop playback of a channel
print(f'channel.pause()         -> ', channel.pause())
spend_time(2)

# pygame.mixer.Channel.unpause
# resume pause playback of a channel
print(f'channel.unpause()       -> ', channel.unpause())
spend_time(2)

# pygame.mixer.Channel.set_volume
# set the volume of a playing channel
print(f'channel.set_volume(0.1) -> ', channel.set_volume(0.1))
spend_time(2)
print(f'channel.set_volume(1)   -> ', channel.set_volume(1))
spend_time(2)
print(f'channel.set_volume(0.5) -> ', channel.set_volume(0.5))
spend_time(2)

# pygame.mixer.Channel.get_volume
# get the volume of the playing channel
print(f'channel.get_volume()    -> ', channel.get_volume())
spend_time(2)

# pygame.mixer.Channel.get_busy
# check if the channel is active
print(f'channel.get_busy()      -> ', channel.get_busy())
spend_time(2)

# pygame.mixer.Channel.get_sound
# get the currently playing Sound
print(f'channel.get_sound()     -> ', channel.get_sound())
spend_time(4)

# pygame.mixer.Channel.queue
# queue a Sound object to follow the current
current_music = pygame.mixer.Sound(playlist[1])
print(f'channel.queue(Sound)    -> ', channel.queue(current_music))
spend_time(1)

pygame.init()       # нужен для отслеживания событий
# pygame.mixer.Channel.set_endevent
# have the channel send an event when playback stops
MUSIC_END = pygame.USEREVENT + 1
channel.set_endevent(MUSIC_END)

# pygame.mixer.Channel.get_queue
# return any Sound that is queued
print(f'channel.get_queue()     -> ', channel.get_queue())
# spend_time(75) 

# pygame.mixer.Channel.get_endevent
# get the event a channel sends when playback stops
i = True
j = 0
while i:
    for event in pygame.event.get():
        if event.type == MUSIC_END:
            print('MUSIC_END EVENT')
            i = False
    j += 1
    if j/1000000 == int(j/1000000):
        print(i/1000000)

# pygame.mixer.Channel.fadeout
# stop playback after fading channel out
spend_time(3)
print(f'channel.fadeout(2000)   -> ', channel.fadeout(2000))
spend_time(3)


# pygame.mixer.Channel.stop
# stop playback on a Channel
print(f'channel.stop()          -> ', channel.stop())





spend_time(2)
pygame.quit()