import config


# retrieve config.ini
c = config.getConfig()


def get_id2line():
	print('getting id2line dict')
	id2line = {}
	file_path = os.path.join(c.get('DATASET', 'DATA_PATH'), c.get('DATASET', 'DATA_FILE'))
	with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f.readlines():
        	# Example Line from cornell_corpus: L1045 +++$+++ u0 +++$+++ m0 +++$+++ BIANCA +++$+++ They do not!
            s = line.split(' +++$+++ ')
            if len(s) == 5:
                if s[4][-1] == '\n':
                    s[4] = s[4][:-1]
                id2line[s[0]] = s[4]
    return id2line


def get_convs():
	print('getting conversations')
	file_path = os.path.join(c.get('DATASET', 'DATA_PATH'), c.get('DATASET', 'DATA_FILE'))
    convs = []
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f.readlines():
			# Example: u0 +++$+++ u2 +++$+++ m0 +++$+++ ['L194', 'L195', 'L196', 'L197']
            parts = line.split(' +++$+++ ')
            if len(parts) == 4:
                conv = []
                for line in parts[3][1:-2].split(', '):
                    conv.append(line[1:-1])
                convs.append(conv)
    return convs


def load():
	id2line = get_id2line()
	convs = get_convs()
