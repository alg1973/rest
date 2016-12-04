import sys
import s2

#from .models import Restaraunt


DEG_OF_100_M=0.00089944
BASE_LEVEL=14
CELLS_SIZE=20

#Latitude: 1 deg = 110.54 km, 1 minute (0.01666666666666666666 deg) is 1.853 km
#so we will use some approximation:
# (100 m = 0.00090465 or 0.00089944234574563700) 
#Longitude: 1 deg = 111.320*cos(latitude) km

def get_cells_of_circle(lat,lng):
#
#    cap = s2.S2Cap.FromAxisAngle(s2.S2LatLng.FromDegrees(lat,lng).ToPoint(),
#                                 s2.S1Angle.Degrees(DEG_OF_100_M*3))
# There is a problem with SWIG with S2Point class so we use latlngrect instead
#
    rect = s2.S2LatLngRect.FromPoint(s2.S2LatLng.FromDegrees(lat,lng))
    rect=rect.ConvolveWithCap(s2.S1Angle.Degrees(DEG_OF_100_M*3))

    coverer = s2.S2RegionCoverer()
    coverer.set_min_level(BASE_LEVEL)
    coverer.set_max_level(BASE_LEVEL)
    coverer.set_max_cells(CELLS_SIZE)
    return  coverer.GetCovering(cap) 


for f in  get_cells_of_circle(55.772516, 37.474153):
    print (f.id()," ")

print ("\n")
    
    
