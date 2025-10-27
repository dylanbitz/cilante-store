from flask import Blueprint, render_template, request, jsonify
from .ml_model import predict_assistant_response

assistant_bp = Blueprint('assistant', __name__)

@assistant_bp.route('/assistant', methods=['GET', 'POST'])
def assistant():
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        response = predict_assistant_response(user_input)
        return jsonify({'response': response})
    return render_template('assistant.html')