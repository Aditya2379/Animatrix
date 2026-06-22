#manim -pql pythagoras.py PythagoreanTheoremProof

from manim import *

class PythagoreanTheoremProof(Scene):
    def construct(self):
        # Define the right triangle
        triangle = Polygon(
            [0, 0, 0],
            [3, 0, 0],
            [0, 4, 0],
            stroke_color=WHITE,
            fill_color=BLUE,
            fill_opacity=0.5
        )

        # Define labels for sides
        a_label = MathTex("a").next_to(triangle.get_vertices()[2], UP)
        b_label = MathTex("b").next_to(triangle.get_vertices()[1], RIGHT)
        c_label = MathTex("c").next_to(triangle.get_center(), UR, buff=0.2)

        # Create labels for the sides of the triangle
        side_a = Line(triangle.get_vertices()[0], triangle.get_vertices()[2], stroke_color=RED)
        side_b = Line(triangle.get_vertices()[0], triangle.get_vertices()[1], stroke_color=GREEN)
        side_c = Line(triangle.get_vertices()[2], triangle.get_vertices()[1], stroke_color=YELLOW)

        # Create labels for the side lengths
        a_val = MathTex("a").move_to(side_a.get_midpoint() + UP * 0.3)
        b_val = MathTex("b").move_to(side_b.get_midpoint() + RIGHT * 0.3)
        c_val = MathTex("c").move_to(side_c.get_midpoint() + UR * 0.3)

        # Draw the squares on each side
        square_a = Square(side_length=side_a.get_length(), fill_color=RED, fill_opacity=0.5)
        square_a.move_to(triangle.get_vertices()[0]).align_to(side_a, direction=DOWN)
        square_a.rotate(PI / 2, about_point=triangle.get_vertices()[0])

        square_b = Square(side_length=side_b.get_length(), fill_color=GREEN, fill_opacity=0.5)
        square_b.move_to(triangle.get_vertices()[0]).align_to(side_b, direction=LEFT)

        square_c = Square(side_length=side_c.get_length(), fill_color=YELLOW, fill_opacity=0.5)
        square_c.move_to(triangle.get_center()).align_to(side_c, direction=UP)
        square_c.rotate(PI / 2, about_point=triangle.get_vertices()[2])
        square_c.rotate(PI / 2, about_point=triangle.get_vertices()[1])


        # Display the identity
        identity = MathTex("a^2 + b^2 = c^2").next_to(triangle, DOWN, buff=2)

        # Animation
        self.play(
            Create(triangle),
            Write(a_val),
            Write(b_val),
            Write(c_val)
        )
        self.play(
            Create(square_a),
            Create(square_b),
            Create(square_c)
        )
        self.play(Write(identity))
        self.wait(2)