import shelve
from models.song import Song

class LibraryDB:
    def __init__(self):
        self.db_file = 'Library.db'

    def get_all(self):
        songs = []
        s = shelve.open(self.db_file)
        for key in s.keys():
            entry = s[key]
            songs.append(Song(entry.path, entry.track_info))
        return songs

    def add_song(self, song):
        entry = SongAdapter(song)
        s = shelve.open(self.db_file)
        s[entry.path] = entry
        s.close()
        return

class SongAdapter:
    def __init__(self, song):
        self.path = song.path
        self.track_info = song.track_info
