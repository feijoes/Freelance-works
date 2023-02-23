with open('fail.txt','r') as f:
    with open('id.txt',  'w') as p:
        p.writelines(set(f.readlines()))
    