from flask import render_template, request, jsonify, current_app
from flask_login import current_user
from cilante.models import db, ChatLogs
from . import assistant
import uuid
#from .ml_model import predict_assistant_response

def procesar_mensaje(mensaje: str) -> str:
    # Aquí se integraría el modelo de ML para generar una respuesta
    # Por ahora, devolvemos una respuesta fija
    return "Hola"

@assistant.route('/chat', methods=['GET', 'POST'])
def chat():
    # procesa el mensaje del usuario, guarda el log y devuelve la respuesta
    if request.method == 'POST':
        user_input = request.get_json(silent=True) or {}
        mensaje = user_input.get('message', '').strip()
        conversacion_id = user_input.get('conversation_id')
        if not mensaje:
            return jsonify({'error': 'Mensaje vacío'}), 400
        if not conversacion_id and current_user.is_authenticated:
            conversacion_id = uuid.uuid4().hex
            
        try:
            respuesta = procesar_mensaje(mensaje)
            if current_user.is_authenticated:
                log = ChatLogs()
                log.user_id = current_user.user_id
                log.conversacion_id = conversacion_id
                log.mensaje_usuario = mensaje
                log.respuesta_bot = respuesta
                db.session.add(log)
                db.session.commit()
            return jsonify({'response': respuesta, 'conversation_id': conversacion_id}), 200
        except Exception as e:
            current_app.logger.error(f"Error al procesar el mensaje: {e}")
            return jsonify({'error': 'Error interno del servidor'}), 500
    # muestra la interfaz de chat y las conversaciones anteriores, solo funciona si el usuario está autenticado
    mensaje = []
    recientes = {}
    botonSi = False
    ultimo_log = None
    if current_user.is_authenticated:
        ultimo_log = ChatLogs.query.filter_by(
            user_id=current_user.user_id
        ).order_by(ChatLogs.created_at.desc()).first()
        if ultimo_log:
            botonSi = request.args.get('restaurar') == '1'
            if botonSi:        
                conversacion_id = ultimo_log.conversacion_id
                if conversacion_id:
                    mensaje = ChatLogs.query.filter_by(
                        user_id=current_user.user_id,
                        conversacion_id=conversacion_id
                    ).order_by(ChatLogs.created_at.asc()).all()
        # mostrar conversaciones anteriores
        conversaciones_query = db.session.query(
            ChatLogs.conversacion_id,
            db.func.max(ChatLogs.created_at).label('last_message'),
            db.func.max(ChatLogs.respuesta_bot).label('last_at')
        ).filter(ChatLogs.user_id == current_user.user_id).group_by(ChatLogs.conversacion_id).order_by(db.desc('last_at')).all()
        recientes = [
            {
                'conversation_id': con.conversacion_id,
                'last_at': con.last_at,
                'preview': (con.last_at[:60] + '...') if con.last_at else ''
            } for con in conversaciones_query
        ]
    return render_template(
        'assistant/chat.html',
        ultimo_log=ultimo_log,
        messages=mensaje,
        conversaciones_recientes=recientes,
        botonSi=botonSi
        )


