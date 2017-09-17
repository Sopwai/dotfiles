# Dotfiles
These are my current dotfiles. This repo should be updated as I update my files, both for people to use and to back up the files. Feel free to take what you want from these files. Please do correct any spelling or grammar mistakes, English is NOT my first language.

## My system
These files are being used on the Fedora 26 partition of my drive. I am using i3-gaps as my WM and Polybar as my status bar.
You will most likely not be able to directly copy and paste my files as yours, but you can go through and use the same settings(probably).
If you do copy and paste anything directly as yours, before opening an issue please make sure that the name of your bar in the polybar config file ```[bar/whateveryouchoosetocallit]``` is the same in the launch.sh file
```# Launch bar1 and bar2
polybar whateveryouchoosetocallit &
```
or however it looks in your launch.sh file. I expect some may vary.
### Dependencies
Things I have installed that you may find helpful(or will need to use some of these files):

* [i3-gaps](https://github.com/Airblader/i3)
* [Polybar](https://github.com/jaagr/polybar)
* [Rofi](https://davedavenport.github.io/rofi/)
* [Compton](https://github.com/chjj/compton)
* [Feh](https://github.com/derf/feh)
* [Wal](https://github.com/dylanaraps/wal)
* [Neofetch](https://github.com/dylanaraps/neofetch)
* There are also some fonts, I will include those in the .fonts folder
### What do they do?

**i3-gaps** is my current *WM*.

**Polybar** is what i use for my *status bar*.

**Rofi** is a *window switcher* on steroids. I use it to replace **_dmenu_**.

**Compton** is a *compositor* for **X**.

**Feh** is an *X11 image viewer* that also manages my wallpaper.

**Wal** generates a color scheme from an image, and sets it to your terminal.

**Neofetch** displays system information. Not *really* needed, but cool to look at.


## A bunch of neat people you should take a peep at

Currently, some chunks of code have been taken from or inspired by:
* [16BitBow](https://github.com/16BitBow/dotfiles)
* [unix121](https://github.com/Sopwai/i3wm-themer) Specifically 'Space'.
* [rintivdorh on reddit](https://www.reddit.com/r/unixporn/comments/5y85do/i3gaps_polybar_cranium/)
