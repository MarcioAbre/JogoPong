import cx_Freeze


executables = [cx_Freeze.Executable('pong.py')]

cx_Freeze.setup(

    name = " pong jogo",
    options = {'build_exe': {'packages':['pygame'],
                'include_files': ['images', 'sounds']}},

    executables = executables

)