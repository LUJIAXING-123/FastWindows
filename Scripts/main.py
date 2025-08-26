from subprocess import run
from time import sleep as wait
import os

class RunMain:

    def __init__(self):
        self.main()

    @staticmethod
    def next_page():
        for i in range(100):
            print()

    def activate(self):
        self.next_page()

        key='NRG8B-VKK3Q-CXVCJ-9G2XF-6Q84J'

        print('激活时请关闭弹出的窗口!')
        print('正在激活，请稍等...')

        run('slmgr.vbs /upk',shell=True)
        run('slmgr.vbs /ipk '+key,shell=True)
        run(os.path.dirname(os.path.realpath(__file__))+"\\bin\\activate.cmd",shell=True,capture_output=True)

        print('正在激活，请不要关闭窗口，正在返回主页面。。。')
        wait(3)
        self.main()

    def update(self):
        self.next_page()
        close_day: str=str(int(input('请输入最大暂停更新的时间(周)：'))*7)
        run('reg add "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\WindowsUpdate\\UX\\Settings" /v FlightSettingsMaxPauseDays /t reg_dword /d {} /f'.format(close_day),shell=True)
        print('请检查是否可以跳过更新到设置的最大周！')
        wait(3)
        self.main()

    def cleanup(self):
        self.next_page()
        clear_path=['C:\Windows\Temp\*','C:\Windows\Prefetch\*','C:\Windows\SoftwareDistribution\Download\*','%temp%\*']

        for path in clear_path:
            run('powershell -Command "Remove-Item {}"'.format(path),shell=True)

        print('程序以浅度清理，正在打开系统清理软件，选择C盘，有清理系统文件的按钮就点，全选就行！')
        run('cleanmgr')
        wait(3)
        self.main()

    def explorer(self):
        self.next_page()

        print('###########################################')
        print()
        print('1) Windows11')
        print('2) Windows10')
        print('q) 退出')
        print()
        print('###########################################')
        print()

        choice=input('选择你的操作：')
        while choice!='q':
            if choice=='1':

                run(os.path.dirname(os.path.realpath(__file__))+'\\bin\\explorer\\win_11.cmd',shell=True)
                print('请检查是否切换成功！')
                wait(3)
                break

            if choice == '2':
                run(os.path.dirname(os.path.realpath(__file__))+'\\bin\\explorer\\win_10.cmd', shell=True)
                print('请检查是否切换成功！')
                wait(3)
                break

        self.main()

    def main(self):

        if os.name == 'nt':
            self.next_page()

            print('欢迎使用FastWindows优化程序!')
            print('使用前请详细阅读GitHub主页(README.md)!')
            print('请使用管理员身份运行!')
            print()
            print('###########################################')
            print()
            print('1) 激活Windows')
            print('2) 关闭Windows更新')
            print('3) 清理Windows垃圾')
            print('4) 切换资源管理器样式')
            print('q) 退出')

            while True:
                choice = input('选择你的操作：')

                if choice == '1':
                    self.activate()
                    break

                if choice == '2':
                    self.update()
                    break

                if choice == '3':
                    self.cleanup()
                    break

                if choice == '4':
                    self.explorer()
                    break

                elif choice == 'q':
                    quit(114514)

                else:
                    print('无效的输入。。。')
                    wait(3)

        else:
            print('你的系统不支持！')
            wait(3)
            quit(114514)

RunMain()