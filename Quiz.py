import random
import time

# Define questions by category and difficulty
questions_by_category = {
    "Python": {
        "easy": [
            {"question": "What is the correct file extension for Python files?", "options": [".pyth", ".pt", ".py", ".p"], "correct": 3},
            {"question": "How do you insert comments in Python code?", "options": ["// This is a comment", "# This is a comment", "<!-- This is a comment -->", "/* This is a comment */"], "correct": 2},
            {"question": "Which data type is used to store a sequence of characters?", "options": ["int", "float", "str", "bool"], "correct": 3},
            {"question": "Which keyword is used to create a function in Python?", "options": ["function", "def", "fun", "define"], "correct": 2},
            {"question": "What is the output of the following code: `print(2 + 3 * 4)`?", "options": ["20", "14", "24", "None of the above"], "correct": 2},
            {"question": "Which of the following is a valid variable name in Python?", "options": ["1st_var", "first-var", "first_var", "first var"], "correct": 3},
            {"question": "What is the result of `5 // 2`?", "options": ["2", "2.5", "3", "3.5"], "correct": 1},
            {"question": "Which of the following operators is used for exponentiation in Python?", "options": ["^", "**", "^^", "*"], "correct": 2},
            {"question": "How do you convert a string to an integer in Python?", "options": ["int(str)", "str(int)", "convert(str)", "to_int(str)"], "correct": 1},
            {"question": "What does the `len()` function do?", "options": ["Calculate the length of a string or list", "Add elements to a list", "Remove elements from a list", "Find the maximum value"], "correct": 1}
        ],
        "medium": [
            {"question": "Which of the following is a mutable data type in Python?", "options": ["tuple", "list", "str", "int"], "correct": 2},
            {"question": "What is the output of `print('Python'[1])`?", "options": ["P", "y", "t", "h"], "correct": 2},
            {"question": "What is the result of `3 ** 2`?", "options": ["6", "9", "8", "12"], "correct": 2},
            {"question": "Which built-in function can be used to find the length of a list?", "options": ["length()", "size()", "len()", "count()"], "correct": 3},
            {"question": "What is the output of the following code snippet?\n`x = [1, 2, 3]\nprint(x[1:3])`", "options": ["[1, 2]", "[2, 3]", "[3]", "[1, 2, 3]"], "correct": 2},
            {"question": "What does the `append()` method do?", "options": ["Adds an element at the end of a list", "Removes an element from a list", "Sorts a list", "Reverses a list"], "correct": 1},
            {"question": "Which statement is used to stop a loop in Python?", "options": ["exit", "stop", "break", "halt"], "correct": 3},
            {"question": "What is the output of `print('Hello'.lower())`?", "options": ["HELLO", "hello", "Hello", "Error"], "correct": 2},
            {"question": "Which function is used to read input from the user?", "options": ["read()", "input()", "scan()", "get()"], "correct": 2},
            {"question": "Which of the following is a valid way to start a loop over a list?", "options": ["for i = 0; i < len(list); i++:", "for item in list:", "while item in list:", "each item in list"], "correct": 2}
        ],
        "hard": [
            {"question": "Which of the following statements is true about Python functions?", "options": ["Functions can only return one value", "Functions can have multiple return statements", "Functions cannot call other functions", "Functions are always named with a keyword"], "correct": 2},
            {"question": "How can you generate a random integer between 5 and 15 (inclusive) in Python?", "options": ["random(5, 15)", "random.randint(5, 15)", "random.range(5, 15)", "random.int(5, 15)"], "correct": 2},
            {"question": "What does the `continue` statement do in a loop?", "options": ["Exits the loop immediately", "Skips the rest of the loop block and starts the next iteration", "Skips to the end of the loop", "Restarts the loop from the beginning"], "correct": 2},
            {"question": "Which of the following is used to handle exceptions in Python?", "options": ["try-except", "if-else", "for-while", "throw-catch"], "correct": 1},
            {"question": "What is the output of `sorted([3, 1, 2], reverse=True)`?", "options": ["[1, 2, 3]", "[3, 2, 1]", "[2, 3, 1]", "[3, 1, 2]"], "correct": 2},
            {"question": "Which of the following decorators is used to define a static method in Python?", "options": ["@staticmethod", "@classmethod", "@staticmethods", "@classmethods"], "correct": 1},
            {"question": "What is the purpose of the `pass` statement?", "options": ["Exit a loop", "Skip the current iteration", "Do nothing and continue", "End a function"], "correct": 3},
            {"question": "Which method is called when an object is created in Python?", "options": ["__create__", "__init__", "__new__", "__start__"], "correct": 2},
            {"question": "What is the result of `list(map(lambda x: x*2, [1, 2, 3]))`?", "options": ["[1, 2, 3]", "[2, 4, 6]", "[3, 4, 5]", "[3, 5, 7]"], "correct": 2},
            {"question": "What is a key feature of dictionaries in Python?", "options": ["They maintain order by default", "They do not allow duplicate keys", "They allow duplicate keys", "They only store numeric keys"], "correct": 2}
        ]
    },
    "HTML": {
        "easy": [
            {"question": "What does HTML stand for?", "options": ["Hyper Text Markup Language", "Hyperlinks and Text Markup Language", "Home Tool Markup Language", "Hyper Tool Markup Language"], "correct": 1},
            {"question": "Which HTML element is used to define the title of a document?", "options": ["<title>", "<head>", "<meta>", "<link>"], "correct": 1},
            {"question": "Which HTML tag is used to define a paragraph?", "options": ["<p>", "<para>", "<pre>", "<pg>"], "correct": 1},
            {"question": "What is the correct HTML tag for inserting a line break?", "options": ["<br>", "<lb>", "<break>", "<hr>"], "correct": 1},
            {"question": "Which HTML element is used to create a hyperlink?", "options": ["<link>", "<a>", "<href>", "<url>"], "correct": 2},
            {"question": "How can you open a link in a new tab/browser window?", "options": ["<a href='url' target='_blank'>", "<a href='url' new>", "<a href='url' open>", "<a href='url' target='new'>"], "correct": 1},
            {"question": "Which HTML attribute is used to define inline styles?", "options": ["class", "style", "styles", "id"], "correct": 2},
            {"question": "Which HTML element is used to specify a header for a document or section?", "options": ["<header>", "<head>", "<section>", "<h1>"], "correct": 1},
            {"question": "Which HTML tag is used to define an internal style sheet?", "options": ["<style>", "<css>", "<script>", "<head>"], "correct": 1},
            {"question": "How do you create an ordered list in HTML?", "options": ["<ol>", "<ul>", "<list>", "<order>"], "correct": 1}
        ],
        "medium": [
            {"question": "What is the correct HTML for creating a checkbox?", "options": ["<input type='checkbox'>", "<checkbox>", "<input type='check'>", "<check>"], "correct": 1},
            {"question": "Which HTML attribute specifies an alternate text for an image?", "options": ["alt", "src", "title", "longdesc"], "correct": 1},
            {"question": "How do you add a background color in HTML?", "options": ["<body style='background-color:blue;'>", "<background>blue</background>", "<body bg='blue'>", "<background color='blue'>"], "correct": 1},
            {"question": "Which element is used for the largest heading?", "options": ["<h6>", "<heading>", "<h1>", "<head>"], "correct": 3},
            {"question": "Which HTML element defines navigation links?", "options": ["<nav>", "<navigate>", "<navbar>", "<navigation>"], "correct": 1},
            {"question": "What is the correct HTML for inserting an image?", "options": ["<img src='image.jpg' alt='MyImage'>", "<image src='image.jpg' alt='MyImage'>", "<img href='image.jpg'>", "<img alt='image.jpg'>"], "correct": 1},
            {"question": "Which tag is used to define an interactive field where users can enter data?", "options": ["<form>", "<input>", "<textarea>", "<label>"], "correct": 2},
            {"question": "Which tag is used to define a table in HTML?", "options": ["<table>", "<tbl>", "<tab>", "<td>"], "correct": 1},
            {"question": "Which tag is used to define a list item?", "options": ["<li>", "<list>", "<item>", "<lii>"], "correct": 1},
            {"question": "How do you specify a specific character encoding in HTML5?", "options": ["<meta charset='UTF-8'>", "<meta encoding='UTF-8'>", "<meta character='UTF-8'>", "<charset='UTF-8'>"], "correct": 1}
        ],
        "hard": [
            {"question": "What does the 'a' element's 'href' attribute do?", "options": ["Specifies the URL of the page the link goes to", "Specifies the anchor text of the link", "Specifies a reference to an image", "Specifies the alt text for an image"], "correct": 1},
            {"question": "What is the purpose of the 'blockquote' element in HTML?", "options": ["To display a long quotation", "To create a bold text", "To create a block of code", "To format text as italic"], "correct": 1},
            {"question": "What is the 'figure' element used for in HTML5?", "options": ["To group images and their captions", "To create a figure list", "To display numerical data", "To specify a figure format"], "correct": 1},
            {"question": "What does the 'data-' prefix in HTML attributes stand for?", "options": ["Custom data attributes", "HTML5 data attributes", "JavaScript data attributes", "CSS data attributes"], "correct": 1},
            {"question": "Which HTML element is used to specify a footer for a document or section?", "options": ["<footer>", "<foot>", "<bottom>", "<section>"], "correct": 1},
            {"question": "What does the 'aside' element represent in HTML5?", "options": ["Content aside from the page content", "The left side of a page", "The right side of a page", "A navigation section"], "correct": 1},
            {"question": "What is the purpose of the 'details' element in HTML5?", "options": ["To specify additional details the user can view or hide", "To create a bullet list", "To create a dropdown menu", "To add metadata to a document"], "correct": 1},
            {"question": "Which HTML element is used to represent the result of a calculation?", "options": ["<output>", "<result>", "<calc>", "<compute>"], "correct": 1},
            {"question": "Which HTML element defines a section in a document?", "options": ["<section>", "<div>", "<article>", "<span>"], "correct": 1},
            {"question": "What is the purpose of the 'canvas' element in HTML5?", "options": ["To draw graphics on a web page", "To create a canvas for painting", "To embed a video", "To create a text area"], "correct": 1}
        ]
    },
    "JavaScript": {
        "easy": [
            {"question": "What is the correct syntax for referring to an external script called 'script.js'?", "options": ["<script src='script.js'>", "<script href='script.js'>", "<script ref='script.js'>", "<script link='script.js'>"], "correct": 1},
            {"question": "How do you write 'Hello World' in an alert box?", "options": ["alertBox('Hello World');", "msg('Hello World');", "msgBox('Hello World');", "alert('Hello World');"], "correct": 4},
            {"question": "How do you create a function in JavaScript?", "options": ["function = myFunction()", "function:myFunction()", "function myFunction()", "createFunction myFunction()"], "correct": 3},
            {"question": "How do you call a function named 'myFunction'?", "options": ["myFunction()", "call function myFunction()", "call myFunction()", "execute myFunction()"], "correct": 1},
            {"question": "How do you write a conditional statement for executing some code if 'i' is equal to 5?", "options": ["if i = 5 then", "if i == 5 then", "if (i == 5)", "if i = 5"], "correct": 3},
            {"question": "How does a WHILE loop start?", "options": ["while i = 1 to 10", "while (i <= 10; i++)", "while (i <= 10)", "while (i++ <= 10)"], "correct": 3},
            {"question": "How does a FOR loop start?", "options": ["for i = 1 to 5", "for (i <= 5; i++)", "for (i = 0; i <= 5)", "for (i = 0; i <= 5; i++)"], "correct": 4},
            {"question": "What is the correct way to write a JavaScript array?", "options": ["var colors = 1 = ('red'), 2 = ('green'), 3 = ('blue')", "var colors = ['red', 'green', 'blue']", "var colors = 'red', 'green', 'blue'", "var colors = (1:'red', 2:'green', 3:'blue')"], "correct": 2},
            {"question": "How do you round the number 7.25 to the nearest integer?", "options": ["rnd(7.25)", "Math.round(7.25)", "Math.rnd(7.25)", "round(7.25)"], "correct": 2},
            {"question": "How do you find the number with the highest value of x and y?", "options": ["Math.max(x, y)", "Math.ceil(x, y)", "top(x, y)", "ceil(x, y)"], "correct": 1}
        ],
        "medium": [
            {"question": "Which operator is used to assign a value to a variable?", "options": ["*", "=", "-", "+"], "correct": 2},
            {"question": "What will the following code return: Boolean(10 > 9)?", "options": ["true", "false", "NaN", "undefined"], "correct": 1},
            {"question": "How can you add a comment in JavaScript?", "options": ["'This is a comment", "// This is a comment", "<!-- This is a comment -->", "** This is a comment"], "correct": 2},
            {"question": "Which event occurs when the user clicks on an HTML element?", "options": ["onchange", "onmouseover", "onclick", "onmouseclick"], "correct": 3},
            {"question": "How do you declare a JavaScript variable?", "options": ["variable carName;", "var carName;", "v carName;", "variable: carName;"], "correct": 2},
            {"question": "Which method can be used to find the length of a string?", "options": ["length()", "getSize()", "size()", "index()"], "correct": 1},
            {"question": "Which method converts a JSON object into a string?", "options": ["JSON.stringify()", "JSON.parse()", "JSON.objectify()", "JSON.convert()"], "correct": 1},
            {"question": "How do you write a comment that has more than one line?", "options": ["// This comment has\n// more than one line", "/* This comment has\nmore than one line */", "<!-- This comment has\nmore than one line -->", "** This comment has\nmore than one line **"], "correct": 2},
            {"question": "Which method is used to access HTML elements using JavaScript?", "options": ["getElementById()", "getElementsByClassName()", "Both getElementById() and getElementsByClassName()", "None of the above"], "correct": 3},
            {"question": "How do you write a JavaScript function that loops through an array?", "options": ["forEach()", "loop()", "each()", "None of the above"], "correct": 1}
        ],
        "hard": [
            {"question": "What is the purpose of the 'this' keyword in JavaScript?", "options": ["Refers to the current object", "Refers to the previous object", "Refers to the global object", "Refers to the new object"], "correct": 1},
            {"question": "What will the following code output?\nconsole.log(typeof NaN);", "options": ["'number'", "'string'", "'NaN'", "'undefined'"], "correct": 1},
            {"question": "What is the correct way to write a JavaScript object?", "options": ["var person = {firstName:'John', lastName:'Doe'};", "var person = (firstName:'John', lastName:'Doe');", "var person = (firstName='John', lastName='Doe');", "var person = {firstName='John', lastName='Doe'};"], "correct": 1},
            {"question": "How do you create a function that receives a function as a parameter?", "options": ["function myFunction(callback) {}", "function myFunction = function(callback) {}", "var myFunction = function(callback) {}", "myFunction: function(callback) {}"], "correct": 1},
            {"question": "Which function can be used to call a function repeatedly with a fixed time delay between each call?", "options": ["setTimeout()", "setInterval()", "setRepeat()", "setLoop()"], "correct": 2},
            {"question": "How do you create a class in JavaScript?", "options": ["class Car {constructor() {}}", "function Car() {}", "var Car = class {}", "Car() => {}"], "correct": 1},
            {"question": "What will the following code output?\nconsole.log(1 + '1');", "options": ["'2'", "'11'", "2", "11"], "correct": 2},
            {"question": "What is the 'spread' operator in JavaScript?", "options": ["...", "<>", "[]", "{}"], "correct": 1},
            {"question": "Which method is used to serialize an object into a JSON string in JavaScript?", "options": ["JSON.stringify()", "JSON.parse()", "JSON.toString()", "JSON.convert()"], "correct": 1},
            {"question": "Which of the following is a valid way to define a method in a JavaScript class?", "options": ["method() {}", "function method() {}", "method = function() {}", "var method = function() {}"], "correct": 1}
        ]
    },
    "CSS": {
        "easy": [
            {"question": "What does CSS stand for?", "options": ["Cascading Style Sheets", "Creative Style Sheets", "Colorful Style Sheets", "Computer Style Sheets"], "correct": 1},
            {"question": "Which property is used to change the background color?", "options": ["background-color", "bgcolor", "color", "bg-color"], "correct": 1},
            {"question": "Which property is used to change the text color of an element?", "options": ["text-color", "color", "font-color", "font-color"], "correct": 2},
            {"question": "Which CSS property is used to change the text size?", "options": ["text-size", "font-size", "font-weight", "text-style"], "correct": 2},
            {"question": "Which CSS property is used to change the font of an element?", "options": ["font-weight", "font-style", "font-family", "font-text"], "correct": 3},
            {"question": "Which property is used to specify the space between the border and the content of an element?", "options": ["margin", "padding", "border-spacing", "border"], "correct": 2},
            {"question": "Which CSS property is used to make text bold?", "options": ["text-decoration", "font-weight", "text-style", "font-bold"], "correct": 2},
            {"question": "Which CSS property is used to change the left margin of an element?", "options": ["margin-left", "left-margin", "padding-left", "margin-left-padding"], "correct": 1},
            {"question": "Which CSS property is used to change the width of an element?", "options": ["width", "length", "height", "size"], "correct": 1},
            {"question": "Which CSS property is used to change the height of an element?", "options": ["height", "length", "width", "size"], "correct": 1}
        ],
        "medium": [
            {"question": "Which CSS property is used to control the text alignment?", "options": ["text-align", "align", "text-align", "align-text"], "correct": 1},
            {"question": "Which property is used to control the spacing between letters?", "options": ["letter-spacing", "spacing", "word-spacing", "text-spacing"], "correct": 1},
            {"question": "Which property is used to control the spacing between lines?", "options": ["line-spacing", "line-height", "line-width", "line-size"], "correct": 2},
            {"question": "Which CSS property is used to hide an element?", "options": ["visibility", "display", "hide", "none"], "correct": 2},
            {"question": "Which CSS property is used to display an element as a block element?", "options": ["display: block", "display: inline", "display: inline-block", "display: none"], "correct": 1},
            {"question": "Which CSS property is used to create space between elements?", "options": ["padding", "margin", "border", "spacing"], "correct": 2},
            {"question": "Which CSS property is used to add a shadow to an element?", "options": ["box-shadow", "shadow", "border-shadow", "element-shadow"], "correct": 1},
            {"question": "Which CSS property is used to set the opacity of an element?", "options": ["visibility", "display", "opacity", "transparency"], "correct": 3},
            {"question": "Which property is used to specify the width of an element's border?", "options": ["border-width", "border-size", "border-height", "border-style"], "correct": 1},
            {"question": "Which property is used to specify the color of an element's border?", "options": ["border-color", "border-style", "border-width", "border-size"], "correct": 1}
        ],
        "hard": [
            {"question": "Which property is used to specify the top margin of an element?", "options": ["margin-top", "top-margin", "padding-top", "top-padding"], "correct": 1},
            {"question": "Which property is used to specify the bottom margin of an element?", "options": ["margin-bottom", "bottom-margin", "padding-bottom", "bottom-padding"], "correct": 1},
            {"question": "Which CSS property is used to specify the left padding of an element?", "options": ["padding-left", "left-padding", "margin-left", "left-margin"], "correct": 1},
            {"question": "Which CSS property is used to specify the right padding of an element?", "options": ["padding-right", "right-padding", "margin-right", "right-margin"], "correct": 1},
            {"question": "Which CSS property is used to specify the background image of an element?", "options": ["background-image", "background", "background-img", "img-background"], "correct": 1},
            {"question": "Which CSS property is used to specify the position of a background image?", "options": ["background-position", "position", "background-location", "location"], "correct": 1},
            {"question": "Which CSS property is used to repeat a background image?", "options": ["background-repeat", "repeat-background", "repeat", "background"], "correct": 1},
            {"question": "Which CSS property is used to specify the size of a background image?", "options": ["background-size", "size", "background", "img-size"], "correct": 1},
            {"question": "Which CSS property is used to specify the position of an element?", "options": ["position", "location", "top", "left"], "correct": 1},
            {"question": "Which CSS property is used to specify the z-index of an element?", "options": ["z-index", "index", "z", "layer"], "correct": 1}
        ]
    },
    "MySQL": {
        "easy": [
            {"question": "What does SQL stand for?", "options": ["Structured Query Language", "Structured Question Language", "Structured Quest Language", "Structured Query Logic"], "correct": 1},
            {"question": "Which SQL statement is used to extract data from a database?", "options": ["GET", "OPEN", "EXTRACT", "SELECT"], "correct": 4},
            {"question": "Which SQL statement is used to update data in a database?", "options": ["SAVE", "UPDATE", "MODIFY", "CHANGE"], "correct": 2},
            {"question": "Which SQL statement is used to delete data from a database?", "options": ["REMOVE", "DELETE", "DROP", "CLEAN"], "correct": 2},
            {"question": "Which SQL statement is used to insert new data into a database?", "options": ["ADD", "INSERT", "CREATE", "NEW"], "correct": 2},
            {"question": "Which SQL clause is used to filter records?", "options": ["WHERE", "IF", "WITH", "FILTER"], "correct": 1},
            {"question": "Which SQL keyword is used to sort the result-set?", "options": ["SORT BY", "ORDER BY", "GROUP BY", "ARRANGE BY"], "correct": 2},
            {"question": "Which SQL statement is used to create a new table in a database?", "options": ["MAKE TABLE", "NEW TABLE", "CREATE TABLE", "TABLE NEW"], "correct": 3},
            {"question": "Which SQL statement is used to modify the structure of a table?", "options": ["MODIFY TABLE", "CHANGE TABLE", "ALTER TABLE", "EDIT TABLE"], "correct": 3},
            {"question": "Which SQL statement is used to remove a table from a database?", "options": ["DELETE TABLE", "DROP TABLE", "REMOVE TABLE", "CLEAR TABLE"], "correct": 2}
        ],
        "medium": [
            {"question": "Which function is used to count the number of rows in SQL?", "options": ["COUNT()", "SUM()", "ADD()", "TOTAL()"], "correct": 1},
            {"question": "Which SQL keyword is used to retrieve unique records?", "options": ["ONLY", "DISTINCT", "UNIQUE", "DIFFERENT"], "correct": 2},
            {"question": "Which SQL clause is used to limit the number of records returned?", "options": ["TOP", "LIMIT", "MAX", "MIN"], "correct": 2},
            {"question": "Which SQL statement is used to return a stored procedure?", "options": ["GET PROCEDURE", "RETURN PROCEDURE", "CALL PROCEDURE", "FETCH PROCEDURE"], "correct": 3},
            {"question": "Which SQL function is used to return the current date?", "options": ["GETDATE()", "NOW()", "CURRENTDATE()", "TODAY()"], "correct": 2},
            {"question": "Which SQL statement is used to return the average value of a numeric column?", "options": ["TOTAL()", "AVERAGE()", "MEAN()", "AVG()"], "correct": 4},
            {"question": "Which SQL statement is used to return the highest value of a numeric column?", "options": ["HIGHEST()", "MAX()", "TOP()", "BIGGEST()"], "correct": 2},
            {"question": "Which SQL statement is used to add a column to a table?", "options": ["ADD COLUMN", "INSERT COLUMN", "NEW COLUMN", "ALTER TABLE"], "correct": 4},
            {"question": "Which SQL clause is used to group rows that have the same values?", "options": ["GROUP BY", "CLUSTER BY", "SORT BY", "COLLECT BY"], "correct": 1},
            {"question": "Which SQL function is used to concatenate two strings?", "options": ["CONCAT()", "APPEND()", "JOIN()", "MERGE()"], "correct": 1}
        ],
        "hard": [
            {"question": "Which SQL clause is used to filter groups of rows?", "options": ["GROUP BY", "WHERE", "HAVING", "FILTER"], "correct": 3},
            {"question": "Which SQL statement is used to return the number of rows affected by a query?", "options": ["ROW COUNT", "AFFECTED ROWS", "ROW TOTAL", "ROW COUNT"], "correct": 2},
            {"question": "Which SQL clause is used to create a link between tables?", "options": ["CONNECT", "JOIN", "LINK", "ASSOCIATE"], "correct": 2},
            {"question": "Which SQL function is used to replace all occurrences of a substring in a string?", "options": ["REPLACE()", "SUBSTITUTE()", "CHANGE()", "ALTER()"], "correct": 1},
            {"question": "Which SQL statement is used to create an index on a table?", "options": ["ADD INDEX", "MAKE INDEX", "CREATE INDEX", "NEW INDEX"], "correct": 3},
            {"question": "Which SQL clause is used to specify conditions on a query?", "options": ["IF", "WHERE", "WHEN", "FILTER"], "correct": 2},
            {"question": "Which SQL statement is used to remove duplicates from a result set?", "options": ["REMOVE DUPLICATES", "DISTINCT", "UNIQUE", "CLEAN"], "correct": 2},
            {"question": "Which SQL function is used to find the remainder of a division?", "options": ["MOD()", "REMAINDER()", "DIV()", "LEFTOVER()"], "correct": 1},
            {"question": "Which SQL statement is used to change the data type of a column?", "options": ["MODIFY COLUMN", "CHANGE COLUMN", "ALTER COLUMN", "UPDATE COLUMN"], "correct": 3},
            {"question": "Which SQL statement is used to return a substring of a string?", "options": ["SUBSTRING()", "SLICE()", "CUT()", "DIVIDE()"], "correct": 1}
        ]
    }
}

