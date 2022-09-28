# scheduleChecker
schedule management program for software project


구조
========
> ### app.py  
메인 파일로 전체적인 코드의 진행을 담당.

> ### modules.성민우.py
요청을 받을 시 오늘의 스케쥴을 반환할 모듈  
```py
def getScheduleInfo(week: int) -> List[ScheduleInfo]:
    return List[ScheduleInfo]

    """
    ScheduleInfo 정보
    scheduleInfo = {
        "name": scheduleInfos[0],  # 수업 이름
        "time": scheduleInfos[1],  # 수업 시간
        "at": scheduleInfos[2],  # 대학관
        "number": scheduleInfos[3]  # 대학관 호실
    }

    함수에서 요청하는 정보
    week : 오늘의 요일을 int화 하여 불러오기
    요일정보 : [월, 화, 수, 목, 금, 토, 일]
    """
``` 

> ### modules.오의찬.py
요청을 받을 시 교수님의 정보를 불러올 모듈

> ### modules.박선영.py
요청을 받을 시 강의실의 위치를 알려줄 모듈     

> ### modules.김진호.py
원하는 기능을 물어보고 프로그램을 종료할지 여부에 대해 

> ### professorInfos.dat
교수님 성함,대학관,호실,내선번호,메일주소

> ### scheduleInfos.dat
강의,강의시간,대학관,호실

> ### adressInfos.dat
대학관이름,네이버주소를 통한 위성좌표 알리미