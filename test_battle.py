from kaggle_environments import make
from main import agent

env = make("cabt", debug=True)

env.run([agent, agent])

for i, player in enumerate(env.steps[-1]):
    print(
        f"player {i}: ",
        f"status={player.status}, "
        f"reward={player.reward}"        
    )


# 対戦結果を保存
html = env.render(mode="html")
with open("result.html", "w", encoding="utf-8") as f:
    f.write(html)

