from modules.박선영 import getAddressInfo
from modules.오의찬 import getProfessorInfos
from modules.김진호 import menu, showData


def getScheduleInfo(week: int):
    file = open("./scheduleInfos.dat", 'r', encoding="utf-8")
    tempSchedule = file.readlines()

    schedules = []
    count = 1

    if week == "Ask":
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
        while menu(menus):
            pass
    elif week > 4:
        print("오늘은 일정이 없습니다.")
        return True
    else:
        for i in tempSchedule:
            i = i.strip()
            if len(schedules) != count:
                schedules.append([])
            if not i or i == "\n":
                count += 1
            else:
                scheduleInfos = i.split(",")
                scheduleInfo = {
                    "name": scheduleInfos[0],
                    "time": scheduleInfos[1],
                    "at": scheduleInfos[2],
                    "number": scheduleInfos[3],
                    "professorInfo": getProfessorInfos(scheduleInfos[0]),
                    "address": getAddressInfo(scheduleInfos[2])
                }
                schedules[count - 1].append(scheduleInfo)
        showData(schedules[week])
        return True
