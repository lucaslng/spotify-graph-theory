from typing import NamedTuple

class UserNode(NamedTuple):

	id_: str
	name: str
	image: str

	def __hash__(self) -> int:
		return hash(id)

class Edge(NamedTuple):

	from_: str
	to: str
	