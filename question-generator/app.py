import os
from flask import Flask, request, jsonify, render_template 
from dotenv import load_dotenv
import openai 

# Load API key from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__) 

@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/generate', methods=['POST'])
def generate_questions():
    content = request.json.get('content', '')
    if not content:
        return jsonify({"error": "No content provided"}), 400

    try:
        # GPT API prompt for generating MCQs
        response = openai.Completion.create(
            engine= "text-davinci-003", 
            prompt=f"Generate three multiple choice questions based on the following content: \n\n{content}",
            max_tokens = 300
        )
        questions = response.choices[0].text.strip()
        return jsonify({"questions": questions})
    except Exception as e:
        return jsonify({"error": str(e)}), 500  

if __name__ == '__main__':
    app.run(debug=True)   