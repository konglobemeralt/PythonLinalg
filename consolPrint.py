Python 3.6.0 (v3.6.0:41df79263a11, Dec 22 2016, 17:23:13) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
s = {2, 3, "sdf"}
>>> "sdf" in s
True
>>> t = {2, 37, "cara"}
>>> u = s | t
>>> u
{2, 3, 37, 'sdf', 'cara'}
>>> u = s & t
>>> u
{2}
>>> | union of set
SyntaxError: invalid syntax
>>> & intersection of set
SyntaxError: invalid syntax
>>> s.add{22}
SyntaxError: invalid syntax
>>> s.add(22)
>>> s
{'sdf', 2, 3, 22}
>>> s.add(34, 34)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    s.add(34, 34)
TypeError: add() takes exactly one argument (2 given)
>>> s.add({2, 3})
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    s.add({2, 3})
TypeError: unhashable type: 'set'
>>> s.add(t)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    s.add(t)
TypeError: unhashable type: 'set'
>>> s.update(t)
>>> s
{2, 3, 37, 22, 'sdf', 'cara'}
>>> s.remove(t)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    s.remove(t)
KeyError: {2, 'cara', 37}
>>> {2 * x for x in {2, 3, 4}}
{8, 4, 6}
>>> {x for x < 10}
SyntaxError: invalid syntax
>>> {x^2 for x in {1, 2, 3, 4, 5}}
{0, 1, 3, 6, 7}
>>> 1^2
3
>>> {x**2 for x in {1, 2, 3, 4, 5}}
{1, 4, 9, 16, 25}
>>> {2**x for x in {1, 2, 3, 4, 5}}
{32, 2, 4, 8, 16}
>>> 2**1
2
>>> {2**x for x in {0, 1, 2, 3, 4}}
{1, 2, 4, 8, 16}
>>> {x*x for x in s | {2, 3}}
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    {x*x for x in s | {2, 3}}
  File "<pyshell#26>", line 1, in <setcomp>
    {x*x for x in s | {2, 3}}
TypeError: can't multiply sequence by non-int of type 'str'
>>> t
{2, 'cara', 37}
>>> s = {1, 2, 3}
>>> {x*x for x in s | {4, 5}}
{1, 4, 9, 16, 25}
>>> {x*x for x in s & {4, 5}}
set()
>>> {x*x for x om s & {1, 2, 3, 4}}
SyntaxError: invalid syntax
>>> {x*x for x in s & {1, 2, 3, 4}}
{1, 4, 9}
>>> {x*x for x in {1, 2, 4} if x == 4}
{16}
>>> {x**y for x in {1, 2, 3, 4, 5} for y in {3, 4, 5, 6}}
{32, 1, 64, 256, 1024, 4096, 8, 15625, 16, 81, 625, 243, 3125, 729, 27, 125}
>>> {x*y for x in {1, 2, 3} for y in {2, 3, 4}}
{2, 3, 4, 6, 8, 9, 12}
>>> {x*y for x in {1, 2, 3} for y in {5, 6, 7}}
{5, 6, 7, 10, 12, 14, 15, 18, 21}
>>> 
>>> {x*y for x in {1, 2, 3} for y in {4, 5, 6} if x != y }
{4, 5, 6, 8, 10, 12, 15, 18}
>>> {x*y for x in {1, 2, 3} for y in {5, 6, 0} if x != y }
{0, 5, 6, 10, 12, 15, 18}
>>> {x*y for x in {1, 2, 1} for y in {2, 3, 4} if x != y }
{2, 3, 4, 6, 8}
>>> {x*y for x in {1, 2, 0.1} for y in {5, 6, 10} if x != y }
{0.5, 1.0, 0.6000000000000001, 5, 6, 10, 12, 20}
>>> S = {1 ,2 ,3, 4}
>>> T = {3, 4, 5, 6}
>>> {x for x in S if x in T}
{3, 4}
>>> lista = [20, 10, 15, 75]
>>> sum(lista)/len(lista)
30.0
>>> andraListan = ["Hej", "World"]
>>> lista = andraListan
>>> lista = [1, 2, 4]
>>> andraListan + listan
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    andraListan + listan
NameError: name 'listan' is not defined
>>> lista + andraListan
[1, 2, 4, 'Hej', 'World']
>>> [2*x for x in {1, 2, 3, 4, 5}]
[2, 4, 6, 8, 10]
>>> [2*x for x in [1, 2, 3, 4, 5, 6]]
[2, 4, 6, 8, 10, 12]
>>> letters = ['A', 'B', 'C']
>>> numbers = [1, 2, 3]
>>> [x + y for x in numbers for y in letters ]
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    [x + y for x in numbers for y in letters ]
  File "<pyshell#56>", line 1, in <listcomp>
    [x + y for x in numbers for y in letters ]
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> [x *y for x in numbers for y in letters ]
['A', 'B', 'C', 'AA', 'BB', 'CC', 'AAA', 'BBB', 'CCC']
>>> [x.toString + y for x in numbers for y in letters ]
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    [x.toString + y for x in numbers for y in letters ]
  File "<pyshell#58>", line 1, in <listcomp>
    [x.toString + y for x in numbers for y in letters ]
