import config


# retrieve config.ini
c = config.getConfig()


def getId2Line():
	print('loading raw data')
	id2line = {}
	file_path = os.path.join(c.get('DATASET', 'DATA_PATH'), c.get('DATASET', 'DATA_FILE'))
	with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
        	# Example Line from cornell_corpus: L1045 +++$+++ u0 +++$+++ m0 +++$+++ BIANCA +++$+++ They do not!
            s = line.split(' +++$+++ ')
            if len(s) == 5:
                if s[4][-1] == '\n':
                    s[4] = s[4][:-1]
                id2line[s[0]] = s[4]
    return id2line



def load():
	getId2Line()