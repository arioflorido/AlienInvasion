# Alien Invasion
A clone of the popular 'Space Invader' game written in Python, based on the book 'Python Crash Course' by Eric Matthes.

# Installation Instructions
  1. Install [python3.8](https://www.python.org/downloads/release/python-3818/).
  2. Install Pygame Dependencies.
     - `sudo apt-get -y update && sudo apt-get install python-dev-is-python3 libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsdl1.2-dev libsmpeg-dev subversion libportmidi-dev ffmpeg libswscale-dev libavformat-dev libavcodec-dev libfreetype6`
  3. Install [pipenv](https://pipenv.pypa.io/en/latest/installation/)
  4. Install Project Dependencies.
     - `pipenv install --system --python 3`
  5. Run the game.
     - `python3 main.py`

# Future Improvements
  - Unit test implementations.
  - Disable window resizing.
  - Dockerization.
    - At the time of writing, it is not ideal to dockerize Pygame applications due to performance implications. More info [here](https://opeonikute.dev/posts/running-pygame-in-a-docker-container-macos#:~:text=It's%20now%20possible%20to%20run,pygame%20and%20python%20).  
