from flask import Flask, jsonify, request

app = Flask(__name__)

# The path to the file containing the latest version number

version_file = 'client.py'

# Read the latest version number from the file

with open(version_file, 'r') as f:

    latest_version = float(f.read())

# Endpoint for getting the latest version

@app.route('/version')

def get_version():

    return jsonify({'version': latest_version})

# Endpoint for updating the latest version

@app.route('/version', methods=['POST'])

def update_version():

    global latest_version

    latest_version = float(request.json['version'])

    # Write the latest version number to the file

    with open(version_file, 'w') as f:

        f.write(str(latest_version))

    return jsonify({'success': True})

# Run the server

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=8000)

