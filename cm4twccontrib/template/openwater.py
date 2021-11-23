import cm4twc


class OpenWaterComponent(cm4twc.component.OpenWaterComponent):
    """component description here"""

    # component definition below
    _inputs_info = {
        'input_name': {
            'kind': 'dynamic',
            'units': '1'
        }
    }
    _outputs_info = {
        'output_name': {
            'units': '1'
        }
    }
    _parameters_info = {
        'parameter_name': {
            'units': '1'
        }
    }
    _constants_info = {
        'constant_name': {
            'units': '1',
            'default_value': 1
        }
    }
    _states_info = {
        'state_name': {
            'units': '1'
        }
    }
    _requires_land_sea_mask = False
    _requires_flow_direction = True
    _requires_cell_area = False

    # component implementation of initialise-run-finalise paradigm below
    def initialise(self, state_name, **kwargs):
        pass

    def run(self,
            # transfers from other components
            evaporation_openwater, surface_runoff, subsurface_runoff,
            # intrinsic component variables
            input_name, parameter_name, constant_name, state_name,
            **kwargs):
        return (
            # transfers to other components
            {
                'water_level': 0
            },
            # intrinsic component outputs
            {
                'output_name': 0
            }
        )

    def finalise(self, state_name, **kwargs):
        pass
