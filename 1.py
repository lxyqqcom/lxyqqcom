import pyautogui,sys,time

def dian():
    
    try:
        pyautogui.click(1877,1048,500,0.05)
    except KeyboardInterrupt:
        sys.exit(0)
        
def main():
    time.sleep(10)
    dian()
    
if __name__=='__main__':
    main()
