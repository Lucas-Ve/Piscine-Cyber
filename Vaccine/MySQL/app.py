from flask import Flask, render_template_string
from sqlalchemy import create_engine, MetaData, Table

app = Flask(__name__)

DATABASE_URI = 'mysql+pymysql://root:root@db/testdb'

engine = create_engine(DATABASE_URI)
metadata = MetaData(bind=engine)
metadata.reflect(bind=engine)
users = Table('users', metadata, autoload_with=engine)

@app.route('/')
def index():
    with engine.connect() as connection:
        result = connection.execute(users.select())
        users_list = [dict(row) for row in result]

    html = """
    <html>
    <head><title>Users</title></head>
    <body>
        <h1>Users</h1>
        <table border='1'>
            <tr><th>Email</th><th>Password</th></tr>
            {% for user in users %}
            <tr><td>{{ user.email }}</td><td>{{ user.password }}</td></tr>
            {% endfor %}
        </table>
    </body>
    </html>
    """
    return render_template_string(html, users=users_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
