import numpy as np

# Importing standard Qiskit libraries
from qiskit import QuantumCircuit, transpile, Aer, IBMQ
from qiskit.tools.jupyter import *
from qiskit.visualization import *
from qiskit.providers.aer import QasmSimulator

from qiskit.providers.ibmq import least_busy
from qiskit import assemble
from qiskit.visualization import plot_histogram
from qiskit.tools.monitor import job_monitor
from QAOA import *
from graph import * 
from distance import *
from scipy.optimize import minimize
from qiskit.test.mock import FakeProvider


# Loading your IBM Quantum account(s)
IBMQ.save_account('459bae2c9f5515389b12ccadc82836b5872efac3efc856c982715acee8e3ccaa9b10d04704743128f3c9155fec9ed64b8f92627bc3928e4b343b0425e926af2c')
IBMQ.load_account()

fake_provider = FakeProvider()
print(fake_provider.backends())
# provider = IBMQ.get_provider(hub='ibm-q-skku', group='snu', project='snu-graduate')
# backend = least_busy(provider.backends(filters=lambda x: x.configuration().n_qubits >= 7 and
#                                     not x.configuration().simulator and x.status().operational==True))
# print("least busy backend: ", backend)

"""
data = np.load("../data/drug145_5.npy")
xdata = data[:, 1:]

# 노드 개수 
data_num = 4
#p 개수 
p_list = list(range(1, 10))

#data import 
# data = np.load("../data/drug145_5.npy")
# data = data[:data_num, 1:]

#Sweep! 
results = []
for func in distance_func_list:
    graph = generate_graph(xdata[:data_num], func, draw=False)
    for p in p_list: 
        #generate beta and gammas 
        print(f"p value is {p} and using function {func}")
        params = [1.0 for i in range(2*p)]
        qaoa = Qaoa(graph=graph, simul=False, real_backend=backend)

        res = minimize(qaoa.execute_circ, 
                        params, 
                        method='COBYLA')
        print(res.fun)
        results.append(res.fun)
        print()
        """