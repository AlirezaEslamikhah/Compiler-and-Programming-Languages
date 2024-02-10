from Gen.JavaParser import ParseTreeListener, JavaParser


class MyListener(ParseTreeListener):
    def __init__(self):
        super().__init__()

    def enterVariableDeclarator(self, ctx: JavaParser.VariableDeclaratorContext):
        line_number = ctx.start.line
        variable_name = ctx.variableDeclaratorId().Identifier().getText()
        parent_ctx = ctx.parentCtx.parentCtx
        declaration_type = parent_ctx.children[0].getText()

        if ctx.variableDeclaratorId().dims():
            array_dims = ctx.variableDeclaratorId().dims().getText()
            print(f'line {line_number}: {declaration_type}{array_dims} - name: {variable_name}')
        else:
            print(f'line {line_number}: {declaration_type} - name: {variable_name}')
