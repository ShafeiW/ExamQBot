# ExamQChatBot

Overview

The Exam Question Generator is a web application that leverages OpenAI's GPT models to generate educational content such as:

    Multiple Choice Questions (MCQs)
    Long Answer Questions
    Flashcards (Term and Definition format)

This tool is designed to help educators, students, and professionals quickly create learning materials based on custom input content.
Features

    Multiple Choice Questions:
        Generates multiple-choice questions with 4 answer options.
        Displays questions in a clean, professional layout with separate boxes for each question.
    Long Answer Questions:
        Generates in-depth, open-ended questions for detailed discussions.
    Flashcards:
        Generates term-definition flashcards for quick learning.
        Allows users to flip between terms and definitions interactively.
    Return to Home Button:
        Enables users to reset the application to its default state.

Technologies Used

    Frontend:
        HTML5, CSS3
        Bootstrap 5 for responsive design
        JavaScript (inline within index.html for frontend functionality)

    Backend:
        Python (Flask framework)
        OpenAI GPT-3.5/4 API for question generation
        Dotenv for managing environment variables

Setup Instructions
1. Clone the Repository

git clone https://github.com/your-username/exam-question-generator.git
cd exam-question-generator

2. Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

3. Install Dependencies

Manually install the required Python packages:

pip install flask python-dotenv openai

4. Set Up Environment Variables

Create a .env file in the project root directory and add your OpenAI API key:

OPENAI_API_KEY=your-openai-api-key

5. Run the Application

flask run

Visit http://127.0.0.1:5000 in your browser to use the app.
Usage

    Enter content in the input box.
    Select the question type:
        Multiple Choice Questions
        Long Answer Questions
        Flashcards
    Click "Generate" to create the desired educational material.
    Use the "Return to Home" button to reset the application.

Project Structure

exam-question-generator/
│
├── app.py                 # Flask backend
├── templates/
│   └── index.html         # Frontend HTML
├── static/
│   └── styles.css         # Custom CSS for the app
├── .env                   # Environment variables (not included in Git)
└── README.md              # Project documentation

Screenshots
Main Page

Generated Questions

Flashcards

Future Enhancements

    Add export functionality to download generated questions in PDF or Word format.
    Integrate user authentication to save and manage content.
    Add more customization options for generated questions (e.g., difficulty level, question count).

Contributing

Contributions are welcome! Please follow these steps:

    Fork the repository.
    Create a new branch for your feature/bug fix.
    Submit a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for details.
Contact

    Author: Your Name
    Email: your.email@example.com