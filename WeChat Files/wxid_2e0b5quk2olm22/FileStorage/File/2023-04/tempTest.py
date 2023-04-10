import os
import subprocess

a = 0
def cmd1():
    try:
        cmd1 = 'd:'
        cmd2 = 'cd D:\MCUXpressoIDE_11.7.0_9198\ide/mcuxpressoidec.exe '
        cmd3 = 'mcuxpressoidec.exe -application com.nxp.mcuxpresso.headless.application --launcher.suppressErrors -noSplash -consoleLog -data D:\\pythonProject4.9-2\\tempWorkspace -run example.build D:\\pythonProject4.9-2\\decorators\\build1.properties'
        cmd = cmd1 + '&&' + cmd2 + '&&' +cmd3
        a = os.popen(cmd).read()
        #print(a)
        if "Exiting with return code: 0" in a:
            print("pass")
            #print("D:\\pythonProject4.9-2\\tempWorkspace"+"")
        elif "Exiting with return code: 1" in a:
            print("Complier Error")
        elif "Exiting with return code: 2" in a:
            print("Internal Error")

        #subprocess.Popen(cmd)
    except Exception as e:
        print("cloc tool fail:" + str(e))

cmd1()



#定义列表
projects = []
#定义实参
path = 'D:\\pythonProject4.9-2\\tempWorkspace'
def find_projectfile_from_path(path):
    # root所指的是当前正在遍历的这个文件夹的本身的地址
    # dirs是一个list ，内容是该文件夹中所有的目录的名字(不包括子目录)
    # files同样是list, 内容是该文件夹中所有的文件(不包括子目录)
    for root,dirs,files in os.walk(path):
        for f in files:
            if f.endswith("evkbimxrt1050_hello_world.axf"):
            # if "hello_world_v3_10.xml" in f:
                #填入列表
                projects.append(os.path.join(root, f))
#调用函数传入path实参
find_projectfile_from_path(path)
#打印列表
result_list = projects[0]
print(result_list)
#print(projects)


