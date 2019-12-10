from time import time

class Camera(object):
    def __init__(self):
        self.frames = []
        self.files = ['0', '1', '2', '3', '4']

        for f in self.files:
            self.frames.append(open('./static/img/img' + f + '.jpeg', 'rb').read())

    def get_frame(self):
        return self.frames[int(time()) % len(self.files)]

if __name__=='__main__':
    cam = Camera()
    cam.get_frame()

