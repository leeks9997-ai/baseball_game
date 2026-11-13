import random 

def make_answer() :
    return random.sample(range(1,10),3)

def check_input(text):
    if len(text) != 3 or not text.isdigit():
        return '세 자리 숫자를 입력하세요!'
    if not text.isdigit() :
        return '숫자만 입력하세요!'
    if '0' in text:
        return '0은 입력할 수 없습니다 (1~9 사이)'
    if len(set(text)) != 3:
        return '중복된 숫자는 입력할 수 없습니다'

    return ''

def to_number(text):
    nums=[]
    for ch in text:
        nums.append(int(ch))
    return nums

def count_strike(answer, guess):
    strike = 0
    for i in range(3):
        if guess[i] == answer[i]:
            strike += 1
    return strike

def count_ball(answer, guess):
    ball = 0
    for i in range(3):
        if guess[i] != answer[i] and guess[i] in answer :
            ball += 1
    return ball

def result_text(strike, ball):
    if strike == 0 and ball == 0:
        return "OUT"
    return f'{strike}S {ball}B'