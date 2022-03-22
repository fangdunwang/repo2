# import json, time, re
# from managements import management_login
# from users import users_login
# from registered import registered
# from back import back
#
# read_movie = open('movie.json', 'r', encoding='utf-8')
# movie = json.loads(read_movie.read())
# read_user = open('user.json', 'r', encoding='utf-8')
# user = json.loads(read_user.read())
# read_management = open('management.json', 'r', encoding='utf-8')
# management = json.loads(read_management.read())
# read_ticket_record = open('ticket_record.json', 'r', encoding='utf-8')
# ticket_record = json.loads(read_ticket_record.read())


def movie_tickets():
    while True:
        permissions = input('请您选择用户操作（1.用户登录 2.注册用户 3. 找回密码 4.退出系统）：')
        if permissions == '1':
            while True:
                login = input('请您选择登录权限（1.个人登录 2.管理登录 3.退出登录）：')
                if login == '1':
                    users_login(user, movie, ticket_record)
                elif login == '2':
                    management_login(management, user, movie, ticket_record)
                elif login == '3':
                    break

        elif permissions == '2':
            registered(user)
        elif permissions == '3':
            back(management, user)
        elif permissions == '4':
            break


movie_tickets()

save = open('movie.json', 'w', encoding='utf-8')
json.dump(movie, save, ensure_ascii=False, indent=4)
save = open('user.json', 'w', encoding='utf-8')
json.dump(user, save, ensure_ascii=False, indent=4)
save = open('management.json', 'w', encoding='utf-8')
json.dump(management, save, ensure_ascii=False, indent=4)
save = open('ticket_record.json', 'w', encoding='utf-8')
json.dump(ticket_record, save, ensure_ascii=False, indent=4)
import time, re

operation = '''********欢迎使用漫漫影院系统*********
  1.查看信息  2.添加会员  3.注销会员 
  4.查看购票  5.影票出售  6.影票退订
  7.查看余票  8.增删管理  9.增删影片 
 10.销售记录 11.修改信息 12.退出系统
*********************************'''


