#######################################################
# Load modules
#######################################################

# Configuration modules
import logging
from etc import flask_config, logger_config

# Flask module
from flask import Flask, render_template, request, jsonify

# Custom modules
from modules import system_activities


#######################################################
# Start Flask framework
#######################################################
app = Flask(__name__)


#######################################################
# Set Flask configuration
#######################################################
app.config.from_object(flask_config.DevelopmentConfig())


#######################################################
# Set routes
#
#   Retrieve request data (POST & GET):
#     request.values.get('parameter')
#######################################################

@app.route('/', methods=['GET', 'POST'])
def hello():
    logging.info('Index has been called')
    return render_template('index.html')

@app.route('/hansi', methods=['GET', 'POST'])
def hansi():
    logging.info('Hansi has been called')
    return 'Yes, this is Hansi!'


@app.route('/get-system-status-api/', methods=['GET', 'POST'])
def get_system_status():
    result = system_activities.get_system_status()
    return jsonify(result)




@app.route('/get-active-job/', defaults={'subsystem':'QINTER'}, methods=['GET', 'POST'])
@app.route('/get-active-job/<subsystem>', methods=['GET', 'POST'])
def get_active_jobs(subsystem):
    rows = system_activities.get_active_jobs(subsystem)
    return render_template('table.html', table=rows)



@app.route('/get-active-job-api/', defaults={'subsystem':'QINTER'}, methods=['GET', 'POST'])
@app.route('/get-active-job-api/<subsystem>', methods=['GET', 'POST'])
def get_logs_api(subsystem):
    result = system_activities.get_active_jobs(subsystem)
    return jsonify(result)




#######################################################
# If you run it directly here ...
#######################################################

if __name__ == '__main__':
    app.run(port=app.config["PORT"],
        host=app.config["HOST"])