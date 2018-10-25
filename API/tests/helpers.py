import json

""" variables """
add_question_url = '/api/v1/questions'
get_questions_url = '/api/v1/questions'
get_question_url = '/api/v1/questions/1'
add_answer_url = '/api/v1/questions/1/answers'
delete_question_url = '/api/v1/questions/1'
get_answers_url = '/api/v1/answers'
get_comments_url = '/api/v1/comments'
add_question_comment_url = '/api/v1/questions/1/comments'
add_answer_comment_url = '/api/v1/answers/1/comments'
add_register_user_url = '/api/v1/auth/signup'
add_login_url = '/api/v1/auth/login'
update_answer_url = '/api/v1/questions/1/answers/1'
accept_answer_url = '/api/v1/questions/1/answers/1'

test_question = {
    "title": "Stop over bleeding artery",
    "body": "I've found someone over bleeding from an accident. I think it's his arteries..."
}
test_answer = {
    "body": "Just stitch it up and use a guaze"
}
test_answer_comment = {
    "body": "Great answer, will try that myself"
}
test_question_comment = {
    "body": "Great question, I'll be waiting for the answers"
}
update_answer_data = {
	"action": "update",
	"body": "Great question, I'll be waiting for the answers"
}
accept_answer_data = {
	"action": "accept"
}
correct_user = {
    'username':'geneowak',
    'password':'helloWorld22',
    'email':'helloWorld@uganda.com'
}
correct_user2 = {
    'username':'geneowak2',
    'password': 'helloWorld222',
    'email': 'helloWorld@uganda2.com'
}

def add_test_user(client):
    return client.post(add_register_user_url, data=correct_user)


def get_auth_token(client):
    request = client.post(add_login_url, data=correct_user)
    if request.status_code != 200:
        raise Exception("failed to authenticate user")
    response = json.loads(request.data.decode())                                                    
    return response['access_token']


def auth_header(token):
    return{
        'authorization': "Bearer {}".format(token)
    }


def login(client, username, password, email):
    return client.post(add_login_url, data={"username":username, "password":password})


def sign_up(client, username, password, email):
    return client.post(add_register_user_url, data={"username": username, "password": password, "email": email})


def add_question(client, token, question):
    return client.post(add_question_url, data=question, headers=auth_header(token))


def get_question(client):
    return client.get(get_question_url)


def get_questions(client):
    return client.get(get_questions_url)


def delete_question(client, token):
    return client.delete(delete_question_url, headers=auth_header(token))


def add_answer(client, token, answer):
    return client.post(add_answer_url, data=answer, headers=auth_header(token))


def update_answer(client, token, data):
    return client.put(update_answer_url, data=data, headers=auth_header(token))


def accept_answer(client, token, data):
    return client.put(accept_answer_url, data=data, headers=auth_header(token))




