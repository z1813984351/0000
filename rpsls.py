#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ��ż���
2020.5.9 
"""

import random


# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
   if name=='ʯͷ':
	   return 0
   elif name=='ʷ����':
	   return 1
   elif name=='ֽ':
	   return 2
   elif name=='����':
	   return 3
   elif name=='����':
	   return 4
   else:
       return 5

def number_to_name(number):
   if number==0:
       b='ʯͷ'
   elif number==1:
	   b='ʷ����'
   elif number==2:
	   b='ֽ'
   elif number==3:
	   b='����'
   else:
	   b='����'
   return b   
	   
	   
	   
	  
def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """
    print("����ѡ��Ϊ��",choice_name)
    pc = name_to_number(player_choice)
    computer_choice=random.randrange(0,4)
    cc = number_to_name(computer_choice)
    print("�������ѡ��Ϊ��",cc)
    d=computer_choice - int(pc)
    if d == 0:
	    print("���ͼ��������һ����")
    elif d == -1 or d == -2 or d ==3 or d ==4:
        print("��Ӯ�ˣ�")
    else:
	    print("����Ӯ�ˣ�")
    return 0

print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
if name_to_number(choice_name) == 5:
	print("No Correct Name!")
else:
    rpsls(choice_name)
