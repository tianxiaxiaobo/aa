import json
import streamlit as st

def login():
    
    st.title('登录')
    st.write('如果没有账号，默认注册新账号')
    st.divider()
   
    user_name = st.text_input("名字")

    user_pwd = st.text_input('密码')
    
    user = {
            'name':user_name,
            'pwd':user_pwd
        }
    
    with open('users/userlist') as f:
        data = json.load(f)
        
        
    for i in data:
      
        if i.get('name')==''or i.get('name')==' ' :
            data.pop(i)
            if i['pwd']==' ' or i['pwd'] == '':
                data.pop(i)
            
        if i == user:
            return user_name
                
        else:
                
            with open('users/userlist', 'w') as f2:
                data.append(user)
                json.dump(data,f2)
            return user_name
            
            
    