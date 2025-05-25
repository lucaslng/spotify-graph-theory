from driver import create_brave_driver
from graphtypes import Edge, UserNode
from login import login
from collections import deque
from collections import defaultdict

from scraper import scrape

from pprint import pprint

from sys import maxsize


def scrape_all(session_token: str, target_id: str, max_depth: int) -> None:

	driver = create_brave_driver()

	login(driver, session_token)
	
	# time.sleep(1000000)

	dq: deque[str] = deque()
	visited: set[str] = set()
	depths: defaultdict[str, int] = defaultdict(lambda: maxsize)

	dq.append(target_id)
	depths[target_id] = 0

	nodes: set[UserNode] = set()
	nodes.add(UserNode(target_id, "origin", ""))
	edges: set[Edge] = set()

	try:
		driver.implicitly_wait(0)

		while dq:
			cur = dq.pop()
			pprint(cur)

			if cur in visited:
				continue

			if depths[cur] >= max_depth:
				continue

			following = scrape(driver, cur)
			nodes.update(following)
			edges.update([Edge(cur, followee.id_) for followee in following])
			for followee in following:
				dq.append(followee.id_)
				depths[followee.id_] = min(depths[followee.id_], depths[cur] + 1)
				print("current depth:", depths[followee.id_])
			
			visited.add(cur)
	except KeyboardInterrupt:
		pass
	finally:
		pprint(nodes)
		print()
		pprint(edges)