# Copyright (c) 2025 Nadeem Khan
# All rights reserved.
# 
# This file is part of the "Dayira" project.
# Unauthorized use, modification, or distribution is prohibited.
# 
# For licensing information, refer to the LICENSE file.

from manim import *
from manim import config as manim_config
import numpy as np

# Configuration Functions
def config_vertical():
    """Apply vertical configuration to Manim."""
    config.background_color = "#0d1117"
    config.pixel_height = 1920
    config.pixel_width = 1080
    config.frame_height = 14.2
    config.frame_width = 8

def config_horizontal():
    """Apply horizontal configuration to Manim."""
    config.background_color = "#0d1117"
    config.pixel_height = 1080
    config.pixel_width = 1920
    config.frame_height = 8
    config.frame_width = 14.2

# Fraction Circle with Effects
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
    """
    # Create a VGroup to hold all the slices
    slices = VGroup()

    # If no slice_color is provided, use a default color (BLUE)
    if slice_color is None:
        slice_color = BLUE

    # Create the individual slices
    for i in range(num_slices):
        slice_start_angle = start_angle + i * 2 * PI / num_slices
        slice_end_angle = start_angle + (i + 1) * 2 * PI / num_slices
        slice_piece = Sector(
            stroke_width=slice_stroke_width,
            radius=radius,
            angle=slice_end_angle - slice_start_angle,
            start_angle=slice_start_angle,
            color=slice_color
        )
        slices.add(slice_piece)

    def animate_effects(scene):
        """Animates explosion, indication, and dimming effects on the slices."""
        # Explosion Animations
        explode_animations = []
        for i, slice_piece in enumerate(slices):
            slice_start_angle = start_angle + i * 2 * PI / num_slices
            slice_mid_angle = slice_start_angle + PI / num_slices
            shift_vector = explode_distance * np.array([np.cos(slice_mid_angle), np.sin(slice_mid_angle), 0])
            explode_animations.append(slice_piece.animate.shift(shift_vector))
        scene.play(AnimationGroup(*explode_animations), rate_func=rate_functions.rush_into)
        scene.wait(2)

        # Indicate specific slices
        if indicate_indices:
            for i in indicate_indices:
                scene.play(Indicate(slices[i], scale_factor=indicate_scale), run_time=indicate_delay)
                slices[i].set_color(indicate_color)
                slices[i].set_scale(indicate_scale)
                scene.wait(indicate_delay)

        # Dim remaining slices
        remaining_slices = [slice_piece for i, slice_piece in enumerate(slices) if i not in indicate_indices]
        scene.play(
            *[slice_piece.animate.set_opacity(remained_opacity).set_color(slice_color) for slice_piece in remaining_slices],
            run_time=color_delay_for_remained_slices
        )

    return slices, animate_effects
