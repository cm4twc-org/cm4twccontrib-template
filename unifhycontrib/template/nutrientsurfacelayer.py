import unifhy


class NutrientSurfaceLayerComponent(unifhy.component.NutrientSurfaceLayerComponent):
    """component description here"""

    # component definition below
    _inwards = {}
    _outwards = {
        'mass_flux_of_nitrogen_as_ammonium_from_atmosphere_to_surface_due_to_deposition',
        'mass_flux_of_nitrogen_as_nitrate_from_atmosphere_to_surface_due_to_deposition',
        'mass_flux_of_sulfur_as_sulfate_from_atmosphere_to_surface_due_to_deposition',
        'mass_concentration_of_carbon_dioxide_in_air'
        }
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
    def initialise(self, input_name, state_name, parameter_name,
                   constant_name, **kwargs):
        if not self.initialised_states:
            state_name.set_timestep(-1, 0.)

    def run(
            self,
            # insert transfers from other components here
            # intrinsic component variables
            input_name, parameter_name, constant_name, state_name,
            **kwargs
    ):
        return (
            # transfers to other components
            {
                'mass_flux_of_nitrogen_as_ammonium_from_atmosphere_to_surface_due_to_deposition': 0,
                'mass_flux_of_nitrogen_as_nitrate_from_atmosphere_to_surface_due_to_deposition': 0,
                'mass_flux_of_sulfur_as_sulfate_from_atmosphere_to_surface_due_to_deposition': 0,
                'mass_concentration_of_carbon_dioxide_in_air': 0
            },
            # intrinsic component outputs
            {
                'output_name': 0
            }
        )

    def finalise(self, state_name, parameter_name, constant_name, **kwargs):
        pass
