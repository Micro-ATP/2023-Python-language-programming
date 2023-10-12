import math

cities = [
    ("北京", 39.9, 116.4),  
    ("上海", 31.2, 121.4),  
    ("广州", 23.1, 113.2), 
    ("南通", 31.3, 120.1),
]

def calcDistance(lat1, lon1, lat2, lon2):
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)
    

    radiusOfEarth = 6371
    
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = radiusOfEarth * c
    
    return distance

def findNearCity():
    userLat = float(input("请输入您的纬度: "))
    userLon = float(input("请输入您的经度: "))
    
    nearestCity = None
    minDistance = float('inf')
    
    for city in cities:
        cityName, cityLat, cityLon = city
        distance = calcDistance(userLat, userLon, cityLat, cityLon)
        
        if distance < minDistance:
            minDistance = distance
            nearestCity = cityName
    
    return nearestCity

nearestCity = findNearCity()
print(f"最近的城市是{nearestCity}")