def management_login(a, b, c, d):
    account = input('请您输入账号：')
    password = input('请您输入密码：')
    if account in a:
        if a[account][0] == password:
            time.sleep(0.5)
            print('密码正确，登录成功！')
            while True:
                print(operation)
                choose = input('请您选择操作选项:')

                if choose == '1':
                    while True:
                        query = input('请你选择查询选项（1.查询会员 2.查询管理 3.退出查询）：')
                        if query == '1':
                            for i in b:
                                time.sleep(0.5)
                                print('会员卡号:{}、会员昵称:{}、会员性别:{}、手机号码:{}'.format
                                      (i, b[i][1], b[i][2], b[i][3]))
                        elif query == '2':
                            for i in a:
                                time.sleep(0.5)
                                print('管理账号:{}、管理昵称:{}、管理性别:{}、手机号码:{}'.format
                                      (i, a[i][1], a[i][2], a[i][3]))
                        elif query == '3':
                            break

                elif choose == '2':
                    while True:
                        add = input('是否需要添加会员（1.需要 2.退出）：')
                        if add == '2':
                            break
                        else:
                            name = input('请您输入会员昵称：')
                            gender = input('请您输入会员性别：')
                            phone = input('请您输入手机号码：')
                            password = input('请您输入登录密码：')
                            account = []
                            for i in b:
                                account.append(int(i))
                            account.sort()
                            b[str(account[-1] + 1)] = [password, name, gender, phone]
                            time.sleep(0.5)
                            print('注册成功！')
                            time.sleep(0.5)
                            print('会员卡号:{}、登录密码:{}、会员昵称:{}、会员性别:{}、手机号码:{}'.format
                                  (str(account[-1] + 1), password, name, gender, phone))

                elif choose == '3':
                    while True:
                        delete = input('是否需要注销会员（1.需要 2.取消）：')
                        if delete == '2':
                            break
                        cancel = input('请您输入需要注销会员卡号：')
                        if cancel not in b:
                            print('卡号输入有误！')
                        else:
                            del b[cancel]
                            time.sleep(0.5)
                            print('会员注销成功！')

                elif choose == '4':
                    while True:
                        query = input('请您选择查询操作（1.查询个人 2.查询全部 3.退出查询）：')
                        if query == '1':
                            query_personal = input('请您输入需要查询会员卡号：')
                            if query_personal in d:
                                for i in d[query_personal]:
                                    time.sleep(0.5)
                                    print('会员卡号:{}、会员昵称:{}、购票影片:{}、影厅座位:{}'.format
                                          (query_personal, b[query_personal][1], i, ' '.join(d[query_personal][i])))
                            else:
                                print('未查询到购票信息！')
                        elif query == '2':
                            for x in d:
                                for y in d[x]:
                                    if x in b:
                                        time.sleep(0.5)
                                        print('会员卡号:{}、会员昵称:{}、购票影片:{}、影厅座位:{}'.format
                                              (x, b[x][1], y, ' '.join(d[x][y])))
                                    else:
                                        time.sleep(0.5)
                                        print('会员卡号:{}、会员昵称:{}、购票影片:{}、影厅座位:{}'.format
                                              (x, a[x][1], y, ' '.join(d[x][y])))

                        elif query == '3':
                            break

                elif choose == '5':
                    card_number = ''
                    judge = input('是否有会员卡（1.有卡 2.无卡）:')
                    if judge == '1':
                        card_number = input('请您输入会员卡号:')
                    elif judge == '2':
                        card_number = account
                    time.sleep(0.5)
                    print('*' * 3 + '电影放映表' + '*' * 3)
                    for x, y in list(enumerate(c, 1)):
                        print(x, y['name'])
                    print('*' * 13)

                    time.sleep(0.5)
                    buy = int(input('请您选择电影场次：'))
                    print('*' * 8 + '电影信息' + '*' * 8)
                    print('影名：{}'.format(c[buy - 1]['name']))
                    print('类别：{}'.format(c[buy - 1]['category']))
                    print('导演：{}'.format(c[buy - 1]['director']))
                    print('演员：{}'.format(c[buy - 1]['actor']))
                    print('*' * 23)

                    while True:
                        time.sleep(0.5)
                        print('*' * 13 + '影厅座位' + '*' * 13)
                        for i in c[buy - 1]['seat']:
                            print('  '.join(i))
                        print('*' * 32)
                        ticket = input('是否继续购票（1.继续 2.退出）：')
                        if ticket == '2':
                            break

                        line_numbers = int(input('请您选择影厅行号：'))
                        seat_numbers = int(input('请您选择影厅座号：'))
                        if c[buy - 1]['seat'][line_numbers][seat_numbers] == '■':
                            print('不好意思，座位已选！')
                        else:
                            c[buy - 1]['seat'][line_numbers][seat_numbers] = '■'
                            time.sleep(0.5)
                            print('购票成功，电影名:{} 座位号:{}排{}号'.format
                                  (c[buy - 1]['name'], line_numbers, seat_numbers))

                            if card_number in d and c[buy - 1]['name'] in d[card_number]:
                                d[card_number][c[buy - 1]['name']].append(
                                    '{}排{}号'.format(line_numbers, seat_numbers))
                            elif card_number in d and c[buy - 1]['name'] not in d[card_number]:
                                d[card_number][c[buy - 1]['name']] = [
                                    '{}排{}号'.format(line_numbers, seat_numbers)]
                            else:
                                d[card_number] = {
                                    c[buy - 1]['name']: ['{}排{}号'.format(line_numbers, seat_numbers)]}

                elif choose == '6':
                    while True:
                        unsubscribe = input('是否需要退订影票（1.需要 2.退出）:')
                        if unsubscribe == '2':
                            break
                        else:
                            card_number = input('请您输入会员卡号:')
                            for i in d[card_number]:
                                if card_number in b:
                                    time.sleep(0.5)
                                    print('卡号:{} 昵称:{} 影名:{} 座位:{}'.format
                                          (card_number, b[card_number][1], i, ' '.join(d[card_number][i])))
                                else:
                                    time.sleep(0.5)
                                    print('卡号:{} 昵称:{} 影名:{} 座位:{}'.format
                                          (card_number, a[card_number][1], i, ' '.join(d[card_number][i])))
                            name = dict(enumerate(d[card_number], 1))
                            for i in name:
                                print(i, name[i])
                            movie_number = int(input('请您选择需要退票电影序号：'))
                            number = dict(enumerate(d[card_number][name[movie_number]], 1))
                            for i in number:
                                print(i, number[i])
                            seat_number = int(input('请您选择需要退票电影座位：'))
                            message = re.findall(r'\d+', number[seat_number])
                            for i in c:
                                if name[movie_number] == i['name']:
                                    i['seat'][int(message[0])][int(message[1])] = '□'
                            d[card_number][name[movie_number]].remove(number[seat_number])
                            time.sleep(0.5)
                            print('退票成功！')
                            if not d[card_number][name[movie_number]]:
                                del d[card_number][name[movie_number]]

                elif choose == '7':
                    more_ticket = []
                    for x in range(len(c)):
                        number = 0
                        for y in c[x]['seat']:
                            number += y.count('□')
                        more_ticket.append(number)
                        time.sleep(0.5)
                        print('影名:{}-余票:{}张'.format(c[x]['name'], more_ticket[x]))

                elif choose == '8':
                    while True:
                        options = input('请您选择操作选项（1.添加管理 2.删除管理 3.退出系统）：')
                        if options == '1':
                            name = input('请您输入管理昵称：')
                            gender = input('请您输入管理性别：')
                            phone = input('请您输入手机号码：')
                            password = input('请您输入登录密码：')
                            account = []
                            for i in a:
                                account.append(int(i))
                            account.sort()
                            a[str(account[-1] + 1)] = [password, name, gender, phone]
                            time.sleep(0.5)
                            print('注册成功！')
                            time.sleep(0.5)
                            print('管理账号:{}、登录密码:{}、管理昵称:{}、管理性别:{}、手机号码:{}'.format
                                  (str(account[-1] + 1), password, name, gender, phone))
                        elif options == '2':
                            while True:
                                delete = input('是否继续删除管理员（1.继续 2.退出）：')
                                if delete == '2':
                                    break
                                else:
                                    card = input('请您输入删除管理员卡号：')
                                    del a[card]
                                    time.sleep(0.5)
                                    print('删除成功！')
                        elif options == '3':
                            break

                elif choose == '9':
                    while True:
                        options = input('请您选择操作选项（1.添加影片 2.删除影片 3.退出系统）：')
                        if options == '1':
                            name = input('请您输入影名:')
                            category = input('请您输入类别:')
                            director = input('请您输入导演:')
                            actor = input('请您输入演员:')
                            seat = [[' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' '],
                                    ['1', '□', '□', '□', '□', '□', '□', '□', '□', '□', '1'],
                                    ['2', '□', '□', '□', '□', '□', '□', '□', '□', '□', '2'],
                                    ['3', '□', '□', '□', '□', '□', '□', '□', '□', '□', '3'],
                                    ['4', '□', '□', '□', '□', '□', '□', '□', '□', '□', '4'],
                                    ['5', '□', '□', '□', '□', '□', '□', '□', '□', '□', '5'],
                                    ['6', '□', '□', '□', '□', '□', '□', '□', '□', '□', '6'],
                                    [' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']]
                            c.append({'name': name, 'category': category, 'director': director, 'actor': actor,
                                      'seat': seat})
                            time.sleep(0.5)
                            print('添加影片成功！')
                        elif options == '2':
                            for x, y in list(enumerate(c, 1)):
                                print(x, y['name'])
                            delete = int(input('请您选择需要删除影片序号：'))
                            c.pop(delete - 1)
                            time.sleep(0.5)
                            print('影片删除成功！')
                        elif options == '3':
                            break

                elif choose == '10':
                    sales_ticket = []
                    for x in range(len(c)):
                        number = 0
                        for y in c[x]['seat']:
                            number += y.count('■')
                        sales_ticket.append(number)
                        time.sleep(0.5)
                        print('影名:{}-售出:{}张'.format(c[x]['name'], sales_ticket[x]))
                elif choose == '11':
                    print('管理卡号:{}、管理昵称:{}、管理性别:{}、手机号码:{}'.format
                          (account, a[account][1], a[account][2], a[account][3]))
                    while True:
                        continues = input('是否需要修改信息（1.需要 2.退出）')
                        if continues == '2':
                            break
                        else:
                            modify = input('请您选择修改选项（1.管理昵称 2.管理性别 3.手机号码）：')
                            if modify == '1':
                                a[account][1] = input('请您输入管理昵称:')
                            elif modify == '2':
                                a[account][2] = input('请您输入管理性别:')
                            elif modify == '3':
                                a[account][3] = input('请您输入手机号码:')
                            time.sleep(0.5)
                            print('信息修改成功！')

                elif choose == '12':
                    break
        else:
            print('密码错误，登录失败！')
    else:
        print('账号错误，请您核对！')