def menu(menus):
    for i in range(len(menus)):
        print("[%d]. %s" % (i + 1, menus[i]["title"]))
    print()
    value = input("원하는 번호를 선택해주세요.(N) : ")
    if value.lower() == 'n':
        return False
    elif int(value) > len(menus):
        return "잘못된 번호입니다."
    else:
        value = int(value)
        return menus[value - 1]["run"](menus[value - 1]["query"])


def showData(data):
    if data is None:
        print("스케쥴이 없습니다.")
        return True
    else:
        for i in data:
            print("과목 : %s\n시간 : %s\n학관 : %s\n관실번호 : %s" %
                  (i["name"], i["time"], i["at"], i["number"]))
            for j in i["professorInfo"]:
                print("성함 : %s\n학관 : %s\n랩실 : %s\n내선번호 : 063-220-%s\n메일주소 : %s@jj.ac.kr\n" %
                      (j["name"], j["lab"], j["labNumber"], j["phoneNumber"], j["email"]))
    return True
