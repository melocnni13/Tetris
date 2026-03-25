#Тетрис в терминале
#1_БЛОК Все данные нужные для игры
import time
import random
import os
import keyboard
len_room=15
height_room=15
#Создание матрицы
def create_matric():
    fields=[]
    for y in range(height_room):
        new_line=[]
        for x in range(len_room):
            new_line.append(0)
        fields.append(new_line)
    return fields
permanent_field=create_matric()
#О(квадрат)
shape_O=[[1,1],
         [1,1]]
#Г(лежачая буква Г)
shape_L=[[0,0,1],
         [1,1,1]]
#Г(лежачая буква Г в другую сторону)
shape_L_left=[[1,0,0],
              [1,1,1]]
#З(змейка!?)
shape_Z=[[1,1,0],
         [0,1,1]]
#З(змейка в другую сторону?!)
shape_Z_left=[[0,1,1],
              [1,1,0]]
#Т(Тешка)
shape_T=[[0,1,0],
         [1,1,1]]
#I(палка)
shape_I=[[1],
         [1],
         [1],
         [1]]
colors=[91, 92, 93, 94, 95, 96, 97]
all_shape=[shape_O,shape_I,shape_L,shape_L_left,shape_Z,shape_Z_left,shape_T]
color_shape=random.choice(colors)
shape=random.choice(all_shape)
next_shape=random.choice(all_shape)
hold_shape=None
hold_color=None
can_hold=True
next_color_shape=random.choice(colors)
shape_x=len_room//2-len(shape[0])//2
shape_y=0
drop_y=0
speed=0.4
direction_shape=''
score=0
#Перезапуск всех данных
def reset():
    global color_shape,shape,next_shape,next_color_shape,shape_x,shape_y,speed,direction_shape,score,permanent_field,hold_shape,hold_color,can_hold
    color_shape=random.choice(colors)
    shape=random.choice(all_shape)
    next_shape=random.choice(all_shape)
    next_color_shape=random.choice(colors)
    shape_x=len_room//2-len(shape[0])//2
    shape_y=0
    speed=0.4
    direction_shape=''
    score=0
    permanent_field=create_matric()
    hold_shape=None
    hold_color=None
    can_hold=True
    return color_shape,shape,next_shape,next_color_shape,shape_x,shape_y,speed,direction_shape,score,permanent_field,hold_shape,hold_color,can_hold
#2_БЛОК Всё связанное с комнатой
#Меню
def menu():
    print('ИГРА ТЕТРИС В ТЕРМИНАЛЕ')
    print('_'*50)
    print('Управление A(вправо), D(влево), W(повороты фигуры),S(вниз),H(удержание фигуры)')
    print('_'*50)
    print('Начать игру(нажмите 1)')
    print('_'*50)
    print('Выход из игры(нажмите любую кнопку)')
    print('_'*50)
    if keyboard.read_key()=='1':
        return True
    else:
        return False
#Окончание игры
def over_game(scores):
    print('Вы проиграли!')
    print('_'*50)
    print('Ваш счёт за игру:',scores)
    print('_'*50)
    print('Начать игру(нажмите 1)')
    print('_'*50)
    print('Выход из игры(нажмите любую кнопку)')
    print('_'*50)
    if keyboard.read_key()=='1':
        return True
    else:
        return False
#Отрисовка будущей фигуры
def draw_next_shape(shapes,color):
    for y in range(len(shapes)):
        for x in range(len(shapes[0])):
            if shapes[y][x]==0:
                print('.',end='')
            else:
                print(f"\033[{color}m#\033[0m", end="")
        print()
#Отрисовка поля
def draw_matric(fields,color):
    print('Счёт:',score)
    if hold_shape:
        print("_"*len_room)
        print('Удерживаемая фигура')
        print()
        draw_next_shape(hold_shape,hold_color)
        print()
        print('_'*len_room)
    print('_'*len_room)
    print()
    print('Следующая фигура')
    print()
    draw_next_shape(next_shape,next_color_shape)
    print()
    print('_'*len_room)
    for y in range(height_room):
        for x in range(len_room):
            if fields[y][x]==0:
                print(".",end="")
            else:
                color=fields[y][x]
                print(f"\033[{color}m#\033[0m", end="")
        print()
