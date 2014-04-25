from models.song import Song


class SongQueue:

    def __init__(self, queue=[], startFrom=0):
        self.queue = queue
        self.startFrom = startFrom
        self.at = startFrom

    def isEmpty(self):
        if len(self.queue) != 0:
            return False
        else:
            return True

    def hasNext(self):
        if (not self.isEmpty() and
            self.at not in [self.startFrom, len(self.queue)]):
            return True
        return False

    def getNext(self):
        if not self.at:
            self.at = self.startFrom
        else:
            if self.hasNext():
                self.at += 1
        return self.getCurrent()

    def hasPrev(self):
        if self.at != self.startFrom and not self.isEmpty():
            return True
        return False

    def getPrev(self):
        if not self.at:
            self.at = self.startFrom
        else:
            if self.hasPrev():
                self.at -= 1
        return self.getCurrent()

    def getCurrent(self):
        #return self.queue[self.at]
        return Song("Beyond_the_Golden_Valleys.mp3")
