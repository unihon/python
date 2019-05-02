from pynput import keyboard
import pyperclip
import reqm

KEYWORK_0 = "Key.ctrl_l"
KEYWORK_1 = "c"
KEYWORK_2 = "q"
keyStack = []

def on_press(key):
    try:
        key_s = key.char
    except AttributeError:
        key_s = str(key)

    keyStackIn(key_s)

def on_release(key):
    try:
        key_s = key.char
    except AttributeError:
        key_s = str(key)

    # 如果一个按键释放占用时间过长，在同时段的其他按键释放则无法触发释放事件
    if keyCheck(key_s):
        return False
    keyStackOut(key_s)

# 对按键栈进行是否符合组合键的判断
# 第一个按下和第一个放开的组合
def keyCheck(key_s):
    if keyStack:
        if keyStack[0] == KEYWORK_0 and key_s == KEYWORK_1:
            query_s = getText()
            if query_s:
                print("Loading...")
                print("┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐")
                res = reqm.requests_data(query_s)
                if res:
                    print(reqm.data_show(res))
                print("┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘")
            # 匹配一次之后清空按键栈，解决线程堵塞，只监听到释放一个按键的问题
            keyStack.clear()
            return False
        elif keyStack[0] == KEYWORK_0 and key_s == KEYWORK_2:
            return True

# 按键进栈
def keyStackIn(key_s):
    if keyStack:
        if key_s != keyStack[-1]:
            keyStack.append(key_s)
    else:
        keyStack.append(key_s)

# 按键出栈
def keyStackOut(key_s):
    if keyStack:
        if key_s != keyStack[-1]:
            keyStack.clear()
        else:
            keyStack.pop()


def getText():
    raw = pyperclip.paste()
    if raw:
        return raw.strip()
    else:
        return None

print("""
┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐
┆ Globle Ctrl+C translate. ┆
┆ Ctrl+Q exit.             ┆
└┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘
""")

with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
    try:
        listener.join()
    except KeyboardInterrupt:
        pass
