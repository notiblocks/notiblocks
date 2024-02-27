class ANSI():
    def background(ansi_code):
        return "\33[{ansi_code}m".format(ansi_code=ansi_code)
    
    def style_text(ansi_code):
        return "\33[{ansi_code}m".format(ansi_code=ansi_code)
    
    def color_text(ansi_code):
        return "\33[{ansi_code}m".format(ansi_code=ansi_code)