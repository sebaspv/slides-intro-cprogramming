from manim import *
from manim_slides import Slide


class Intro(Slide):
    def construct(self):
        ft = Paragraph(
            "¡Bienvenido!",
            "Programación Competitiva 101",
            "Club de Algoritmia Puebla",
            alignment="left",
        )
        self.play(FadeIn(ft))
        self.next_slide()
        self.play(FadeOut(ft))
        prog_comp = Text("Programación Competitiva")
        icpc = SVGMobject("img/wk01/ICPC_Foundation_logo.svg")
        prog_comp.move_to(2.5*UP)
        icpc.move_to(2.5*RIGHT)
        exp_icpc = Paragraph(
            "• Resolver problemas conocidos en \nla menor cantidad de tiempo posible!",
            "\n\t- Lo suficientemente eficaz ;)",
            "\t- Conocidos - no problemas de investigación",
            "\t- Competencias a nivel (inter)nacional!",
            "\t- ICPC"
        )
        exp_icpc.scale(0.4)
        exp_icpc.align_to(LEFT)
        exp_icpc.move_to((2*LEFT))
        icpc_slide = Group(prog_comp, icpc, exp_icpc)
        self.play(FadeIn(icpc_slide))
        self.next_slide()
        self.play(FadeOut(icpc_slide))
        
