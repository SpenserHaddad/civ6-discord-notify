import json
import os
from typing import Tuple
import click
from .server import app, game_tracker


@click.command()
@click.option(
    "-h", "--host", show_default=True, help="The host to listen on", default="0.0.0.0"
)
@click.option(
    "-p", "--port", show_default=True, help="The port to bind to", default=12156
)
@click.option("--discord-token", help="Discord API Token", required=True)
@click.option(
    "--game-data",
    help="Saved game data in JSON file (can be called multiple times)",
    type=click.Path(exists=True, file_okay=True, dir_okay=False),
    multiple=True,
)
def main(
    host: str, port: int, discord_token: str, game_data: Tuple[str],
):
    for game_data_file in game_data:
        with open(game_data_file) as f:
            saved_game_data = json.load(f)
        for saved_game in saved_game_data:
            game_tracker.add_game_dict(saved_game)
    os.environ["CIV6_NOTIFY_DISCORD_TOKEN"] = discord_token
    app.run(host, port)


if __name__ == "__main__":
    main(auto_envvar_prefix="CIV6_NOTIFY")
