from flask import Blueprint, request, jsonify

from src.clients.manage_incident import IncidentClient
from src.commands.ping import Ping
from src.commands.get_user import GetUser
from src.commands.get_incidents import GetIncidents

from src.errors.errors import NotFound

services_bp = Blueprint('services', __name__)

@services_bp.route('/ping', methods=['GET'])
def ping():
    command = Ping()
    return jsonify({'message': command.execute()}), 200

# Endpoints for User

@services_bp.route('/get_user/<user_id>', methods=['GET'])
def get_user(user_id):
    try:
        command = GetUser(user_id)
        result = command.execute()
        return jsonify(result), 200
    except NotFound as e:
        return jsonify({'error': str(e)}), 404
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

# Endpoints for Incident
@services_bp.route('/get_incidents/<company>', methods=['GET'])
def get_incidents(company):
    try:
        agenteId = request.args.get('agenteId')
        tipoIncidente = request.args.get('tipoIncidente')
        fechaInicio = request.args.get('fechaInicio')
        fechaFin = request.args.get('fechaFin')

        command = GetIncidents(company, {
            'agenteId': agenteId,
            'tipoIncidente': tipoIncidente,
            'fechaInicio': fechaInicio,
            'fechaFin': fechaFin
        })
        result = command.execute()
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': 'Internal server error: {}'.format(e)}), 500



