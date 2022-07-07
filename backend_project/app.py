from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/page1')
def page1():
    return render_template('page1.html')

@app.route('/page2')
def page2():
    return render_template('page2.html')

@app.route('/page3')
def page3():
    return render_template('page3.html')

@app.route('/page4')
def page4():
    return render_template('page4.html')

@app.route('/page5')
def page5():
    return render_template('page5.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/javascript')
def red():
    return redirect(url_for('script'))

@app.route('/script')
def script():
    return render_template('index.html')

@app.route('/js')
def blue():
    return redirect(url_for('jsfile'))

@app.route('/jsfile')
def jsfile():
    return render_template('index.html')




if __name__=="__main__":
    app.run(debug=True, port=8000)