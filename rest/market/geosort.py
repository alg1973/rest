import sys
import s2
import geocoder

#from .models import Restaraunt



#14 level - 200-400 meters radius
BASE_LEVEL=14

CELLS_SIZE=20

#Latitude: 1 deg = 110.54 km, 1 minute (0.01666666666666666666 deg) is 1.853 km
#so we will use some approximation:
# (100 m = 0.00090465 or 0.00089944234574563700) 
#Longitude: 1 deg = 111.320*cos(latitude) km

#So it's angle in degrees for 100 meters 
DEG_OF_100_M=0.00089944


def get_cells_of_region(lat,lng):
#
#    cap = s2.S2Cap.FromAxisAngle(s2.S2LatLng.FromDegrees(lat,lng).ToPoint(),
#                                 s2.S1Angle.Degrees(DEG_OF_100_M*3))
# There is a problem with SWIG with S2Point class so we use latlngrect instead
#
    cap = s2.S2LatLngRect.FromPoint(s2.S2LatLng.FromDegrees(lat,lng))
    cap=rect.ConvolveWithCap(s2.S1Angle.Degrees(DEG_OF_100_M*3))

    coverer = s2.S2RegionCoverer()
    coverer.set_min_level(BASE_LEVEL)
    coverer.set_max_level(BASE_LEVEL)
    coverer.set_max_cells(CELLS_SIZE)
    return  coverer.GetCovering(cap) 


def address2latlng(address):
    # yandex geocoder lang='ru-RU', google geocoder language='ru'
    geo=geocoder.yandex(address,lang='ru')
    return dict([('lat',double(geo.lat)),('lng',double(geo.lng))])

def latlng2sell(g):
    latlng = s2.S2LatLng.FromDegrees(g['lat'],g['lng'])
    cell = s2.S2CellId.FromLatLng(latlng).parent(geosort.BASE_LEVEL)
    return cell.id()
 
def addr2cell(addr):
    g=geosort.address2latlng(address)
    return latlng2sell(g)
    




#for f in  get_cells_of_circle(55.772516, 37.474153):
#    print (f.id()," ")
#
#print ("\n")
    
    
