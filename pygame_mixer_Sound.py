# https://www.pygame.org/docs/ref/mixer.html#pygame.mixer.Sound
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


# # Create a new Sound object from a file or buffer object
# pygame.mixer.Sound(playlist[0])
# # Sound(filename) -> Sound
# # Sound(file=filename) -> Sound
# # Sound(file=pathlib_path) -> Sound
# # Sound(buffer) -> Sound
# # Sound(buffer=buffer) -> Sound
# # Sound(object) -> Sound
# # Sound(file=object) -> Sound
# # Sound(array=object) -> Sound
current_music = pygame.mixer.Sound(playlist[0])
print(f'current_music = pygame.mixer.Sound({playlist[0]})', current_music)



# # pygame.mixer.Sound.play
# # begin sound playback
# pygame.mixer.Sound(playlist[0]).play()
# # (loops=0, maxtime=0, fade_ms=0) -> Channel
# # loop = -1  - бесконечно
# # loop = 0   - без повтора
# # loop = 1   - повторить 1 раз
# # maxtime = 5000 - максимальное время воспроизведения, ms
# # fade_ms = 3000 - затухание, ms - НЕ РАБОТАЕТ!

channel = current_music.play()
# channel = current_music.play(maxtime=10000)
# channel = current_music.play(loops=1)
# channel = current_music.play(fade_ms=5000)
print(f'pygame.mixer.Sound({playlist[0]}).play()', channel)


# # # pygame.mixer.Sound.stop
# # # stop sound playback
# spend_time(10)
# # pygame.mixer.Sound(playlist[0])
# current_music.stop()
# print(f'pygame.mixer.Sound({playlist[0]}).stop()')

# # # pygame.mixer.Sound.fadeout
# # # stop sound playback after fading out
# # # pygame.mixer.Sound.fadeout(3000) # - НЕ РАБОТАЕТ!
# current_music.fadeout(3000)
# # channel.fadeout(3000)
# print('pygame.mixer.Sound({playlist[0]}).fadeout(3000)')
# spend_time(10)

# # # pygame.mixer.Sound.set_volume
# # # set the playback volume for this Sound
current_music.set_volume(1)
print("set the playback volume for this Sound 100%")
# # channel.set_volume(1)
# # print("set the playback volume for this Channel 100%")
spend_time(5)
current_music.set_volume(0.2)
print("set the playback volume for this Sound 20%")
# channel.set_volume(0.2)
# print("set the playback volume for this Channel 20%")
# spend_time(5)


# pygame.mixer.Sound.get_volume
# get the playback volume
print("get the playback volume, Channel", channel.get_volume())
spend_time(5)

# pygame.mixer.Sound.get_num_channels
# count how many times this Sound is playing
print("count how many times this Sound is playing", current_music.get_num_channels())
spend_time(5)


# pygame.mixer.Sound.get_length
# get the length of the Sound
print(f'get the length of the Sound: {current_music.get_length()} s')
spend_time(5)


# pygame.mixer.Sound.get_raw
# return a bytestring copy of the Sound samples.
# Return a copy of the Sound object buffer as a bytes.
print(f'return a bytestring copy of the Sound samples : {playlist[0]} ')
with open(file='crash.wav', mode='wb') as file:
    file.write(current_music.get_raw())
spend_time(5)

crash = load_all_music('.')
crash_music = pygame.mixer.Sound(crash[0])
channel = crash_music.play()
print(f'Play a bytestring copy of the Sound samples : {crash[0]} ')
spend_time(10)

# time.sleep(5000)                       # устанавливаем задержку на 3 секунды
