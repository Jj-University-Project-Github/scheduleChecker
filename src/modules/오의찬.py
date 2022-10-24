"""
학번 : 202068068
이름 : 오의찬
기여 : 교수님의 정보가 담겨있는 파일을 불러와 가공하는 함수와 헌혈 정보를 업데이트, 불러오는 기능, 프로그램이 실행되었을 때 콘솔창을 청소하는 기능을 제작하였습니다.
"""

from datetime import date


def getProfessorInfos(subject): #교수 정보를 불러오는 함수

    file = open("./professorInfos.dat", 'r', encoding="utf-8")
    tempProfessor = file.readlines()
    """
    파일을 읽어 모든 줄의 내용을 리스트에 저장
    """

    professors = []  # 교수정보가 저장될 리스트

    for i in tempProfessor: # 위 교수정보가 저장된 리스트를 가공하는 반복문, 위 공백 리스트에 가공된 정보를 추가
        professorInfos = i.strip().split(',')  # i번째 줄의 정보에서 양 끝의 공백란을 제거하고 ','를 기준으로 문자를 나눠 리스트화
        professorInfo = {
            "name": professorInfos[0],
            "lab": professorInfos[1],
            "labNumber": professorInfos[2],
            "phoneNumber": professorInfos[3],
            "email": professorInfos[4],
            "subject": professorInfos[5]
        }
        professors.append(professorInfo)    # professors리스트 가장 마지막에 professorInfo 추가

    professorInfo = []  #교수 정보중 하나를 배열로 저장
    for i in professors:
        if i["subject"] == subject: # schedulenlnfos의 과목 정보를 받아와 professorlnfos의 과목을 비교
            professorInfo.append(i) # professorInfo리스트 가장 마지막에 i 추가
    if len(professorInfo) == 0:  # 만약 교수님의 정보가 하나도 확인되지 않는다면
        return None  # 없다고 반환
    else:  # 아닐경우
        return professorInfo  # 교수님의 정보를 반환


def getLastBloodDonateDay(query=None):
    """
    마지막으로 헌혈한 날을 반환하는 함수로
    헌혈 정보가 담긴 파일에서 헌혈 데이터를 불러와 출력함
    """
    file = open("./bloodDonateDay.dat", "r", encoding="utf-8")
    year, month, day = file.read().split(",") #파일의 날짜 데이터를 나눔
    return "%s년 %s월 %s일에 헌혈하셨습니다." % (year, month, day)


def updateLastBloodDonateDay(query=None):
    """
    마지막으로 헌혈한 날을 헌혈 정보 파일에 저장하는 함수로
    datetime 라이브러리의 date 모듈을 활용함
    """
    file = open("./bloodDonateDay.dat", "w", encoding="utf-8")
    today = date.today() #오늘 날짜를 받아옴
    file.write("%s,%s,%s" % (today.year, today.month, today.day)) #받아온 날짜 데이터를 연, 월, 일 순으로 저장
    return "업데이트 되었습니다."


def consoleClear():
    """
    콘솔을 클리어하는 함수
    """
    print("\n" * 30)
    return