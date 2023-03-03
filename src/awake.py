try:
    import pyautogui
    import time
    import sys
    from datetime import datetime
    from rich.console import Console
    from rich import print
    from rich.progress import track
except ImportError:
    from pip._internal import main as pip
    pip(['install', '--user', 'pyautogui'])
    pip(['install', '--user', 'rich'])
    import pyautogui
    from rich.console import Console
    from rich import print
    from rich.progress import track


pyautogui.FAILSAFE = False
numMin = None
console = Console()
if ((len(sys.argv)<2) or sys.argv[1].isalpha() or int(sys.argv[1])<1):
    numMin = 1
else:
    numMin = int(sys.argv[1])

#with console.status("[bold green]..jigglin...") as status:
while(True):
    x=0
    for step in track(range(numMin*60), description='[!] jigglin' in..'): #while(x<numMin):
        time.sleep(1)
        x+=1
    print(":thumbs_up: Starting to jiggle {}".format(datetime.now().time()))
    for i in range(0,200):
        pyautogui.moveTo(0,i*4)
    pyautogui.moveTo(1,1)
    for i in range(0,3):
        pyautogui.press("shift")
    print("[bold green][+][/bold green] jiggled at {}".format(datetime.now().time()))
