from flask import Blueprint, request, jsonify
import subprocess
import tempfile

bp = Blueprint('terminal', __name__)

@bp.route('/execute', methods=['POST'])
def execute_code():
    code = request.json.get('code', '')
    
    try:
        result = subprocess.run(
            ['python', '-c', code],
            capture_output=True,
            text=True,
            timeout=30,
            check=True
        )
        return jsonify({'output': result.stdout, 'error': ''})
    except subprocess.TimeoutExpired:
        return jsonify({'output': '', 'error': 'Время выполнения превышено (30 сек)'})
    except subprocess.CalledProcessError as e:
        return jsonify({'output': '', 'error': e.stderr})
    except Exception as e:
        return jsonify({'output': '', 'error': str(e)})
