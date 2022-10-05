from datetime import date
from modules.성민우 import getScheduleInfo
from modules.김진호 import menu
from modules.박선영 import consoleClear

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
    }
]

"""
> 필요한 데이터

1. 요청을 받을 시 교수님의 정보를 불러올 모듈       난이도 : 3 
2. 요청을 받을 시 강의실의 위치를 알려줄 모듈       난이도 : 3
3. 요청을 받을 시 오늘의 스케쥴을 반환할 모듈       난이도 : 6
4. 원하는 기능을 물어보고 프로그램을 종료할지 여부에 대해 물어볼 기능 난이도 : 5
5. 윤년 계산기                               난이도 : 3
6. 헌혈 가능 날짜 계산기                       난이도 : 5
7. 콘솔 청소기능                             난이도 : 1
8. 파일 내용 저장 기능                        난이도 : 3
"""

"""
> 파일 데이터 

professorInfos 내용
교수님 성함,대학관,호실,내선번호,메일주소

scheduleInfos 내용
강의,강의시간,대학관,호실

adressInfos 내용
대학관이름,네이버주소를 통한 위성좌표 알리미
"""

consoleClear()
while True:
    result = menu(menus)
    if result == False:
        break
    else:
        print(result)
    pass
