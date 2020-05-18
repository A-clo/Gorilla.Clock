    p
    try:
        if sys.platform == 'darwin':
            
            subprocess.run(['terminal-notifier', '-title', '🦧', '-message', msg])
            subprocess.run(['say', '-v', 'Daniel', msg])
        elif sys.platform.startswith('linux'):
            
            subprocess.Popen(["notify-send", '🦧', msg])
        else:
            
            
            pass

    except:
        
        pass

def help():
    appname = sys.argv[0]
    appname = appname if appname.endswith('.py') else 'tomato' 
    print('====== 🦧 Gorilla Clock =======')
    print(f'{appname}         # start a {WORK_MINUTES} minutes tomato clock + {BREAK_MINUTES} minutes break')
    print(f'{appname} -t      # start a {WORK_MINUTES} minutes tomato clock')
    print(f'{appname} -t <n>  # start a <n> minutes tomato clock')
    print(f'{appname} -b      # take a {BREAK_MINUTES} minutes break')
    print(f'{appname} -b <n>  # take a <n> minutes break')
    print(f'{appname} -h      # help')


if __name__ == "__main__":
    main()
