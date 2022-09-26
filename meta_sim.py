from parameters import Parameters
from dynamical_system import CoronaSim

class MultipleModelRunsIdenticalParameters:
    def __init__(self, n_sim):
        # run_multiple_simulations_same_parameters
        pass

    def run_multiple_simulations_same_parameters(self):
        for i_ in range(n_sim):
            print('Running simulation {} / {}'.format(i_ + 1, n_sim))
            params = Parameters(sim_id=i_, seed=i_)
            CS = CoronaSim(params)
            CS.run_sim()

        # TODO: file name handling 


def run_single_simulation():
    params = Parameters()
    CS = CoronaSim(params)
    CS.run_sim()

def run_standard_parameters():
    params = Parameters()
    run_single_simulation(params)
    
if __name__ == '__main__':
    run_single_simulation()
