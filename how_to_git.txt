sourcetree; git gui

vs code; 
폴더를 vs code로 엶
-> 터미널이 그 폴더 경로로 이미 지정돼 있음
git init #폴더가 git의 관리 하에 들어가게 됨
git config --global user.name "내이름"
git config --global user.email "내메일주소"

>>>git ignore
https://velog.io/@conatuseus/.gitignore-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0-imk4708751
.gitignore: 깃에서 특정 파일 혹은 디렉토릴르 관리 대상에서 제외할 때 사용하는 파일
메모장으로 관리하지 않을 파일명을 써넣고 ".gitignore" 이름으로 저장
// 현재 Repository의 cache를 모두 삭제
git rm -r --cached .
// .gitignore에 넣은 파일 목록들을 제외하고 다른 모든 파일을 다시 track하도록 설정
git add .
// commit
git commit -m "fixed untracked files"
