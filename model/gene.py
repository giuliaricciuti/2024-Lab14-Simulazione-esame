from dataclasses import dataclass


@dataclass
class Gene:
    GeneID: str
    Chromosome: int

    def __eq__(self, other):
        return self.GeneID == other.GeneID

    def __hash__(self):
        return hash(self.GeneID)

