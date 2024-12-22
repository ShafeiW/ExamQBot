# ExamQChatBot

### **Overview**
The **Exam Question Generator** is a web application that leverages OpenAI's GPT models to generate educational content such as:
- Multiple Choice Questions (MCQs)
- Long Answer Questions
- Flashcards (Term and Definition format)

This tool is designed to help educators, students, and professionals quickly create learning materials based on custom input content.

---

## **Features**
- **Multiple Choice Questions**:
  - Generates multiple-choice questions with 4 answer options.
  - Displays questions in a clean, professional layout with separate boxes for each question.
- **Long Answer Questions**:
  - Generates in-depth, open-ended questions for detailed discussions.
- **Flashcards**:
  - Generates term-definition flashcards for quick learning.
  - Allows users to flip between terms and definitions interactively.
- **Return to Home Button**:
  - Enables users to reset the application to its default state.

---

## **Technologies Used**
- **Frontend**:
  - HTML5, CSS3
  - Bootstrap 5 for responsive design
  - JavaScript (inline within `index.html` for frontend functionality)

- **Backend**:
  - Python (Flask framework)
  - OpenAI GPT-3.5/4 API for question generation
  - Dotenv for managing environment variables

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/exam-question-generator.git
cd exam-question-generator
```

### **2. Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```


### **3. Install Dependencies**
Manually install the required Python packages:
```bash
pip install flask python-dotenv openai
```

### **4. Set Up Environment Variables**
Create a .env file in the project root directory and add your OpenAI API key:
```bash
OPENAI_API_KEY=your-openai-api-key
```

### **5. Run the Application**
```bash
flask run
```

