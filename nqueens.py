print("hello quenns")
import random
import sys


class Solver_8_queens(object):
    """docstring"""

    def __init__(self, pop_size=100, cross_prob=0.5, mut_prob=0.25):
        """Constructor"""
        self.pop_size = pop_size
        self.cross_prob = cross_prob
        self.mut_prob = mut_prob
        self.best_fit = 0
        self.epoch_num = 0
        self.visualization="ff\nff"
        row = 8
        col = 2
        self.pop = [[[self.rnd(nrow,ncol) for ncol in range(col)] for nrow in range(row)]for npop_size in range(pop_size)]

    def vis(self,p):
        row = 8
        col = 8
        n = 8
        nrow = 0
        res = ""
        tr = ""
        while nrow < row:
            ncol = 0
            while ncol < col:
                nn = 0
                while nn < n:
                    if p[nn][0] == nrow and p[nn][1] == ncol:
                        tr = "Q"
                        break
                    else:
                        tr = "+"
                    nn = nn + 1
                res = res + tr
                ncol = ncol + 1
            res = res + "\n"
            nrow = nrow + 1
        #res=str(p)
        return (res)

    def rnd(self,row,col):
        if col == 0:
            res = row
        else:
            res = random.randint(0,7)
        return (res)

    def fit(self,p):
        res = 1
        tr0 = 0
        while tr0 < 8:
            tr1 = 0
            while tr1 < 8:
                if p[tr0][0] == p[tr1][0] and tr0 != tr1:
                    res = res - 0.06
                if p[tr0][1] == p[tr1][1] and tr0 != tr1:
                    res = res - 0.06
                if p[tr0][0] - p[tr0][1] == p[tr1][0] - p[tr1][1] and tr0 != tr1:
                    res = res - 0.06
                tr1 = tr1 + 1
            tr0 = tr0 + 1
        if res < 0:
            res = 0.01
        return (res)

    def cross(self,p1,p2):
        i = 0
        while i < 8:
            tmp1 = str(bin(p1[i][1]))[2:]
            if len(tmp1) == 1:
                tmp1 = "00" + tmp1
            if len(tmp1) == 2:
                tmp1 = "0" + tmp1
            tmp2 = str(bin(p2[i][1]))[2:]
            if len(tmp2) == 1:
                tmp2 = "00" + tmp2
            if len(tmp2) == 2:
                tmp2 = "0" + tmp2
            r = random.randint(1, 2)
            tmp1left = tmp1[:r]
            tmp1right = tmp1[r:]
            tmp2left = tmp2[:r]
            tmp2right = tmp2[r:]
            tmp1 = tmp1left + tmp2right
            tmp2 = tmp2left + tmp1right
            tmp1 = int("0b" + tmp1, 2)
            tmp2 = int("0b" + tmp2, 2)
            p1[i][1] = tmp1
            p2[i][1] = tmp2
            i = i + 1

        return (p1,p2)

    def mutation(self,p):
        i = random.randint(0, 7)
        tmp = str(bin(p[i][1]))[2:]
        if len(tmp) == 1:
            tmp = "00" + tmp
        if len(tmp) == 2:
            tmp = "0" + tmp
        r = random.randint(0, 2)
        if tmp[r] == "0":
            tmp = tmp[:r-1] + "1" + tmp[:r+1]
        else:
            tmp = tmp[:r-1] + "0" + tmp[:r+1]
        tmp = int("0b" + tmp, 2)
        p[i][1] = tmp

        return (p)

    def solve(self, min_fitness=0.95, max_epochs=100):
        bft = 0
        bind = 0
        epochs = 0
        while epochs < max_epochs:
            nft = 0
            ft = [0 for nft in range(self.pop_size)]
            sft = 0
            while nft < self.pop_size:
                ft[nft] = self.fit(self.pop[nft])
                if ft[nft] > bft:
                    bft = ft[nft]
                    bind = nft
                sft = sft + ft[nft]
                nft = nft + 1
            npr = 0
            pr = [0 for npr in range(self.pop_size)]
            while npr < self.pop_size:
                pr[npr] = ft[npr]/sft
                npr = npr + 1
            if bft <= min_fitness:
                if random.random() <= self.cross_prob:
                    i = 0
                    while i < self.pop_size:
                        if random.random() <= pr[i]:
                            j = 0
                            while j < self.pop_size:
                                if random.random() <= pr[j] and i != j:
                                    self.pop[i], self.pop[j] = self.cross(self.pop[i], self.pop[j])
                                j = j + 1
                        i = i + 1
                if random.random() <= self.mut_prob:
                    i = random.randint(0, self.pop_size - 1)
                    self.pop[i] = self.mutation(self.pop[i])
            else:
                break
            nft = 0
            bft = 0
            ft = [0 for nft in range(self.pop_size)]
            while nft < self.pop_size:
                ft[nft] = self.fit(self.pop[nft])
                if ft[nft] > bft:
                    bft = ft[nft]
                    bind = nft
                nft = nft + 1
            epochs = epochs + 1

        self.visualization=self.vis(self.pop[bind])
        self.best_fit = bft
        self.epoch_num = epochs
        """
        Stop this
        """
        return (self.best_fit, self.epoch_num, self.visualization)


print("Python version:",sys.version)

solver=Solver_8_queens()
best_fit, epoch_num, visualization=solver.solve()

#print(solver.pop[0])

print("Best solution:")
print("Fitness:",best_fit)
print("Iterations:",epoch_num)
print(visualization)
