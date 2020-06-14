def Print_menu():
    print("#---------------------------------------------#")
    print("1. 크롤링하기")
    print("2. 내용 보여주기")
    print("0. 종료\n")
    menu = input("메뉴선택: ")
    return int(menu)


def main():
    print()
    print("          crawling      \n")
    print("메뉴 생성\n")
    while 1:
        menu = Print_menu()

        # ----- 크롤링 하기 -----
        if menu == 1:
            import subprocess
            from glob import glob
            filelist = glob("crawling.py")

            for file in filelist:
                subprocess.call(['python', file])
                break

        # ----- 내용 보여주기 -----
        elif menu == 2:
            import subprocess
            from glob import glob
            filelist = glob("readline_all.py")

            for file in filelist:
                subprocess.call(['python', file])

        else:
            print("종료되었습니다.")
            break


if __name__ == "__main__":
    main()
