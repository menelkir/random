#!/usr/bin/env python

import dbus
import os

class MediaPlayer:
    """Recieves state from a MediaPlayer using dbus."""

    player_properties = False

    def __init__(self, player_name):
        # Get an instance of the dbus session bus, and retrieve
        #  a proxy object for accessing the MediaPlayer
        session_bus = dbus.SessionBus()
        player_proxy = session_bus.get_object(
            'org.mpris.MediaPlayer2.%s' % player_name,
            '/org/mpris/MediaPlayer2'
        )
        
        # Apply the interface 'org.freedesktop.DBus.Properties to
        #  the player proxy, allowing us to call .Get() and .GetAll()
        self.player_properties = dbus.Interface(player_proxy, 'org.freedesktop.DBus.Properties')

    """
        Retrieve the properties from the Player interface, return a
         song string.
    """
    def song_string(self):
        props = self.player_properties.GetAll('org.mpris.MediaPlayer2.Player')
        return "%s - %s" % (
            props["Metadata"]["xesam:artist"][0],
            props["Metadata"]["xesam:title"],
        )

    """
        Retrieve properties from the MediaPlayer2 interface, return
         whether a screen is maximised or not.
    """
    def is_fullscreen(self):
        props = self.player_properties.GetAll('org.mpris.MediaPlayer2')
        return bool(props["Fullscreen"])


player = MediaPlayer('strawberry')
# print("Status: %s" % ("Do Not Disturb" if player.is_fullscreen() else "Available"))
print("Playing: %s" % (player.song_string()))

g15screen = ("g15message -d 10 -c %s " % '"'+(player.song_string())+'"' )
os.system(g15screen)
