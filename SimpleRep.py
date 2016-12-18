class SimpleRep(object):
    def __init__(self, bpm, block_size, nskips, time):
        self.bpm = bpm
        self.block_size = block_size
        self.nskips = nskips
        self.time = time

    def gen_rep_time(self):
        """
        Lógica de generar el tiempo que se demore en llegar a la próxima repetición.
        """
        sec_per_beat = 60/self.bpm
        time_left_on_block = (sec_per_beat * self.block_size) - self.time
        time_skipping = sec_per_beat * self.block_size * self.nskips

        next_time = time_left_on_block + time_skipping + self.time

        return next_time

    
