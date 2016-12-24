import threading
import Player
from SimpleRep import SimpleRep
from Player import Player


class Main(object):
    """This class starts the app"""
    @staticmethod
    def start():
        print("Starting Tripper")

    @staticmethod
    def create_simple_rep(bpm, block_size, nskips, time, reps):
        s = SimpleRep(bpm, block_size, nskips, time, reps)
        return s.generate_list()

    @staticmethod
    def play_rep(sample_id, slist):
        p = Player(sample_id)
        p.play_list(slist)

Main.start()
print(Main.create_simple_rep(120, 7, 2, 2.4, 20))
# Main.play_rep("bells.wav", Main.create_simple_rep(120, 7, 2, 2.4, 20))
