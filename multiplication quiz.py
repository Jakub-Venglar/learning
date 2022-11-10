import pyinputplus as pyip
import random, time

numOfQuestions = 3
asked = 0
correctAnswers = 0

for questionNumber in range(numOfQuestions):
    num1= random.randint(0,9)
    num2= random.randint(0,9)
    prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)
    asked += 1
    try:
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1*num2)],
                            blockRegexes=[('.*', 'Incorrect')],
                            timeout = 8, limit = 3)
    except pyip.TimeoutException:
        print('nestihls to')
    except pyip.RetryLimitException:
        print('jsi marny')
    else:
        print('pasak')
        correctAnswers += 1
    time.sleep(1)
    print('Correct %s / %s' % (correctAnswers, asked))

print('konec qizu')