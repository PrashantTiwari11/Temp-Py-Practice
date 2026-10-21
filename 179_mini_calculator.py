"""Arithmetic-only calculator using AST parsing; does not evaluate arbitrary Python."""
import ast,operator,math
OPS={ast.Add:operator.add,ast.Sub:operator.sub,ast.Mult:operator.mul,ast.Div:operator.truediv,ast.FloorDiv:operator.floordiv,ast.Mod:operator.mod,ast.Pow:operator.pow,ast.UAdd:operator.pos,ast.USub:operator.neg}
def calc(expr):
 def visit(n):
  if isinstance(n,ast.Expression): return visit(n.body)
  if isinstance(n,ast.Constant) and type(n.value) in (int,float): return n.value
  if isinstance(n,ast.UnaryOp) and type(n.op) in OPS: return OPS[type(n.op)](visit(n.operand))
  if isinstance(n,ast.BinOp) and type(n.op) in OPS:
   a,b=visit(n.left),visit(n.right)
   if isinstance(n.op,ast.Pow) and abs(b)>10: raise ValueError("Exponent too large.")
   x=OPS[type(n.op)](a,b)
   if not math.isfinite(float(x)) or abs(x)>1e100: raise ValueError("Result too large.")
   return x
  raise ValueError("Use numbers and arithmetic operators only.")
 return visit(ast.parse(expr,mode="eval"))
def main():
 hist=[]
 while True:
  s=input("Expression (history/clear/exit): ").strip()
  if s=="exit": break
  if s=="history":
   print("\n".join(hist) if hist else "No history."); continue
  if s=="clear": hist.clear(); print("Cleared."); continue
  try: line=f"{s} = {calc(s)}"; print(line); hist.append(line)
  except (SyntaxError,ValueError,ZeroDivisionError,OverflowError) as e: print("Invalid:",e)
if __name__=="__main__": main()
