"""Narrow static review protocol for this str-to-runs task; not a general sandbox."""
import ast

PURE = {'len': len, 'range': range, 'min': min}
ALLOWED = (ast.Module, ast.FunctionDef, ast.arguments, ast.arg, ast.Assign, ast.AugAssign,
           ast.Name, ast.Load, ast.Store, ast.Constant, ast.List, ast.Tuple, ast.Subscript,
           ast.For, ast.While, ast.If, ast.Return, ast.Expr, ast.Call, ast.Attribute,
           ast.BinOp, ast.Add, ast.Sub, ast.Mult, ast.FloorDiv, ast.Mod,
           ast.Compare, ast.Eq, ast.NotEq, ast.Lt, ast.LtE, ast.Gt, ast.GtE,
           ast.BoolOp, ast.And, ast.Or, ast.UnaryOp, ast.Not, ast.USub, ast.Break, ast.Continue)

class PolicyError(ValueError): pass
def require(ok, code):
    if not ok: raise PolicyError(code)

def review(tree):
    require(type(tree) is ast.Module and len(tree.body)==1 and type(tree.body[0]) is ast.FunctionDef,
            'BLOCKED_TOP_LEVEL_EXECUTION')
    fn=tree.body[0];a=fn.args
    require(fn.name=='runs' and not fn.decorator_list and fn.returns is None and not fn.type_comment
            and not getattr(fn,'type_params',[]) and len(a.args)==1 and a.args[0].arg=='s'
            and a.args[0].annotation is None and not a.defaults and not a.kw_defaults
            and not a.kwonlyargs and not a.posonlyargs and a.vararg is None and a.kwarg is None,
            'BLOCKED_FUNCTION_CONTRACT')
    lists={n.targets[0].id for n in ast.walk(fn) if type(n) is ast.Assign and len(n.targets)==1
           and type(n.targets[0]) is ast.Name and type(n.value) is ast.List}
    for n in ast.walk(tree):
        require(type(n) in ALLOWED, 'BLOCKED_UNREVIEWED_SYNTAX_OR_CAPABILITY')
        if type(n) is ast.FunctionDef: require(n is fn,'BLOCKED_NESTED_FUNCTION')
        if type(n) is ast.Name:
            require(not n.id.startswith('_'),'BLOCKED_PRIVATE_NAME')
            if type(n.ctx) is ast.Store:
                require(n.id not in PURE and n.id not in ('runs','s'),'BLOCKED_BINDING_MUTATION')
        if type(n) is ast.Constant:
            require(type(n.value) in (int,str,bool,type(None)),'BLOCKED_CONSTANT_TYPE')
        if type(n) in (ast.Assign,ast.AugAssign):
            targets=n.targets if type(n) is ast.Assign else [n.target]
            for t in targets:
                require(type(t) is ast.Name or (type(t) is ast.Subscript and type(t.value) is ast.Name
                        and t.value.id in lists),'BLOCKED_MUTATION_TARGET')
        if type(n) is ast.Attribute:
            require(n.attr=='append' and type(n.value) is ast.Name and n.value.id in lists
                    and type(n.ctx) is ast.Load,'BLOCKED_ATTRIBUTE_ACCESS')
        if type(n) is ast.Call:
            require(not n.keywords and not any(type(x) is ast.Starred for x in n.args),'BLOCKED_CALL_ARGUMENTS')
            if type(n.func) is ast.Name:
                require(n.func.id in PURE,'BLOCKED_CALL_CAPABILITY')
                lo,hi={'len':(1,1),'range':(1,3),'min':(1,3)}[n.func.id]
                require(lo<=len(n.args)<=hi,'BLOCKED_CALL_ARITY')
            else:
                require(type(n.func) is ast.Attribute and n.func.attr=='append' and len(n.args)==1,
                        'BLOCKED_CALL_CAPABILITY')
    return 'STATIC_REVIEW_PURE_BUILTINS_LOCAL_LIST_ONLY'
