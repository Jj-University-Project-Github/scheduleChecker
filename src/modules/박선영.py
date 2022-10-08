# 이름 : 박선영
# 학번 : 202268022
# 한일 : 주소를 불러와 출력해주는 함수와
#       윤년을 계산하는 함수 
#       다시 헌혈이 가능한 날을 불러오는 기능을 만들었습니다.

def getAddressInfo(name):
    file = open("./addressInfos.dat", 'r', encoding="utf-8")
    tempAddress = file.readlines()

    addresses = []

    for i in tempAddress:
        addressInfos = i.split(",")
        addressInfo = {
            "name": addressInfos[0],
            "address": addressInfos[1]
        }
        addresses.append(addressInfo)
    addressInfo = [i for i in addresses if i["name"] == name]
    return addressInfo


def getLastDay(year, month):
    if month == 2:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            return 29
        else:
            return 28
    elif month % 2 == 0:
        return 30
    else:
        return 31


def getCanBloodDonateDay(query=None):
    file = open("./bloodDonateDay.dat", "r", encoding="utf-8")

    lastYear, lastMonth, lastDay = file.read().split(",")
    lastYear = int(lastYear)
    lastMonth = int(lastMonth)
    lastDay = int(lastDay)

    lastDay += 60
    while lastDay > getLastDay(lastYear, lastMonth):
        lastMonth += 1
        if lastMonth > 12:
            lastYear += 1
            lastMonth -= 12
        lastDay -= getLastDay(lastYear, lastMonth)

    return "%d년 %d월 %d일에 다시 헌혈을 하실 수 있습니다." % (lastYear, lastMonth, lastDay)
