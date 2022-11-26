import cv2
from datetime import datetime


def create_text(img, out_path):

    final_str = ""
    # Iterate over each pixel and set color for the corresponding cell.
    for row in img:
        for pixel in row:
            if pixel < 64:
                final_str += "#"
            elif pixel < 128:
                final_str += "*"
            else:
                final_str += " "

        final_str += "\n"
    with open(out_path, "w") as f:
        f.write(final_str)


def img_to_text(img, out_path=None, scale_percent=None, width=150, height=150):
    if scale_percent:
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)

    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

    if not out_path:
        out_path = f"output/text/out_{str(datetime.today()).replace(':', '-')}.txt"

    create_text(gray, out_path)
    return out_path
