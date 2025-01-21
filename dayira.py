# Copyright (c) 2025 Nadeem Khan
# All rights reserved.
# 
# This file is part of the "Dayira" project.
# Unauthorized use, modification, or distribution is prohibited.
# 
# For licensing information, refer to the LICENSE file.

from manim import *
import numpy as np

def create_fraction_circle_with_effects(
    radius=2, 
    num_slices=6, 
    slice_color=None, 
    indicate_color=None, 
    remained_opacity=0.5, 
    start_angle=0, 
    explode_distance=0.05, 
    indicate_indices=None, 
    indicate_scale=1.1, 
    indicate_delay=0.5,
    color_delay_for_remained_slices=0.5,
    slice_stroke_width=0.001
):
    """
    Creates a fraction circle with multiple slices and applies various effects such as explosion, indication,
    and dimming for remaining slices.

    Parameters:
    radius (float): The radius of the circle (default is 2).
    num_slices (int): The number of slices to divide the circle into (default is 6).
    slice_color (Color, optional): The color for the slices (default is None, which uses BLUE).
    indicate_color (Color, optional): The color to apply to indicated slices.
    remained_opacity (float): The opacity for the non-indicated slices after effects (default is 0.5).
    start_angle (float): The starting angle for the first slice (default is 0).
    explode_distance (float): The distance by which slices explode outwards (default is 0.05).
    indicate_indices (list, optional): A list of slice indices to be indicated (default is None).
    indicate_scale (float): The scale factor for the indicated slices (default is 1.1).
    indicate_delay (float): The delay time for indicating slices (default is 0.5).
    color_delay_for_remained_slices (float): The delay time for dimming the remaining slices (default is 0.5).
    slice_stroke_width (float): The stroke width for each slice (default is 0.001).
    
    Returns:
    slices (VGroup): A VGroup containing the generated slice objects.
    animate_effects (function): A function to animate the explosion, indication, and dimming effects.
    """

    # Create a VGroup to hold all the slices
    slices = VGroup()

    # If no slice_color is provided, use a default color (BLUE)
    if slice_color is None:
        slice_color = BLUE

    # Create the individual slices based on the number of slices and the radius
    for i in range(num_slices):
        # Calculate the start and end angles for each slice
        slice_start_angle = start_angle + i * 2 * PI / num_slices
        slice_end_angle = start_angle + (i + 1) * 2 * PI / num_slices

        # Create a slice (Sector) and add it to the VGroup
        slice_piece = Sector(
            stroke_width=slice_stroke_width,
            radius=radius,
            angle=slice_end_angle - slice_start_angle,
            start_angle=slice_start_angle,
            color=slice_color  # Apply the specified color for all slices
        )
        slices.add(slice_piece)

    def animate_effects(scene):
        """
        This function defines the animations for the explosion, indication, and dimming effects on the slices.
        
        Parameters:
        scene (Scene): The scene in which to play the animations.
        """

        # Create a list to hold the explosion animations
        explode_animations = []

        # Loop over each slice and create an explosion effect
        for i, slice_piece in enumerate(slices):
            # Calculate the starting angle for each slice
            slice_start_angle = start_angle + i * 2 * PI / num_slices
            # Find the middle angle for explosion direction
            slice_mid_angle = slice_start_angle + PI / num_slices
            # Calculate the outward shift vector for the explosion
            shift_vector = explode_distance * np.array([np.cos(slice_mid_angle), np.sin(slice_mid_angle), 0])

            # Add the explosion animation for each slice
            explode_animations.append(slice_piece.animate.shift(shift_vector))

        # Play the explosion animations with a "rush into" effect
        scene.play(AnimationGroup(*explode_animations), rate_func=rate_functions.rush_into)
        scene.wait(2)

        # Indicate specific slices if requested
        if indicate_indices:
            for i in indicate_indices:
                # Scale the indicated slice and change its color
                scene.play(
                    Indicate(slices[i], scale_factor=indicate_scale), run_time=indicate_delay
                )
                slices[i].set_color(indicate_color)
                slices[i].set_scale(indicate_scale)  # Maintain scale after indication
                scene.wait(indicate_delay)

        # Dim the remaining slices that were not indicated
        remaining_slices = [slice_piece for i, slice_piece in enumerate(slices) if i not in indicate_indices]
        scene.play(
            *[slice_piece.animate.set_opacity(remained_opacity).set_color(slice_color) for i, slice_piece in enumerate(remaining_slices)],
            run_time=color_delay_for_remained_slices
        )

    # Return the slices and the animate_effects function to be used in the scene
    return slices, animate_effects
