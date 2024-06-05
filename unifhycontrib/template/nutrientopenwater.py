import unifhy


class NutrientOpenWaterComponent(unifhy.component.NutrientOpenWaterComponent):
    """component description here"""

    # component definition below
    _inwards = {
        'mass_flux_of_dissolved_inorganic_carbon_from_soil_in_surface_runoff',
        'mass_flux_of_dissolved_organic_carbon_from_soil_in_surface_runoff',
        'mass_flux_of_dissolved_nitrogen_as_ammonium_from_soil_in_surface_runoff',
        'mass_flux_of_dissolved_nitrogen_as_nitrate_from_soil_in_surface_runoff',
        'mass_flux_of_dissolved_organic_nitrogen_from_soil_in_surface_runoff',
        'mass_flux_of_dissolved_phosphorus_from_soil_in_surface_runoff',
        'mass_flux_of_dissolved_calcium_from_soil_in_surface_runoff',
        'mass_flux_of_dissolved_sulfur_as_sulfate_from_soil_in_surface_runoff',
        'mass_flux_of_dissolved_silicon_from_soil_in_surface_runoff',
        'mass_flux_of_dissolved_inorganic_carbon_from_soil_in_subsurface_runoff',
        'mass_flux_of_dissolved_organic_carbon_from_soil_in_subsurface_runoff',
        'mass_flux_of_dissolved_nitrogen_as_ammonium_from_soil_in_subsurface_runoff',
        'mass_flux_of_dissolved_nitrogen_as_nitrate_from_soil_in_subsurface_runoff',
        'mass_flux_of_dissolved_organic_nitrogen_from_soil_in_subsurface_runoff',
        'mass_flux_of_dissolved_phosphorus_from_soil_in_subsurface_runoff',
        'mass_flux_of_dissolved_calcium_from_soil_in_subsurface_runoff',
        'mass_flux_of_dissolved_sulfur_as_sulfate_from_soil_in_subsurface_runoff',
        'mass_flux_of_dissolved_silicon_from_soil_in_subsurface_runoff',
        'mass_flux_of_nitrogen_as_ammonium_from_atmosphere_to_surface_due_to_deposition',
        'mass_flux_of_nitrogen_as_nitrate_from_atmosphere_to_surface_due_to_deposition',
        'mass_flux_of_sulfur_as_sulfate_from_atmosphere_to_surface_due_to_deposition',
        'mass_concentration_of_carbon_dioxide_in_air',
        'water_volume_in_surface_routing_channels',
        'water_volume_in_subsurface_routing_channels',
        'outgoing_water_volume_transport_out_of_surface_cell',
        'outgoing_water_volume_transport_out_of_subsurface_cell',
        'upward_volume_transport_of_liquid_water_between_subsurface_and_surface',        
    }
    _outwards = {}
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
    def initialise(self, input_name, state_name, parameter_name,
                   constant_name, **kwargs):
        if not self.initialised_states:
            state_name.set_timestep(-1, 0.)

    def run(
            self,
            # transfers from other components
            mass_flux_of_dissolved_inorganic_carbon_from_soil_in_surface_runoff,
            mass_flux_of_dissolved_organic_carbon_from_soil_in_surface_runoff,
            mass_flux_of_dissolved_nitrogen_as_ammonium_from_soil_in_surface_runoff,
            mass_flux_of_dissolved_nitrogen_as_nitrate_from_soil_in_surface_runoff,
            mass_flux_of_dissolved_organic_nitrogen_from_soil_in_surface_runoff,
            mass_flux_of_dissolved_phosphorus_from_soil_in_surface_runoff,
            mass_flux_of_dissolved_calcium_from_soil_in_surface_runoff,
            mass_flux_of_dissolved_sulfur_as_sulfate_from_soil_in_surface_runoff,
            mass_flux_of_dissolved_silicon_from_soil_in_surface_runoff,
            mass_flux_of_dissolved_inorganic_carbon_from_soil_in_subsurface_runoff,
            mass_flux_of_dissolved_organic_carbon_from_soil_in_subsurface_runoff,
            mass_flux_of_dissolved_nitrogen_as_ammonium_from_soil_in_subsurface_runoff,
            mass_flux_of_dissolved_nitrogen_as_nitrate_from_soil_in_subsurface_runoff,
            mass_flux_of_dissolved_organic_nitrogen_from_soil_in_subsurface_runoff,
            mass_flux_of_dissolved_phosphorus_from_soil_in_subsurface_runoff,
            mass_flux_of_dissolved_calcium_from_soil_in_subsurface_runoff,
            mass_flux_of_dissolved_sulfur_as_sulfate_from_soil_in_subsurface_runoff,
            mass_flux_of_dissolved_silicon_from_soil_in_subsurface_runoff,
            mass_flux_of_nitrogen_as_ammonium_from_atmosphere_to_surface_due_to_deposition,
            mass_flux_of_nitrogen_as_nitrate_from_atmosphere_to_surface_due_to_deposition,
            mass_flux_of_sulfur_as_sulfate_from_atmosphere_to_surface_due_to_deposition,
            mass_concentration_of_carbon_dioxide_in_air,
            water_volume_in_surface_routing_channels,
            water_volume_in_subsurface_routing_channels,
            outgoing_water_volume_transport_out_of_surface_cell,
            outgoing_water_volume_transport_out_of_subsurface_cell,
            upward_volume_transport_of_liquid_water_between_subsurface_and_surface, 
            # intrinsic component variables
            input_name, parameter_name, constant_name, state_name,
            **kwargs
    ):
        return (
            # transfers to other components
            {},
            # intrinsic component outputs
            {
                'output_name': 0
            }
        )

    def finalise(self, state_name, parameter_name, constant_name, **kwargs):
        pass
