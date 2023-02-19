"""
Chapter4 Advanced(4) - 나만의 패키지 만들기(4) -Github 배포
Keyword - Github

"""
"""

"""

# python04_03 : 완성된 패키지 임포트
from python04_03 import GifConverter as gfc

# 클래스 생성
c = gfc("./project/images/*.png", './project/image_out/result.gif', (320,240))

# 실행
c.convert_gif()

"""
패키지 배포 순서(github)
1. https://github.com 회원 가입

2. git 설치 확인(생략) - -> /gitignore 파일 고려

3. gut add -> commit -> pusg
    - git repository 저장소 생성
    - git init
    - git add .
    - git status
    - git commit -m 'message'
    - git remote add origin 'your reposutory'
    - git pusgh origin master

4. PyPi 형태의 패키지 구조를 github repository에 Push

5. 설치 확인(pip install git + https://yout-repository-url)

"""