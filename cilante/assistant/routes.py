from flask import Blueprint, render_template, request, jsonify
from . import assistant
#from .ml_model import predict_assistant_response

@assistant.route('/assistant', methods=['GET', 'POST'])
def assistantfunc():
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        #response = predict_assistant_response(user_input)
        #return jsonify({'response': response})
        return jsonify({'response': 'Hola'})
    return render_template('assistant.html')