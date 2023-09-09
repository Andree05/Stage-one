from flask import Flask, request, jsonify
import datetime
import os
import sys

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_andrew():
    # Parse query parameters
    slack_name = request.args.get('slack_name', 'fagbemi_andrew')
    track = request.args.get('track', 'backend')

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
        'slack_name': slack_name,
        'current_day': day_of_week,
        'utc_time': utc_time.strftime('%Y-%m-%d %H:%M:%S'),
        'track': track,
        'github_file_url': file_url,
        'github_repo_url': source_code_url,
        'status_code': 'Success'
    }

    return jsonify(response_data), 200

if __name__ == '__main__':
    app.run(debug=True)
