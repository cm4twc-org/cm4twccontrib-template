import cm4twc


class SurfaceLayerComponent(cm4twc.component.SurfaceLayerComponent):
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
    _requires_flow_direction = False
    _requires_cell_area = False

    # component implementation of initialise-run-finalise paradigm below
    def initialise(self, state_name, **kwargs):
        pass

    def run(self,
            # transfers from other components
            soil_water_stress, water_level,
            # intrinsic component variables
            input_name, parameter_name, constant_name, state_name,
            **kwargs):
        return (
            # transfers to other components
            {
                'throughfall': 0,
                'snowmelt': 0,
                'transpiration': 0,
                'evaporation_soil_surface': 0,
                'evaporation_ponded_water': 0,
                'evaporation_openwater': 0
            },
            # intrinsic component outputs
            {
                'output_name': 0
            }
        )

    def finalise(self, state_name, **kwargs):
        pass
