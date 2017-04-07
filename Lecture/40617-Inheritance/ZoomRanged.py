from Ranged import Ranged

class ZoomRanged(Ranged):
    MAX_CAPACITY = 6
    DEFAULT_ZOOM = 4

    def __init__(self, attack, name, zoom):
        super().__init__(attack,name, ZoomRanged.MAX_CAPACITY)
        #before setting the zoom, check that it is valid
        if zoom >0 and zoom <= 10:
            self.__zoom = zoom
        else:
            self.__zoom = ZoomRanged.DEFAULT_ZOOM

    def getZoom(self):
        return self.__zoom

    def setZoom(self, zoom):
        if zoom >0 and zoom <= 10:
            self.__zoom = zoom
        else:
            self.__zoom = ZoomRanged.DEFAULT_ZOOM

    #Override
    def __str__(self):
        msg = super().__str__() + ", Zoom: " + str(self.__zoom)
        return msg

    #override
    def use(self):
        result = self.reduceCapacity(2) #calls on the parent class's version
        if result == True:
            print("Zoom ranged weapon fired")
        else:
            print("Capacity empty. Cannot use zoom ranged weapon.")