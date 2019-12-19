from flask import Flask, escape, request, render_template

import random

app = Flask(__name__)

@app.route('/') #여기로 요청을 보냄
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'# 어퍼스트로피 문제 해결

@app.route('/hi')
def hi():
    name ="강규현"
    return render_template('hi.html',  html_name= name)
# html_name을 hi.html에 포함시켜 렌더하라

@app.route('/greeting/<string:name>')
def greeting(name) : 
    def_name = name
    return render_template('greeting.html', html_name= def_name)


@app.route('/cube/<int:num>')
def cube(num):
    def_num = num
    cube_num = num**3
    return render_template('cube.html', cube_num = cube_num, html_num = def_num)


@app.route('/fstring')
def fstring():
    fstring ="강규현"
    name = "강동주"
    return f"제 이름은 {fstring} {name}입니다."

@app.route('/dinner')
def dinner() :
    menu =['삼각김밥','컵라면','스테이크','마라탕','훠궈']
    dinner = random.choice(menu)
    menu_image={ '삼각김밥':'https://ppss.kr/wp-content/uploads/2017/12/%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C-7-1.jpg',
    '컵라면': 'https://cdn.crowdpic.net/detail-thumb/thumb_d_378BA60B966894DC61DCEC443E424FA3.jpg',
    '스테이크' : 'http://www.hotelavia.net/news/photo/201612/1085_2119_3512.jpg',
    '마라탕' : 'https://img.ssfshop.com/cmd/LB_500x660/src/https://img.ssfshop.com/goods/ORBR/19/06/25/GPAQ19062509070_0_ORGINL.jpg',
    '훠궈' : 'https://funshop.akamaized.net//products/0000062075/vs_image800.jpg?1576755600'}       
    img_url =menu_image[dinner]
    return render_template('dinner.html', dinner=dinner, img_url=img_url)


@app.route('/movies')
def movies():
    movies= ['조커','겨울왕국2','터미네이터','어벤져스']
    return render_template('movies.html', movies1 = movies)


# @app.route('/cube/<int:num>')
# def cube(num):



if __name__=="__main__":
    app.run(debug=True)