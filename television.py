class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.status = False
        self.muted = False
        self.channel = 0
        self.volume = 0

    def power(self):
        if self.status:
            self.status = False
        else:
            self.status = True

    def mute(self):
        if self.status:
            if self.muted:
                self.muted = False
            else:
                self.muted = True
    def channel_up(self):
        if self.status:
            if self.channel == 3:
                self.channel = 0
            else:
                self.channel += 1

    def channel_down(self):
        if self.status:
            if self.channel == 0:
                self.channel = 3
            else:
                self.channel -= 1

    def volume_up(self):
        if self.status:
            self.muted = False
            if self.volume == 2:
                self.volume = 2
            else:
                self.volume += 1

    def volume_down(self):
        if self.status:
            self.muted = False
            if self.volume == 0:
                self.volume = 0
            else:
                self.volume -= 1

    def __str__(self):
        if self.muted:
            return f'Power = {self.status}, Channel = {self.channel}, Volume = {0}'
        else:
            return f'Power = {self.status}, Channel = {self.channel}, Volume = {self.volume}'
