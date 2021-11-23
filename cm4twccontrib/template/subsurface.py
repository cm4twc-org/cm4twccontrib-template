import cm4twc


class SubSurfaceComponent(cm4twc.component.SubSurfaceComponent):
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
    def initialise(self, state_name, parameter_name, constant_name, **kwargs):
        pass

    def run(self,
            # transfers from other components
            evaporation_soil_surface, evaporation_ponded_water,
            transpiration, throughfall, snowmelt, water_level,
            # intrinsic component variables
            input_name, parameter_name, constant_name, state_name,
            **kwargs):
        return (
            # transfers to other components
            {
                'surface_runoff': 0,
                'subsurface_runoff': 0,
                'soil_water_stress': 0
            },
            # intrinsic component outputs
            {
                'output_name': 0
            }
        )

    def finalise(self, state_name, parameter_name, constant_name, **kwargs):
        pass
