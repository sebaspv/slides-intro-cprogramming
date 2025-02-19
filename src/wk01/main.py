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
        prog_comp.move_to(2.5 * UP)
        icpc.move_to(2.5 * RIGHT)
        exp_icpc = Paragraph(
            "• Resolver problemas conocidos en \nla menor cantidad de tiempo posible!",
            "\n\t- Lo suficientemente eficaz ;)",
            "\t- Conocidos - no problemas de investigación",
            "\t- Competencias a nivel (inter)nacional!",
            "\t- ICPC",
            "\t- Solo nos importan los datos del juez online",
        )
        exp_icpc.scale(0.4)
        exp_icpc.align_to(LEFT)
        exp_icpc.move_to(((2.5) * LEFT))
        icpc_slide = Group(prog_comp, icpc, exp_icpc)
        self.play(FadeIn(icpc_slide))
        self.next_slide()
        self.play(FadeOut(icpc_slide))
        ex = Title("Ejemplo: Codeforces 1030A. In Search of an Easy Problem")
        self.play(FadeIn(ex))
        self.next_slide()
        prog_types = Paragraph(
            "Existen distintos tipos de competidores:",
            '\t - El "borroso"',
            '\t - El "lento"',
            "\t - El que se rinde",
            "\t - El programador competitivo",
            "\t - El programador *muy* competitivo",
        )
        prog_types.scale(0.7)
        self.play(FadeIn(prog_types))
        self.next_slide()
        self.play(FadeOut(prog_types), FadeOut(ex))
        htbcomp = Title("¿Cómo puedo ser competitivo?")
        self.play(FadeIn(htbcomp))
        self.next_slide()
        t1 = Paragraph(
            "• Tip 1: Identificar (y conocer) tipos de problemas",
            "\t- Ad Hoc",
            "\t- Fuerza bruta",
            "\t- Programación dinámica",
            "\t- Grafos",
            "\t- Matemáticas",
            "\t- Procesamiento de Strings",
        )
        t1.scale(0.7)
        self.play(FadeIn(t1))
        self.next_slide()
        self.play(FadeOut(t1))
        t2 = Paragraph(
            "Prueba rápida de verificación:\n",
            "\t• Dados N personas y M amistades entre personas, \nencuentra el grupo de amigos más grande.\n 1 <= N <= 1000, 0 <= M <= 1000",
        )
        t2.scale(0.7)
        self.play(FadeIn(t2))
