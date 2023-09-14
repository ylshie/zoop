import os
from app import app
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from roop.core import task
import multiprocessing
from multiprocessing import Process, Queue
from flask_cors import CORS
from flask import jsonify
import roop.globals
import uuid

cors1 = CORS(app, resources={r"/*": {"origins": "*"}})
print("------- set cors --------")
#multiprocessing.set_start_method('spawn')
#print("------- set start method --------")

roop.globals.set_method = False
@app.route('/api/generate', methods=['POST'])
def generate():
	print('generate', request.files)
	if 'video' not in request.files or 'face' not in request.files:
		flash('No file part')
		print('No file part')
		return redirect(request.url)
	video = request.files['video']
	image = request.files['face']
	if video.filename == '':
		flash('No image selected for uploading')
		print('No image selected for uploading')
		return redirect(request.url)
	elif image.filename == '':
		flash('No video selected for uploading')
		print('No video selected for uploading')
		return redirect(request.url)
	else:
		imagepath = secure_filename(image.filename)
		videopath = secure_filename(video.filename)
		id = uuid.uuid1()
		outpath = secure_filename(str(id) + ".mp4")
		#outpath = secure_filename("output.mp4")
		image.save(os.path.join(app.config['UPLOAD_FOLDER'], imagepath))
		video.save(os.path.join(app.config['UPLOAD_FOLDER'], videopath))
		#print('upload_video filename: ' + filename)
		flash('Video successfully uploaded and displayed below')
		if roop.globals.set_method == False:
			multiprocessing.set_start_method('spawn')
			print("------- set start method --------")
			roop.globals.set_method = True
		print("------- allocate process --------")
		data = {
			'video': os.path.join(app.config['UPLOAD_FOLDER'], videopath),
			'face': os.path.join(app.config['UPLOAD_FOLDER'], imagepath),
			'output': os.path.join(app.config['UPLOAD_FOLDER'], outpath)
		}
		spawn = False
		if roop.globals.queue == None:
			roop.globals.queue = Queue()
			spawn = True

		q = roop.globals.queue
		q.put(data)
		#p = multiprocessing.Process(target=task, args=(os.path.join(app.config['UPLOAD_FOLDER'], videopath), os.path.join(app.config['UPLOAD_FOLDER'], imagepath), os.path.join(app.config['UPLOAD_FOLDER'], outpath) ) )
		#print("------- start processs --------")
		#p.start()
		if spawn:
			p = Process(target=loop, args=(q,) )
			print("------- start processs --------")
			p.start()
		d = {'queue': q.qsize(),'filename': outpath}
		return jsonify(d)
		#p.join()
		#return render_template('upload.html', filename=outpath)

@app.route('/')
def upload_form():
	return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_video():
	print('upload_video', request.files)
	if 'video' not in request.files or 'face' not in request.files:
		flash('No file part')
		return redirect(request.url)
	video = request.files['video']
	image = request.files['face']
	if video.filename == '':
		flash('No image selected for uploading')
		return redirect(request.url)
	elif image.filename == '':
		flash('No video selected for uploading')
		return redirect(request.url)
	else:
		imagepath = secure_filename(image.filename)
		videopath = secure_filename(video.filename)
		id = uuid.uuid1()
		outpath = secure_filename(str(id) + ".mp4")
		image.save(os.path.join(app.config['UPLOAD_FOLDER'], imagepath))
		video.save(os.path.join(app.config['UPLOAD_FOLDER'], videopath))
		#print('upload_video filename: ' + filename)
		flash('Video successfully uploaded and displayed below')
		#task(os.path.join(app.config['UPLOAD_FOLDER'], videopath),
        #     os.path.join(app.config['UPLOAD_FOLDER'], imagepath),
        #    os.path.join(app.config['UPLOAD_FOLDER'], outpath))
		#multiprocessing.set_start_method('spawn')
		print("------- allocate process --------")
		data = {
			'video': os.path.join(app.config['UPLOAD_FOLDER'], videopath),
			'face': os.path.join(app.config['UPLOAD_FOLDER'], imagepath),
			'output': os.path.join(app.config['UPLOAD_FOLDER'], outpath)
		}
		spawn = False
		if roop.globals.queue == None:
			roop.globals.queue = Queue()
			spawn = True

		q = roop.globals.queue
		q.put(data)
		#p = Process(target=task, args=(os.path.join(app.config['UPLOAD_FOLDER'], videopath), os.path.join(app.config['UPLOAD_FOLDER'], imagepath), os.path.join(app.config['UPLOAD_FOLDER'], outpath) ) )
		if spawn:
			p = Process(target=loop, args=(q,) )
			print("------- start processs --------")
			p.start()
		#p.join()
		return render_template('upload.html', filename=outpath)

def loop(q):
	while True:
		data = q.get()
		#task(data['video'], data['face'], data['output'])
		pp = Process(target=task, args=(data['video'], data['face'], data['output']) )
		print("------- start sub processs --------")
		pp.start()
		pp.join()

@app.route('/display/<filename>')
def display_video(filename):
	#print('display_video filename: ' + filename)
	return redirect(url_for('static', filename='uploads/' + filename), code=301)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
	
