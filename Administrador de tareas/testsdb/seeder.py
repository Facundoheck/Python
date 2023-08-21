from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models import Test, Tarea, Base

if __name__ == "__main__":
    engine = create_engine('sqlite:///C:\\TUIA\\CUAT1\\prog1\\python\\Administrador de tareas\\testsdb\\test_2.db')
    
    Session = sessionmaker(bind=engine)
    session = Session()

    Tareas = [
        Tarea(
            nombre="Limpiar la cocina",
            descripcion="Hoy antes del mediodia",
            completada=False
        ),
        Tarea(
            nombre="Sacar la basura",
            descripcion="Hoy antes de las 21",
            completada=True
        )
    ]

    test = Test(test_name="Python", tareas=Tareas)
    session.add(test)
    session.commit()
