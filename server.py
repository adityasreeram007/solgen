from flask import Flask,jsonify,render_template
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('create.html')

if __name__=='__main__':
    
    
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    
    app.run(port=5001)