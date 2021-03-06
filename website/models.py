from . import db 
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstName = db.Column(db.String(150))

class Student(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    tNumber = db.Column(db.String(150), unique=True)
    firstName = db.Column(db.String(150))
    middleName = db.Column(db.String(150))
    lastName = db.Column(db.String(150))
    term = db.Column(db.String(150))
    level = db.Column(db.String(150))
    pProgram = db.Column(db.String(150))
    pPname = db.Column(db.String(150))
    pCollege = db.Column(db.String(150))
    pDept = db.Column(db.String(150))
    pDeptDesc = db.Column(db.String(150))
    sProgram = db.Column(db.String(150))
    sPname = db.Column(db.String(150))
    sCollege = db.Column(db.String(150))
    sDept = db.Column(db.String(150))
    sDeptDesc = db.Column(db.String(150))
    decision = db.Column(db.String(150))
    admit = db.Column(db.Date())
    sAddress1 = db.Column(db.String(150))
    sAddress2 = db.Column(db.String(150))
    city = db.Column(db.String(150))
    state = db.Column(db.String(150))
    zip = db.Column(db.String(150))
    phoneArea = db.Column(db.String(150))
    phoneNum = db.Column(db.String(150))
    phoneNumEx = db.Column(db.Integer)
    email = db.Column(db.String(150))
    ualrEmail = db.Column(db.String(150))
    ethnicity = db.Column(db.String(150))
    sex = db.Column(db.String(150))
    admission = db.Column(db.String(150))
    studentType = db.Column(db.String(150))
