# how to use git in windows
윈도우 - cmd 창에서

1. 처음 설정할 때
```
git config --global user.name "leejin21c"
git config --global user.email "leejin21c@gmail.com"
git config --list
git init
git status
git add -A
git status
git commit -m "write something down"
git remote add stock https://github.com/leejin21/algProbSolve-PY.git
# stock 대신 다른 거 써도 됨 (origin) + 주소도 레포지터리 주소 달라지면 주소 다르게 써 주기
git push stock master
# 위에 있는 것 다르게 썼으면 여기도 고려해서 다르게 써주기
```

2. 나중에 그냥 업데이트 해 주기
```
cd c:\\dev\pyproject\algCour
git status
git add -A
git status
git commit -m "여기 뭐라도 쓰기"
git push stock master
```

3. .gitignore에 추가해 주는 방법
```
# 아직 안 해봄

```

4. git remote add 어쩌고 부분 안 되면 아래 링크 보기
https://yunseul-light.blogspot.com/2017/08/github-windows-git.html
