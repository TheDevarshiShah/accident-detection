from project import db
from project.com.vo.LoginVO import LoginVO

class RegisterVO(db.Model):
    __tablename__ = 'registermaster'
    registerId = db.Column('registerId', db.Integer, primary_key=True, autoincrement=True)
    registerTrafficPoliceStationName = db.Column('registerTrafficPoliceStationName', db.String(100),nullable=False)
    registerAreaName = db.Column('registerAreaName', db.String(100),nullable=False)
    registerContactNo = db.Column('registerContactNo', db.String(100),nullable=False)
    registerAddress = db.Column('registerAddress', db.String(100),nullable=False)
    #register_LoginId = db.column("register_LoginId",db.Integer, db.ForeignKey(LoginVO.loginId))
    register_LoginId = db.Column("register_LoginId",db.Integer,db.ForeignKey(LoginVO.loginId))
    def as_dict(self):
        return {
            'registerId': self.registerId,
            'registerTrafficPoliceStationName': self.registerTrafficPoliceStationName,
            'registerAreaName': self.registerAreaName,
            'registerContactNo': self.registerContactNo,
            'registerAddress': self.registerAddress,
            'register_LoginId': self.register_LoginId
        }

db.create_all()
