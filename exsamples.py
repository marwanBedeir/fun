import cv2
from excel import excel
from text import text


def img_to_excel():
    img_path = "examples/img_to_excel/in.jpeg"
    out_path = "examples/img_to_excel/out.xlsx"
    img = cv2.imread(img_path)
    excel.img_to_excel(img, out_path)


def img_to_text():
    img_path = "examples/img_to_text/in.jpeg"
    out_path = "examples/img_to_text/out.txt"
    img = cv2.imread(img_path)
    text.img_to_text(img, out_path)

# img_to_excel()
# img_to_text()
