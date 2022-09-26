import numpy as np
import copy
import pandas as pd

class CoronaSim:
    def __init__(self, params):
        self.params = params 
        self.state = {
                'y' : self.params['y_init'], 
                'x' : self.params['x_init'], 
                'z' : self.params['z_init'], 
                'w' : self.params['w_init'], 
                't' : self.params['t_init'], 
                }
        self.prev_state = copy.copy(self.state)
        self.RNG = np.random.RandomState(self.params['seed'])
        self.dt = self.params['dt']
        self.states = []
        self.output_fn = self.params.paths['output_folder'] + self.params.paths['sim_output_fn']
        
    def run_sim(self):
        for _step in range(n_steps):
            self.prev_state = copy.copy(self.state)
            for k in self.state.keys():
                self.update_state(k)
            self.states.append(copy.copy(self.state))
        self.state_log = pd.DataFrame(self.states)
        self.state_log.to_csv(self.output_fn, index=False)

    def update_state(self, state_var):
        if state_var == 'y':
            self.update_healthy()
        elif state_var == 'x':
            self.update_infected()
        elif state_var == 'z':
            self.update_dead()
        elif state_var == 'w':
            self.update_recovered()
        elif state_var == 't':
            self.state['t'] = self.prev_state['t'] + self.dt

    def update_healthy(self):
        dy = - self.params['r_yx'] * self.prev_state['y'] * self.prev_state['x']
        self.state['y'] += self.dt * dy 
        
    def update_infected(self):
        dx = self.params['r_yx'] * self.prev_state['y'] * self.prev_state['x'] \
                - self.params['r_xz'] * self.prev_state['x'] \
                - self.params['r_xw'] * self.prev_state['w'] \
                + max(0, self.RNG.normal(self.params['p_x'][0], self.params['p_x'][1]))
        self.state['x'] += self.dt * dx
        self.state['x'] = max(0, self.state['x'])

    def update_dead(self):
        dz = self.params['r_xz'] * self.prev_state['x']
        self.state['z'] += self.dt * dz

    def update_recovered(self):
        dw = self.params['r_xw'] * self.prev_state['x']
        self.state['w'] += self.dt * dw


if __name__ == '__main__':
    run_multiple_simulations_same_parameters()
