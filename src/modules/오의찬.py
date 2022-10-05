def getProfessorInfos(subject):
    file = open("./professorInfos.dat", 'r', encoding="utf-8")
    tempProfessor = file.readlines()

    professors = []

    for i in tempProfessor:
        professorInfos = i.strip().split(",")
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
    if len(professorInfo) == 0:
        return None
    else:
        return professorInfo


def getLastBloodDonateDay(query=None):
    file = open("../bloodDonateDay.dat", "r", encoding="utf-8")
    year, month, day = file.read().split(",")
    return "%s년 %s월 %s일에 헌혈하셨습니다." % (year, month, day)
