"""
학번 : 202068068
이름 : 오의찬
기여 : 교수님의 정보가 담겨있는 파일을 불러와 가공하는 함수와 헌혈 정보를 업데이트, 불러오는 기능, 프로그램이 실행되었을 때 콘솔창을 청소하는 기능을 제작하였습니다.
"""

from datetime import date


def getProfessorInfos(subject):
    """
    교수님의 정보를 불러오는 함수입니다.
    """

    file = open("./professorInfos.dat", 'r', encoding="utf-8")
    tempProfessor = file.readlines()
    """
    파일을 읽어 모든 줄의 내용을 리스트로 담습니다.
    """

    professors = [] # 교수님의 정보가 담길 리스트입니다.

    for i in tempProfessor:
        """
        위에서 교수님의 정보가 불려온 리스트를 가공하는 반복문입니다.
        이 반복문은 위 공백 리스트에 가공된 정보를 추가합니다.
        """
        professorInfos = i.strip().split(',') # i번째 줄의 정보에서 양 끝의 공백란을 제거하고 ','를 기준으로 문자를 쪼개어 리스트화 합니다.
        professorInfo = {
            "name": professorInfos[0],
            "lab": professorInfos[1],
            "labNumber": professorInfos[2],
            "phoneNumber": professorInfos[3],
            "email": professorInfos[4],
            "subject": professorInfos[5]
        }
        professors.append(professorInfo)
    professorInfo = [i for i in professors if i["subject"] == subject]
    if len(professorInfo) == 0: # 만약 교수님의 정보가 하나도 확인되지 않는다면
        return None # 없다고 반환
    else: # 아닐경우
        return professorInfo # 교수님의 정보를 반환


def getLastBloodDonateDay(query=None):
    """
    마지막으로 헌혈한 날을 반환하는 함수로
    헌혈 정보가 담긴 파일에서 헌혈 데이터를 불러와 출력합니다.
    """
    file = open("./bloodDonateDay.dat", "r", encoding="utf-8")
    year, month, day = file.read().split(",")
    return "%s년 %s월 %s일에 헌혈하셨습니다." % (year, month, day)

def updateLastBloodDonateDay(query=None):
    """
    마지막으로 헌혈한 날을 헌혈 정보 파일에 저장하는 함수로
    datetime 라이브러리의 date 모듈을 활용하였습니다.
    """
    file = open("./bloodDonateDay.dat", "w", encoding="utf-8")
    today = date.today()
    file.write("%s,%s,%s" % (today.year, today.month, today.day))
    return "업데이트 되었습니다."

def consoleClear():
    """
    콘솔을 청소하는 함수입니다.
    """
    print("\n" * 30)
    return