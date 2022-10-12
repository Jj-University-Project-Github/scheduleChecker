from datetime import date
from modules.성민우 import getScheduleInfo
from modules.김진호 import menu
from modules.박선영 import getCanBloodDonateDay
from modules.오의찬 import getLastBloodDonateDay, updateLastBloodDonateDay, consoleClear

# 메인 메뉴
menus = [
    {
        "title": "오늘의 시간표 보기",
        "run": getScheduleInfo,
        "query": date.today().weekday()
    },
    {
        "title": "요일별 시간표 보기",
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

consoleClear() # 프로그램 실행시 첫 메뉴를 보이기 위해 모든 채팅을 밀어내는 기능

while True:
    result = menu(menus) # 메뉴 입력 결과값을 받아오는 변수 
    if result == False: # 만약 입력이 끝났다는 신호가 오면
        break # 반복을 중지
    else: # 아닐 경우
        print(result) # 메뉴 사용에 대한 결과값을 출력
    pass
