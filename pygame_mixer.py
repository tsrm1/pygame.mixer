# https://www.pygame.org/docs/ref/mixer.html#pygame.mixer.init
import pygame


# preset the mixer init arguments
pygame.mixer.pre_init()
# default:
# frequency=44100,
# size=-16, 
# channels=2, 
# buffer=512, 
# devicename=None, 
# allowedchanges=AUDIO_ALLOW_FREQUENCY_CHANGE | AUDIO_ALLOW_CHANNELS_CHANGE | AUDIO_ALLOW_FORMAT_CHANGE | AUDIO_ALLOW_ANY_CHANGE
print("preset the mixer init arguments")


# initialize the mixer module
pygame.mixer.init()
print("initialize the mixer module")

# # uninitialize the mixer
# pygame.mixer.quit()
# print('uninitialize the mixer')

# test if the mixer is initialized
pygame.mixer.get_init()
# (frequency, format, channels)  (44100, -16, 2)
# None
print("test if the mixer is initialized:", pygame.mixer.get_init())


# stop playback of all sound channels
pygame.mixer.stop()
print("stop playback of all sound channels")

# temporarily stop playback of all sound channels
pygame.mixer.pause()
print("temporarily stop playback of all sound channels")

# resume paused playback of sound channels
pygame.mixer.unpause()
print("resume paused playback of sound channels")

# set the total number of playback channels
# argument in milliseconds. After the sound is muted the playback will stop
pygame.mixer.fadeout(1000)
print("set the total number of playback channels")

# set the total number of playback channels
# The default value is 8
pygame.mixer.set_num_channels(8)
print("set the total number of playback channels")

# get the total number of playback channels
pygame.mixer.get_num_channels()
print("pygame.mixer.get_num_channels(): ", pygame.mixer.get_num_channels())

# reserve channels from being automatically used
pygame.mixer.set_reserved(1)
print("pygame.mixer.set_reserved(1): ", pygame.mixer.set_reserved(1))

# find an unused channel
# This will find and return an inactive Channel object.
pygame.mixer.find_channel()
print("find an unused channel: ", pygame.mixer.find_channel())

# test if any sound is being mixed
# Returns True if the mixer is busy mixing any channels. 
# If the mixer is idle then this return False
pygame.mixer.get_busy()
print("test if any sound is being mixed", pygame.mixer.get_busy())

# get the mixer's SDL version
# (major, minor, patch)
pygame.mixer.get_sdl_mixer_version()
print("get the mixer's SDL version: ", pygame.mixer.get_sdl_mixer_version())

