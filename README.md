Hello, welcome to my CS Stat Tracker by ocul1 !

Within this repo, is the python code for a CLI that will take the stats of your CS match and the map, and then store it into a json file, that you can look at the entirety of with a simple command.

# What it does:
  This tool records amtches, stores tham as JSON, and then gives the aggregate stats like overall K/D and winrate. 
  I made this program as a newer iteration of another repo that i have on my github, but with the knowledge that i have learned from argparsing

# Requirements:
  1. A computer capable of running Python 3
  2. Argparse and JSON are apart of the standard library, so it has no external dependencies :)

# Usage:
  1. To record a match:
     python cli-cstracker.py add --map Mirage --kills 20 --deaths 20 --rounds-won 13 --rounds_lost 3
     
  2. List all recorded matches
     python cli-cstracker.py list
     
  3. Show aggregate stats
     python cli-cstracker.py stats

  To see full list of options for the CLI:
    python cli-cstracker.py --help
