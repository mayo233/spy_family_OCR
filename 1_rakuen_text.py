#システムの利用を宣言する
import sys
import os

#PyOCRを読み込む    
from PIL import Image
import pyocr

#OpenCVの利用を宣言する(画像に四角を書き込む際に使用)
import cv2

#Tesseractのインストール場所をOSに教える
tesseract_path = "C:\Program Files\Tesseract-OCR" 
if tesseract_path not in os.environ["PATH"].split(os.pathsep):
    os.environ["PATH"] += os.pathsep + tesseract_path

#OCRエンジンを取得する
tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("OCRエンジンが指定されていません")
    sys.exit(1)
else:
    tool = tools[0]

#画像の読み込み
file_path = "C:/Users/homur/Downloads/mission.jpg"
img = Image.open(file_path)
img2 = cv2.imread(file_path)

box_builder = pyocr.builders.WordBoxBuilder(tesseract_layout=6)
text_position = tool.image_to_string(img, lang="jpn", builder=box_builder)

# 取得した座標と文字を出力し、画像に枠を書き込む
order_dict = {"O": None, "R": None, "D": None, "ES": None, "R": None}  # ORDER の順番
for res in text_position:
    if res.content in order_dict:
        print(res.content)
