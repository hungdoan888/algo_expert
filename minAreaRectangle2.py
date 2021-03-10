
def minimumAreaRectangle(points):
    
    # Create xPosMap
    xPosMap = {}
    for i in range(len(points)):
        if points[i][0] not in xPosMap:
            xPosMap[points[i][0]] = [points[i][1]]
        else:
            xPosMap[points[i][0]].append(points[i][1])
        
    # Sort keys and values from least to greatest
    for key in xPosMap:
        xPosMap[key].sort()   
    xPosMap = dict(sorted(xPosMap.items()))
    
    # Create edges dictionary
    edges = {}
    minArea = float("inf")
    for x, yValues in xPosMap.items():
        for i in range(len(yValues)):
            for j in range(i):
                yLine = "".join([str(yValues[j]), ":", str(yValues[i])])
                if yLine in edges:
                    area = (x - edges[yLine]) * (yValues[i] - yValues[j])
                    if area < minArea:
                        minArea = area
                edges[yLine] = x
    return minArea if minArea != float("inf") else 0

points = [
  [1, 5],
  [5, 1],
  [4, 2],
  [2, 4],
  [2, 2],
  [1, 2],
  [4, 5],
  [2, 5],
  [-1, -2]
]
minimumAreaRectangle(points)