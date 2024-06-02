import quart, aiosqlite

app = quart.Quart(__name__)

@app.route('/')
async def hello():
    async with aiosqlite.connect('data.db') as db:
        async with db.execute('SELECT COUNT(*) FROM questions') as cursor:
            count = await cursor.fetchone()
    return {
        'code': 200,
        'message': 'API is running fine!',
        'questions': count[0]
    }

@app.route('/get')
async def get_questions():
    async with aiosqlite.connect('data.db') as db:
        async with db.execute('SELECT * FROM questions ORDER BY RANDOM() LIMIT 1') as cursor:
            question = await cursor.fetchone()
    return {
        'id': question[0],
        'question': question[1],
        'ans_a': question[2],
        'ans_b': question[3],
        'ans_c': question[4],
        'ans_d': question[5],
        'correct': question[6],
        'image': question[7]
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1101, debug=False)
