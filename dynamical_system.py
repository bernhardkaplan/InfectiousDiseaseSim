import numpy as np
import copy
import pandas as pd


class CoronaSim:

    def __init__(self, output_fn, seed=0):

        self.y_init = 1. # healthy (not recovered)
        self.x_init = 0. # infected
        self.z_init = 0. # dead
        self.w_init = 0. # recovered
        self.t_init = 0  # time

        self.state = {
                'y' : self.y_init, 
                'x' : self.x_init, 
                'z' : self.z_init, 
                'w' : self.w_init,
                't' : self.t_init,
                }
        self.prev_state = copy.copy(self.state)

        self.RNG = np.random.RandomState(seed)
        # rates for state transitions
        self.r_yx = 0.1 # rate for healthy -> infected
        self.p_x = (1e-3, 1e-4) # chance for infected people coming from external
        self.r_xz = 0.0001 # rate for infected -> dead
        self.r_xw = 0.001 # rate for infected -> recovered
        self.dt = 1
        self.states = []
        self.output_fn = output_fn
        
    def run_sim(self, n_steps=100):
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
        dy = - self.r_yx * self.prev_state['y'] * self.prev_state['x']
        self.state['y'] += self.dt * dy 
        

    def update_infected(self):
        dx = self.r_yx * self.prev_state['y'] * self.prev_state['x'] \
                - self.r_xz * self.prev_state['x'] \
                - self.r_xw * self.prev_state['w'] \
                + max(0, self.RNG.normal(self.p_x[0], self.p_x[1]))
        self.state['x'] += self.dt * dx


    def update_dead(self):
        dz = self.r_xz * self.prev_state['x']
        self.state['z'] += self.dt * dz

    def update_recovered(self):
        dw = self.r_xw * self.prev_state['x']
        self.state['w'] += self.dt * dw


if __name__ == '__main__':

    CS = CoronaSim('corona_sim.csv')
    n_steps = int(1e4)
    CS.run_sim(n_steps=n_steps)


