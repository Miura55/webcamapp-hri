#! /usr/local/bin
# coding: utf-8
# 参考：https://qiita.com/sti320a/items/3cdafb737d2c16fbaa51
from flask import Flask, render_template, Response
from camera import Camera

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('view.html')

@app.route('/feed')
def feed():
    frame=Camera().get_frame()
    return Response(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n', mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
