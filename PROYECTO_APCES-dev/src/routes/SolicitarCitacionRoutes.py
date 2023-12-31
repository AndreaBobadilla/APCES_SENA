from src.models.SolicitarCita import solicitarCitacion
from ..services.SolicitarCitacionServices import SolicitarCitacionService
from ..models.Forms import  *
import base64
from io import BytesIO
from flask import Blueprint, render_template, redirect, request, url_for, make_response, send_file
from flask_login import login_required, current_user
from ..routes.wrappers.wrappers import decorador_rol_usuario, decorador_estado_usuario
from ..helpers.helpers import generate_password_and_user

#Blueprint para categorizar las rutas del usuario 
calls= Blueprint('calls_blueprint', __name__)

@calls.route("/solicitarCitacion", methods=["POST", "GET"])
def solicitudCita():
    formSolicitarCita = FormularioSolicitarCitacion()
    if formSolicitarCita.validate_on_submit() and request.method == "POST":
        solicitar = solicitarCitacion(
            None,
            num_Ficha = request.form["num_Ficha"],
            nombre_Aprendiz = request.form["nombre_Aprendiz"],
            correo_Aprendiz = request.form["correo_Aprendiz"],
            llamados = request.files["llamados"].read(), 
        )
        
        SolicitarCitacionService.solicitar_citacion(solicitar)
        
        
        return redirect(url_for("calls_blueprint.visualizarSolicitudes"))

    return render_template("solicitarCitacion.html", formSolicitarCita = formSolicitarCita)
