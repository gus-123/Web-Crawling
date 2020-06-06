import subprocess
from glob import glob
filelist = glob("text_alphabet_recog2.py")

for file in filelist:
    subprocess.call(['python', file])


def Print_menu():
    print("#---------------------------------------------#")
    print("1. 주석 달기")
    print("2. 파파고 번역")
    print("3. 웹 크롤링")
    print("0. 종료\n")
    menu = input("메뉴선택: ")
    return int(menu)

def main():

    print()
    print("          글씨인식 시스템 부가기능      \n")
    print("메뉴 생성\n")
    while 1:
        menu = Print_menu()

        # ----- 주석 달기 -----
        if menu == 1:
            import subprocess
            from glob import glob
            filelist = glob("CampusMap.py")

            for file in filelist:
                subprocess.call(['python', file])

        # ----- 파파고 번역 -----
        elif menu == 2:
            import subprocess
            from glob import glob
            filelist = glob("papago.py")

            for file in filelist:
                subprocess.call(['python', file])

        # ----- 웹 크롤링 -----
        elif menu == 3:
            import subprocess
            from glob import glob
            filelist = glob("crawling.py")

            for file in filelist:
                subprocess.call(['python', file])

            f = open('output.txt', 'w')
            out = subprocess.check_output(['crawling.py'], shell=True, encoding='utf-8')
            f.write(out)
            f.close()


        else:
            print("종료되었습니다.")
            break

if __name__ == "__main__":
    main()