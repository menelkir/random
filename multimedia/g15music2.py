#!/usr/bin/env python

import dbus
import subprocess

class MediaPlayer:
    player_properties = False
    def __init__(self, player_name):
        session_bus = dbus.SessionBus()
        player_proxy = session_bus.get_object(
            'org.mpris.MediaPlayer2.%s' % player_name,
            '/org/mpris/MediaPlayer2'
        )
        self.player_properties = dbus.Interface(player_proxy, 'org.freedesktop.DBus.Properties')

    def song_string(self):
        props = self.player_properties.GetAll('org.mpris.MediaPlayer2.Player')
        return "%s" % (
            props["Metadata"]["xesam:title"],
        )

    def artist_string(self):
        props = self.player_properties.GetAll('org.mpris.MediaPlayer2.Player')
        return "%s" % (
            props["Metadata"]["xesam:artist"][0],
            )

    def is_fullscreen(self):
        props = self.player_properties.GetAll('org.mpris.MediaPlayer2')
        return bool(props["Fullscreen"])


player = MediaPlayer('strawberry')
# print("Status: %s" % ("Do Not Disturb" if player.is_fullscreen() else "Available"))
print("Playing: %s" % (player.song_string()))

def buceta(cmd):
    subprocess.Popen(cmd, shell=True, executable='/usr/bin/g15message')

cmd = subprocess.call(["g15message", "-d 10", "-c", "-t", (player.artist_string()), (player.song_string())])
