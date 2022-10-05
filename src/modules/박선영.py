def consoleClear():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    return


def getAddressInfo(name: str) -> str:
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
