# Файл в котором

from main_app import app, config

from flask import render_template, send_file


@app.route('/')
def index():
    return render_template('video.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


@app.route('/payment')
def payment():
    return render_template('payment.html')


@app.route('/payment_2')
def payment_2():
    return render_template('payment_2.html')


@app.route('/download')
def download():
    path = "download_file/book.pdf"
    return send_file(path, as_attachment=True)


@app.route('/result')
def result():
    return render_template('result.html')
