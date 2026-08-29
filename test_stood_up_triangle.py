#test_stood_up_triangle.py
#
#----------------------------------------------------------#
# A test program for CS630, week 8, Assignment 2, SNHU
# By Matthew Heusser M.Heusser@snhu.edu Jun 2025
#
#
# To Run:
# 1) First, port 5082 needs to be free on localhost
#
# 2) Then, set up an API Server:
#    At the command line:
#
#    python3 stand_up_triangle_api.py
#
# 3) Run pytest:
#     
#    pytest
#
#----------------------------------------------------------#


import requests
import triangle

BASE_URL = "http://localhost:5082/triangle"

def test_get_equilateral():
    # GET /triangle?a=1&b=1&c=1
    params = {"a": 1, "b": 1, "c": 1}
    resp = requests.get(BASE_URL, params=params)
    assert resp.status_code == 200, f"Unexpected status code: {resp.status_code}"
    data = resp.json()
    assert data == {"type": "equilateral"}
