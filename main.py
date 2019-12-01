from tkinter import *
from tkinter import messagebox
import os

def clear(*al):
   for i in al:
       i.destroy()

def info():##Student information
    x = Label(win,text='Name')
    x.pack()
    name = Entry(win)
    name.pack(fill = X)
    y = Label(win,text='ID')
    y.pack()
    idd = Entry(win)
    idd.pack(fill=X)

    wait_0 = IntVar()
    begin = Button(win,text='Begin',command= lambda: wait_0.set(1))
    begin.pack()
    begin.wait_variable(wait_0)

    n,m = name.get(),idd.get()
    clear(x,y,name,idd,begin)
    return (n,m)


def questions_read():## Reading the question files from folder
    ques_file_names = ()
    with os.scandir('questions') as questions:
        for que in questions:
            if que.is_file() and str(que.name)[-4:] == '.txt':
                ques_file_names += (que.name,)        
    return (ques_file_names)
                
def display_question(question_file):## Displaying questions with options
    text_file =  open('questions/'+question_file, "r")
    data = text_file.readlines()
    text_file.close()

    question,option_1,option_2,option_3,option_4 = StringVar(),StringVar(),StringVar(),StringVar(),StringVar()
        
    question.set(data[0].strip())
    option_1.set(data[1].strip()[3:])
    option_2.set(data[2].strip()[3:])
    option_3.set(data[3].strip()[3:])
    option_4.set(data[4].strip()[3:])
    #student_answer = input('Enter your choice? ')
    #print ()
    v = StringVar()
    v.set(None)
    q = Label(win,textvariable = question)
    a = Radiobutton(win, textvariable=option_1, variable=v, value='a')
    b = Radiobutton(win, textvariable=option_2, variable=v, value='b')
    c = Radiobutton(win, textvariable=option_3, variable=v, value='c')
    d = Radiobutton(win, textvariable=option_4, variable=v, value='d')
    q.pack()
    a.pack()
    b.pack()
    c.pack()
    d.pack()
   
    wait = IntVar()
    submit = Button(win,text='submit',command= lambda: wait.set(1))
    submit.pack()
    submit.wait_variable(wait)
    clear(q,a,b,c,d,submit)

    return v.get()

def get_answers():##Reading the answer file
    answers = ()
    text_file = open('answers.txt')
    ans_files = text_file.readlines()
    text_file.close()
    for an in ans_files:
        answers += (an.strip(),)
    return answers


def result(report,info,student):## Generating Personlized Report
    sname = Label(win,text='Name: '+info[0])
    sname.pack()
    sid = Label(win,text='ID: '+info[1])
    sid.pack()
    cans = get_answers()
    c = 0
    head = Label(win,text=" Q#\tCorrect Answers\tYour Answers")
    head.pack()
    
    for p,q in zip(cans,student):
        c += 1
        Label(win,text="%s\t\t%s\t\t%s"%(c,p,q)).pack()

    total,correct = len(report),report.count(True)
    percent = (correct/total)*100
    
    Label(win,text='You scored %s out of %s'%(correct,total)).pack()
    Label(win,text='Percentage: %s '%(percent)).pack()

    wait_2 = IntVar()
    endd = Button(win,text='Close Now',command= lambda: wait_2.set(1))
    endd.pack()
    endd.wait_variable(wait_2)

    win.destroy()
    

def main(): ## Main functions
    
    start.destroy()
    stu_info = info()
    report = []
    student_answers = ()
    question_files = questions_read()
    
    for ans_no,file_names in enumerate(question_files):
        
        qq = Label(win,text='Question #%s '%(ans_no+1))
        qq.pack()
        stu_ans = display_question(file_names)
        qq.destroy()
        student_answers += (stu_ans,)
        if stu_ans == get_answers()[ans_no]:
            report.append(True)
        else: report.append(False)
        
    end = Label(win, text = 'Test Finished!')
    end.pack()
    rep = Label(win, text = 'Your report is ready')
    rep.pack()

    wait_1 = IntVar()
    fin = Button(win,text='Result',command= lambda: wait_1.set(1))
    fin.pack()
    fin.wait_variable(wait_1)
    clear(end,rep,fin)

    result(report,stu_info,student_answers)
    
    
win = Tk()
win.title('MCQs TEST')
win.geometry('300x230')
start = Button(win,text='start',command=main)
start.pack(side=TOP)
win.mainloop()

    
