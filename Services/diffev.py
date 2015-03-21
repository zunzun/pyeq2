from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import
import numpy, numpy.random

'''
Differential Evolution Optimization

:Author: Robert Kern

Copyright 2005 by Robert Kern.

Licence:
Copyright (c) 2001, 2002 Enthought, Inc.

All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

  a. Redistributions of source code must retain the above copyright notice,
     this list of conditions and the following disclaimer.
  b. Redistributions in binary form must reproduce the above copyright
     notice, this list of conditions and the following disclaimer in the
     documentation and/or other materials provided with the distribution.
  c. Neither the name of the Enthought nor the names of its contributors
     may be used to endorse or promote products derived from this software
     without specific prior written permission.


THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH
DAMAGE.
'''

# heavily edited from original code
class DiffEvolver(object):

    def __init__(self, func, pop0, crossover_rate, scale, prng):
        self.func = func
        self.population = numpy.array(pop0)
        self.npop, self.ndim = self.population.shape
        self.crossover_rate = crossover_rate
        self.prng = prng
        self.scale = scale
        self.generations = 0

        self.pop_values = [self.func(m) for m in self.population]
        bestidx = numpy.argmin(self.pop_values)
        self.best_vector = self.population[bestidx]
        self.best_value = self.pop_values[bestidx]


    # heavily edited from original code
    def solve(self, sufficientSolution, newgens=100):
        
        # Did generation zero already reach a sufficient solution?
        if self.best_value <= sufficientSolution:
            gen = 0
            return self.best_vector

        for gen in xrange(1, newgens+1):
            randints = numpy.random.random_integers(0, self.npop-1, (self.npop, 2))
            for candidate in range(self.npop):
                i1, i2 = randints[candidate]
                
                # this is the "difference" in differential evolution
                diff1 = self.scale * (self.population[i1] - self.population[i2])

                # crossover,  or "mating" probability with the "fittest" individual
                trial = numpy.where(self.prng.rand(self.ndim) < self.crossover_rate, self.best_vector + diff1, self.population[candidate])

                trial_result = self.func(trial)
                
                # this is the "evolution" in differential evolution, also called "survival of the fittest"
                if numpy.isfinite(trial_result) and numpy.isfinite(self.pop_values[candidate]) and trial_result < self.pop_values[candidate]:
                    self.population[candidate] = trial
                    self.pop_values[candidate] = trial_result
                    if trial_result < self.best_value:
                        self.best_vector = trial
                        self.best_value = trial_result

            if max(self.pop_values) - min(self.pop_values) <= 1.0E-6:
                break
            if self.best_value <= sufficientSolution:
                break
        self.generations = gen
        return self.best_vector
