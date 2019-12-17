from time import time
import glob

class Camera(object):
    def __init__(self):
        self.frames = []
        self.files = glob.glob("./static/img/*.jpg")
        if len(self.files) == 0:
            self.files = ['0', '1', '2', '3', '4']
            for f in self.files:
                self.frames.append(open('./static/img/dammy/img' + f + '.jpeg', 'rb').read())
        else:
            for f in self.files:
                self.frames.append(open(f, "rb").read())

    def get_frame(self):
        return self.frames[int(time()) % len(self.files)]

if __name__=='__main__':
    cam = Camera()
    cam.get_frame()

