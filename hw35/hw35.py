'''
Зробити виведення даних у вигляді json з пакету report за допомогою flask
report_framework (2).zip report_framework (2).zip29 квітня 2024, 12:31 PM
'''

# app.py
from flask import Flask, jsonify, request
import os
from report import main as main_report, sort_race_logs
from file_handler import read_data_fromfile

app = Flask(__name__)

@app.route('/race_results', methods=['GET'])
def get_race_results():
    folder = request.args.get('folder', default='racing_data', type=str)
    order = request.args.get('order', default='asc', type=str)
    driver = request.args.get('driver', default='', type=str)

    if order not in ['asc', 'desc']:
        return jsonify({"error": "Invalid order value, should be 'asc' or 'desc'"}), 400

    try:
        race_results, abbrs = main_report(folder)
        race_results_sorted = sort_race_logs(race_results, order)
        race_table = prepare_race_table(race_results_sorted, abbrs, driver)
        if not race_table:
            return jsonify({"error": "Driver not found"}), 404
        return jsonify(race_table), 200
    except FileNotFoundError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def prepare_race_table(race_results: dict[str, str], abbrs: dict[str, tuple[str, str]], current_driver: str):
    """Prepare race data to print"""
    race_table = []
    for counter, code in enumerate(race_results, 1):
        driver = abbrs[code][0]
        company = abbrs[code][1]
        race_time = race_results[code]
        if current_driver:
            if driver == current_driver:
                race_table.append({"position": counter, "driver": driver, "company": company, "race_time": race_time})
                break
            continue
        race_table.append({"position": counter, "driver": driver, "company": company, "race_time": race_time})

    if current_driver and not race_table:
        return False
    return race_table

if __name__ == '__main__':
    app.run(debug=True)

# Супер. усміхаюсь