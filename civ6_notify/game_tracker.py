from dataclasses import dataclass, field, asdict
from typing import Dict, Optional


@dataclass
class CivPlayer:
    name: str
    mention_in_channel: bool = False
    direct_message: bool = False


@dataclass
class CivPlayByCloudGame:
    name: str
    players: Dict[str, CivPlayer] = field(default_factory=dict)
    turn_count: int = 0
    current_player: Optional[str] = None


class CivGameTracker:
    def __init__(self):
        self._games: Dict[str, CivPlayByCloudGame] = {}

    def update_game(self, game_name: str, player_name: str, turn: int):
        game = self._games[game_name]
        game.current_player = player_name
        game.turn_count = turn
        print(f"{game.name}: It's {player_name}'s turn (Turn {turn})'")

    def add_game(self, game: CivPlayByCloudGame):
        self._games[game.name] = game

    def add_game_dict(self, game_data: Dict):
        name = game_data["name"]
        players = {p["name"]: CivPlayer(**p) for p in game_data["players"]}
        turn_count = game_data.get("turn_count", 0)
        current_player = game_data.get("current_player", None)
        self._games[name] = CivPlayByCloudGame(
            name=name,
            players=players,
            turn_count=turn_count,
            current_player=current_player,
        )

    def to_dict(self) -> Dict:
        return {"games": [asdict(game) for game in self._games.values()]}

    @staticmethod
    def from_dict(game_data: Dict) -> "CivGameTracker":
        tracker = CivGameTracker()
        for g in game_data["games"]:
            tracker.add_game_dict(g)
        return tracker
