
import re_hadoop
ip = input('Enter Your IP : ')
file = open('hadoop_menu.html', 'w+')
file.write(re_hadoop.hadoop(ip))
file.close()
