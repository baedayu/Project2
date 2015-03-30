TEST_LIST_OF_SESSIONS = [['[1] Intro to serious programming',['We can do any computation by designing a program using programming language (like Python!) to make the computer do processing step by step and eventually accomplish the final goal.', 'The python interpreter reads and execute the program.', 'BE CAREFUL!! The program must exactly adhere to the strict grammatical rule. Unless "Syntax error" will appear. And the meaning of the programming language must be clear (interpreted in only one way), not ambiguous.' ]], ['[2] Variables and strings', ['We can assign a number or string into a variable by using "=". This puts the content on the right into the left.','Variables can be repeatly used and updated to a new value. Useful in loops and functions.', 'Strings are chain of characters or numbers. We can index, parcellate strings and find subcomponent strings. Useful in text mining.']], ['[3] Input-function-output', ['Function(procedure) allows us to store the repeating contents and call the function when needed, not writing the same codes over and over.', 'We can make functions. When needed, we call the function and give appropriate number of inputs then the output would be returned!' ]]]

EXAMPLE_LIST_OF_ITEMS1 = ['We can do any computation by designing a program using programming language (like Python!) to make the computer do processing step by step and eventually accomplish the final goal.', 'The python interpreter reads and execute the program.', 'BE CAREFUL!! The program must exactly adhere to the strict grammatical rule. Unless "Syntax error" will appear. And the meaning of the programming language must be clear (interpreted in only one way), not ambiguous.' ]
EXAMPLE_LIST_OF_ITEMS2 = ['We can assign a number or string into a variable by using "=". This puts the content on the right into the left.','Variables can be repeatly used and updated to a new value. Useful in loops and functions.', 'Strings are chain of characters or numbers. We can index, parcellate strings and find subcomponent strings. Useful in text mining.']
EXAMPLE_LIST_OF_ITEMS3 = ['Function(procedure) allows us to store the repeating contents and call the function when needed, not writing the same codes over and over.', 'We can make functions. When needed, we call the function and give appropriate number of inputs then the output would be returned!' ]

def make_item_HTML(list_of_items):
    HTML = ""
    for item in list_of_items:
        item_HTML = '<li>' + item + '</li>'
        HTML = HTML + '''
            ''' + item_HTML
    return HTML

def generate_des_HTML(list_of_items):
    html_text_1 = '''
    <div class="description">
        <ol> ''' + make_item_HTML(list_of_items)
    html_text_2 = '''
        </ol>
    </div>'''
    full_html_text = html_text_1 + html_text_2
    return full_html_text

def generate_session_HTML(session_title, list_of_items):
    html_text_1 = '''
<div class = "session">
    <div class = "session-title">
        ''' + session_title 
    html_text_2 = '''
    </div> ''' + generate_des_HTML(list_of_items)
    html_text_3 = '''
</div> '''
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def make_HTML(session):
    session_title = session[0]
    list_of_items = session[1]
    return generate_session_HTML(session_title, list_of_items)

def make_HTML_for_many_sessions(list_of_sessions):
    HTML = ""
    for session in list_of_sessions:
        session_HTML = make_HTML(session)
        HTML = HTML + session_HTML
    return HTML 


print make_item_HTML(EXAMPLE_LIST_OF_ITEMS1)
print generate_des_HTML(EXAMPLE_LIST_OF_ITEMS1)
print make_HTML_for_many_sessions(TEST_LIST_OF_SESSIONS)


