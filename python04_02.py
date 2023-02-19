"""
Chapter4 Advanced(4) - 나만의 패키지 만들기(1)
Keyword - png(jpg) to gif, pill, image

"""
"""
패키지를 작성
-> 정적이미지(JPG, PNG) -> 동적이미지(GIF) 이미지 변환 패키지

"""

import glob
from PIL import Image

# 이미지, 결과 생성 경로
path_in = './project/images/*.png'
path_out = './project/image_out/result.gif'

# 첫 번째 이미지 & 모든 이미지 리스트 팩킹
# img, *images = [Image.open(f) for f in sorted(glob.glob(path_in))]

# 리사이즈(필요한 경우)
img, *images = [Image.open(f).resize((320, 240), Image.ANTIALIAS) for f in sorted(glob.glob(path_in))]

# 이미지 저장
img.save(
    fp = path_out,
    format = 'GIF',
    append_images = images,
    save_all = True,
    duration = 500,
    loop = 0
)