#encoding=utf-8

import os
import random
import codecs

workspace = 'SogouC.reduced/Reduced'


def process_article(article_path):
	text = ''
	with codecs.open(article_path, 'r', 'gbk','ignore') as fin:
		for line in fin:
			line = line.strip()
			if len(line) > 0:
				text += line
	return text

def main():
	texts = []
	for file in os.listdir(workspace):
		sub_file = os.path.join(workspace, file)
		if not os.path.isdir(sub_file): continue
		files_num = len(os.listdir(sub_file))
		article_ids = set()
		while True:
			article_id = random.randint(10,files_num)
			article_ids.add(article_id)
			texts.append(process_article(sub_file + '/' + str(article_id) + '.txt'))
			if len(article_ids) == 1: break
		random.shuffle(texts)
	
	for index in range(len(texts)):
		print('article_' + str(index) + '\t' + texts[index])

if __name__ == '__main__':
	main()
