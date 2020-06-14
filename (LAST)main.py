import subprocess
from glob import glob
from tkinter import *
from tkinter import messagebox

filelist = glob("text_alphabet_recog.py")

for file in filelist:
    subprocess.call(['python', file])

def campusmap():
    filelist = glob("CampusMap.py")

    for file in filelist:
        subprocess.call(['python', file])
        break

def translate():
    filelist = glob("papago.py")

    for file in filelist:
        subprocess.call(['python', file])

def crawling():
    filelist = glob("crawling.py")

    for file in filelist:
        subprocess.call(['python', file])


def calendar():
    filelist = glob("Calendar.py")

    for file in filelist:
        subprocess.call(['python', file])

def close():
    messagebox.showinfo("종료", "프로그램을 종료합니다.")
    quit()


def main():
    window = Tk()
    window.title("메뉴선택")  # GUI창 이름변경
    window.geometry("640x400+100+100")  # 크기 설정
    window.resizable(0, 0)
    photo = PhotoImage(file="CBNU.png");
    labe2 = Label(window, image=photo);
    labe3 = Label(window, text='글씨 인식 프로그램', font=(30))

    # 호출
    b1 = Button(window, text="1. 번역", width=15, height=5, compound="c", command=translate)
    b2 = Button(window, text="2. 웹 크롤링", width=15, height=5, compound="c", command=crawling)
    b3 = Button(window, text="3. 학교 위치 정보", width=15, height=5, compound="c", command=campusmap)
    b4 = Button(window, text="4. 캘린더", width=15, height=5, compound="c", command=calendar)
    b5 = Button(window, text="5. 종료", width=15, height=5, compound="c", command=close)

    labe2.pack()
    labe3.pack()
    b1.pack(side=LEFT, padx=10)
    b2.pack(side=LEFT, padx=10)
    b3.pack(side=LEFT, padx=10)
    b4.pack(side=LEFT, padx=10)
    b5.pack(side=LEFT, padx=10)

    window.mainloop()


main()
