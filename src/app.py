from datetime import date
from modules.성민우 import getScheduleInfo
from modules.김진호 import menu
from modules.박선영 import getCanBloodDonateDay
from modules.오의찬 import getLastBloodDonateDay, updateLastBloodDonateDay, consoleClear

menus = [
    {
        "title": "오늘의 시간표 보기",
        "run": getScheduleInfo,
        "query": date.today().weekday()
    },
    {
        "title": "월별 시간표 보기",
        "run": getScheduleInfo,
        "query": "Ask"
    },
    {
        "title": "헌혈 가능일자 확인",
        "run": getCanBloodDonateDay,
        "query": None
    },
    {
        "title": "마지막 헌혈정보 확인",
        "run": getLastBloodDonateDay,
        "query": None
    },
    {
        "title": "마지막 헌혈정보 업데이트",
        "run": updateLastBloodDonateDay,
        "query": None
    }
]

consoleClear()
while True:
    result = menu(menus)
    if result == False:
        break
    else:
        print(result)
    pass
