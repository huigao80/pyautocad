import sys
import jieba
import os
import jieba.analyse
reload(sys)
sys.setdefaultcoding('utf-8')

top_num = 30

soruce_dir = './result'
top_dir = './'
top_file = 'czh.txt'

def get_topic():
    print 'start process...'
    top_filename = os.path.join(top_dir,topfile)
    if os.path.exists(top_filename):
        print top_filename + 'exists!'
        os.remove(top_filename)
    file_write = file(top_filename,'w')
    
    for dirpaths,dirnames,files in os.walk(source_dir):
        for item in files:
            user_id = item.split('.')[0]
            file_name = os.path.join(source_dir,item)
            content = open(file_name,'r').read()
            tags = jieba.analyse.extract_tags(content,top_num)
            line = '用户' + user_id + '的关键词为:' +','.join(tags)
            file_write.writelines(line + '\n')
            
    print 'fininsed!'

if __name__ == '__main__':
    print 'go'
    get_topic()
