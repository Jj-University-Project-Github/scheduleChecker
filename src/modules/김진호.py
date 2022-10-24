"""
학번 : 202268020
이름 : 김진호
기능 : 메뉴 선택 기능, 화면 상에 내용이 보이도록 출력.
"""

def menu(menus):
    """
    각 메뉴별 제목과 실행할 내용, 매개변수를 받아와 적절하게 가공하고 결과값을 반환합니다.
    """
    for i in range(len(menus)): #for문으로 문장을 메뉴 수만큼 반복
        print("[%d]. %s" % (i + 1, menus[i]["title"])) #i번째 메뉴 표현 및 i번째 메뉴의 제목 출력하기
    print() #입력줄을 나누기 위해 공백으로 print를 실행함.
    value = input("원하는 번호를 선택해주세요.(N) : ") #원하는 번호를 입력
    if value.lower() == 'n': #만약 입력받은 번호가 n 또는 N일 경우
        return False #종료 신호 반환
    elif int(value) > len(menus) or int(value) < 0: #입력받은 번호가 기존 번호보다 크거나 0보다 작을 경우
        return "잘못된 번호입니다."
    else: #정상적으로 입력되었다면
        value = int(value) #입력된 번호의 내용을 매개변수와 함께 실행하기
        return menus[value - 1]["run"](menus[value - 1]["query"]) #menu에서 +1 -> value에서 -1


def showData(data):
    """
    스케쥴 데이터를 과목, (강의)시간, 학관, 관실번호, 교수님의 성함,학관,랩실,내선번호,메일주소 등을 출력합니다.
    """
    if data is None: #만약 데이터가 없을 경우
        print("스케쥴이 없습니다.")
        return True #정상실행이 되었다고 반환
    else: #만약 데이터가 있을 경우
        for i in data: #과목 데이터를 불러와서 i에 대입하기
            print("과목 : %s\n시간 : %s\n학관 : %s\n관실번호 : %s" %
                  (i["name"], i["time"], i["at"], i["number"])) #i번째 강의의 과목, 시간, 학관, 관실번호를 출력.
            for j in i["professorInfo"]: #i번째 강의의 교수님 정보를 j에 대입
                print("성함 : %s\n학관 : %s\n랩실 : %s\n내선번호 : 063-220-%s\n메일주소 : %s@jj.ac.kr\n" %
                      (j["name"], j["lab"], j["labNumber"], j["phoneNumber"], j["email"])) #위에서 j에 입력된 교수님의 성함, 학관, 랩실, 내선번호, 메일주소 출력
    return True #정상실행이 되었다고 반환
