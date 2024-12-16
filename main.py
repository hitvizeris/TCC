from flask  import Flask, render_template #importando a biblioteca flask
from flask_sqlalchemy import SQLAlchemy#importando a biblioteca sqlachemy

app = Flask(_name_)# criando uma instância da classe Flask
app.config['SECRET_KEY'] = 'DIE'
app.config['SQALCHEMY_DATABASE_URI'] = 'sqalite:///TM.db'

db = SQLAlchemy()#criando uma instância da classe SQLAlchemy


class Pratos:
    id = db.Collumn(db.Integer, Primary_key = True, autoincrement = True)
    nome = db.Collumn(db.String(100), nullable = False)
    preco = db.collumn(db.Float, nullable = False)
    categoria = db.collumn(db.String(100), nullable = False)
    


class CasdastroFrom(FlaskForm):
    nome = StringField('Nome')
    preco = FloatField('Preco')
    categoria = SelectField('Categoria')
    submit = Submitfiel('Cadastrar')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', metjods = ['GET', 'POST'])
def cadastro():
        if from.validade_on_submit():
            Pratos =Pratos(nome = form.nome.data, preco = form.preco.data, categoria = form.categoria.data) 
            db.session.add(pratos)
            db.session.commit()
            return 'Prato cadastrado com sucesso!'
        return render_template('cadastro.html', form = form )


if _name_ == '_main_':
    with app.app_context():
        db.create_all()
    app.run(debug = True) 