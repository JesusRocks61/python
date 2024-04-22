import pytest
from television import *

class Test:
    def setup_method(self):
        self.tv1 = Television()

    def teardown_method(self):
        del self.tv1

    def test_init(self):
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_power(self):
        self.tv1.power() # Turn on TV
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'

        self.tv1.power() # Turn off TV
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_mute(self):
        self.tv1.power() # Turn on TV
        self.tv1.volume_up() # Turn up 1 volume
        self.tv1.mute() # Mute TV
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'

        self.tv1.mute() # Unmute TV
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 1'

        self.tv1.mute() # Mute TV
        self.tv1.power() # Turn off TV
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'

        self.tv1.power() # Turn on TV to unmute again
        self.tv1.mute() # Unmute TV
        self.tv1.power() # Turn off TV
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 1'

    def test_channel_up(self):
        self.tv1.channel_up() # Shouldn't raise since TV is not on
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'

        self.tv1.power() # Turn on TV
        self.tv1.channel_up() # Raises Channel to 1
        assert self.tv1.__str__() == 'Power = True, Channel = 1, Volume = 0'

        self.tv1.channel_up() # Raises Channel to 2
        self.tv1.channel_up() # Raises Channel to 3
        self.tv1.channel_up() # Resets Channel back to 0
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'

    def test_channel_down(self):
        self.tv1.channel_down() # Shouldn't be lowered since TV is not on
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'

        self.tv1.power() # Turns on TV
        self.tv1.channel_down() # Makes Channel 3, the max, since it is already at 0
        assert self.tv1.__str__() == 'Power = True, Channel = 3, Volume = 0'

    def test_volume_up(self):
        self.tv1.volume_up() # Shouldn't be raised since TV is not on
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'

        self.tv1.power() # Turns TV on
        self.tv1.volume_up() # Raises Volume to 1
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 1'

        self.tv1.mute() # Mutes the TV
        self.tv1.volume_up() # Unmutes the TV and raises Volume to 2
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 2'

        self.tv1.volume_up() # Already at Max Volume so it stays at 2
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 2'

    def test_volume_down(self):
        self.tv1.volume_down() # Shouldn't be lowered since TV is not on
        assert self.tv1.__str__() == 'Power = False, Channel = 0, Volume = 0'

        self.tv1.power() # Turns TV on
        self.tv1.volume_up() # Sets Volume to 1
        self.tv1.volume_up() # Sets Volume to 2
        self.tv1.volume_down() # Sets Volume to 1
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 1'

        self.tv1.mute() # Mutes the TV
        self.tv1.volume_down() # Unmutes the TV and sets Volume to 0
        assert self.tv1.__str__() == 'Power = True, Channel = 0, Volume = 0'

