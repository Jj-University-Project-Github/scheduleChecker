# scheduleChecker
schedule management program for software project


구조
========
> ### app.py  
메인 파일로 전체적인 코드의 진행을 담당.

> ### modules.성민우.py
메뉴에서 요청을 받은 스케쥴을 반환하는 모듈  
마무리 코드 병합  

> ### modules.오의찬.py
요청을 받을 시 교수님의 정보를 불러오는 모듈  
파일 내용 저장 기능  
콘솔 청소기능 

> ### modules.박선영.py
헌혈 가능 날짜 계산기 
요청을 받고 강의실의 위치를 알려줄 모듈     
윤년 계산기  

> ### modules.김진호.py
메뉴 UI 출력
스케줄 데이터 출력
원하는 기능을 물어보고 프로그램을 종료할지 여부에 대해 물어볼 기능


> ### professorInfos.dat
교수님 성함,대학관,호실,내선번호,메일주소, 과목

> ### scheduleInfos.dat
강의,강의시간,대학관,호실

> ### adressInfos.dat
대학관이름,네이버주소를 통한 위성좌표 알리미

> ### bloodDonateDay.dat  
마지막으로 헌혈한 날을 저장하는 공간
