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
        dscontent = Code(code_string=code1, language="cpp")
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
        reverse(numeros.begin(), numeros.end()) // invierte todo en O(n)
        """
        vec2 = Code(code_string=code2, language="cpp")
        self.play(FadeIn(vec2))
        self.play(Transform(dslib, nuev))
        self.next_slide()
        nuev2 = Title("Ordenar cosas")
        code3 = """
        // ordenar (recomendado)
        sort(numeros.begin(), numeros.end());
        // ordenar estable
        stable_sort(numeros.begin(), numeros.end());
        // solo necesitamos ordenar los k-primeros elementos
        partial_sort(s.begin(), s.begin() + 3, s.end());
        """
        vec3 = Code(code_string=code3, language="cpp")
        self.play(Transform(vec2, vec3))
        self.play(Transform(dslib, nuev2))
        self.next_slide()
        nuev3 = Title("Buscar cosas")
        code4 = """
        // busqueda binaria en un vector (debe estar ordenado)
        *lower_bound(numeros.begin(), numeros.end(), 4);
        *upper_bound(numeros.begin(), numeros.end(), 4);
        """
        vec4 = Code(code_string=code4, language="cpp")
        self.play(Transform(vec2, vec4))
        self.play(Transform(dslib, nuev3))
        self.next_slide()
        nuev4 = Title("Otras igual de interesantes")
        ot = Paragraph(
            "Lista Ligada: list<int> - No tan usada :)",
            "Stack: stack<int> - Tampoco tan usado - usa un vector",
            "Queue: queue<int> - Usado en BFS, Topological Sort, etc.",
            "Deque: deque<int> - Usado en algunos algoritmos con strings, sliding window...",
            "Todos cuentan con las operaciones pop() y push()",
            "Deque tiene pop_front(), pop_back(), push_front() y push_back()",
            line_spacing=0.5
        )
        ot.scale(0.5)
        self.play(Transform(dslib, nuev4))
        self.play(FadeOut(vec2))
        self.play(FadeIn(ot))
        self.next_slide()
        self.play(FadeOut(ot))
        prob1 = Title("102951B - Studying Algorithms")
        self.play(Transform(dslib, prob1))
        self.next_slide()
        nuev5 = Title("Lo jugoso - maps y sets")
        info = Paragraph(
            "Sets: BSTs con un nombre bonito",
            "\t- set<int> set_ejemplo;",
            "\t- Únicamente guardan datos únicos (como un BST)",
            "\t- Búsqueda de elementos en O(log n)",
            "\t- Inserción de elementos en O(log n)",
            "\t- Soporta lower_bound y upper_bound",
            "\t- set_ejemplo.insert(x), set_ejemplo.erase(x)",
            line_spacing=0.8
        )
        info.scale(0.5)
        self.play(Transform(dslib, nuev5))
        self.play(FadeIn(info))
        self.next_slide()
        self.play(FadeOut(info))
        nuevinfo = Paragraph(
            "Mapas: BSTs que guardan llave y valor",
            "\t- Igualito a los diccionarios/hash tables que ya conoces :)",
            "\t- map<int, int> mapa; significa que la llave es un int y el valor un int",
            "\t^ pero puede ser cualquier tipo de dato ordenable :)",
            "\t- Inserción, asignación y búsqueda en O(log n)",
            "\t- mapa[1] = 2; mapa.erase(1);",
            "\t- mapa.find(x) == mapa.end(); - el valor no se ha encontrado",
            line_spacing=0.8
        )
        nuevinfo.scale(0.5)
        self.play(FadeIn(nuevinfo))
        self.next_slide()
        self.play(FadeOut(nuevinfo))
        prob2 = Title("855A. Tom Riddle's Diary")
        self.play(Transform(dslib, prob2))
        self.next_slide()
        self.play(FadeOut(dslib))
        final = Paragraph(
            "“Those who can imagine anything, can create the impossible.”",
            "\t- Alan Turing",
            "¡Respira! Ya terminó lo feo :)"
        )
        final.scale(0.6)
        self.play(FadeIn(final))

