# stand_up_triangle_api.py
# An API Program for CS630, week 8, Assignment 2, SNHU
# By Matthew Heusser M.Heusser@snhu.edu Jun 2025
#
#
# To use:
# 
# python3 stand_up_triangle_api.py
#
# Runnng on port 5082, mostly because it is assignment 8-2
#
# Sample browser URL to test:
#  http://localhost:5082/triangle?a=1&b=1&c=1
#
# Sample curl command to test:
# curl -X GET "http://localhost:5082/triangle?a=1&b=1&c=1" 
#
#
#   
#
#  
#
#----------------------------------------------------------#

from flask import Flask, request, jsonify
from triangle import classify_triangle

app = Flask(__name__)

@app.route('/triangle', methods=['GET', 'POST'], strict_slashes=False)
@app.route('/triangle/', methods=['GET', 'POST'], strict_slashes=False)
def triangle_endpoint():
    """
    GET  /triangle?a=3&b=4&c=5
    POST /triangle with JSON { "a":3, "b":4, "c":5 }

    Response JSON: { "type": "scalene" }
    """
    # Handle GET parameters
    if request.method == 'GET':
        try:
            a = float(request.args.get('a', ''))
            b = float(request.args.get('b', ''))
            c = float(request.args.get('c', ''))
        except ValueError:
            return jsonify(error="Parameters a, b, and c must be numbers"), 400
    else:
        data = request.get_json(force=True, silent=True)
        if not data or any(key not in data for key in ('a', 'b', 'c')):
            return jsonify(error="Missing parameters: a, b, c required"), 400
        try:
            a, b, c = float(data['a']), float(data['b']), float(data['c'])
        except (ValueError, TypeError):
            return jsonify(error="Parameters a, b, and c must be numbers"), 400

    # Classify triangle using the provided function
    tri_type = classify_triangle(a, b, c)
    return jsonify(type=tri_type)

if __name__ == '__main__':
    # On macOS: disable reloader to avoid multiprocessing issues
    app.run(host='0.0.0.0', port=5082, debug=True, use_reloader=False)
