# Update
It took me a while to get my code to work, it was hard, but at least i'm able to done it,
this development version included a **NEW** fading transiton! With the new transition a
new part type `fade` is also included.

The `fade` keyword comes with 3 configure settings (used for default fading):
- `in_duration`: This controls the duration of the dissapearing image (default is 0.5 seconds)
- `hold_duration`: This controls the duration of the screen when it stayed as black (default is 0 second, which means the holding will be skipped)
- `out_duration`: This controls the duration of the appearing image (default is 0.5)

To use different duration for the fade in, hold and out without having the default settings modified.

```python
# The duration must always: in -> hold -> out so if you're not modifying in that order, fill the value 
# you didn't want to modify with the default in config file.
[ "fade", "in_image", "out_image", in_duration, 0.5, out_duration ]
``` 

For a clearer view about the newly included transition, the clip below here will help you.
![recording](recording.gif)

**NOTE**: I changed the output program to use `cx_Freeze` instead, hope you don't mind 😅
