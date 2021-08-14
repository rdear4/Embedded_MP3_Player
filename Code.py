import board
import audiomp3
import audioio
import digitalio
import time
# Required for CircuitPlayground Express
#speaker_enable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
#speaker_enable.switch_to_output(value=True)

led = digitalio.DigitalInOut(board.D13)
shutoff = digitalio.DigitalInOut(board.D12)

led.direction = digitalio.Direction.OUTPUT
shutoff.direction = digitalio.Direction.OUTPUT

filename = "Kansas.mp3"

data = open(filename, "rb")
mp3 = audiomp3.MP3Decoder(data)
a = audioio.AudioOut(board.A0)

print("playing")
a.play(mp3)

while a.playing:
    print("playing...")
    time.sleep(1)

shutoff.value = True
