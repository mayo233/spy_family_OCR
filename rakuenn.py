# # 
# import pyocr 
# from PIL import Image
# import sys
# import pytesseract
# from PIL import Image

# # 画像を読み込む
# img = Image.open("C:/Users/homur/Downloads/mission.jpg")

# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'




# # 画像からテキストを探して取り出す、langは英語、日本語などのパラメータ設定できる
# text = pytesseract.image_to_string(img, lang='jpn')



# #文字を読み取る

# print(text)

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

print(text_position)



# 取得した座標と文字を出力し、画像に枠を書き込む
order_dict = {"O": None, "R": None, "D": None, "ES": None, "R": None}  # ORDER の順番
for res in text_position:
    print(res.content)
    if res.content in order_dict:
        print(res.position)
        order_dict[res.content] = res.position
        cv2.rectangle(img2, res.position[0], res.position[1], (0, 0, 255), 2)

# ORDERの順番で線を引く
order_keys = ["O", "R", "D", "ES", "R"]
prev_pos = None
for key in order_keys:
    if key in order_dict and order_dict[key] is not None:
        center_pos = ((order_dict[key][0][0] + order_dict[key][1][0]) // 2, 
                      (order_dict[key][0][1] + order_dict[key][1][1]) // 2)
        if prev_pos is not None:
            cv2.line(img2, prev_pos, center_pos, (255, 0, 0), 2)
        prev_pos = center_pos

# #文字と座標を読み取る
# box_builder = pyocr.builders.WordBoxBuilder(tesseract_layout=6)
# text_position = tool.image_to_string(img,lang="jpn",builder=box_builder)

# #取得した座標と文字を出力するし、画像に枠を書き込む
# for res in text_position:
#     print(res.content)

#     if res.content == "O":
#         print(res.position)
#         cv2.rectangle(img2,res.position[0],res.position[1],(0,0,255),2)

    
#     if res.content == "R":
#         print(res.position)
#         cv2.rectangle(img2,res.position[0],res.position[1],(0,0,255),2)

#     if res.content == "ES":
#         print(res.position)
#         cv2.rectangle(img2,res.position[0],res.position[1],(0,0,255),2)

#     if res.content == "D":
#         print(res.position)
#         cv2.rectangle(img2,res.position[0],res.position[1],(0,0,255),2)



    
#四角を書き込んだ画像を表示する
cv2.imshow("image",img2)
cv2.imwrite("C:/Users/homur/Downloads/family.jpg",img2)
cv2.waitKey(0)

