import webbrowser

def r():
  u="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
  webbrowser.open(u)

def main():
    print("You are about to be rickrolled!")
    r()

def a():
  x = int(input("1*1=? "))
  if x == 1: return True
  else: return False

def b():
  if a():
    main()
  else:
    print("Somehow you escaped...")

b()
