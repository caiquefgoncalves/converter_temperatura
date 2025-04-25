from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/converter_temperatura', methods=['POST'])
def converter_temperatura():
    try:
        celsius = float(request.form['temperatura'])
        fahren = round((celsius * 9 / 5) + 32, 2)
        kel = round(celsius + 273.15, 2)



        return render_template('index.html', celsius=celsius, fahren=fahren, kel=kel)
    except ValueError:
        error = "Por favor, insira um valor numérico válido."
        return render_template('index.html', error=error)
    except Exception as e:
        error = f'Ocorreu um erro inesperado: {str(e)}'
        return render_template('index.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)