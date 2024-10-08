# Programming Quiz Application


# ScreenShot
![Expense Tracker Screenshot](screenshots/screenshot.png)

## Demo Video
[Watch the demo video](https://youtu.be/Kmgu2mH9Fxo)



# Overview

This programming quiz app offers a comprehensive testing environment across multiple programming languages including Python, HTML, JavaScript, CSS, and MySQL. Each category features questions at three difficulty levels: Easy, Medium, and Hard. The application utilises a console-based interface to interact with users, presenting questions, capturing responses, and providing real-time feedback.

# Features

- Multi-Category Support: Users can select from multiple programming categories, each with tailored questions.
- Difficulty Levels: Each category includes three levels of difficulty, allowing users to test their knowledge depth.
- Immediate Feedback: Users receive immediate feedback after answering each question, including the correct answer if their response was incorrect.
- Score Tracking: Scores are tracked throughout the session, with a summary provided at the end.
- Leaderboard: A leaderboard displays top scores, showing the best performers across all sessions.
- Dynamic Flow: Users can choose to retake the quiz, switch categories, or adjust difficulty levels seamlessly.

# Key Functions

- display_welcome_message(): Introduces the quiz and its rules.
- select_category(): Allows users to choose the quiz category.
- select_difficulty(): Lets users set the difficulty level for the quiz.
- ask_question(): Manages the display of questions and collection of answers.
- calculate_score(): Computes the score based on correct responses.
- display_results(): Summarizes the quiz results, showing the user's performance.
- display_leaderboard(): Shows the top scores from all users.
- display_thank_you_message(): Concludes the quiz with a polite thank-you note.
- end_quiz(): Provides options to retake the quiz, change settings, or exit.

# Program Flow

- Initialization: Starts with a welcome message explaining the quiz format.
- Category Selection: Users select the programming language category.
- Difficulty Selection: Users choose the difficulty level.
- Quiz Interaction: The quiz cycles through the selected questions, capturing user inputs and providing feedback.
- Scoring and Results: After the last question, the score is displayed along with performance feedback.
- Post-Quiz Options: Users can opt to retry the quiz, change settings, view the leaderboard, or exit.
- Leaderboard Display: If chosen, the leaderboard is displayed, showing top performances.

# Running the Quiz

- To run the quiz, execute the run_quiz() function from the main module. The function initializes the quiz, handles session control, and manages user interactions throughout the quiz life cycle.

if **name** == "**main**":
run_quiz()

# Additional Notes

This quiz application is designed for educational purposes to help users assess and improve their programming knowledge across different languages and difficulty levels.

