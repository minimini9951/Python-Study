user_Info = {}


class Bank:
    def create_Account(self):  # 계좌 개설
        num = int(input('만들 계좌번호 : '))
        if num not in user_Info.keys():  # 안에 키가 없을경우
            name = input('본인 이름 : ')
            money = int(input('예금 금액 : '))
            print('=' * 21)
            print('\n계좌가 개설되었습니다.')
            user_Info[num] = [name, money]  # num을 키로 갖는, value를 리스트로 저장
        else:
            print('=' * 21)
            print('\n중복된 계좌번호입니다.')
        self.menu()  # 젤 밑에 def menu를 만들어둠.

    def money_in(self):  # 입금처리
        num = int(input('계좌번호 입력 : '))
        if num in user_Info.keys():
            value = int(input('입금할 금액 : '))
            user_Info[num][1] += value  # 0번째는 name, 1번째는 value
            print('=' * 21)
            print('\n입금이 완료되었습니다.')
        else:
            print('=' * 21)
            print('\n잘못된 계좌번호입니다.')
        self.menu()

    def money_out(self):  # 출금처리
        num = int(input('계좌번호 입력 : '))
        if num in user_Info.keys():
            value = int(input('출금할 금액 : '))
            if user_Info[num][1] > value:
                user_Info[num][1] -= value
                print('=' * 21)
                print('\n출금이 완료되었습니다.')
            elif user_Info[num][1] == value:
                user_Info[num][1] = 0
                print('=' * 21)
                print('\n출금이 완료되었습니다.')
            else:
                print('\n잔액이 부족합니다.')
        else:
            print('\n잘못된 계좌번호입니다.')
        self.menu()

    def send_money(self):  # 송금처리
        num1 = int(input('자신의 계좌번호 입력 : '))
        if num1 in user_Info.keys():
            num2 = int(input('입금할 계좌번호 입력 : '))
            if num2 in user_Info.keys():
                value = int(input('송금할 금액 입력 : '))
                user_Info[num1][1] -= value  # 자기 계좌에서 빼고
                user_Info[num2][1] += value  # 남의 계좌에 더해주고
                print('=' * 21)
                print('\n송금완료 되었습니다.')
            else:
                print('=' * 21)
                print('\n송금하려는 계좌는 존재하지 않거나 잘못된 계좌번호 입니다.')
        else:
            print('=' * 21)
            print('\n존재하지 않거나 잘못된 계좌번호 입니다.')
        self.menu()  # 메뉴로 돌아가

    def all_Account(self, all_money=0):  # 전체 고객조회  #이게 어려웠대
        if user_Info == {}:  # 딕셔너리가 비어있으면,
            print('=' * 21)
            print('\n고객이 없습니다.')
        else:
            for num in user_Info:  # num은 user_Info의 key와 같다.
                print('이름 : {}, 계좌번호 : {}, 예금금액 : {}원'.format(
                    user_Info[num][0], num, user_Info[num][1]))
                all_money += user_Info[num][1]
            print('=' * 21)
            print('\n총 예금금액 : {}원'.format(all_money))
        self.menu()

    def menu(self):
        print('\n===== Bank Main =====')
        print('1. 계좌개설')
        print('2. 입금처리')
        print('3. 출금처리')
        print('4. 송금처리')
        print('5. 전체고객 잔액조회')
        print('6. 프로그램 종료')
        print('=' * 21)
        menu = input('원하는 메뉴 = ')
        if menu == '1':
            self.create_Account()
        elif menu == '2':
            self.money_in()
        elif menu == '3':
            self.money_out()
        elif menu == '4':
            self.send_money()
        elif menu == '5':
            self.all_Account()
        elif menu == '6':
            print('=' * 21)
            print('\n프로그램을 종료합니다.')
        else:
            print('=' * 21)
            print('\n잘못된 키를 입력하셨습니다.')
        self.menu()


b = Bank()
b.menu()
