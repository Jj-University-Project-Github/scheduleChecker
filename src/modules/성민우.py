"""
> 이름
성민우

> 학번
202268018  


> 제작 내용
-   스케쥴 정보를 불러와 가공한 뒤 오늘의 시간표를 
    오의찬 선배님이 가공한 교수님들의 정보와
    박선영이 만든 함수로부터 강의가 이루어지는 학관의 주소를 불러와
    진호의 함수를 통해 시간표와 교수님의 정보, 확관 주소를 함께 출력합니다.
"""

from modules.김진호 import menu, showData
from modules.박선영 import getAddressInfo
from modules.오의찬 import getProfessorInfos


def getScheduleInfo(week):
    """
    week: int   # 오늘의 주일 정보를 요청합니다.
    """
    file = open("./scheduleInfos.dat", 'r', encoding="utf-8")
    # 스케쥴 정보를 utf-8으로 인코딩하여 불러옵니다.
    # 불러온 정보는 readlines를 통해 한줄한줄 list화 하여 변수에 저장합니다.
    tempSchedule = file.readlines()

    schedules = []  # 가공된 스케쥴 정보(type = dict)가 저장되는 공간입니다.
    count = 1  # 주일마다의 정보를 가공할때 핸들링을 위해 주일 스케쥴 수를 확인하는 변수입니다.

    if week == "Ask":  # 원하는 주간 스케쥴 정보를 직접 입력할 때 사용하는 명령어 입니다.
        # 원하는 주일의 정보를 불러오는 메뉴입니다.
        menus = [
            {
                "title": "월",
                "run": getScheduleInfo,
                "query": 0
            },
            {
                "title": "화",
                "run": getScheduleInfo,
                "query": 1
            },
            {
                "title": "수",
                "run": getScheduleInfo,
                "query": 2
            },
            {
                "title": "목",
                "run": getScheduleInfo,
                "query": 3
            },
            {
                "title": "금",
                "run": getScheduleInfo,
                "query": 4
            },
        ]
        while menu(menus):  # 메뉴가 끝났다는 메세지가 돌아올 때 까지 반복합니다.
            pass  # 반복하는 동안 실행할 코드가 없으므로 pass를 사용하였습니다.
    elif week > 4:  # 만약 4보다 큰 수가 입력될 경우 주말이므로 무시합니다.
        """
        진호의 코드에서 이미 처리된 코드이기에 사실상 의미가 없지만
        만약 메뉴에서 처리되지 않았을 경우 이와 같이 처리하여야 하므로
        예시상 추가하였습니다.
        """
        print("오늘은 일정이 없습니다.")
        return True
    else:
        for i in tempSchedule: # i에는 각 주일별 스케쥴 정보가 담겨있습니다.
            i = i.strip() # 각 스케쥴 정보의 양 끝에 있는 공백을 제거합니다.
            if len(schedules) != count: # 만약 스케쥴을 담는 공간의 크기와 주일 스케쥴 수 핸들러의 크기가 다를 경우
                schedules.append([]) # 새로운 주일의 정보를 담을 공간을 생성합니다.
            if not i or i == "\n": # 만약 스케쥴 정보가 비어있거나 \n일 경우
                count += 1 # 핸들러에 1을 더합니다.
            else: # 정상적인 경우
                scheduleInfos = i.split(",") # 정보를 "","를 기준으로 나눈 뒤
                scheduleInfo = {
                    "name": scheduleInfos[0],
                    "time": scheduleInfos[1],
                    "at": scheduleInfos[2],
                    "number": scheduleInfos[3],
                    "professorInfo": getProfessorInfos(scheduleInfos[0]),
                    "address": getAddressInfo(scheduleInfos[2])
                } # 정보에 맞게 문자열을 딕셔너리 화 하여
                schedules[count - 1].append(scheduleInfo) # 주일 스케쥴 정보에 데이터를 추가
        showData(schedules[week]) # 가공된 모든 정보를 출력해주는 함수에 리스트를 전송
        return True # 정상적으로 실행되었다는 신호를 반환