GoPro Video
---
GoPro videos are cut into 4GB sized files, meaning they are chaptered. 
This script automatically gets the fileformat that can be used to concat GoPro videos together using ffmpeg

Usage:
---
1. Update the path (todo: pass it in through cli args)
2. cd into the dir that now has the relevant `.txt` files
3. Run either the command using `GNU Parallel` or the one using a simple bash-loop in your terminal

```sh
parallel ffmpeg -f concat -safe 0 -i {} -c copy {.}.mp4 ::: *.txt
```

```sh
for txtfile in *.txt; do ffmpeg -f concat -safe 0 -i "$txtfile" -c copy "${txtfile%.txt}.mp4"; done
```