leaderboard = []  # List to store leaderboard data

def display_welcome_message():
    print("Welcome to the Programming Quiz!")
    print("You will be presented with multiple-choice questions.")
    print("Please select the correct answer by entering the corresponding number.\n")

def select_category():
    print("Select a category:")
    for index, category in enumerate(questions_by_category.keys(), start=1):
        print(f"{index}. {category}")
    
    while True:
        try:
            choice = int(input("Enter your choice: "))
            categories = list(questions_by_category.keys())
            if 1 <= choice <= len(categories):
                return categories[choice - 1]
            else:
                print("Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def select_difficulty(category):
    print("Select the difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    
    difficulties = ["easy", "medium", "hard"]  # Maintaining a list of difficulty levels

    while True:
        try:
            choice = int(input("Enter your choice (1-3): "))
            if 1 <= choice <= 3:
                difficulty = difficulties[choice - 1]
                return difficulty, questions_by_category[category][difficulty]  # Ensure this returns two values
            else:
                print("Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")


def ask_question(question_data):
    print(question_data["question"])
    for i, option in enumerate(question_data["options"], 1):
        print(f"{i}. {option}")
    
    while True:
        try:
            answer = int(input("Your answer (1-4): "))
            if 1 <= answer <= 4:
                if answer == question_data["correct"]:
                    print("Correct!\n")
                else:
                    print(f"Incorrect. The correct answer is {question_data['options'][question_data['correct'] - 1]}.\n")
                return answer
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

def calculate_score(user_answers, questions):
    score = 0
    for user_answer, question in zip(user_answers, questions):
        if user_answer == question["correct"]:
            score += 1
    return score

def display_results(score, total_questions, time_taken):
    print(f"\nYour total score is {score} out of {total_questions}.")
    print(f"Time taken: {time_taken:.2f} seconds.")
    if score == total_questions:
        print("Excellent! You got all the answers correct!")
    elif score >= total_questions / 2:
        print("Good job! You have a good understanding of the material.")
    else:
        print("Keep practicing! You'll get better with more practice.")

def display_thank_you_message():
    print("\nThank you for taking the quiz! We hope you learned something new.")

def end_quiz():
    while True:
        print("\nWhat would you like to do next?")
        print("1. Retake the quiz with the same category and difficulty level")
        print("2. Choose a different category or difficulty level")
        print("3. View Leaderboard")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice == 1:
                return "retake"
            elif choice == 2:
                return "new"
            elif choice == 3:
                return "leaderboard"
            elif choice == 4:
                print("Goodbye!")
                return "exit"
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

def display_leaderboard():
    print("\nLeaderboard:")
    sorted_leaderboard = sorted(leaderboard, key=lambda x: (-x['score'], x['time']))  # Sort by score and time
    for entry in sorted_leaderboard[:5]:  # Display top 5 scores
        print(f"{entry['name']} - Score: {entry['score']}, Time: {entry['time']:.2f} seconds, Category: {entry['category']}, Difficulty: {entry['difficulty']}")

    print("\nPress any key to return to the main menu...")
    input()  # Wait for user input to return to the main menu



def run_quiz():
    while True:
        display_welcome_message()
        name = input("Enter your name: ")
        category = select_category()
        difficulty, questions = select_difficulty(category)  # Unpacking the returned values
        
        random.shuffle(questions)  # Randomize question order
        
        user_answers = []
        start_time = time.time()  # Record the start time
        for question in questions:
            user_answer = ask_question(question)
            user_answers.append(user_answer)
        end_time = time.time()  # Record the end time

        score = calculate_score(user_answers, questions)
        time_taken = end_time - start_time  # Calculate the duration
        display_results(score, len(questions), time_taken)
        leaderboard.append({
            "name": name, 
            "score": score, 
            "time": time_taken,
            "category": category,
            "difficulty": difficulty
        })  # Add score and time to leaderboard

        display_thank_you_message()

        action = end_quiz()
        if action == "new":
            continue  # Start over with new category or difficulty
        elif action == "leaderboard":
            display_leaderboard()
            continue  # Return to the main menu after viewing the leaderboard
        elif action == "exit":
            break  # Exit the quiz loop



if __name__ == "__main__":
    run_quiz()
