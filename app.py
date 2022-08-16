#Created by : Aswin KS
import argparse
import random
from flask import Flask
from pywebio import *
from pywebio.output import *
from pywebio.input import *
import  time
from pywebio.platform.flask import webio_view
from pywebio.session import run_js, set_env


#Creating  a flask app
app=Flask(__name__)

def main():
    set_env(title="PassGen")
    def generatepass(x,length):
        length=length

        total=""

        # Creating valid data range
        upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower_case = upper_case.lower()
        numbers = "0123456789"
        symbols = "!@#$%^&*()><."

        if 'Uppercase' in x:
                total+=upper_case
        if 'Lowercase' in x:
              total += lower_case

        if 'Numbers' in x:
            total += numbers

        if 'Symbols' in x:
            total += symbols


        if length > len(total):
            total = total * 4


        # Generating the password
        for i in range(length):


            passwd = "".join(random.sample(total, length))

        return (passwd)

    put_html(r"""<h1  align="center"><strong>PassGen-Complex Password Generator</strong></h1>""")
    img = open('logo.png', 'rb').read()  # logo
    put_image(img, width='100px')  # size of image

    x = checkbox('Customize your password', options=['Uppercase', 'Lowercase', 'Numbers', 'Symbols'], inline=True),


    if x[0]==[] :
        popup("Data Required!",[
              "Choose one option to generate password\n\n"
              "Numbers, ",
              'Symbols, ',
              'Lowercase, ',
              'Uppercase.',


        ])
        time.sleep(2)
        run_js('window.location.reload()')

    else:


        x = str(x)


        #length
        val=slider(label='Choose Password length', name=None, value=0, min_value=8, max_value=35, step=1, validate=None,required=True)
        length = int(val)
        password=generatepass(x,length)

        put_html(r"""<h3  align="center"><strong>Password Generated</strong></h3>""")

        put_processbar('bar')
        for i in range(1, 3):
            set_processbar('bar', i / 2)
            time.sleep(0.2)





        def btn_click(btn_val):
            if btn_val == 'Home':
                run_js('window.location.reload()')
            elif btn_val == "About":
                popup("About",
                      [put_html('<h2>Created by Aswin Ks</h2>'),
                       put_html('<h3>This Project is created using Python, Pywebio and Flask</h3>'),
                       'Find More @ https://github.com/aswinks1995',
                       ]

                      )
            elif btn_val=='Copy to Clipboard':
                #pyperclip.copy(password)   #To copy password to clipboard

                toast('This feature is in testing stage!', duration=3, position='center', color='success', onclick=None)

        put_table([

            ['Password', password,put_buttons(['Copy to Clipboard','Home','About'],onclick=btn_click)],

            ])
        img = open('git.png', 'rb').read()  # logo
        put_image(img, width='60px')  # size of image
        put_text("More @https://github.com/aswinks1995")






#To allow reloading of web browser and mentioning the port
app.add_url_rule('/','webio_view',webio_view(main),methods=['GET','POST','OPTIONS'])
if __name__ =='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument("-p","--port",type=int,default=8080)
    args=parser.parse_args()

    start_server(main,port=args.port)