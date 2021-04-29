import pygame
import math






def grahamScan(points):
    
    sortedPoints = points.sort(key = lambda point: point[1])
    bottomMostY = sortedPoints[0][1]
    
    bottomLeftMost = getBottomLeftMost(bottomMostY,sortedPoints)

    sortedAngles = sortByAngle(bottomLeftMost,points)

    return getConvexHull(bottomLeftMost,sortedAngles)


def getConvexHull(startingPoint,sortedAngles):
    convexHullStack = [startingPoint,startingPoint[0]+.1,startingPoint[1]]]
    leftTestLine = [startingPoint, [startingPoint[0]+.1,startingPoint[1]] ]
    for i in range(1,len(sortedAngles)):
        element = sortedAngles[i]
        angle,pointKey = element[0],element[1]
        point = destringify(pointKey)
        if not isLeft(leftTestLine[0],leftTestLine[1],point):
            pass



def destringify(point):
    x,y = point.split(":")
    return [int(x),int(y)]




def isLeft(a,b,c) -> bool:
 ##return ((b.X - a.X)*(c.Y - a.Y) - (b.Y - a.Y)*(c.X - a.X)) > 0;
    return ((b[0] - a[0])*(c[1] - a[1]) - (b[1] - a[1])*(c[0] - a[0])) >=0 0





    





def getBottomLeftMost(bottomMostY,points):
    minX = float("inf")
    for point in points:
        if point[1] != bottomMostY:
            break
        if point[x] < minX:
            minX = pointX
    return minX
    



def sortByAngle(referencePoint,points):
    angles = []
    for point in points:
        if point == referencePoint:
            continue
        pointKey = stringify(point[0],point[1])
        angles.append(calculateAngle(referencePoint,point),pointKey)
    
    angles.sort(key=lambda angle: angle[0])

    return angles

def stringify(x,y):
    return str(x) + ":" + str(y)


def calculateAngle(point1,point2):
    dy=(y2 - y1)
    dx=(x2 - x1)
    radians = math.atan2(dy,dx)
    return radians

