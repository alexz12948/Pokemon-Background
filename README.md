# Random Desktop Background Pokemon

The purpose of this project was to show how to automate certain processes using python for the [Tufts Coding 101 Pre-College Course](https://universitycollege.tufts.edu/high-school/programs/coding-101). The script leverages the [Pokemon API](https://pokeapi.co)

## Source

This project idea was taken from a Youtube Video that I watched, which will be linked in the Resources section below

## Set Up
Note that this will only work for MacOS users

In a terminal, run:
1. `python3 -m venv env` to generate a virtual environment
2. `. env/bin/activate` to start up the virtual environment
3. `pip3 install -r requirements.txt` to download all of the required libraries

You then must go into `get_pokemon_background.py` and change the variable called `FILENAME` towards the top of the file to be where you directory is located (Run `pwd` in the terminal to get an idea if you are not sure how to do that)

Finally, run `python3 get_pokemon_background.py` to get a new background

You can edit the way that it looks by going to System Preferences -> Desktop & Screen Saver and adjusting the images there

## Cronjobs

Cronjobs are tasks that can run at an interval that you set. To read more, [look here](https://www.hostinger.com/tutorials/cron-job)

### How to set it up

I would recommend looking at this [Youtube Video](#resources) since he does a great job of explaining it

Additionally, if it doesn't run and you are running it on MacOS, you will probably need to allow the cron command to have full disk access. Here is the [stack overflow post](https://stackoverflow.com/questions/62876343/permissionerror-errno-1-operation-not-permitted-users-local-path-venv-py) I used to fix this problem

## Resources

* [Youtube Video Inspiration](https://www.youtube.com/watch?v=5bTkiV_Aadc)
* [Helpful Page of How to use Crontab](https://www.baeldung.com/linux/create-crontab-script#1-install-a-new-file-to-crontab)
* [Crontab Guru](https://crontab.guru) - A good resource for figuring out cron schedule expressions

## Future Edits

- [ ] Utilize other APIs (such as the NASA api) to create more random background images
- [ ] Make it generalizable for other operating systems
