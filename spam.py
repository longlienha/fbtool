import pyperclip, pyautogui, random, time

print("tool spam")
msg = input("nhap noi dung: ").split(" || ")
n = int(input("so lan spam: "))
m = float(input("time delay: "))

for i in range(5, 0, -1):
    print(str(i)+"...")
    time.sleep(1)
print("bat dau")

for i in range(n):
    pyperclip.copy(random.choice(msg))
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    time.sleep(m)
print("ket thuc")