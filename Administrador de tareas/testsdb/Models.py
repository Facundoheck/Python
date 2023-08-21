from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Test(Base):
    __tablename__ = "Tests"
    test_id = Column(Integer, primary_key=True)
    test_name = Column(String(200))
    
    tareas = relationship("Tarea", back_populates="test")  # Definir la relación

class Tarea(Base):
    __tablename__ = "Tareas"
    tarea_id = Column(Integer, primary_key=True)
    nombre = Column(String(200))
    descripcion = Column(String(500))
    completada = Column(Boolean, nullable=True)
    test_id = Column(Integer, ForeignKey("Tests.test_id"))  # Clave foránea
    
    test = relationship("Test", back_populates="tareas")  # Definir la relación

engine = create_engine('sqlite:///C:\\TUIA\\CUAT1\\prog1\\python\\Administrador de tareas\\testsdb\\test_2.db')
Base.metadata.create_all(engine)
