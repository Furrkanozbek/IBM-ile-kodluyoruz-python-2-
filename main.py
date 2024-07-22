import math
#noktaları points listi altında belirledik
points = [(1, 2), (4, 5), (3, 1), (7, 6)]
#öklid mesafe hesaplama fonksiyonu burada sqrt fonksiyonu karekök için kullanılır.
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
#mesafeler hesaplanıp distances adlı listeye ekleniyor
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)
#min fonksiyonu kullanarak distances listesindeki en küçük eleman bulunur.
min_distance = min(distances)
print("Minimum Öklid mesafesi:", min_distance)
