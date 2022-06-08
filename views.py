import tkinter as tk
from tkinter import Tk, filedialog
from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from pytube import YouTube

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form.get('url')
        if len(url) < 1:
            pass
        else:
            try:
                session['my_url'] = url
                my_video = YouTube(url)
                return redirect(url_for('views.video'))
            except:
                flash('URL not found', category='error')
                return render_template('home.html')
    return render_template('home.html')

@views.route('/video', methods=['GET', 'POST'])
def video():
        url = session.get('my_url', None)
        my_video = YouTube(url)
        return render_template('video.html', url=url, my_video=my_video)

@views.route('/downloadMP4', methods=['GET', 'POST'])
def downloadMP4():
    root = Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1) # Opens file dialog in front of all windows
    path = filedialog.askdirectory() # Open directory
    root.destroy()

    my_url = session.get('my_url', None)
    my_video = YouTube(my_url)
    my_video = my_video.streams.get_highest_resolution()
    my_video.download(path)
    return render_template('download.html', my_url=my_url)

@views.route('/downloadMP3', methods=['GET', 'POST'])
def downloadMp3():
    root = Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1) # Opens file dialog in front of all windows
    path = filedialog.askdirectory() # Open directory
    root.destroy() 

    my_url = session.get('my_url', None)
    my_video = YouTube(my_url)
    my_video = my_video.streams.get_audio_only()
    my_video.download(path)
    return render_template('download.html', my_url=my_url)
    