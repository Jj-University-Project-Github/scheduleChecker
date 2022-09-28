"""
> 이름 
성민우

> 학번 
202268018

> 주제
요청을 받을 시 오늘의 스케쥴을 반환할 모듈
"""


from typing import List


class ScheduleInfo:
    name = str
    time = str
    at = str
    number = str


def getScheduleInfo(week: int) -> List[ScheduleInfo]:
    """
    반환 값
    > 만약 수업이 있을 경우
    {
        "name": str,  # 수업 이름
        "time": str,  # 수업 시간
        "at": str,  # 대학관
        "number": str  # 대학관 호실
    }[]
    """
    # 필요한 파일 호출
    # scheduleInfos.dat를 utf-8 방식으로 읽어와 scheduleDB에 저장
    scheduleDB = open("../scheduleInfos.dat", "r", encoding="utf-8")
    """
    scheduleInfos 내용
    강의,강의시간,대학관,호실
    """
    # 파일 가공
    tempSchedule = scheduleDB.readlines()  # 읽어온 파일의 모든 줄을 각각 잘라 리스트로 임시저장

    schedules = []  # 스케쥴을 올바르게 가공하여 저장하기 위해 생성
    count = 1  # 매 요일의 스케쥴을 위해 따로 제작
    for i in tempSchedule:  # 매 줄을 하나씩 i에 대입하여 아래의 코드를 실행
        i = i.strip()  # i의 좌측과 우측의 공백을 제거
        if len(schedules) != count:  # 만약 스케쥴을 저장할 공간에 리스트가 모자랄 경우
            schedules.append([])  # 빈 리스트는 스케쥴 저장 공간에 추가
        if not i or i == "\n":  # 만약 i가 공백일 경우
            count += 1  # count에 1을 추가
        else:  # 만약 i가 공백이 아닐 경우
            scheduleInfos = i.split(",")  # ,를 기준으로 문자열을 잘라 리스트로 저장
            scheduleInfo = {  # 스케쥴 정보가 저장될 공간, type : dict
                "name": scheduleInfos[0],  # 수업 이름
                "time": scheduleInfos[1],  # 수업 시간
                "at": scheduleInfos[2],  # 대학관
                "number": scheduleInfos[3]  # 대학관 호실
            }
            schedules[count - 1].append(scheduleInfo)  # 가공된 수업 정보를 올바른 위치에 추가
    if week > 4:  # 만약 주말이 아닐 경우
        return None  # None을 반환
    else:  # 만약 평일일 경우
        return schedules[week]


if __name__ == "__main__":
    from datetime import date
    today = date.today()
    week = today.weekday()

    schedule = getScheduleInfo(week)
    print(schedule)
