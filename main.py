import bs4, requests, random, sqlite3

# create table questions(
# 	id int primary key not null,
#   question text not null,
#   ans_a text not null,
#   ans_b text not null,
#   ans_c text not null,
#   ans_d text not null,
#   correct varchar(1) not null,
#   image text
#  );

def download_page():
    print('DLP >> Downloading page')
    url = "https://www.praktycznyegzamin.pl/inf03ee09e14/teoria/wszystko/"
    page = requests.get(url)
    print('DLP >> Page downloaded')
    return page.text

def parse_page(page):
    print('PP >> Parsing page')
    soup = bs4.BeautifulSoup(page, 'html.parser')
    print('PP >> Page parsed')
    return soup

def get_questions(soup):
    print('GQ >> Getting questions')
    questions = []
    # find all div's with class question
    for question in soup.find_all('div', class_='question'):
        # in div with class title within given div, find text (just text between tags <div>dsd</div>)
        question_text = question.find('div', class_='title').text
        question_id = int(random.randint(1000000, 9999999))
        # there are 4 answers, find all div's with class answer for given question, but one of them has class correct, so it would look like this "answer correct"
        answers = question.find_all('div', class_='answer')
        # loop through them and get 4 answers - THERE ARE ALWAYS 4 ANSWERS
        ans_a = answers[0].text[3:]
        ans_b = answers[1].text[3:]
        ans_c = answers[2].text[3:]
        ans_d = answers[3].text[3:]
        # find div with class correct and get text from it
        correct = question.find('div', class_='correct').text[0]
        # check if there is image inside in the question
        image = question.find('img')
        if image:
            image = "https://www.praktycznyegzamin.pl/inf03ee09e14/teoria/wszystko/" + image['src']
        else:
            image = None
        # append to questions list
        questions.append({
            'id': question_id,
            'question': question_text,
            'ans_a': ans_a,
            'ans_b': ans_b,
            'ans_c': ans_c,
            'ans_d': ans_d,
            'correct': correct,
            'image': image
        })
    print('GQ >> Questions gathered')
    return questions


# get questions and save them to json file.
questions = get_questions(parse_page(download_page()))
import json
with open('questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False)

# submit to database
conn = sqlite3.connect('data.db')
c = conn.cursor()
# insert questions to database
for question in questions:
    c.execute("INSERT INTO questions VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (question['id'], question['question'], question['ans_a'], question['ans_b'], question['ans_c'], question['ans_d'], question['correct'], question['image']))
    conn.commit()
    print('SQL >> Inserted question with id:', question['id'])
















