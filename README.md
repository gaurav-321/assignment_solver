Write readme.md for this github repo in editor. 
File Path : README.MD
File Content : # Assignment Solver In Python

A assignment solving program by providing it text it turns into images that looks handwritten

---

## How to setup

Simply open up your terminal and type

```
pip3 install -r requirements.txt
```

## To Run the Assignment Solver

open input/document.txt and add your content.If you want the line to have black color add '#' in front of the line and if you want the content to be center and black add "##" in front insted
Then save and simply run the below command
```
python3 main.py
```

## What is the Assignment Solver?

It is an open source Assignment Solver used to write text from file into image in custom handwritting font. It can work work on any clear image that is similar to the one i am using. It uses simple algorithm to detect lines drawn on the image and uses the co-ordinates to write text.

##Output is like this

![First Image](output/0.png?raw=true "Title")
![Second Image](output/1.png?raw=true "Title")
![Third Image](output/2.png?raw=true "Title")


### This is a contributions for open source projects, if you are utilizing this project please give credit to my github Ordinary Pythoneer

[<img src="https://img.youtube.com/vi/fRjA7gJhdGw/maxresdefault.jpg" width="50%">](https://youtu.be/fRjA7gJhdGw)

------------------------------------------------------------File Path : input/document.txt
File Content : ##Chapter 1

#How are udsdsads?sd
I am definitely not finefsdfsdfgsdgfdgggggggggg fgfdegfrdeg


#What was this program made for?
To avoid writing assignment manually

#Can anyone use it?
Yup definitely

#Can anyone use it?
Yup definitelyThe quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog.The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog.The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog.The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog.The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog.


#Write quick brown fox 10 times?
The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog.The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog.The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog.The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog.The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog.

------------------------------------------------------------File Path : input/document_edited0.txt
File Content : ###Chapter 1

#How are udsdsads?sd
I am definitely not finefsdfsdfgsdgfdgggggggggg fgfdegfrdeg

------------------------------------------------------------File Path : input/document_edited1.txt
File Content : over the lazy dog. The quick brown fox jumps over the
lazy dog. The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.The quick brown
fox jumps over the lazy dog. The quick brown fox jumps
over the lazy dog. The quick brown fox jumps over the
lazy dog. The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.The quick brown
fox jumps over the lazy dog. The quick brown fox jumps
over the lazy dog. The quick brown fox jumps over the
lazy dog. The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.The quick brown
fox jumps over the lazy dog. The quick brown fox jumps
over the lazy dog. The quick brown fox jumps over the
lazy dog. The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog.

------------------------------------------------------------File Path : main.py
File Content : import os
import re
import shutil
import traceback
from glob import glob
from random import randint
import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

PAGE_IMG = "pages/notebook_1.jpg"
FONTS = glob("fonts\\test\\my_font\\*")


# Important Functions
def chunks(l, n):
    n = max(1, n)
    return [l[i:i + n] for i in range(0, len(l), n)]


def clean_line(input_line):
    return input_line.strip().replace("#", "").replace("  ", "")


# Image load class
class Page:
    def __init__(self):
        self.lines = []
        self.img_loc = PAGE_IMG
        self.page_img = []

    def find_lines(self):
        image = cv2.imread(self.img_loc)
        gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        for y, row in enumerate(gray_img[10:-10]):
            found = np.where(row < 150)[0]
            self.lines.append((found[0], y)) if len(found > 0) else 1
        self.page_img = image
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
        self.text_formatted = []

    def row_check(self, line):
        char_limit = ROW_WIDTH
        count_w = 0
        for i, char in enumerate(line):
            if char == " ":
                count_w += 1
                if i > char_limit:
                    return count_w
        return len(line.split(" "))

    def document_parse(self, total_lines):
        text_temp = []
        with open(self.file_loc) as infile:
            for index, line in enumerate(infile.readlines()):
                formatting = re.findall("^[#]*", line)  # format stored
                line = line.replace("#", "").replace("\n", "")
                line_split = line.split(" ")
                while True:
                    ROW_WIDTH = self.row_check(line)  # Number of words in row

                    if len(line_split) > ROW_WIDTH:
                        line_split = line_split[ROW_WIDTH:]
                        text_temp += [[formatting[0]] + line_split[:ROW_WIDTH]] if formatting[0] != "" else [
                            line_split[:ROW_WIDTH]]
                    else:
                        text_temp += [[formatting[0]] + line_split[:ROW_WIDTH]] if formatting[0] != "" else [
                            line_split[:ROW_WIDTH]]
                        break
        return chunks(text_temp[:-1], total_lines)

    def write_text(self, image, text, location, color, gap=0):
        font = ImageFont.truetype(FONTS[FONT_LOC], FONT_SIZE + randint(0, 2))
        img_pil = Image.fromarray(image)
        draw = ImageDraw.Draw(img_pil)
        x, y = location[0] + randint(-7, 7) + gap + SPAN_LENGTH, location[
            1] - ROW_HEIGHT
        draw.text((x, y), clean_line(text), font=font, fill=color)
        return np.array(img_pil)

    def write_from_list(self, page_obj, list_text):
        temp_img = page.page_img
        for index, line in enumerate(list_text):
            gap = 6 + randint(1, 3)
            if "##" in line:
                color = (93, 90, 90, 255)
                gap = page.page_img.shape[1] / 2 - len(line) * 30
            elif '#' in line:
                color = (93, 90, 90, 255)
            else:
                color = (131, 80, 66, 255)
            temp_img = self.write_text(temp_img, " ".join(line),
                                       page_obj.lines[index], color, gap=gap)
        return temp_img


def nothing(*args):
    pass


def init():
    shutil.rmtree("output")
    os.mkdir("output")
    cv2.namedWindow("Threshold", cv2.WINDOW_NORMAL)
    cv2.createTrackbar("SPAN_LENGTH", "Threshold", SPAN_LENGTH, 100, nothing)
    cv2.createTrackbar("ROW_HEIGHT", "Threshold", ROW_HEIGHT, 50, nothing)
    cv2.createTrackbar("ROW_WIDTH", "Threshold", ROW_WIDTH, 100, nothing)
    cv2.createTrackbar("FONT_SIZE", "Threshold", FONT_SIZE, 80, nothing)
    cv2.createTrackbar("ROW_SKIP", "Threshold", ROW_SKIP, 20, nothing)
    cv2.createTrackbar("FONT_LOC", "Threshold", FONT_LOC, len(FONTS) - 1, nothing)


def update_vals():
    global SPAN_LENGTH, ROW_HEIGHT, ROW_WIDTH, FONT_SIZE, ROW_SKIP, FONT_LOC
    SPAN_LENGTH, ROW_HEIGHT, ROW_WIDTH, FONT_SIZE, ROW_SKIP, FONT_LOC = (
        cv2.getTrackbarPos('SPAN_LENGTH', 'Threshold'),
        cv2.getTrackbarPos('ROW_HEIGHT', 'Threshold'),
        cv2.getTrackbarPos('ROW_WIDTH', 'Threshold'),
        cv2.getTrackbarPos('FONT_SIZE', 'Threshold'),
        cv2.getTrackbarPos('ROW_SKIP', 'Threshold'),
        cv2.getTrackbarPos('FONT_LOC', 'Threshold'))


if __name__ == '__main__':
    with open("last_config.conf") as file:
        SPAN_LENGTH, ROW_HEIGHT, ROW_WIDTH, FONT_SIZE, ROW_SKIP, FONT_LOC = [int(x) for x in
                                                                             file.read().split(",")]
    init()
    page = Page()
    page.find_lines()
    document = Document()
    text_formatted = document.document_parse(len(page.lines))
    for index, current_para in enumerate(text_formatted):
        try:
            while True:
                update_vals()
                text_formatted = document.document_parse(len(page.lines))
                final_img = document.write_from_list(page, text_formatted[index])
                cv2.imshow("ss", final_img)
                if cv2.waitKey(1000) & 0XFF == ord("q"):
                    break
            cv2.imwrite(f"output/{index}.png", final_img)
        except:
            print(traceback.print_exc())
    with open("last_config.conf", "w") as file:
        file.write(",".join([str(x) for x in [SPAN_LENGTH, ROW_HEIGHT, ROW_WIDTH, FONT_SIZE, ROW_SKIP, FONT_LOC]]))

------------------------------------------------------------File Path : requirements.txt
File Content : pillow
opencv-python
numpy
------------------------------------------------------------