AttributeError: 'int' object has no attribute 'toString'
>>> [[x, y] for x in numbers for y in letters ]
[[1, 'A'], [1, 'B'], [1, 'C'], [2, 'A'], [2, 'B'], [2, 'C'], [3, 'A'], [3, 'B'], [3, 'C']]
>>> LofLists = [[1, 2, 3, 4], [10], [5, 5], [1, 1, 2, 8]]
>>> sum(LofLists)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    sum(LofLists)
TypeError: unsupported operand type(s) for +: 'int' and 'list'
>>> sum([sum x for x in LofList])
SyntaxError: invalid syntax
>>> sum([sum(x) for x in LofList])
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    sum([sum(x) for x in LofList])
NameError: name 'LofList' is not defined
>>> sum([x for x in LofList])
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    sum([x for x in LofList])
NameError: name 'LofList' is not defined
>>> [x for x in LofList]
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    [x for x in LofList]
NameError: name 'LofList' is not defined
>>> sum([sum(x) for x in in x for x in LofList])
SyntaxError: invalid syntax
>>> sum([sum(x) for x in x for x in LofList])
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    sum([sum(x) for x in x for x in LofList])
NameError: name 'x' is not defined
>>> sum([sum(x) for x in LofList])
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    sum([sum(x) for x in LofList])
NameError: name 'LofList' is not defined
>>> ([sum(x) for x in LofList])
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    ([sum(x) for x in LofList])
NameError: name 'LofList' is not defined
>>> sum([sum(x) for x in LofLists])
42
>>> LofLists = [[.25, .75, .1,], [-1, 0], [4, 4, 4, 4]]
>>> sum([sum(x) for x in LofLists])
16.1
>>> [x, y, z, w] = [1, 2, 3, 4]
>>> x
1
>>> y
2
>>> z
3
>>> [x, y, z, w,u] = [1, 2, 3, 4]
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    [x, y, z, w,u] = [1, 2, 3, 4]
ValueError: not enough values to unpack (expected 5, got 4)
>>> [x, y, z, w] = [1, 2, 3, 4], 5
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    [x, y, z, w] = [1, 2, 3, 4], 5
ValueError: not enough values to unpack (expected 4, got 2)
>>> S = {-4, -2, 1, 2, 5, 0}
>>> ((x, y, z) for x in S for y in S for z in S if x+y+z == 0)
<generator object <genexpr> at 0x101af4bf8>
>>> {(x, y, z) for x in S for y in S for z in S if x+y+z == 0}
{(1, 1, -2), (0, -2, 2), (0, 2, -2), (2, 2, -4), (2, 0, -2), (2, -4, 2), (-2, 0, 2), (-2, 1, 1), (2, -2, 0), (-4, 2, 2), (-2, 2, 0), (0, 0, 0), (1, -2, 1)}
>>> [(x, y, z) for x in S for y in S for z in S if x+y+z == 0 if x!=y!=z!=0]
[(0, 2, -2), (0, -2, 2), (1, -2, 1), (2, 0, -2), (2, -4, 2), (-2, 0, 2)]
>>> {(x, y, z) for x in S for y in S for z in S if x+y+z == 0}
{(1, 1, -2), (0, -2, 2), (0, 2, -2), (2, 2, -4), (2, 0, -2), (2, -4, 2), (-2, 0, 2), (-2, 1, 1), (2, -2, 0), (-4, 2, 2), (-2, 2, 0), (0, 0, 0), (1, -2, 1)}
>>> [(x, y, z) for x in S for y in S for z in S if x+y+z == 0 if x!=0 && y!=0 && z!=0]
SyntaxError: invalid syntax
>>> [(x, y, z) for x in S for y in S for z in S if x+y+z == 0 if x!=0 & y!=0 & z!=0]
[]
>>> [(x, y, z) for x in S for y in S for z in S if x+y+z == 0 if (x!=0 && y!=0 && z!=0)]
SyntaxError: invalid syntax
>>> [(x, y, z) for x in S for y in S for z in S if x+y+z == 0 if (x!=0 & y!=0 & z!=0)]
[]
>>> [(x, y, z) for x in S for y in S for z in S if x+y+z == 0 && (x!=0 && y!=0 && z!=0)]
SyntaxError: invalid syntax
>>>  [(x, y, z) for x in S for y in S for z in S if x+y+z == 0 & (x!=0 && y!=0 && z!=0)]
 
SyntaxError: unexpected indent
>>> [(x, y, z) for x in S for y in S for z in S if x+y+z == 0 & (x!=0 & y!=0 & z!=0)]
[(0, 0, 0), (0, 2, -2), (0, -2, 2), (1, 1, -2), (1, -2, 1), (2, 0, -2), (2, 2, -4), (2, -4, 2), (2, -2, 0), (-4, 2, 2), (-2, 0, 2), (-2, 1, 1), (-2, 2, 0)]
>>>  [(x, y, z) for x in S for y in S for z in S if x+y+z == 0 && (x!=0 && y!=0 && z!=0)]
 
SyntaxError: unexpected indent
>>> [(x, y, z) for x in S for y in S for z in S if x+y+z == 0 && (x!=0 && y!=0 && z!=0)]
SyntaxError: invalid syntax
>>> [(x, y, z) for x in S for y in S for z in S if x+y+z == 0 & (x!=0 && y!=0 && z!=0)]
SyntaxError: invalid syntax
>>>  [(x, y, z) for x in S for y in S for z in S if x+y+z == 0 && !(x==0 & y==0 & z==0)]
 
SyntaxError: unexpected indent
>>> [(x, y, z) for x in S for y in S for z in S if x+y+z == 0 && !(x==0 & y==0 & z==0)]
SyntaxError: invalid syntax
>>> [(x, y, z) for x in S for y in S for z in S if x+y+z == 0 & !(x==0 & y==0 & z==0)]
SyntaxError: invalid syntax
>>> [(x, y, z) for x in S for y in S for z in S if x+y+z == 0 & (x!=0 & y!=0 & z!=0)]
[(0, 0, 0), (0, 2, -2), (0, -2, 2), (1, 1, -2), (1, -2, 1), (2, 0, -2), (2, 2, -4), (2, -4, 2), (2, -2, 0), (-4, 2, 2), (-2, 0, 2), (-2, 1, 1), (-2, 2, 0)]
>>> 
