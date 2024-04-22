class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        '''
        Sets up the television object
        Sets status (power) to False
        Sets muted to False
        Sets Channel to 0
        Sets Volume to 0
        '''
        self.status = False
        self.muted = False
        self.channel = 0
        self.volume = 0

    def power(self):
        '''Used to turn on or off the television object'''
        if self.status:
            self.status = False
        else:
            self.status = True

    def mute(self):
        '''Used to put mute on or off the television object'''
        if self.status:
            if self.muted:
                self.muted = False
            else:
                self.muted = True
    def channel_up(self):
        '''Used to turn up the channel for the television object'''
        if self.status:
            if self.channel == 3:
                self.channel = 0
            else:
                self.channel += 1

    def channel_down(self):
        ''' Used to turn down the channel for the television object '''
        if self.status:
            if self.channel == 0:
                self.channel = 3
            else:
                self.channel -= 1

    def volume_up(self):
        ''' Used to turn up the volume for the television object'''
        if self.status:
            self.muted = False
            if self.volume == 2:
                self.volume = 2
            else:
                self.volume += 1

    def volume_down(self):
        '''Used to turn down the volume for the television object'''
        if self.status:
            self.muted = False
            if self.volume == 0:
                self.volume = 0
            else:
                self.volume -= 1

    def __str__(self):
        '''Displays the Power, Channel, and Volume'''
        if self.muted:
            return f'Power = {self.status}, Channel = {self.channel}, Volume = {0}'
        else:
            return f'Power = {self.status}, Channel = {self.channel}, Volume = {self.volume}'
