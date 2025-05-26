from cx_Freeze import setup, Executable
import os

proj = os.getenv('GAMEDIR', '.')
target_name = os.getenv('TARGET_NAME')

class Build:

    def __init__(self, gamedir=proj, version="1.0", icon='icon.ico', files=[ "data" ], script='game.py', base="gui", compress=False):
        os.chdir(gamedir)
        self.gamedir = proj
        self.version = version
        self.executable = Executable(icon=icon, script=script, base=base, target_name=target_name or script.split('.')[0])
        self.build_exe_options = {
            'includes': [ 'Novel_Python', 'pygame' ],
            'excludes': [ 'tkinter', 'unittest' ],
            'include_files': files,
            'no_compress': not compress,
        }

    def start(self):
        setup(name=self.gamedir,
              version=self.version,
              options={ 'build_exe': self.build_exe_options },
              executables=[self.executable]
              )

if __name__ == '__main__':
    build = Build()
    build.start()

