# Dungeon Descent
A rogue-like dungeon crawler game made in Python and using the TCOD library
<img src="https://raw.githubusercontent.com/jackylau-nyc/dungeon-descent/main/readme-intro.png" width="800">

## Index

- [About](#about)
- [Usage](#usage)
  - [Installation](#installation)
  - [Commands](#commands)
  - [Controls](#controls)
- [Development](#development)
  - [Pre-Requisites](#pre-requisites)
  - [Contribution](#contribution)
- [Resources](#resources)
- [Gallery](#camera-gallery)
- [Credit/Acknowledgment](#star2-creditacknowledgment)

## About
A multi-level dungeon crawler game entirely in the terminal. A tunneling algorithm was used to procedurally generate each floor of the dungeon with items and monsters scattered throughout the rooms. A basic AI is implemented to control the monsters actions and the engine handles the overworld view. As you survive combat, you gain experience to level up and as you progress through the dungeon floors, the loot gets better but the difficulty scales up.

## Usage


### Installation
- Clone the repository into the folder of your choice

```
$ git clone "https://github.com/jackylau-nyc/roguelike-dev.git"
```

### Commands
- After navigating to the folder, you can start the game by running
```
$ python main.py
```

### Controls
Left Hand Controls | Right Hand Controls
------------ | -------------
[W] - Upwards Movement | [U] - Pickup Item
[A] - Leftwards Movement | [ I ] - Open Up Inventory Menu to Use Consumeables or Equip/Unequip Wearables
[S] - Downwards Movement | [O] - Open Up Inventory Menu to Drop Item
[D] - Rightwards Movement | [P] - Player Character Information
[Q] - Upper-Left Movement | [H] - Descend Staircase
[E] - Upper-Right Movement | [ [ ] - Look at highlighted tile
[Z] - Lower-Left Movement | [1-9] Use/Equip/Unequip or Drop Item after Opening Corresponding Inventory Menu
[C] - Upper-Right Movement |
[X] - Wait |
[ESC] - Quit Game |
[TAB] - History |

Mouse can be used to hover over tiles and select targets

## Development

### Pre-Requisites
List all the pre-requisites the system needs to develop this project.
- [Python 3.7 or higher](https://www.python.org/downloads/) (Currently using 3.8 as of July 2020)
- The latest version of [TCOD Library](https://python-tcod.readthedocs.io/en/latest/installation.html)
- An editor of choice (I used VScode)

 ### Contribution

 Your contributions are always welcome and appreciated. Following are the things you can do to contribute to this project.

 1. **Report a bug**

 If you think you have encountered a bug, and I should know about it, feel free to report it [here](https://github.com/jackylau-nyc/dungeon-descent/issues) and I will take care of it.

 2. **Create a pull request**

 It can't get better than this, your pull request will be appreciated by the community. You can get started by picking up any open issues from [here](https://github.com/jackylau-nyc/dungeon-descent/pulls) and make a pull request.

 > If you are new to open-source, make sure to check read more about it [here](https://www.digitalocean.com/community/tutorial_series/an-introduction-to-open-source) and learn more about creating a pull request [here](https://www.digitalocean.com/community/tutorials/how-to-create-a-pull-request-on-github).

## Resources
- [RogueBasin](http://www.roguebasin.com/index.php?title=Main_Page)
- [Roguelike Development Subreddit](https://www.reddit.com/r/roguelikedev/)
- [Roguelike Tutorial](http://rogueliketutorials.com/)

## Gallery
<img src="https://raw.githubusercontent.com/jackylau-nyc/dungeon-descent/main/gameplay_ss.png" width="800">

## Credit/Acknowledgment
Me!