#Добавление фигуры в поле
def draw_shape(fields,shapes,x,y,color):
    for row in range(len(shapes)):
        for col in range(len(shapes[row])):
            if shapes[row][col]==1:
                fields[row+y][col+x]=color
#Очистка экрана
def clear_display():
    if os.name == 'nt':
        os.system('cls')
#Падение фигуры
def fall_shape(y):
    if y<height_room:
        return y+1
    else:
        return y
#Управление фигурой
def move_shape(direction,x):
    if direction=='A':
        return x-1
    elif direction=='D':
        return x+1
    else:
        return x
#Проверка границ для фигуры
def check_collision(fields,shapes,x,y):
    for row in range(len(shapes)):
        for col in range(len(shapes[0])):
            if shapes[row][col]!=0:
                if x<0 or x+col>=len_room:
                    return True
                if y+row>=height_room or y+row<0:
                    return True
                if fields[row+y][col+x]!=0:
                    return True
    return False
#Повороты фигуры
def rotated_shape(shapes):
    row=len(shapes)
    col=len(shapes[0])
    rotated=[]
    for y in range(col):
        new_line=[]
        for x in range(row-1,-1,-1):
            new_line.append(shapes[x][y])
        rotated.append(new_line)
    return rotated
#Для удаления линии
def clear_line_shapes(fields):
    clear_lines=0
    y=height_room-1
    while y>=0:
        if 0 not in fields[y]:
            del fields[y]
            fields.insert(0,[0]*len_room)
            clear_lines+=1
        else:
            y-=1
    return clear_lines
#3_БЛОК Игровой цикл
if menu():
    while True:
        if keyboard.is_pressed('A'):
            if not check_collision(permanent_field, shape, shape_x - 1, shape_y):
                direction_shape = 'A'
                shape_x = move_shape(direction_shape, shape_x)
        elif keyboard.is_pressed('D'):
            if not check_collision(permanent_field, shape, shape_x + 1, shape_y):
                direction_shape = 'D'
                shape_x = move_shape(direction_shape, shape_x)
        elif keyboard.is_pressed('W'):
            if not check_collision(permanent_field, rotated_shape(shape), shape_x, shape_y):
                shape = rotated_shape(shape)
        elif keyboard.is_pressed('S'):
            if not check_collision(permanent_field, shape, shape_x, shape_y+3):
                shape_y+=3
        elif keyboard.is_pressed('H'):
            if can_hold:
                if hold_shape==None:
                    hold_shape=shape
                    hold_color=color_shape
                    shape=next_shape
                    color_shape=next_color_shape
                    next_shape=random.choice(all_shape)
                    next_color_shape=random.choice(colors)
                elif hold_shape!=None:
                    shape,hold_shape=hold_shape,shape
                    color_shape,hold_color=hold_color,color_shape
                shape_x=len_room//2-len(shape[0])//2
                shape_y=0
                can_hold=False
        drop_y=shape_y
        while not check_collision(permanent_field, shape, shape_x, drop_y+1):
            drop_y=fall_shape(drop_y)
        clear_display()
        display_field = [row[:] for row in permanent_field]
        draw_shape(display_field,shape,shape_x,drop_y,90)
        draw_shape(display_field, shape, shape_x, shape_y, color_shape)
        draw_matric(display_field, color_shape)
        if check_collision(permanent_field, shape, shape_x, shape_y + 1):
            draw_shape(permanent_field, shape, shape_x, shape_y, color_shape)
            multiplier = clear_line_shapes(permanent_field)
            if multiplier >= 1:
                score += 100 * multiplier
                if score % 200 == 0 and speed>0.2:
                    speed -= 0.01
            shape = next_shape
            next_shape = random.choice(all_shape)
            color_shape = next_color_shape
            next_color_shape = random.choice(colors)
            shape_x = len_room // 2 - len(shape[0]) // 2
            shape_y = 0
            can_hold=True
            if check_collision(permanent_field, shape, shape_x, shape_y):
                clear_display()
                if over_game(score):
                    reset()
                    continue
                else:
                    break
        else:
            shape_y = fall_shape(shape_y)
        time.sleep(speed)
