import os
import argparse
import json
DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)),"matches.json")
mappool = ["Ancient", "Anubis", "Inferno", "Mirage", "Nuke", "Overpass", "Vertigo"]

def cmd_add(args):
    matches = load_matches()
    match = {
        "map": args.map,
        "kills": args.kills,
        "deaths": args.deaths,
        "rounds_won": args.rounds_won,
        "rounds_lost": args.rounds_lost,
    }
    matches.append(match)
    save_matches(matches)
    print(f"Saved: {args.map} ({args.kills}/{args.deaths})")

def cmd_list(args):
    matches = load_matches()
    for match in matches:
        print(f"{match['map']} {match['kills']}/{match['deaths']} {match['rounds_won']} - {match['rounds_lost']}")

def cmd_stats(args):
    matches = load_matches()
    if not matches:
        print("No matches recorded yet.")
        return
    total_kills = 0
    total_deaths = 0
    wins = 0 

    for match in matches:
        total_kills += match['kills']
        total_deaths += match['deaths']
        if match['rounds_won']>match['rounds_lost']:
            wins += 1

    total_matches = len(matches)
    win_rate = wins / total_matches * 100
    if total_deaths == 0:
        kd = total_kills
    else:
        kd = total_kills / total_deaths

    print(f"Matches: {total_matches}")
    print(f"K/D: {kd:.2f}")
    print(f"Win rate: {win_rate:.1f}%")

def load_matches():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_matches(matches):
    with open(DATA_FILE, "w") as f:
        json.dump(matches, f, indent=2)

def main():
    parser = argparse.ArgumentParser(
        prog="cstrack",
        description="record and analyze your CS matches."
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="record a new match")
    add_parser.add_argument("--map", choices=mappool, required=True, help="map played")
    add_parser.add_argument("--kills", type=int, required=True, help="kills per match")
    add_parser.add_argument("--deaths", type=int, required=True,help="deaths per match" )
    add_parser.add_argument("--rounds-won", type=int, required=True, help="rounds won per match")
    add_parser.add_argument("--rounds-lost", type=int, required=True, help="rounds lost per match")
    add_parser.set_defaults(func=cmd_add)

    list_parser = subparsers.add_parser("list", help="list recorded matches")
    list_parser.set_defaults(func=cmd_list)

    stats_parser = subparsers.add_parser("stats",help="show aggregate stats")
    stats_parser.set_defaults(func=cmd_stats)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
