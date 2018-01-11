users=[]
with open('data.txt','r') as f:
   for line in f:
     user_fields=line.split(',')
     user={
         'email':user_fields[0],
         'first_name':user_fields[1],
         'last_name':user_fields[2]
     }
     users.append(user)

with open('users.txt','w') as f:
    for user in users:
        line='{},{},{}'.format(user['email'],user['first_name'], user['last_name'])
        f.writelines(line)