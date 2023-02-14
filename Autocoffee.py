material = {'커피': 3, '물': 3, '컵': 3, '프림': 3, '설탕': 3}
# 커피 종류별 재료가 세팅
# 커피 3, 물 3, 컵 3, 프림 3, 설탕 3
# 재료 소진시 해당 커피는 판매 불가능

money = {'블랙커피': 1000, '설탕커피': 1000, '프림커피': 1500, '밀크커피': 2000, 'money_in': 0}
# 블랙 = 1000 설탕 = 1000 프림 = 1500 밀크 = 2000


class Auto_coffee():  # 커피자동판매기

    def run(self):
        while True:
            self.get_cof()  # print coffee name & coffee value
            self.get_money()  # 금액 투입 및 투입된 금액 출력
            self.select_coffee()  # 원하는 커피 선택 후 나옴

    # 금액 투입 # 확인 완료
    def get_money(self):
        money_in = 0
        while True:
            print('= ' * 12 + '금액투입' + ' =' * 12 + '\n')
            print('현재 투입된 금액 : {}원\n'.format(money['money_in']))
            if money['money_in'] > money['블랙커피'] or money['money_in'] > money['설탕커피'] or money['money_in'] > money['프림커피'] or money['money_in'] > money['밀크커피']:
                self.select_coffee()
                break
            else:
                money_in = input('투입 금액 : ')  # money_in에 투입할 금액을 입력받고
                print()
                if money_in != '':  # money_in이 공백일 때 예외처리
                    # 투입 금액에 manager(대, 소문자) 입력시
                    if money_in == 'manager' or money_in == 'MANAGER':
                        self.manager_sys()  # 커피 자동 판매기 관리 프로그램으로 연결
                        break
                    try:
                        money_in = int(money_in)  # money_in을 형변환 시도
                        if money_in > 0:
                            if money['money_in'] == '0':  # 처음 등록할 때
                                money['money_in'] = money_in
                            else:
                                # 형변환 성공시 'money_in'을 키로 투입 금액을 저장
                                money['money_in'] += money_in
                                print('투입 금액 : {}원\n'.format(
                                    money['money_in']))
                                break
                        else:
                            print('돈을 투입해 주세요.\n')
                    except:
                        print('투입 금액에 숫자를 입력해 주세요.\n')  # 형변환 실패 시 오류 문구 출력
                else:
                    print('돈을 투입해 주세요.\n')

    # 매니저 시스템 # 확인 완료
    def manager_sys(self):
        while True:
            print('= ' * 12 + '유지 보수' + ' =' * 12 + '\n')
            print('1. 재료보충\n2. 금액 조정\n3. 시스템종료\n')
            sel = input('실행할 명령 입력 : ')
            print()
            if sel != '':
                if sel == '1' or '2' or '3':
                    if sel == '1':
                        self.sys_fill()  # 1. 재료 보충
                    elif sel == '2':
                        self.sys_change_val()  # 2. 금액 조정
                    elif sel == '3':
                        print('금액 투입으로 돌아갑니다.\n')  # 3. 시스템 종료
                        self.run()
                        break
            else:
                print('번호를 입력해주세요.')

    # 1. 재료 보충 # 확인 완료
    def sys_fill(self):
        while True:
            count = 0
            print('= ' * 12 + '재료' + ' =' * 12 + '\n')
            print(
                f'커피 : {material["커피"]}, 물 : {material["물"]}, 설탕 : {material["설탕"]}, 프림 : {material["프림"]}, 컵 : {material["컵"]}')
            print('1) 전체 2) 커피 3) 물 4) 설탕 5) 프림 6) 컵')
            print()
            sel = input('보충할 재료의 번호를 입력해 주세요.(종료는 q 입력) : ')
            print()
            if sel != '':
                if sel == 'q':
                    break
                else:
                    if sel == '1':
                        for i in material:
                            if material[i] == 3:
                                count += 1
                        if count == 5:
                            print('모든 재료가 가득 차있습니다.\n\n관리 프로그램으로 돌아갑니다.\n')
                            break
                        else:
                            print('모든 재료를 보충했습니다.\n\n관리 프로그램으로 돌아갑니다.\n')
                            break
                    else:  # 1이 아닐경우(2, 3, 4, 5, 6)
                        if sel == '2':
                            if material['커피'] != 3:
                                material['커피'] = 3
                                print('커피를 보충했습니다.\n')
                            else:
                                print('이미 커피는 가득 차 있습니다.\n')
                        elif sel == '3':  # elif sel == i + 1:
                            if material['물'] != 3:
                                material['물'] = 3
                                print('물을 보충했습니다.\n')
                            else:
                                # print('이미 {}은 가득 차 있습니다.\n.format(i)')
                                print('이미 물은 가득 차 있습니다.\n')
                        elif sel == '4':
                            if material['설탕'] != 3:
                                material['설탕'] = 3
                                print('설탕을 보충했습니다.\n')
                            else:
                                print('이미 설탕은 가득 차 있습니다.\n')
                        elif sel == '5':
                            if material['프림'] != 3:
                                material['프림'] = 3
                                print('프림을 보충했습니다.\n')
                            else:
                                print('이미 프림은 가득 차 있습니다.\n')
                        elif sel == '6':
                            if material['컵'] != 3:
                                material['컵'] = 3
                                print('컵을 보충했습니다.\n')
                            else:
                                print('이미 컵은 가득 차 있습니다.\n')
                        else:
                            print('잘못 입력하셨습니다.\n')
            else:
                print('번호칸은 비워둘 수 없습니다.')

    # 2. 금액 조정 # 확인 완료
    def sys_change_val(self):
        while True:
            self.get_cof()
            sel_cof = input('가격을 변경할 커피 이름 입력 : ')
            print()
            if sel_cof != '':
                if sel_cof in money.keys():
                    val = input('변경할 금액 입력 : ')
                    print()
                    if val != '':
                        try:
                            val = int(val)
                            if val > 0:
                                if sel_cof == '블랙커피':
                                    money['블랙커피'] = val
                                    print(
                                        '블랙커피의 가격이 {}원으로 변경되었습니다.\n'.format(val))
                                    break
                                elif sel_cof == '설탕커피':
                                    money['설탕커피'] = val
                                    print(
                                        '설탕커피의 가격이 {}원으로 변경되었습니다.\n'.format(val))
                                    break
                                elif sel_cof == '프림커피':
                                    money['프림커피'] = val
                                    print(
                                        '프림커피의 가격이 {}원으로 변경되었습니다.\n'.format(val))
                                    break
                                elif sel_cof == '밀크커피':
                                    money['밀크커피'] = val
                                    print(
                                        '밀크커피의 가격이 {}원으로 변경되었습니다.\n'.format(val))
                                    break
                            else:
                                print('0 보다 낮은 가격으로는 설정할 수 없습니다.\n')
                        except:
                            print('변경할 금액은 숫자여야 합니다.\n')
                    else:
                        print('커피 가격은 비워둘 수 없습니다.\n')
                else:
                    print('커피 이름을 다시 입력해주세요.\n')
            else:
                print('커피 이름은 비워둘 수 없습니다.\n')

    # 커피이름 + 가격 출력 # 확인 완료
    def get_cof(self):
        print('= ' * 12 + '커피자판기' + ' =' * 12 + '\n')
        print('1. 블랙커피({}원) 2. 설탕커피({}원) 3. 프림커피({}원) 4. 밀크커피({}원)\n'.format(
            money['블랙커피'], money['설탕커피'], money['프림커피'], money['밀크커피']))

    # 커피 종류 선택 및 가격 출력 # 확인 완료
    def select_coffee(self):
        while True:
            self.get_cof()
            cof = input('원하는 커피 입력(종료를 원하면 엔터) : ')  # 예외처리(공백)
            print()
            if cof != '':  # 예외처리(공백)
                self.con_material(cof)
                break
            else:
                while True:
                    esc = input('원하는 커피가 없으시면 프로그램을 종료할까요? [Y / N] : ')
                    print()
                    if esc == 'y' or esc == 'Y':
                        print('프로그램을 종료합니다.\n\n돈을 돌려 드리겠습니다.\n')
                        print('나올 금액 : {}원\n'.format(money['money_in']))
                        money['money_in'] = 0
                        self.run()
                    elif esc == 'n' or esc == 'N':
                        print('커피 선택 화면으로 돌아갑니다.\n')
                        break
                    else:
                        print('Y와 N중에서 입력해 주세요.\n')

    # 선택한 커피 종류에 따라서 재료 소모 # 작동은 하지만 가격 더해야함 + 길이 줄이기
    def con_material(self, cof):
        if cof == '블랙커피':
            if money['money_in'] >= money['블랙커피']:
                money['money_in'] -= money['블랙커피']
                # 다른 재료들의 갯수가 0보다 크다면
                if material['커피'] > 0 and material['물'] > 0 and material['컵'] > 0:
                    material['커피'] -= 1
                    material['물'] -= 1
                    material['컵'] -= 1
                    print('블랙커피 나왔습니다.\n')
                else:
                    print('재료가 없습니다.\n돈은 돌려 드리겠습니다.')
                    money['money_in'] += money['블랙커피']
            else:
                print('잔액이 부족합니다.\n')

        elif cof == '설탕커피':
            if money['money_in'] >= money['설탕커피']:
                money['money_in'] -= money['설탕커피']
                if material['커피'] > 0 and material['물'] > 0 and material['컵'] > 0 and material['설탕'] > 0:
                    material['커피'] -= 1
                    material['물'] -= 1
                    material['컵'] -= 1
                    material['설탕'] -= 1
                    print('설탕커피 나왔습니다.\n')
                else:
                    print('재료가 없습니다.\n돈은 돌려 드리겠습니다.')
                    money['money_in'] += money['설탕커피']
            else:
                print('잔액이 부족합니다.\n')

        elif cof == '프림커피':
            if money['money_in'] >= money['프림커피']:
                money['money_in'] -= money['프림커피']
                if material['커피'] > 0 and material['물'] > 0 and material['컵'] > 0 and material['프림'] > 0:
                    material['커피'] -= 1
                    material['물'] -= 1
                    material['컵'] -= 1
                    material['프림'] -= 1
                    print('프림커피 나왔습니다.\n')
                else:
                    print('재료가 없습니다.\n돈은 돌려 드리겠습니다.')
                    money['money_in'] += money['프림커피']
            else:
                print('잔액이 부족합니다.\n')

        elif cof == '밀크커피':
            if money['money_in'] >= money['밀크커피']:
                money['money_in'] -= money['밀크커피']
                if material['커피'] > 0 and material['물'] > 0 and material['컵'] > 0 and material['프림'] > 0 and material['설탕']:
                    material['커피'] -= 1
                    material['물'] -= 1
                    material['컵'] -= 1
                    material['프림'] -= 1
                    material['설탕'] -= 1
                    print('밀크커피 나왔습니다.\n')
                else:
                    print('재료가 없습니다.\n돈은 돌려 드리겠습니다.')
                    money['money_in'] += money['프림커피']
        else:
            print('커피 이름을 입력해 주세요.\n')


cof = Auto_coffee()
cof.run()
