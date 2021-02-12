class Stack:

     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)


class BracketCheker():

  def __check_bracket_paired(self, open_bracket, close_bracket):
    return close_bracket == '}' and open_bracket == '{' or\
        close_bracket == ')' and open_bracket == '(' or\
        close_bracket == ']' and open_bracket == '['

  def check(self, line):

    bracket_stack = Stack()

    for i in range(len(line)):
      bracket = line[i]
      if bracket  in '{([':
        bracket_stack.push(bracket)
      if bracket in '])}':
        if not bracket_stack.isEmpty():
          close_bracket = bracket
          open_bracket = bracket_stack.pop()
          if not self.__check_bracket_paired(open_bracket, close_bracket):
            return False
        else:
          return False

    if not bracket_stack.isEmpty():
      return False

    return True


def assert_equal(actual, expected):
  return expected == actual


cheker = BracketCheker()

print(assert_equal(cheker.check(''), True), end=' ')
print(assert_equal(cheker.check('abc'), True), end='\n')

print(assert_equal(cheker.check('{([])}'), True), end=' ')
print(assert_equal(cheker.check('a{b(c[d]e)f}g'), True), end='\n')

print(assert_equal(cheker.check('{(})'), False), end=' ')
print(assert_equal(cheker.check('abc{def(g}hi)jk'), False), end='\n')

print(assert_equal(cheker.check('(){}[]'), True), end=' ')
print(assert_equal(cheker.check('(abc){def}g[hik]lm'), True), end='\n')

print(assert_equal(cheker.check('{([])([{])}'), False), end=' ')
print(assert_equal(cheker.check('{a(bc[d]ef)ghi(jkim[{nop]qr)stu}vwxyz'), False), end='\n')

print(assert_equal(cheker.check('[()}]'), False), end=' ')
print(assert_equal(cheker.check('abc[def(ghi)jkim}nop]'), False))