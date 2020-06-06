import json
from os import path
from quart import Quart, request
from .game_tracker import CivGameTracker

app = Quart(__name__)

local_path = path.abspath(path.dirname(__file__))
sample_json_path = path.join(local_path, "..", "sample_games.json")
with open(sample_json_path) as f:
    game_data = json.load(f)

game_tracker = CivGameTracker.from_dict(game_data)


@app.route("/civ6", methods=["POST"])
async def civ_webhook():
    data = json.loads(await request.get_data())
    try:
        game_name = data["value1"]
        player_name = data["value2"]
        turn_count = int(data["value3"])
    except KeyError:
        pass

    game_tracker.update_game(game_name, player_name, turn_count)
    return "success\n"


if __name__ == "__main__":
    app.run()
