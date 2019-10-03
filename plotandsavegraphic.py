import matplotlib.pyplot as plt
import numpy as np
import os


class plotandsave():

    def __init__(self, logfile, path='./'):
        self._week = logfile.getWeek()
        self._totcalls = logfile.getTotCalls()

    def _operatorsTupla(self):
        return ('David', 'Emanuele', 'Pino')

    def _operatorsACalls(self):
        return (7, 8, 2)

    def plot(self, filename, path='./'):
        opNames = self._operatorsTupla()
        opNum = len(opNames)
        opCalls = self._operatorsACalls()

        fig = plt.figure()
        ind = np.arange(opNum)
        w = 0.35

        p1 = plt.bar(ind, (self._totcalls, self._totcalls, self._totcalls), w)
        p2 = plt.bar(ind, opCalls, w)

        plt.title('calls report week ' + str(self._week))
        plt.ylabel('Number of calls')
        plt.xlabel('Operators')

        plt.xticks(ind, opNames)
        plt.yticks(np.arange(0, self._totcalls + 5, 5))
        plt.legend((p1[0], p2[0]), ('Men', 'Women'))
        # fig = plt.figure()
        # plt.show()
        fullPath = os.path.join(path, str(filename))
        fig.savefig(fullPath)
        return fullPath + '.png'
