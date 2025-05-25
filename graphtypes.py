from typing import NamedTuple

class UserNode(NamedTuple):

	id_: str
	name: str
	image: str

class Edge(NamedTuple):

	from_: str
	to: str
	