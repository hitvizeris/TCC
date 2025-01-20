from flask  import Flask, render_template #importando a biblioteca flask
from flask_sqlalchemy import SQLAlchemy #importando a biblioteca sqlachemy
from flask_wtf import FlaskForm #importando a biblioteca flaskForm
from wtforms import Form, StringField, SubmitField, PasswordField, BooleanField, SubmitField, SelectField, FloatField

app = Flask(__name__)# criando uma instância da classe Flask
app.config['SECRET_KEY'] = 'DIE'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///TM.db'

bancoDados = SQLAlchemy(app)#criando uma instância da classe SQLAlchemy


class Pratos():
    id = bancoDados.Column(bancoDados.Integer, primary_key = True, autoincrement = True)
    nome = bancoDados.Column(bancoDados.String(100), nullable = False)
    preco = bancoDados.Column(bancoDados.Float, nullable = False)
    categoria = bancoDados.Column(bancoDados.String(100), nullable = False)
    
class CasdastroForm(FlaskForm):
    nome = StringField('Nome')
    preco = FloatField('Preco')
    categoria = SelectField('Categoria')
    submit = SubmitField('Cadastrar')


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
        if Form.validade_on_submit():
            Pratos =Pratos(nome = Form.nome.data, preco = Form.preco.data, categoria = Form.categoria.data) 
            bancoDados.session.add(Pratos)
            bancoDados.session.commit()
            return 'Prato cadastrado com sucesso!'
        return render_template('cadastro.html', Form = Form)


if __name__ == '__main__':
    with app.app_context():
        bancoDados.create_all()
    app.run(debug = True) 