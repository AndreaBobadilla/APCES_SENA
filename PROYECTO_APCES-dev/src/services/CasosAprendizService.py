#Importamos la conexión a BD
from ..database.db_mysql import get_connection
from ..helpers.helpers import generate_password
from ..models.Casos import casosAprendiz 
from ..uploads.ModificarArchivos import modificar_template

class CasosAprendizService():

    @classmethod
    def crear_caso_aprendiz(cls, casoApren):
        try:
            conexion = get_connection()
            with conexion.cursor() as cursor:
                sql = """INSERT INTO casosAprendiz (tipo_Documento, num_Documento, num_Ficha, nombre_Aprendiz, correo_Aprendiz) VALUES (%s, %s, %s, %s, %s)"""
                datos = (
                    casoApren.tipo_Documento,
                    casoApren.num_Documento,
                    casoApren.num_Ficha,
                    casoApren.nombre_Aprendiz,
                    casoApren.correo_Aprendiz,
    
                )
                cursor.execute(sql, datos)
                if modificar_template(datos):
                    print("ARCHIVO CREADO CON EXITO")
                else: 
                    print("Se presentó un error")
                conexion.commit()
        except Exception as ex:
            raise ex