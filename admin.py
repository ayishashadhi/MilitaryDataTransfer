from flask import*
from database import*
admin = Blueprint('admin',__name__)

@admin.route('/adminhome')
def adminhome():
    return render_template("admin.html")

@admin.route('/managedesignation',methods=['get','post'])
def managedesignation():
    if 'submit' in request.form:
        dname=request.form['designation_name']

        qur="insert into designation values(null,'%s')"%(dname)
        a=insert(qur)
        if a:
            return """<script>alert('added');window.location='/adminhome'</script>"""

    return render_template("managedesignation.html")





@admin.route('/managedepartment',methods=['get','post'])
def managedepartment():
    if 'submit' in request.form:
        dname=request.form['department_name']
        uname=request.form['username']
        p=request.form['password']
        
        qry="insert into login values(null,'%s','%s','department')"%(uname,p)
        b=insert(qry)


        qur="insert into department values(null,'%s','%s')"%(b,dname)
        a=insert(qur)
        if a:
            return """<script>alert('added');window.location='/adminhome'</script>"""
        
    data={}
    qur="select * from department"
    a=select(qur)
    data['view']=a
    return render_template("managedepartment.html",data=data)



@admin.route('/view_soldiers')
def view_soldiers():
    data={}
    qry="select * from solider"
    ab=select(qry)
    data['view']=ab
    print(data,"KKKKKKKKKKKKKKKKKKKKKK")
    return render_template("view_soldiers.html",data=data)

@admin.route('/department_complaint')
def department_complaint():
    data={}
    qry="select * from department_complaint"
    ab=select(qry)
    data['view']=ab
    print(data,"KKKKKKKKKKKKKKKKKKKKKK")
    return render_template("department_complaint.html",data=data)

@admin.route('/admin_send_complaints_reply')
def admin_send_complaints_reply():
    return render_template("admin_send_complaints_reply.html")