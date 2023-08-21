from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from Models import Test, Tarea, Base
from sqlite3 import ProgrammingError

#esta clase se encarga de la conexion con la base de datos
class Controller:
    def __init__(self) -> None:
        engine = create_engine(
        "sqlite:///C:\\TUIA\\CUAT1\\prog1\\python\\Administrador de tareas\\testsdb\\test_2.db"
    )
    
        Session = sessionmaker(bind=engine)
        self.session = Session()
        
    def create_empty_test(self,_test_name):
        test = self.session.query(Test).filter(Test.test_name == _test_name).first()
        if test == None:
            new_test = Test(test_name = _test_name)
            self.session.add(new_test)
            self.session.commit()
        else:
            raise ProgrammingError("Ya existe un test con ese nombre")