from flask import Flask, render_template, request, jsonify
import subprocess
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tutorials')
def tutorials():
    return render_template('tutorials.html')

@app.route('/challenges')
def challenges():
    return render_template('challenges.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/tutorials/basic-concepts')
def basic_concepts():
    return render_template('tutorials/basic-concepts.html')

@app.route('/tutorials/control-structures')
def control_structures():
    return render_template('tutorials/control-structures.html')

@app.route('/tutorials/functions-modules')
def functions_modules():
    return render_template('tutorials/functions-modules.html')

@app.route('/tutorials/data-structures')
def data_structures():
    return render_template('tutorials/data-structures.html')

@app.route('/challenges/beginner')
def beginner_challenges():
    return render_template('challenges/begineer-level.html')

@app.route('/challenges/intermediate')
def intermediate_challenges():
    return render_template('challenges/intermediate-level.html')

@app.route('/challenges/advanced')
def advanced_challenges():
    return render_template('challenges/advanced-level.html')

@app.route('/challenges/beginner/hello-world')
def hello_world_challenge():
    return render_template('challenges/begineer/hello_world.html')

@app.route('/challenges/beginner/calculator')
def calculator_challenge():
    return render_template('challenges/begineer/calculator.html')

@app.route('/challenges/beginner/fizzbuzz')
def fizzbuzz_challenge():
    return render_template('challenges/begineer/fizzbuzz.html')

@app.route('/challenges/intermediate/data-structures')
def data_structures_challenge():
    return render_template('challenges/intermediate/data-structures.html')

@app.route('/challenges/intermediate/sorting-algorithms')
def sorting_algorithms_challenge():
    return render_template('challenges/intermediate/sorting-algorithms.html')

@app.route('/challenges/advanced/algorithm-optimization')
def algorithm_optimization_challenge():
    return render_template('challenges/advanced/algorithm-optimization.html')

@app.route('/challenges/advanced/real-world-data')
def real_world_data_challenge():
    return render_template('challenges/advanced/real-world-data.html')

@app.route('/challenges/games/code_breaker')
def code_breaker():
    return render_template('challenges/games/code_breaker.html')

@app.route('/challenges/games/quest_for_loops')
def quest_for_loops():
    return render_template('challenges/games/quest_for_loops.html')

@app.route('/challenges/games/function_frenzy')
def function_frenzy():
    return render_template('challenges/games/function_frenzy.html')

@app.route('/submit_solution', methods=['POST'])
def submit_solution():
    code = request.form['code']
    
    # Write the code to a temporary Python file
    with open('temp_code.py', 'w') as file:
        file.write(code)
    
    try:
        # Run the code using subprocess and capture the output
        result = subprocess.run(['python', 'temp_code.py'], capture_output=True, text=True, timeout=5)
        output = result.stdout + result.stderr
        os.remove('temp_code.py')  # Clean up the temporary file after execution
        return jsonify({'status': 'success', 'output': output})
    except subprocess.TimeoutExpired:
        os.remove('temp_code.py')  # Clean up the temporary file on timeout
        return jsonify({'status': 'error', 'message': 'Code execution timed out.'})
    except Exception as e:
        os.remove('temp_code.py')  # Clean up the temporary file on any error
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
