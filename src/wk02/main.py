from manim import *
from manim_slides import Slide


class DSAlgo(Slide):
    def construct(self):
        dsaint = Paragraph(
            "¡Bienvenido!",
            "Programación Competitiva 101",
            "Sesión 2: Introducción a DS",
            alignment="left",
        )
        self.play(FadeIn(dsaint))
        self.next_slide()
        self.play(FadeOut(dsaint))
        dslib = Paragraph(
            "DS con la librería estándar 'std::'",
        )
        self.play(FadeIn(dslib))
        self.next_slide()
        dslibnext = Title("DS con la librería estándar 'std::'")
        self.play(Transform(dslib, target_mobject=dslibnext))
        code1 = """
        #include <bits/stdc++.h>

        using namespace std;
        """
        dscontent = Code(
            code_string=code1,
            language="cpp"
        )
        self.play(FadeIn(dscontent))
        self.next_slide()
        self.play(FadeOut(dscontent))
        nuev = Title("Vectores - Arreglos dinámicos")
        code2 = """
        vector<int> numeros;
        numeros.push_back(1);
        numeros.push_back(2);
        numeros.pop_back();
        numeros.size();
        cout << numeros[0]; // 1
        """
        vec2 = Code(
            code_string=code2,
            language="cpp"
        )
        self.play(FadeIn(vec2))
        self.play(Transform(dslib, nuev))
