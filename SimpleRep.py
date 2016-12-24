class SimpleRep(object):
    def __init__(self, bpm, block_size, nskips, time, reps):
        self.bpm = bpm
        self.block_size = block_size
        self.nskips = nskips
        self.time = time
        self.reps = reps
        # Debe tener un player, para tocarse a si mismo :S

    def gen_rep_time(self):
        """
        Generates time for next repetition
        """
        sec_per_beat = 60/self.bpm
        time_left_on_block = (sec_per_beat * self.block_size) - self.time
        time_skipping = sec_per_beat * self.block_size * self.nskips

        next_time = time_left_on_block + time_skipping + self.time

        return next_time

    def generate_list(self):
        """
        Generates the list with sleep times for the threads
        """
        lista_tiempos = []
        i = 0
        ntime = self.gen_rep_time()
        while i < self.reps:
            lista_tiempos.append(ntime)
            i += 1
        return lista_tiempos
