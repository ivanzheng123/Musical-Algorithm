from random import choices, randint, randrange, random, sample
from typing import List, Optional, Callable, Tuple

Genome = List[int]
Population = List[Genome]
FitnessFunc = Callable[[Genome], int]

#generates the genomes of k length
def gen_genome(length: int) -> Genome:
    return choices ([0,1], k=length)

#gets the most favorable genomes and splits it at a certain point to merge it into each other
def crossover_func(gen1: Genome, gen2: Genome) -> Tuple[Genome, Genome]:
    if len(gen1) < 2:
        return gen1, gen2
    
    randNum = randint(1, len(gen1) - 1)
    return gen1[0:randNum] + gen2[randNum:], gen1[randNum:] + gen2[0:randNum]


#randomly mutates a genome and changes the number on the genome which changes the notes played
def mutation(genome: Genome, num: int=1, probability: float = 0.5) -> Genome:
    for i in range(num):
        index = randrange(len(genome))
        genome[index] = genome[index] if random() > probability else abs(genome[index] - 1)
    return genome

#selects the actual population going to the next generation
def selection_pair(pop: Population, fit: FitnessFunc) -> Population:
    return sample(
        population = generate_weighted_distribution(pop, fit),
        k = 2
    )

#determine if gene pool goes to next generation depending on user rating
def generate_weighted_distribution(pop: Population, fit: FitnessFunc) -> Population:
    result = []
    
    for gene in pop:
        result += [gene] * int(fit(gene)+1)
    return result






