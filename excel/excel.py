import cv2
import xlsxwriter
from datetime import datetime


def create_excel(img, out_path):
    workbook = xlsxwriter.Workbook(out_path)
    worksheet = workbook.add_worksheet()

    # Iterate over each pixel and set color for the corresponding cell.
    r = 0
    c = 0
    for row in img:
        worksheet.set_row(r, 10)
        c = 0
        for pixel in row:
            hex_color = '#%02x%02x%02x' % tuple(pixel)
            hex_color = hex_color.upper()
            _format = workbook.add_format()
            _format.set_bg_color(hex_color)
            worksheet.write(r, c, '', _format)
            c += 1
        r += 1

    worksheet.set_column(0, c, 1)

    workbook.close()


def img_to_excel(img, out_path=None, scale_percent=None, width=150, height=150, gray=False):
    if scale_percent:
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)

    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

    if gray:
        gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
        final_img = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
    else:
        # OpenCV uses BGR as its default colour order for images
        # So, we need to convert it back to RGB
        final_img = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)

    if not out_path:
        out_path = f"output/excel/out_{str(datetime.today()).replace(':', '-')}.xlsx"

    create_excel(final_img, out_path)
    return out_path
