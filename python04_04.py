"""
Chapter4 Advanced(4) - 나만의 패키지 만들기(3) -PyPi 배포
Keyword - PyPi, build, package deploy

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
패키지 배포 순서(PyPi)

1. https://pypi.org 접속

2. 프로젝트 구조 확인

3.__init__.py

4. 프로젝트 Root에 필수 파일 작성
    - README.md
    - setup.py
    - setup.cfg(optional)
    - LICENSE
    - MANIFEST.in

5. pip install setuptools wheel 설치 후 빌드 업 -> 설치판 생성
    - 설치 1 : python -m pip install --upgrade setuptools wheel (가상환경 사용)
    - 설치 2 : python -m pip install --user --upgrade setuptools wheel
    - 빌드 방법 : python setup.py sdist bdist_wheel

6. PyPi 배포
    - 설치 : pip install twine
    - 업로드 : python -m twine upload dist/*

7. 설치 확인 : pip install pygifconvt_test
    from pygifconvt_test.converter import GifConverter 

"""