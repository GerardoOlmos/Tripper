from pydub import AudioSegment
from pydub.playback import play
import threading
import time


class Player(object):
    """
    This class plays the samples given by the lists and the sample ids
    """
    def __init__(self, sample_id):
        self.sample_id = sample_id

    def play_sample(self):
        song = AudioSegment.from_wav(self.sample_id)
        play(song)

    def play_list(self, list_):
        for t in list_:
            threading.Thread(target=self.play_sample).start()
            time.sleep(t)
