import random
import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image
import time

page = cv2.imread(f"pages/page_1.jpg")
page_gray = cv2.cvtColor(page, cv2.COLOR_BGR2GRAY)
ROW_HEIGHT = 34
INPUT_FILE = "input/document.txt"


def find_lines(image):
    starting_point = []
    end_point = []
    for y, row in enumerate(image):
        for x, pixel in enumerate(row[5:200]):
            if pixel < 50:
                starting_point.append((x, y))
                cv2.circle(page, (x, y), 3, (255, 0, 0), -1)
                break
            else:
                continue
        for x, pixel in enumerate(row[::-1][5:200]):
            x = len(row) - x
            if pixel < 50:
                end_point.append((x, y))
                cv2.circle(page, (x, y), 3, (255, 0, 0), -1)
                break
            else:
                continue
    return starting_point, end_point


def clean_line(input_line):
    return input_line.strip().replace("#", "")


def fix_inputfile_length():
    text = []
    with open("input/document.txt") as file:
        text.extend(file.readlines())
        finding = True
        while finding:
            for index, line in enumerate(text):
                if len(clean_line(line)) > 70:
                    text[index] = line[:70]+"\n"
                    if "#" in line:
                        text.insert(index + 1, "#-" + line[72:])
                    else:
                        text.insert(index + 1, "-"+ line[72:])
                    break
                elif index + 1 >= len(text):
                    finding = False
    with open("input/document_edited.txt", "w") as out:
        for line in text:
            out.write(line)


def input_file_parser():
    f = time.time()
    start_point, end_point = find_lines(page_gray)
    for arr in [start_point, end_point]:
        for x, y in arr:
            for temp in range(y - 10, y + 10):
                if (x, temp) in start_point and temp != y:
                    start_point.remove((x, y))
                    break
    print(start_point)
    print(time.time() - f)
    with open("input/document_edited.txt", "r") as file:
        text = file.readlines()
        for index, line in enumerate(text):
            SPAN_LENGTH = 10 + random.randint(1, 10)
            if "##" in line:
                color = (58, 56, 67, 255)
                SPAN_LENGTH = int(page.shape[1] / 2) - len(clean_line(line)) * 8

            elif '#' in line:
                color = (93, 90, 90, 255)
            else:
                color = (131, 80, 66, 255)
            write_text(clean_line(line).replace(" ", "  "), start_point[index], color, SPAN_LENGTH=SPAN_LENGTH)


def write_text(text, location, color, size=37, SPAN_LENGTH=10 + random.randint(1, 10)):
    global page
    fontpath = "fonts/Kristi.ttf"
    font = ImageFont.truetype(fontpath, size + random.randint(0, 4))
    img_pil = Image.fromarray(page)
    draw = ImageDraw.Draw(img_pil)
    x, y = location[0] + SPAN_LENGTH, location[1] - ROW_HEIGHT
    draw.text((x, y), text, font=font, fill=color)
    page = np.array(img_pil)


def fix_list(list_temp):
    mean_list = [j - i for i, j in zip(list_temp[:-1], list_temp[1:])]
    return sum(mean_list) / len(mean_list)


if __name__ == "__main__":
    find_lines(page_gray)
    fix_inputfile_length()
    input_file_parser()
    cv2.imshow("f", cv2.resize(page, (0, 0), fx=0.7, fy=0.7))
    cv2.waitKey(0)
