"""
A sample Hello World server.
"""
import os
from flask import Flask, render_template
import topicwizard
import joblib
# pylint: disable=C0103
topic_data = joblib.load('topic_data.joblib')


app_test = topicwizard.get_dash_app(topic_data,exclude_pages = {'words','documents'})



if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app_test.run(debug=False, port=8080)
