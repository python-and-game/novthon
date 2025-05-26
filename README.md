# novthon 1.1
This release brings new features while fixing and improving old features

# Update
- `game.py` has better code now
- `Novel_Python.scene.menu` and `Novel_Python.scene.cmenu` has an error at the key navigation but it is now fixed
- added a `build.py` file using cx_Freeze
  + Copy game.py file to your project
  + Create an icon or copy the default game's icon or use pygame icon
  + Set the environment variable `GAMEDIR` in your console to the location of your project's directory
    (e.g: `set GAMEDIR = D:/novthon-1.1/soda_saga`)
  + If you want to change the name of your executable file, set the environment variable `TARGET_NAME` to
  the name you want for the executable file (e.g: `set TARGET_NAME=soda`)
  + Then run `python build.py build` to build your project
  + Test the executable
