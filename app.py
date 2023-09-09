from flask import Flask, request, jsonify
import datetime
import os
import sys

app = Flask(__name__)

@app.route('/andrew', methods=['GET'])
def get_andrew():
    # Parse query parameters
    slack_name = request.args.get('slack_name', 'Fagbemi Andrew')
    track = request.args.get('track', 'Backend')

    # Get current day of the week
    day_of_week = datetime.datetime.utcnow().strftime('%A')

    # Get current UTC time with validation of +/-2
    utc_time = datetime.datetime.utcnow()
    utc_offset = int(request.args.get('utc_offset', '0'))
    if abs(utc_offset) <= 2:
        utc_time += datetime.timedelta(hours=utc_offset)
    else:
        return jsonify({'Status Code': 'Invalid UTC Offset'}), 400

    # Get GitHub URLs
    file_url = 'https://github.com/Andree05/Stage-One/app.py'
    source_code_url = 'https://github.com/Andree05/Stage-One/'

    # Response data
    response_data = {
        'Slack name': slack_name,
        'Current day of the week': day_of_week,
        'Current UTC time': utc_time.strftime('%Y-%m-%d %H:%M:%S'),
        'Track': track,
        'GitHub URL of the file being run': file_url,
        'GitHub URL of the full source code': source_code_url,
        'Status Code': 'Success'
    }

    return jsonify(response_data), 200

#New route for publicly accessible endpoint
@app.route('/public_endpoint', methods=['GET'])
def get_public_info():
    #Parse query parameters
    slack_name = request.args.get('slack_name', 'Fagbemi Andrew')
    track = request.args.get('track', 'Backend')

    #Create a response dictionary
    response_data = {
        'Slack name': slack_name,
        'Track': track
    }

    return jsonify(response_data), 200

@app.route('/api', methods=['GET'])
def get_info():
    # Parse query parameters
    slack_name = request.args.get('slack_name', 'Fagbemi Andrew')
    track = request.args.get('track', 'Backend')

    # Get current day of the week
    day_of_week = datetime.datetime.utcnow().strftime('%A')

    # Get current UTC time with validation of +/-2
    utc_time = datetime.datetime.utcnow()
    utc_offset = int(request.args.get('utc_offset', '0'))
    if abs(utc_offset) <= 2:
        utc_time += datetime.timedelta(hours=utc_offset)
    else:
        return jsonify({'Status Code': 'Invalid UTC Offset'}), 400

    # Response data
    response_data = {
        'Slack name': slack_name,
        'Track': track,
        'Current day of the week': day_of_week,
        'Current UTC time': utc_time.strftime('%Y-%m-%d %H:%M:%S'),
        'Status Code': 'Success'
    }

    return jsonify(response_data), 200

if __name__ == '__main__':
    app.run(debug=True)
