import random
from pathlib import Path

import pandas


def load_deck() -> list[int]:
    path = Path(__file__).parent / "deck.csv"
    return pandas.read_csv(path, header=None)[0].tolist()

def agent(observations: dict) -> list[int]:
    select = observations["select"]
    
    # ゲーム開始時は使用する60枚のデッキを返す
    if select is None:
        return load_deck()
    
    # 提示された合法手からランダムに選ぶ
    options = select["option"]
    count = select["maxCount"]

    return random.sample(range(len(options)), count)
