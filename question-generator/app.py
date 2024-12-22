import os
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import openai

print("Needed to add billing then generate new key! :/")
# Load API key from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

#Helper functions:
def clean_flashcard_output(raw_output):
    # Split the output into lines and filter valid "Term: Definition" lines
    flashcards = []
    for line in raw_output.split("\n"):
        if ":" in line:  # Only include lines with the 'Term: Definition' structure
            parts = line.split(":", 1)
            term = parts[0].strip()
            definition = parts[1].strip()
            if term and definition:  # Ensure both term and definition exist
                flashcards.append(f"{term}: {definition}")
    return "\n".join(flashcards)

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
            prompt = (
                f"Generate three flashcards in the format 'Term: Definition'."
                f" Each Term should be concise and represent a key concept from the following content."
                f" Each Definition should be short, clear, and directly explain the Term."
                f" Do not include any additional text, titles, special characters, or formatting outside the 'Term: Definition' structure."
                f"\n\n{content}"
            )
        else:
            return jsonify({"error": "Invalid question type provided"}), 400

        # Call OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use "gpt-4" if available for higher quality
            messages=[
                {"role": "system", "content": "You are a helpful assistant that generates educational content."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300
        )

        # Extract response
        raw_output = response['choices'][0]['message']['content'].strip()

        # Clean output for flashcards, if applicable
        if question_type == 'flashcards':
            clean_output = clean_flashcard_output(raw_output)
        else:
            clean_output = raw_output

        return jsonify({"questions": clean_output})

    except openai.error.OpenAIError as openai_error:
        # Handle OpenAI API-specific errors
        print(f"OpenAI API error: {openai_error}")
        return jsonify({"error": "Failed to fetch a response from OpenAI. Please try again later."}), 500
    except KeyError as key_error:
        # Handle unexpected response structure
        print(f"KeyError in OpenAI response: {key_error}")
        return jsonify({"error": "Unexpected response structure from OpenAI. Please try again later."}), 500
    except Exception as e:
        # Log unexpected errors for debugging
        print(f"Unhandled error: {e}")
        return jsonify({"error": "An unexpected error occurred. Please try again later."}), 500



if __name__ == '__main__':
    app.run(debug=True)
