from manim import *
from dayira import *

color_primary = "#13315c"
color_secondary = "#f9dc5c"
color_accent = "#ffffff"
config.background_color = color_primary
custom_font = "Candara"
config.pixel_height = 1280
config.pixel_width = 720


class MyScene(Scene):
    def construct(self):

        text = MathTex(r"\frac{2}{3}").scale(4)
        text.set_color(color_accent)
        self.play(Write(text))
        self.wait(2)

        self.play(text.animate.shift(UP * 7))
        self.wait(1)

        slices, apply_effects = create_fraction_circle_with_effects(
            radius=2, 
            num_slices=6, 
            slice_color=color_accent,
            indicate_color=color_secondary, 
            remained_opacity=0.05,
            start_angle=PI/3,
            explode_distance=0.2, 
            indicate_indices=[0],
            indicate_scale=1.2, 
            indicate_delay=0.5,
            color_delay_for_remained_slices=0.5,
            slice_stroke_width=1
        )

        slices.shift(ORIGIN + DOWN * 3)
        slices.scale(2.5)
        self.play(FadeIn(slices))
        self.wait(2)

        apply_effects(self)
        self.wait(3)
        self.play(FadeOut(slices), FadeOut(text))
        self.wait(2)
