from dataclasses import dataclass

@dataclass
class Mat:
	num_1: int
	num_2: int
	
	def add(self):
		return self.num_1 + self.num_2
	
	def subtract(self):
		return self.num_1 - self.num_2


if __name__=="__main__":
	m = Mat(15,5)
	print(m.add())