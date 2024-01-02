## 클래스 선언
class  Car :
    speed = 0

    def upSpeed(self, value) :
        self.speed = self.speed + value

    def downSpeed(self, value) :
        self.speed = self.speed- value

class Sedan(Car) :
    seatNum = 0

    def getSeatNum(self) :
        return self.seatNum

class Truck(Car) :
    capacity = 0

    def getCapacity(self) :
        return self.capacity

class Santafe(Sedan) :
    pass
    
# 변수 선언
sedan1, truck1, santafe1 = None, None, None

# 메인 코드 부분
sedan1 = Sedan()
truck1 = Truck()
santafe1 = Santafe()

sedan1.upSpeed(100)
truck1.upSpeed(80)
santafe1.upSpeed(120)

sedan1.seatNum=5
truck1.capacity = 50
santafe1.seatNum=7

print("승용차의 속도는  %d km, 좌석수는 %d개입니다." % (sedan1.speed, sedan1.getSeatNum() ))
print("트럭의 속도는  %d km, 총중량는 %d톤입니다." % (truck1.speed, truck1.getCapacity() ))
print("산타페의 속도는  %d km, 좌석수는 %d개입니다." % (santafe1.speed, santafe1.getSeatNum() ))
