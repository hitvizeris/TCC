from flask  import Flask, redirect, render_template, request, session, url_for #importando a biblioteca flask
from flask_sqlalchemy import SQLAlchemy #importando a biblioteca sqlachemy
from flask_wtf import FlaskForm #importando a biblioteca flaskForm
from wtforms import FileField, Form, StringField, SubmitField, SubmitField, SelectField, FloatField
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)# criando uma instância da classe Flask
app.config['SECRET_KEY'] = 'DIE'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///TM.db'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

bancoDados = SQLAlchemy(app)#criando uma instância da classe SQLAlchemy

class CadastroForm(FlaskForm):
    nome = StringField('Nome')
    preco = FloatField('Preco')
    descricao = StringField('descricao')
    categoria = SelectField('Categoria',  choices=[('entrada','Entrada'),('principal', 'Principal'), ('sobremesa', 'Sobremesa')])
    submit = SubmitField('Cadastrar')
    imagem = FileField('Imagem')

class Pratos(bancoDados.Model):
    id = bancoDados.Column(bancoDados.Integer, primary_key = True, autoincrement = True)
    nome = bancoDados.Column(bancoDados.String(100), nullable = False)
    preco = bancoDados.Column(bancoDados.Float, nullable = False)
    descricao = bancoDados.Column(bancoDados.String(160), nullable = False)
    categoria = bancoDados.Column(bancoDados.String(100), nullable = False)
    imagem = bancoDados.Column(bancoDados.String(250), nullable=False)
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/localizacao')
def localizacao():
    return render_template('localizacao.html')

@app.route('/quemsomos')
def quemsomos():
    return render_template('quemsomos.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = CadastroForm()
    if form.validate_on_submit():
        imagem = form.imagem.data
        image_path = f'{app.config["UPLOAD_FOLDER"]}/{secure_filename(imagem.filename)}'
        pratos = Pratos(
            nome = form.nome.data, 
            preco = form.preco.data, 
            descricao = form.descricao.data,
            categoria = form.categoria.data,
            imagem=image_path)
        imagem.save(image_path)
        bancoDados.session.add(pratos)
        bancoDados.session.commit()
        return 'Prato cadastrado com sucesso!'
    
    return render_template('cadastro.html', form = form, prato=None)

@app.route('/editar/<int:id>', methods=['GET','POST'])
def editar(id):
    prato = Pratos.query.get(id)
    form = CadastroForm(obj=prato) 
    if form.validate_on_submit():
        imagem = form.imagem.data
        image_path = f'{app.config["UPLOAD_FOLDER"]}/{secure_filename(imagem.filename)}'
        prato.nome = form.nome.data
        prato.preco = form.preco.data
        prato.descricao = form.descricao.data
        prato.categoria = form.categoria.data
        bancoDados.session.commit()
        imagem.save(image_path)
        return redirect(url_for('gerenciarDados'))
    return render_template('cadastro.html', form=form, prato=prato)

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

@app.route('/cardapio')
def cardapio():
    dadosEntrada = bancoDados.session.query(Pratos).filter_by(categoria = 'entrada')
    dadosPrincipal = bancoDados.session.query(Pratos).filter_by(categoria = 'principal')
    dadosSobremesa = bancoDados.session.query(Pratos).filter_by(categoria = 'sobremesa')
    
    return render_template('cardapio.html', dadosEntrada=dadosEntrada, dadosPrincipal=dadosPrincipal, dadosSobremesa=dadosSobremesa)

if __name__ == '__main__':
    with app.app_context():
        bancoDados.create_all()
    app.run(debug = True) 