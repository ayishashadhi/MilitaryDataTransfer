from flask import*
from database import *
public=Blueprint('public',__name__)

@public.route('/')
def home():
    return render_template("home.html")
 

@public.route("/log",methods=['get','post'])
def login():
    if 'login' in request.form:
        uname=request.form['username']
        p=request.form['password']

        print(uname,p,"=====================")
        qry="select * from login where username='%s' and password='%s'"%(uname,p)
        res=select(qry)
        print(res)
        if res:
            session['log']=res[0]['login_id']
            if res[0]['usertype']=='admin':
                return redirect(url_for('admin.adminhome'))
        else:
            return '''<script>alert("invalid username or password");window.location="/login"</script>'''

    return render_template("login.html")

@public.route("/reg")
def reg():
    return render_template("registre.html")
