import os
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import openai

print("Needed to add billing then generate new key! :/")
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
    question_type = request.json.get('questionType', 'mcq')  # Default to MCQs
    if not content:
        return jsonify({"error": "No content provided"}), 400

    try:
        # Adjust the system prompt based on the question type
        if question_type == 'mcq':
            prompt = f"Generate three multiple-choice questions based on the following content:\n\n{content}"
        elif question_type == 'long_answer':
            prompt = f"Generate three long-answer questions based on the following content:\n\n{content}"
        elif question_type == 'flashcards':
            prompt = f"Generate three flashcards in the format 'Term: Definition' based on the following content:\n\n{content}"
        else:
            return jsonify({"error": "Invalid question type provided"}), 400

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use "gpt-4" for higher quality if available
            messages=[
                {"role": "system", "content": "You are a helpful assistant that generates educational content."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300
        )
        questions = response['choices'][0]['message']['content'].strip()
        return jsonify({"questions": questions})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
