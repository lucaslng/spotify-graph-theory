from dataclasses import dataclass

@dataclass
class User:

	uid: str
	name: str
	img_url: str
	follower_ids: list[str]
	following_ids: list[str]