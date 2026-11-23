from engine.nbspec import *
# Classic. Numbers: compute by hand: push 5,3,7,2 -> mins 5,3,3,2; pop -> min 3
EP = epd('S1E28', 'Min Stack', 'Stack', 'Medium', 'min-stack', hook='store the min with every item')
A = [5, 3, 7, 2]
S = [
 ('A design question that looks easy, until they ask for the minimum in O of 1.', hook(big='min() in O(1)', sub='design question', at_co='design', at_lpa='minimum')),
 ('Build a stack with push, pop, and get minimum. All in O of 1.', ques('stack: push, pop, getMin', 'all in O(1)')),
 ('Push 5, 3, 7, 2. Minimum is 2. Pop. Minimum is 3.', ex(A, 'Push 5, 3, 7, 2.', big='min 2 → pop → min 3', big_at='minimum#1')),
 ('Keeping one min variable fails. Pop the 2, and you no longer know the old minimum.',
  dict(h=dict(t='One min variable?', at=.05), lines=[L('min = 2 … pop 2 → min = ?', 'pop', 'blk', 60), L('✗ old minimum is lost', 'longer', 'red', 64)])),
 ('The trick: store each item with the minimum so far. The top always knows the current minimum.',
  dict(stack=4, lines=[L('push (value, min so far)', 'store', 'blue', 58, b=True), L('getMin = top.min', 'top', 'grn', 58)])),
 ('Push 5, min 5. Push 3, min 3. Push 7, min still 3. Push 2, min 2. Pop the 2. Top says min 3.',
  dict(stack=4, ev=[['5#1', dict(ptr={'i': 0}, push='5 · min 5')], ['3#1', dict(ptr={'i': 1}, push='3 · min 3')], ['7', dict(ptr={'i': 2}, push='7 · min 3')], ['2#1', dict(ptr={'i': 3}, push='2 · min 2')],
                     ['pop', dict(pop=1, mark={3: 'dim'})], ['top', dict(st='getMin() = [3]')]])),
 ('Every operation is O of 1. Extra space O of n.', cx('O(1) per operation · O(n) space', None, 'Stack', 'pair each value with the running min')),
 ('Comment NOTES, and I will send you five more stack questions.', cta('5 more stack questions')),
]
NARRATION, NB = build(S, 'num', A)
