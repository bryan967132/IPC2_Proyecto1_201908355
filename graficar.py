class graficar:
    def dibujar(self,i,f,c,mosaico):
        mosaicodot = ''
        mosaicodot += """
    Foo"""+str(i + 1)+""" [
        label=<
            <table border="0" cellborder="1" cellspacing="0" cellpadding="4">"""
        i = 0
        while i < f:
            mosaicodot += """
                <tr>"""
            j = 0
            while j < c:
                if mosaico.get(i,j) == 'B':
                    mosaicodot += """
                    <td bgcolor = "black"></td>"""
                else:
                    mosaicodot += """
                    <td bgcolor = "white"></td>"""
                j += 1
            mosaicodot += """
                </tr>"""
            i += 1
        mosaicodot += """ 
            </table>
        >
    ];"""
        return mosaicodot
    
    def conectar(self,x):
        mosaicodot = ''
        i = 1
        while i < x:
            mosaicodot += """
    Foo""" + str(x - 1) + " -> " + "Foo" + str(x)
            i += 1
        return mosaicodot
    
    def getDot(self,cuerpo,conectado):
        mosaicodot = """digraph {
    node [shape = none]
    rankdir=DOWN;\n"""
        mosaicodot += cuerpo
        mosaicodot += conectado
        mosaicodot += """
}"""
        return mosaicodot