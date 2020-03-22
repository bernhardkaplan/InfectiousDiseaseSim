import utils
import json_tricks

class Parameters(dict):
    def __init__(self, sim_id=0, seed=0, output_folder=None):
        self.__setitem__('sim_id', sim_id)
        self.__setitem__('seed', seed)
        self.__setitem__('dt', 1)
        self.set_rates()
        self.set_init_values()
        self.paths = Paths(sim_id, output_folder)
        self.set_rates()
        self.export_parameters()

    def set_sim_parameters(self):
        self.__setitem__('n_steps', 1000)

    def set_init_values(self):
        self.__setitem__('y_init', 1.) # healthy (not recovered)
        self.__setitem__('x_init', 0.) # infected
        self.__setitem__('z_init', 0.) # dead
        self.__setitem__('w_init', 0.) # recovered
        self.__setitem__('t_init', 0 ) # time

    def set_rates(self):
        # rates for state transitions
        self.rates = {
                'r_yx' : 0.1,           # rate for healthy -> infected
                'p_x' : (1e-3, 1e-4),   # chance for infected people coming from external
                'r_xz' : 1e-4,          # rate for infected -> dead
                'r_xw' : 1e-3,          # rate for infected -> recovered
                }
        # as this class is inherited from dict,
        # we'd like to access all parameters directly
        # without using a seperate dict
        # using the dict above is more for coding convenience
        for k, v in self.rates.items():
            self.__setitem__(k, v)

    def export_parameters(self):
        with open(self.paths['param_fn'], 'w') as f:
            json_tricks.dump(self, f)


class Paths(dict):
    def __init__(self, sim_id, output_folder=None):
        self.set_folders(output_folder)
        self.set_base_filenames()
        self.set_filenames(sim_id)

    def set_folders(self, output_folder):
        if output_folder == None:
            output_folder = 'sim_results/'
        else:
            assert(type(output_folder) == str)
            if not output_folder.endswith('/'):
                output_folder += '/'
        self.folders = {
                'output_folder' : output_folder,
                }
        for k, v in self.folders.items():
            self.__setitem__(k, v)
            utils.check_folder(v)

    def set_base_filenames(self):
        self.base_fns = {
                'sim_output_fn_base' : ('corona_sim', '.csv'),
                'param_fn_base' : ('parameters', '.json'),
                }

    def set_filenames(self, sim_id):
        for k, v in self.base_fns.items():
            new_key = k.split('_base')[0]
            new_value = self.__getitem__('output_folder') + v[0] + '_' + str(sim_id) + v[1]
            self.__setitem__(new_key, new_value)

    def get_filename(self, key):

        pass
