from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename


# inicialização da aplicação
app = Flask(__name__)

# funcação para rota inicial
@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        # se a requisicão for do tipo GET  renderiza o template inicial
        return render_template('index.html')
    # se a requsição for do tipo POST ... 
    elif request.method == 'POST':
        # recupera o arquivo "upado"
        f = request.files['dados']
        print(f.filename)
        # salva o arquivo na diretório atual do projeto
        f.save(secure_filename(f.filename))
        return redirect(url_for('analise', filename=f.filename))
       

# funcação para rota inicial
@app.route("/analise/<filename>", methods=['POST', 'GET'])
def analise(filename):
    linhas_ = []
    if request.method == 'GET':
        # se a requisicão for do tipo GET  renderiza o template inicial
        with open(secure_filename(filename), 'r') as f:
            linhas = f.readlines()
            quantidades_colunas = 0
            cont = True
            for i in linhas:
                if cont:
                    quantidades_colunas = len(i.split('\t'))
                    cont = False
                linhas_.append(i.split('\t'))
        return render_template('parametros.html', linhas=linhas_, colunas=quantidades_colunas)
    if request.method == 'POST':
        for i in request.form:
            print(request.form[i])
        return render_template('parametros.html')