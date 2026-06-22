#manim -pql --flush_cache fourier_series.py

from manim import *
import numpy as np

class FourierSquareWave(Scene):
    def construct(self):
        # --- Configuration ---
        num_harmonics = 5  # Sum at least the first 5 odd harmonics
        scale_factor = 1.5
        square_wave_color = WHITE
        graph_color = YELLOW
        axis_color = GREY

        # --- Axes Setup ---

        my_axes = Axes(
            x_range=[-PI, PI, PI/2],
            y_range=[-3, 3, 1],
            x_length=8,
            y_length=5,
        )

        x_labels = VGroup(
            MathTex("-\\pi").next_to(my_axes.c2p(-PI, 0), DOWN),
            MathTex("-\\frac{\\pi}{2}").next_to(my_axes.c2p(-PI/2, 0), DOWN),
            MathTex("0").next_to(my_axes.c2p(0, 0), DOWN),
            MathTex("\\frac{\\pi}{2}").next_to(my_axes.c2p(PI/2, 0), DOWN),
            MathTex("\\pi").next_to(my_axes.c2p(PI, 0), DOWN),
        )

        axes_group = VGroup(my_axes, x_labels)

        # --- Square Wave Definition ---
        def square_wave(x):
            return scale_factor if 0 < x < PI else -scale_factor if -PI < x < 0 else 0
        square_wave_graph = my_axes.plot(square_wave,color=square_wave_color)
        square_wave_label = Tex("Square Wave").to_corner(UL)
       
        # --- Fourier Series Components ---
        colors = [RED, BLUE, GREEN, PURPLE, ORANGE]

        def get_harmonic(n, x_val):
            # Amplitude of the nth odd harmonic is 4*scale_factor / (n*PI)
            amplitude = (4 * scale_factor) / (n * PI)
            return amplitude * np.sin(n * x_val)

        harmonic_graphs = []
        current_sum_graph = my_axes.plot(lambda x: 0, color=graph_color)
        current_sum_func = lambda x: 0

        # --- Animation ---
        self.play(Create(axes_group), Write(square_wave_label))
        self.play(Create(square_wave_graph))
        self.wait(1)

        harmonic_labels = VGroup()

        for i in range(num_harmonics):
            n = 2 * i + 1  # Odd harmonic number
            color = colors[i % len(colors)]

            # Create the lambda for the current harmonic
            harmonic_func_lambda = lambda x, n_val=n: get_harmonic(n_val, x)
            harmonic_graph = my_axes.plot(harmonic_func_lambda, color=color)

            # Update the cumulative sum function and graph
            # Use lambda to ensure correct scope for current_sum_func
            previous_sum_func = current_sum_func
            current_sum_func = lambda x, p_func=previous_sum_func, h_func=harmonic_func_lambda: p_func(x) + h_func(x)
            new_sum_graph = my_axes.plot(current_sum_func, color=graph_color)

            # Create labels
            harmonic_label_text = f"sin({n}x) / {n}"
            harmonic_label = MathTex(harmonic_label_text, color=color).to_corner(DR).shift(DOWN * (i * 0.75 + 1))
            harmonic_labels.add(harmonic_label)

            sum_label = Tex(f"Sum of first {i+1} harmonics")
            # Animate the addition of the harmonic and the update of the sum
            self.play(
                Create(harmonic_graph),
                FadeIn(harmonic_label, shift=UP),
                Transform(current_sum_graph, new_sum_graph),
                FadeIn(sum_label, shift=UP),
                run_time=1.5
            )
            self.wait(0.5)

            harmonic_graphs.append((harmonic_graph, color))

        # --- Final State ---
        self.wait(2)