def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
    <div class="ls"
        <h3>
            <b>
            ''' + concept_title
    html_text_2 = '''
            </b>
        </h3>
    </div>
    <div class="notes">
        ''' + concept_description
    html_text_3 = '''
    </div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def get_title(concept):
    start_location = concept.find('TITLE:')
    end_location = concept.find('DESCRIPTION:')
    title = concept[start_location+7 : end_location-1]
    return title

def get_description(concept):
    start_location = concept.find('DESCRIPTION:')
    description = concept[start_location+13 :]
    return description

def get_concept_by_number(text, concept_number):
    counter = 0
    while counter < concept_number:
        counter = counter + 1
        next_concept_start = text.find('TITLE:')
        next_concept_end   = text.find('TITLE:', next_concept_start + 1)
        concept = text[next_concept_start:next_concept_end]
        text = text[next_concept_end:]
    return concept
        

TEST_TEXT = """TITLE: Program, Computer and Interpretar
DESCRIPTION: A program tells the computer what to do. It is a very precise sequence of steps. A Computer is a universal machine which has a few simple instructions that it can execute. It executes these instructions super fast. The combination computer and program can do any computation. A interpretar is a translater that translate your code into machine code and execute it directly on the computer
TITLE: Programming Languages and Phyton
DESCRIPTION: There are many programming languages. Our native language can't 
be used to create programme because it isn't as precise as a Phyton for ex. 
They are much stricter than speaking languages.
Phyton is a high-level programming language. Using Python the programmers can write instructions for computers in a way that the computer can understand 
TITLE: Grammar
DESCRIPTION: Every programming language has a grammar that defines what strings are in the language. Backus-Naur Form is a way to understand programming language grammar using the rules of English grammar. A Phyton expression is statement that follow the rules and the grammar of the Phyton language
TITLE: Variables. String and Number types of variables
DESCRIPTION: Variables are names which refer to values in a program. It is important to create assignment statement before use a variable. It looks like example_var = 'Udacity'. It has name followed by equal symbol followed by an expression. After it the name has the value that expression has.
String variables are surrounded by " " or ' '. It is very important to use the same sign as the start sign. The folowing examples aren't valid strings: 'first_example" or "second_exaple'. In Python, "2" is a string while 2 is a number. In Python 2 + 2 will give 4 while "2" + "2" will give "22". It looks strange but we can multiple string with number. For ex. "2" * 5 will give "22222". In addition, triple quotes creates a multi-line string.
TITLE: Differences between equal sign "=" in the math and the same in Python
DESCRIPTION: In math 2 + 2 = 4 but in Python "example = 4" means the variable takes the value of 4. After that it can take a value of 5 with statements like "example = 5" and so on.
TITLE: Using built in procedure "find" with strings. Indexing strings
DESCRIPTION: We can use "find" to see the position of the found sub-string in the string - str.find("str", number). The output will be a number refering to the position. If the found sub-string is not in the string, the output will be negative number -1. We can use parameter a number with "find" in order to skip any position of the found sub-string. String can be indexed which means to exctract subsequences from the string - str.index(start:end) . It starts from 0 when the number is possitive while when the number is negative it starts from the back side of the string.
TITLE: Making and Using functions
DESCRIPTION: A function or procedure is module of code that accomplish a specific task. There are built in functions and self made functions. Usually they take in data, process it and return result. After you make a function it can be used many times. A function can has many arguments as inputs. Once a function is created it can be called from other functions. You can use key word "def" to create a function. After the name there are parameters surrounded by parentheses. The code of the function is in the body. You should use "RETURN" statement in the body in order to get the output. Without this expression we will not get output. We can use the function when we write the name and use the values as parameters. We are able to write multi-line strings if we use triple quotes.
TITLE: Decisions using comparisons. If..else comparison
DESCRIPTION: In Python we can use math signs in order to do comparisons. It is allowed to use a less then and a greater then sign that compares 2 numbers. We have also a less then or equal and a greater then or equal. The output of a comparison is boolean value: It is either the value "True" or the value "False". The way to use IF statements is the keyword "IF" followed by a comparison followed by colon. We have the block inside the IF. The block is the code that will run when the comparison is true. When the comparison is false the code after else will be executed.
TITLE: Statements with OR and While Loop.
DESCRIPTION: "OR" gives a logical OR of the two operands as follow: True or False is True, True or True is also True, True or True is again True and False or False is False. While Loop is a way to do thing over and over again. It contains the keyword "While", followed by a test expression, followed by colon - while expression:block statement(s). Inside we have a block. We execute the code inside the block over and over agin until the test expression is False. We can interupt the While Loop with the keyword "Break". When the Break is true it goes out of the While Loop.
TITLE: Lists and Nested List. List Operations. Mutation and Aliasing. Index of a list.
DESCRIPTION: Lists are like strings but more powerful - ['obj1', 'obj2', 2014, 2015]. Whereas string has to be created from characters, lists contain any elements that we want. Nested List is a list which exists in a element of a list - [['obj11',2013], 'obj2', 2014, 2015]. A List supports MUTATION. It is the way that we can change the value of a list after we have created it. We can change some elements in the list. ALIASING is the way that two variables refer to one value. If we changes the second character in the value of the first variable it also change the value of the second variables. APPEND - list.append(obj) - with this method we can add a new element in a list. The result will be mutating of that list. 
Plus "+" - it is concatenation of two lists and it doesn't mutate - it creates a new lists. LEN - it is a operator that count the elements of the input - len(s). It works also with string, lists etc. The output is the lenght of the input data. Index method finds elements in a list and the output is the position of that element - list.index(s)
TITLE: Loop on a lists using FOR
DESCRIPTION: Using FOR is the way to loop in a list. The syntax is FOR followed by a name of element followed by IN and followed by the list name. After that is the block statement - for e in list: block statement """


def generate_all_html(text):
    current_concept_number = 1
    concept = get_concept_by_number(text, current_concept_number)
    all_html = ''
    while concept != '':
        title = get_title(concept)
        description = get_description(concept)
        concept_html = generate_concept_HTML(title, description)
        all_html = all_html + concept_html
        current_concept_number = current_concept_number + 1
        concept = get_concept_by_number(text, current_concept_number)
    return all_html


#print generate_all_html(TEST_TEXT)

html_head = '''<html>
    <head>
	    <meta charset="utf-8">
	    <link rel="stylesheet" type="text/css" href="Stage2.css">
	    <title>My web notes for STAGE 2</title>
    </head>
<body>
    <h1>Important notes in STAGE 2<br>Automate your code!</h1>
<div class="content">
'''

html_bottom = '''
</div>
</body>
</html>'''

print html_head + generate_all_html(TEST_TEXT) + html_bottom