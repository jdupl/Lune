from PySide import QtGui

from views.status.playback_controls import PlaybackControls
from views.status.progress_bar import ProgressBar
from views.status.trackinfo import Trackinfo


class Status(QtGui.QWidget):
    def __init__(self, player):
        QtGui.QWidget.__init__(self)

        self.player = player

        self.controls = PlaybackControls(player)
        self.progress = ProgressBar(player)
        self.trackinfo = Trackinfo(player)
        
        layout = QtGui.QHBoxLayout(self)
        
        layout.addWidget(self.trackinfo)
        layout.addWidget(self.progress)
        layout.addWidget(self.controls)