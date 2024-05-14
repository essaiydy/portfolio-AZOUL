from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from models.user import Base, User


class Db_storage:
    __session = None
    __engine = None
    
    def __init__(self):
        self.__engine = create_engine('mysql://root:""@localhost/azoul')
        
    def add(self, obj):
        self.__session.add(obj)
        self.__session.commit()
        
    def usr(self, id):
        return self.all()[id]
        # return self.__session.query(User.password).filter_by(email=email).one()[0]
        
    def login(self, email):
        for user in self.all():
            if self.all()[user]['email'] == email:
                return self.all()[user]
        return None
        
    
    def all(self):
        dic_users = {}
        for user in self.__session.query(User).all():
            dic_users[str(user.id)] = {'name': user.name,
                                  'email': user.email,
                                     'psw': user.password,
                                     'age': user.age,
                                     'gender': user.gender,
                                     'country': user.country,
                                     'level': user.level,
                                     'job': user.job,
                                     'weight': user.weight,
                                     'height': user.height,
                                     'situation': user.situation,
                                     'disease': user.diseases,
                                     'img': user.img,
                                     'id': user.id}
        return dic_users
    
    def settings(self, id, info):
        updated_user = self.__session.query(User).filter_by(id=id).first()
        if updated_user:
            for key in info:
                k = eval(key)
                if key not in ['email', 'psw']:
                    updated_user.k = info[key]
                else:
                    updated_user.k = updated_user.k
            self.__session.commit()
        
    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(factory)
        self.__session = Session