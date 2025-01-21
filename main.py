from flask  import Flask, redirect, render_template, request, url_for #importando a biblioteca flask
from flask_sqlalchemy import SQLAlchemy #importando a biblioteca sqlachemy
from flask_wtf import FlaskForm #importando a biblioteca flaskForm
from wtforms import Form, StringField, SubmitField, SubmitField, SelectField, FloatField

app = Flask(__name__)# criando uma instância da classe Flask
app.config['SECRET_KEY'] = 'DIE'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///TM.db'

bancoDados = SQLAlchemy(app)#criando uma instância da classe SQLAlchemy

class CadastroForm(FlaskForm):
    nome = StringField('Nome')
    preco = FloatField('Preco')
    categoria = SelectField('Categoria',  choices=[('entrada','Entrada'),('principal', 'Principal'), ('sobremesa', 'Sobremesa')])
    submit = SubmitField('Cadastrar')

class Pratos(bancoDados.Model):
    id = bancoDados.Column(bancoDados.Integer, primary_key = True, autoincrement = True)
    nome = bancoDados.Column(bancoDados.String(100), nullable = False)
    preco = bancoDados.Column(bancoDados.Float, nullable = False)
    categoria = bancoDados.Column(bancoDados.String(100), nullable = False)
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/localizacao')
def localizacao():
    return render_template('localizacao.html')

@app.route('/quemsomos')
def quemsomos():
    return render_template('quemsomos.html')

@app.route('/cardapio')
def cardapio():
    return render_template('cardapio.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = CadastroForm(request.form)
    if form.validate() and request.method == "POST":
        pratos = Pratos(
            nome = form.nome.data, 
            preco = form.preco.data, 
            categoria = form.categoria.data) 
        bancoDados.session.add(pratos)
        bancoDados.session.commit()
        return 'Prato cadastrado com sucesso!'
    
    return render_template('cadastro.html', form = form)

@app.route('/editar/<int:id>', methods=['GET','POST'])
def editar(id):
    prato = Pratos.query.get(id)
    form = CadastroForm(obj=prato)
    if form.validate_on_submit():
        prato.nome = form.nome.data
        prato.preco = form.preco.data
        prato.categoria = form.categoria.data
        bancoDados.session.commit()
        return redirect(url_for('gerenciarDados'))
    return render_template('cadastro.html', form=form)

@app.route('/excluir/<int:id>')
def excluir(id):
    prato = Pratos.query.get(id)
    bancoDados.session.delete(prato)
    bancoDados.session.commit()
    return redirect(url_for('gerenciarDados'))

@app.route('/gerenciarDados')
def gerenciarDados():
    dados = Pratos.query.all()
    return render_template('gerenciarDados.html', dados=dados)

if __name__ == '__main__':
    with app.app_context():
        bancoDados.create_all()
    app.run(debug = True) 