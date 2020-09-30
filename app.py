from flask import Flask, render_template, Response, url_for, request, jsonify
from camera import vcam
import cv2
import tkinter

app = Flask(__name__)

#main routes
@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', title = "Home")

@app.route('/tool')
def tool():
	return render_template('project.html', title = "Interactive Tool")
'''
def gen(camera):
	while True:
		level = 0
		frame = camera.get_frame(level)
		yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')'''

@app.route('/video')
def video():
	return Response(gen(vcam()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/exp')
def exp():
	return render_template('exp.html', title = "Explanation")

#tool routes

@app.route('/project/browse_loaded')
def browse_loaded():
	return render_template('browse_loaded.html', title = "Pre-Loaded")

@app.route('/project/upload_play')
def upload_play():
	return render_template('upload_play.html', title= "Upload and Play")


@app.route('/project/live_camera', methods=["POST", "GET"])

def live_camera():
	return render_template('live_camera.html', title = "Live Camera")

def gen(camera):

	while True:
		file = open("level.txt", "r")
		level = file.read()
		level = int(level)
		file.close()
		frame = camera.get_frame(level)

		yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/exp/physics_exp')
def physics_exp():
	return render_template('physics_exp.html', title = "Physics")

@app.route('/exp/math_exp')
def math_exp():
	return render_template('math_exp.html', title = "Math")

@app.route('/instructions')
def instructions():
	return render_template('instructions.html', title = "Instructions")



#image pages


if __name__ == '__main__':
	app.run(debug = True)