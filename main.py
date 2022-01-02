import os
import random
import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image, ImageChops, ImageMath
import time, timeit

PAGE_IMG = "pages/notebook_1.jpg"
FONT_DIR = "fonts/test/my_font/"
fonts = os.listdir(FONT_DIR)
# For notebook_1
SPAN_LENGTH = 2
ROW_HEIGHT = 5
ROW_WIDTH = 54
FONT_SIZE = 25
ROW_SKIP = 3
"""
# For page_3
SPAN_LENGTH = 2
ROW_HEIGHT = 5
ROW_WIDTH = 60
FONT_SIZE = 20
ROW_SKIP = 0

"""
"""
# For page_1
SPAN_LENGTH = 2
ROW_HEIGHT = 15
ROW_WIDTH = 49
FONT_SIZE = 40
ROW_SKIP = 0
"""


def clean_line(input_line):
    return input_line.strip().replace("#", "")


class Page:
    def __init__(self):
        self.lines = []
        self.img_loc = PAGE_IMG
        self.page_img = []

    def load_page(self):
        image = cv2.imread(self.img_loc)
        gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        for y, row in enumerate(gray_img[10:-10]):
            found = np.where(row < 150)[0]
            self.lines.append((found[0], y)) if len(found > 0) else 1

        self.page_img = np.array(image)

    def show_img(self):
        cv2.imshow("img", self.page_img)
        cv2.waitKey(0)

    def find_lines(self):
        for index, row in enumerate(self.page_img):
            if 0 in row:
                self.lines.append((index, np.where(row == 0)[0][0]))
        del_ele = []
        for y2, y1 in zip(self.lines[1:], self.lines[:-1]):
            if y2[1] in range(y1[0] - 10, y1[1] + 10):
                del_ele.append(y2)
        for x in del_ele:
            self.lines.remove(x)
        self.lines = self.lines[ROW_SKIP:]


class Document:
    def __init__(self):
        self.file_loc = "input/document.txt"
        self.temp_loc = "input/document_edited.txt"

    def document_parse(self, page_obj):
        text = []
        total_lines = len(page_obj.lines)
        with open(self.file_loc) as file:
            text.extend(file.readlines())
            finding = True
            while finding:
                for index, line in enumerate(text):
                    if len(clean_line(line)) > ROW_WIDTH:
                        text[index] = line[:ROW_WIDTH] + "\n"
                        if line[ROW_WIDTH+1] != "" or line[ROW_WIDTH+2] != "":#dd
                            if "#" in line:
                                text.insert(index + 1, "#-" + line[ROW_WIDTH:])
                            else:
                                text.insert(index + 1, "-" + line[ROW_WIDTH:])
                        else:
                            if "#" in line:
                                text.insert(index + 1, "#" + line[ROW_WIDTH:])
                            else:
                                text.insert(index + 1, "" + line[ROW_WIDTH:])
                        break
                    elif index + 1 >= len(text):
                        finding = False
        with open(self.temp_loc, "w") as out:
            for line in text[:total_lines]:
                out.write(line)

    def write_text(self, image, text, location, color, size=FONT_SIZE, gap=0):
        global SPAN_LENGTH, ROW_HEIGHT
        font_path = FONT_DIR+random.choice(fonts)
        font = ImageFont.truetype(font_path, size + random.randint(0, 2))
        img_pil = Image.fromarray(image)
        draw = ImageDraw.Draw(img_pil)
        x, y = location[0] + SPAN_LENGTH + random.randint(-2, 7) + gap, location[1] - ROW_HEIGHT
        draw.text((x, y), text, font=font, fill=color)
        return np.array(img_pil)

    def write_from_document(self, page_obj):
        self.document_parse(page_obj)
        with open(self.temp_loc, "r") as file:
            text = file.readlines()
            for index, line in enumerate(text):
                gap = 10 + random.randint(1, 10)
                if "##" in line:
                    color = (58, 56, 67, 255)
                    gap = int(page_obj.page_img.shape[1] / 2) - (len(clean_line(line)) / 2) * 14

                elif '#' in line:
                    color = (93, 90, 90, 255)
                else:
                    color = (131, 80, 66, 255)
                page.page_img = self.write_text(page.page_img, clean_line(line).replace(" ", "  "),
                                                page_obj.lines[index], color, gap=gap)


if __name__ == '__main__':
    page = Page()
    page.load_page()
    page.find_lines()
    document = Document()
    document.write_from_document(page)
    print(page.lines)
    page.show_img()
