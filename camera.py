from time import time
import os, re
import glob

class Camera(object):
    def __init__(self):
        self.frames = []
        # self.files = glob.glob("./static/img/*.jpg")
        self.files = sorted(glob.glob('./static/img/*.jpg'), key=numericalSort)
        if len(self.files) == 0:
            self.files = ['0', '1', '2', '3', '4']
            for f in self.files:
                self.frames.append(open('./static/img/dammy/img' + f + '.jpeg', 'rb').read())
        else:
            for f in self.files:
                self.frames.append(open(f, "rb").read())
    def get_frame(self):
        # return self.frames[int(time()) % len(self.files)]
        return self.frames[-1]

def numericalSort(value):
    numbers = re.compile(r'(\d+)')
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

if __name__=='__main__':
    cam = Camera()
    cam.get_frame()

