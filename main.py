from flask import*
from public import*
from admin import*
app=Flask(__name__)

app.secret_key="abcd"
app.register_blueprint(public)
app.register_blueprint(admin)

app.run(debug=True,port=5002)
