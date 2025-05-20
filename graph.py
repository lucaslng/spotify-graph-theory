import networkx as nx

import matplotlib.pyplot as plt
import matplotlib
import requests
from io import BytesIO
from PIL import Image
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from user import User

def get_user_edges(user: User) -> list[tuple[str, str]]:
	return list(map(lambda followee_id: (user.uid, followee_id), user.following_ids))


def graph(users: dict[str, User]) -> None:
	matplotlib.rcParams['toolbar'] = 'None'

	G = nx.DiGraph()
	G.add_edges_from(*map(get_user_edges, users.values()))

	pos = nx.spring_layout(G)

	fig, ax = plt.subplots(figsize=(8, 8))

	nx.draw_networkx_edges(G, pos, ax=ax, arrows=True)

	for uid, (x, y) in pos.items():
			response = requests.get(users[uid].img_url)
			img = Image.open(BytesIO(response.content))

			imagebox = OffsetImage(img, zoom=0.3) # type: ignore
			ab = AnnotationBbox(imagebox, (x, y), frameon=False)
			ax.add_artist(ab)

			ax.text(x, y - 0.1, users[uid].name, ha='center', va='top')

	ax.set_axis_off()
	plt.show()
