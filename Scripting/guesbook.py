from flask import Flask

app = Flask(__name__) #creating app

@app.route('/')
def inicio():
    return '<h1>Inicio</h1>'
    
@app.route('/home') #Create route
def index():
    return '<h1>Home</h1>'

@app.route('/metodos',  methods=['GET','POST']) 
def metodo():
    return '<h1>Metodos</h1>'

if __name__ == '__main__':
    app.run(debug=True)


