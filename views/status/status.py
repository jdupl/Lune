from PySide import QtGui

from .playback_controls import PlaybackControls
from .progress_bar import ProgressBar
from .trackinfo import Trackinfo


class Status(QtGui.QWidget):
    def __init__(self, player):
        QtGui.QWidget.__init__(self)
        self.setObjectName('status')
        self.player = player

        self.controls = PlaybackControls(player)
        self.progress = ProgressBar(player)
        self.trackinfo = Trackinfo(player.status_vm)
        
        layout = QtGui.QHBoxLayout(self)
        layout.setContentsMargins(0,10,0,0)

        layout.addWidget(player.status_vm.album_art_display)
        layout.addWidget(self.trackinfo)
        layout.addWidget(self.progress)
        layout.addWidget(self.controls)
