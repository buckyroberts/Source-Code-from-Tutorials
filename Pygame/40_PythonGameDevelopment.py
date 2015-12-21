# THIS SCRIPT SHOULD BE CALLED SETUP.PY
import cx_Freeze 

executables = [
        #                   name of your game script
        cx_Freeze.Executable("slither.py") 
] 
cx_Freeze.setup( 
        name = "Slither", 
        options = {"build_exe": {"packages":["pygame"],"include_files":["apple.png","snakehead.png"]}},
        description = "Slither game tutorial", 
        executables = executables)


#python setup.py build
#python setup.py bdist_msi
