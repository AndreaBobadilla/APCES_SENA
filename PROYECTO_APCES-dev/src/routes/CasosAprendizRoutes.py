from src.models.Casos import casosAprendiz
from ..services.CasosAprendizService import CasosAprendizService
from ..models.Forms import  *
import base64
from io import BytesIO
from flask import Blueprint, render_template, redirect, request, url_for, make_response, send_file
from flask_login import login_required, current_user
from ..routes.wrappers.wrappers import decorador_rol_usuario, decorador_estado_usuario
from ..helpers.helpers import generate_password_and_user

#Blueprint para categorizar las rutas del usuario 
calls= Blueprint('calls_blueprint', __name__)

@calls.route("/crearCaso", methods=["POST", "GET"])
def crearCaso():
    formCrearCaso = FormularioCrearCasoAprendiz()
    if formCrearCaso.validate_on_submit() and request.method == "POST":
        casos = casosAprendiz(
            None,
            tipo_Documento = request.form["tipo_Documento"],
            num_Documento = request.form["num_Documento"],
            num_Ficha = request.form["num_Ficha"],
            nombre_Aprendiz = request.form["nombre_Aprendiz"],
            correo_Aprendiz = request.form["correo_Aprendiz"],
        )
        
        CasosAprendizService.crear_caso_aprendiz(casos)
        
        
        return redirect(url_for("calls_blueprint.visualizarCaso"))

    return render_template("crearCaso.html", formCrearCaso = formCrearCaso)
