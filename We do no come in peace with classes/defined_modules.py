import math
def circletouch(pos1,rad1,pos2,rad2):
    x = abs(abs(pos1[0])-abs(pos2[0]))
    y = abs(abs(pos1[1])-abs(pos2[1]))
    if math.sqrt(x**2 + y**2) < rad1+rad2:
        return True

def degtodir(self,flyspeed,bulletdir):
    y = flyspeed * math.sin(bulletdir/180*math.pi)
    x = flyspeed * math.cos(bulletdir/180*math.pi)
    return x,y

def dirtodeg(x,y):
    #deg = math.atan(y/x)*180/math.pi
    try:
        deg = math.atan2(x,y)
        deg = 360-deg*57.29+90
    except:
        x+=0.001
        y+=0.001
        deg = math.atan2(x,y)
        deg = 360-deg*57.29+90
    return deg

def locatedir(pos1,pos2,speed):
    distancex=pos1[0]-pos2[0]
    distancey=pos1[1]-pos2[1]
    distance=math.sqrt(distancex**2+distancey**2)
    distancex = distancex/distance*speed
    distancey = distancey/distance*speed
    return [distancex,distancey]

def touch(pos1,size1,pos2,size2):
    nx2 = pos1[0] + size1[0]/2
    ny2 = pos1[1] + size1[1]/2
    nx1 = pos1[0] - size1[0]/2
    ny1 = pos1[1] - size1[1]/2
    nx4 = pos2[0] + size2[0]/2
    ny4 = pos2[1] + size2[1]/2
    nx3 = pos2[0] - size2[0]/2
    ny3 = pos2[1] - size2[1]/2
    #print(nx1,ny1,nx2,ny2,nx3,ny3,nx4,ny4)
    if ny3 < ny2 and ny3 > ny1 or ny4 > ny1 and ny3 < ny2:
        if nx3 < nx2 and nx3 > nx1 or nx4 > nx1 and nx3 < nx2:
            return True

def stufftouchedtiles(pos,size,tiles):
    touched = []
    for tile in tiles:
        if tile.touching(pos,size) == True:
            touched.append(tile.gettype())
    #print(touched)
    return touched

