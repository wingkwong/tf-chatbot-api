import config
import random
import os

# retrieve config.ini
c = config.getConfig()


def get_id2line():
    print('getting id2line dict')
    id2line = {}
    file_path = os.path.join(c.get('DATASET', 'DATA_PATH'), c.get('DATASET', 'DATA_LINE_FILE'))
    print(file_path)
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f.readlines():
            # Example Line from cornell_corpus: L1045 +++$+++ u0 +++$+++ m0 +++$+++ BIANCA +++$+++ They do not!
            s = line.split(' +++$+++ ')
            if len(s) == 5:
                if s[4][-1] == '\n':
                    s[4] = s[4][:-1]
                id2line[s[0]] = s[4]
        print('*********************')
        print('lines count: %d' % len(id2line))
        print('*********************')
    return id2line


def get_convs():
    print('getting conversations')
    file_path = os.path.join(c.get('DATASET', 'DATA_PATH'), c.get('DATASET', 'DATA_CONV_FILE'))
    convs = []
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f.readlines():
            # Example: u0 +++$+++ u2 +++$+++ m0 +++$+++ ['L194', 'L195', 'L196', 'L197']
            con = line.split(' +++$+++ ')
            if len(con) == 4:
                conv = []
                for line in con[3][1:-2].split(', '):
                    conv.append(line[1:-1])
                convs.append(conv)
        print('*********************')
        print('conversations count: %d' % len(convs))
        print('*********************')
    return convs


def get_questions_answers(id2line, convs):
    print('getting questions and answers')
    questions, answers = [], []
    # create sets for checking if q & a have already been added or not
    added_questions, added_answers = set(), set()
    duplicated = 0
    for conv in convs:
        for i, line in enumerate(conv[:-1]):
            # q: odd & a: even
            if not conv[i] in id2line or not conv[i+1] in id2line:
                continue
            question = id2line[conv[i]]
            answer = id2line[conv[i+1]]
            # skip duplicated cases
            if question in added_questions or answer in added_answers:
                duplicated += 1
                continue
            questions.append(question)
            added_questions.add(question)
            answers.append(answer)
            added_answers.add(answer)
    print('duplicated: ', duplicated)
    return questions, answers


def process(questions, answers):
    print('running process')
    # 2 encoders and 2 decoders for train and test
    files = ['test.enc', 'test.dec', 'train.enc', 'train.dec']
    # created a folder for storing them
    try:
        os.makedirs(c.get('PROCESSED', 'PROCESSED_PATH'))
    except OSError:
        print('PROCESSED_PATH EXISTS')
        pass
    # prepare to write each file to PROCESSED_PATH
    fs = []
    for file in files:
        fs.append(open(os.path.join(c.get('PROCESSED', 'PROCESSED_PATH'), file), 'w'))

    # choose TRAINING_SIZE sets as testing sets
    test_sets = random.sample([i for i in range(len(questions))], c.getint('DATASET', 'TRAINING_SIZE'))
    for i in range(len(questions)):
        if i in test_sets:
            # test set
            fs[0].write(questions[i] + '\n')
            fs[1].write(answers[i] + '\n')
        else:
            # train set
            fs[2].write(questions[i] + '\n')
            fs[2].write(answers[i] + '\n')
        if i % 10000 == 0:
            print('\n written {} lines'.format(i))

    for f in fs:
        f.close()


def create_vocab():
    print ('create vocab for train encoder and decoder')


def load():
    print('loading')
    id2line = get_id2line()
    convs = get_convs()
    questions, answers = get_questions_answers(id2line, convs)
    process(questions, answers)
    create_vocab()


if __name__ == '__main__':
    load()