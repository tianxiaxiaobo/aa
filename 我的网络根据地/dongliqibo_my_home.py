import streamlit as st
import PIL
import PIL.Image as Image
import datetime,os
from login import login
import json

user = False
page = st.sidebar.radio('我的首页',['我的兴趣推荐','我的图片处理工具','我的智慧词典','我的留言区','前往帖子区','自拍','登录'])

def read():
    with open('says.json','r+',encoding='utf-8') as f:
        file = json.load(f)
        return file

def write(user):
    txt=st.text_area()
    with open('says.json','a',encoding='utf-8') as f:
        file = json.dump({'user':user,'string':txt},f)
        
def talking_page():
    if user == False:
        login()
    else:
        for i in file:
            st.title(i['user'])
            st.write(i['string'])
        if st.button('写贴'):
            txt=st.text_input('xie')
            if st.button('提交'):
                write(user)

def zipai():
    picture = st.camera_input("Take a picture")

    if picture:
         st.image(picture)
        
def loginpage():
    user=login()
    st.write('欢迎'+str(user))
    
def img_change(img,rc,gc,bc):
    width,height =img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            #获取RGB值
            r =img_array[x,y][rc]
            g=img_array[x,y][gc]
            b=img_array[x,y][bc]
            img_array[x,y]=(r,g,b)
    return img
    
def page_2():
    st.write(":film_frames:图片处理小程序:film_frames:")
    uploaded_file = st.file_uploader("上传图片",type=['png','jpeg','jpg' ])
    if uploaded_file:
        #获取图片文件的名称、类型和大小
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size =uploaded_file.size
        img =Image.open(uploaded_file)
        st.image(img)
        st.image(img_change(img,0,2,1))
        tab1,tab2,tab3,tab4= st.tabs(["原图","改色1","改色2","改色3"])
                                    
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img,0,2,1))
        with tab3 :
            st.image(img_change(img,1,2,0))
        with tab4:
            st.image(img_change(img,1,0,2))
        

def page_3():
    time = datetime.datetime.now()
    st.write('智慧词典')
    history_file = "data\history.json"
    
    
    #从本地文件中将词典信息读取出来，并存储在列表中
    with open('words_space.txt','r',encoding='utf-8')as f:
        words_list=f.read().split('\n')#将列表中的每一项内容再进行分割，分为“编号、单词、解释”
        
    for i in range(len(words_list)):
        words_list[i]= words_list[i].split('#')
        #导入字典，（单词：编号，解释）
        
    words_dict ={}
    for i in words_list:
        words_dict[i[1]]=[int(i[0]),i[2]]
    with open('check_out_times.txt',encoding='utf-8')as f:
        times_list = f.read().split('\n')#将列表转为字典]]]]]]]]]]]]]]]]]]]]]]
        for i in range(len(times_list)):
            times_list[i]= times_list[i].split('#')
        times_dict ={}
        for i in times_list:
            times_dict[int(i[0])]=int(i[1])#编号:次数 
    #输入
    word = st.text_input('请输入要查询的单词')
    
            
    if word in words_dict:
        n=words_dict[word][0]
        st.write(words_dict[word])
        #显示查询内容
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]#查找编号
        if n in times_dict:
            times_dict[n]+= 1
        else:
            times_dict[n] = 1
            
        with open('check_out_times.txt','w',encoding='utf-8')as f:
            message=''
            for k,v in times_dict.items():#k是编号，v是次数
                message +=str(k)+'#'+ str(v) + '\n'
            message =  message[:-1]
            f.write(message)
        st.write('查询次数:'+str(times_dict[n]))
        
        if word=='python' or word=='java':
            st.code('''#恭喜你触发彩蛋，这是一行python代码,
                    print('hello world')''')
            
    if word =='snow':
        st.snow()
    if word == 'birthday':
        st.balloons()


def page_4():
    
    
    st.write('我的留言区')
    #从文件中加载内容，并处理成列表
    with open('leave_messages.txt','r',encoding='utf-8') as f:
        messages_list=f.read().split('\n')
        for i in range(len(messages_list)):       
            messages_list[i] = messages_list[i].split('#')
        for i in messages_list:
            if i[1]=='阿短':
                with st.chat_message('星'):
                    st.write(i[1],':',i[2])
                
            elif i[1]=='编程猫':
                with st.chat_message('◎'):
                    st.write(i[1],':',i[2])#st.text(i[1]+':'+i[2])
        name = st.selectbox('我是.……',['阿短',"编程猫"])
        new_message = st.text_input('想要说的话..')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1),name, new_message])
        with open('leave messages.txt','w',encoding='utf-8') as f:
            
            for i in messages_list:
                message +=i[0]+'#'+ i[1]+'#'+i[2]+'\n'
                message = message[:-1]
                f.write(message)

def page_1():
    '''我的兴趣推荐'''
    with open('霞光.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
    st.image('slogan.png')
    st.write('我的电影推荐')
    st.write('《冰雪奇缘》')
    st.write('-----------------------------')
    st.write('我的游戏推荐')
    st.write('《弹丸论破》、《dota2》、《hitman》')
    st.image('mengma.png')
    st.write('dota2教学视频BV')
    st.write('BV1fw411b7j6')
    st.write('-----------------------------')
    st.write('我的书籍推荐')
    st.write('《我的奋斗》')
    st.image('wodefendou.png')
    st.write('-----------------------------')
    st.text('我的习题集推荐')
    st.write('无')
    st.write('-----------------------------')

    
if page == '我的兴趣推荐':
    
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智慧词典':
    page_3()
elif page == '我的留言区':
    
    page_4()
elif page=='前往发帖区':
    talking_page()
elif page=='自拍':
    zipai()
elif page == '登录':
    loginpage()

