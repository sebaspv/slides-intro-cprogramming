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
        pres = Title("Presentación")
        yo = Paragraph(
            "• Yo: Sebastian (obvio todos me dicen Sebas)",
            "• Finalista Regional ICPC Mexico 2024",
            "• Vicepresidente de CAP",
            "• Co-organizador de Code Rush 2025",
            "• Algunas internships (y voy a explicar pq)",
        )
        yo.scale(0.7)
        self.play(FadeIn(Group(pres, yo)))
        self.next_slide()
        self.play(FadeOut(Group(pres, yo)))
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
            "• Tip: Identificar (y conocer) tipos de problemas",
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
        self.next_slide()
        self.play(FadeOut(t2))
        t3 = Paragraph(
            "• Tip: Trabajo en equipo!",
            "\t- Practicar programar en una hoja de papel (en serio)",
            "\t- Practicar generar casos de prueba",
        )
        t3.scale(0.7)
        self.play(FadeIn(t3))
        self.next_slide()
        self.play(FadeOut(Group(htbcomp, t3)))
        pract_title = Title("Práctica, práctica, práctica")
        self.play(FadeIn(pract_title))
        t4 = Paragraph(
            "• Jueces en línea: lugares para practicar ejercicios",
            "\t- Codeforces (https://codeforces.com/)",
            "\t- AtCoder (https://atcoder.jp/)",
            "\t- Kattis (https://www.kattis.com/)",
        )
        t4.scale(0.7)
        self.play(FadeIn(t4))
        self.next_slide()
        self.play(FadeOut(Group(pract_title, t4)))
        status_title = Title("El arte de probar código")
        t5 = Paragraph(
            "• Al final del día solo queremos un AC :)",
            "• Aun así, puede que recibamos: :(",
            "\t-Error de presentación (PE)",
            "\t-Respuesta incorrecta (WA)",
            "\t-Tiempo límite excedido (TLE)",
            "\t-Memoria límite excedida (MLE)",
            "\t-Error de ejecución (RTE)",
        )
        t5.scale(0.7)
        self.play(FadeIn(Group(t5, status_title)))
        self.next_slide()
        self.play(FadeOut(Group(t5, status_title)))
        self.play(
            FadeIn(
                Group(
                    Paragraph("¡Comenzemos esta aventura juntos!", "Muchas gracias :)")
                )
            )
        )
