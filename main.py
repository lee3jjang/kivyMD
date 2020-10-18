from todo_crud import *
from datetime import date

def show_todo_all():
    print('전체 TODO 리스트입니다')
    todolist = get_todo_all()
    print('id 내용 카테고리 완료일자')
    for todo in todolist:
        print(todo[0], todo[1], todo[2], todo[4])

def show_todo_complete():
    print('완료된 TODO 리스트입니다')
    todolist = get_todo_complete()
    print('id 내용 카테고리 완료일자')
    for todo in todolist:
        print(todo[0], todo[1], todo[2], todo[4])

def show_todo_not_complete():
    print('미완료된 TODO 리스트입니다')
    todolist = get_todo_not_complete()
    print('id 내용 카테고리')
    for todo in todolist:
        print(todo[0], todo[1], todo[2])

def get_action():
    print('어떤 활동을 하시겠나요?')
    print('1. TODO 추가하기')
    print('2. TODO 삭제하기')
    print('3. TODO 완료시키기')
    print('4. 완료시킨 TODO 취소하기')
    print('5. 전체 TODO 조회하기')
    print('6. 완료된 TODO 조회하기')
    print('7. 미완료된 TODO 조회하기')
    print('8. 종료하기')
    while True:
        num = input('활동> ')
        if num in [str(x) for x in range(1, 9)]:
            print()
            break
        print('1~8번 중에 선택해주세요')
    return num

def interface_insert_todo():
    print('컨텐츠를 입력하세요')
    contents = input('컨텐츠> ')
    print('카테고리를 입력하세요')
    category = input('카테고리> ')
    if contents == '' and category == '':
        print('TODO 입력이 취소되었습니다')
        print()
        return
    insert_todo(contents, category)
    print('새로운 TODO가 등록되었습니다')
    print()

def interface_delete_todo():
    print('어떤 것을 지울건가요?')
    todolist = get_todo_not_complete()
    print('id 내용 카테고리')
    for todo in todolist:
        print(todo[0], todo[1], todo[2])
    id = input('ID> ')
    delete_todo(id)
    print(f'{id}번을 삭제했습니다')
    print()

def interface_complete_todo():
    print('어떤 것을 완료시킬건가요?')
    todolist = get_todo_not_complete()
    print('id 내용 카테고리')
    for todo in todolist:
        print(todo[0], todo[1], todo[2])
    id = input('ID> ')
    today = date.today().strftime('%Y-%m-%d')
    complete_todo(id, today)
    print(f'{id}번을 완료시켰습니다')
    print()

def interface_undo_complete_todo():
    print('어떤 것을 완료취소 할건가요?')
    todolist = get_todo_complete()
    print('id 내용 카테고리 완료일자')
    for todo in todolist:
        print(todo[0], todo[1], todo[2], todo[4])
    id = input('ID> ')
    undo_complete_todo(id)
    print(f'{id}번을 완료취소 시켰습니다')
    print()

if __name__ == '__main__':
    show_todo_not_complete()
    while True:
        num = get_action()
        if num == '8':
            print('프로그램이 종료됩니다')
            break
        elif num == '1':
            interface_insert_todo()
        elif num == '2':
            interface_delete_todo()
        elif num == '3':
            interface_complete_todo()
        elif num == '4':
            interface_undo_complete_todo()
        elif num == '5':
            show_todo_all()
            input()
        elif num == '6':
            show_todo_complete()
            input()
        elif num == '7':
            show_todo_not_complete()
            input()