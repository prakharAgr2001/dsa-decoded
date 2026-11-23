from engine.nbspec import *
# Classic. Numbers: compute.py E17 ([4,2,7,1,8,3], k=3: sums 13, 10, 16, 12 -> max 16, avg 5.33)
EP = epd('S1E17', 'Maximum Average Subarray I', 'Sliding window', 'Easy', 'maximum-average-subarray-i', hook='slide, do not re-add')
A = [4, 2, 7, 1, 8, 3]
S = [
 ('The first sliding window question every interviewer expects you to know cold.', hook(big='Sliding window', sub='the starter', at_co='first', at_lpa='window')),
 ('Find the group of 3 neighbours with the biggest average.', ques('3 neighbours in a row', 'with the biggest average')),
 ('Numbers: 4, 2, 7, 1, 8, 3. Best group: 7, 1, 8. Sum 16.', ex(A, 'Numbers: 4, 2, 7, 1, 8, 3.', big='7 + 1 + 8 = 16', big_at='best', ev=[['best', dict(win=[2, 4, 'g'])]])),
 ('Re-adding every group from scratch is n times k work. Wasteful.',
  dict(h=dict(t='Brute force: re-add every group', at=.05), lines=[L('each window: add k numbers again', 'every', 'blk'), L('✗ O(n·k)', 'wasteful', 'red', 74)])),
 ('The trick: slide the window. Add the number coming in, subtract the number going out.',
  dict(lines=[L('sum += incoming', 'add', 'grn', 60, b=True), L('sum −= outgoing', 'subtract', 'red', 60, b=True)], ev=[['slide', dict(win=[0, 2, 'g'])]])),
 ('First window: 13. Slide: plus 1, minus 4, 10. Plus 8, minus 2, 16. Plus 3, minus 7, 12. Best is 16.',
  dict(table=T(['window', 'in', 'out', 'sum'], [['4 2 7', '', '', 13], ['2 7 1', 1, 4, 10], ['7 1 8', 8, 2, 16], ['1 8 3', 3, 7, 12]], [260, 150, 150, 200]),
       ev=[[0.05, dict(win=[0, 2, 'g'])], ['13', dict(row=0)], ['10', dict(win=[1, 3, 'g'], row=1)], ['16#1', dict(win=[2, 4, 'g'], row=2)], ['12', dict(win=[3, 5, 'g'], row=3)], ['best', dict(win=[2, 4, 'g'], st='max = [16] → avg 5.33')]])),
 ('Each number enters once and leaves once. O of n.', cx('O(n) time · O(1) space', 'O(n·k)', 'Sliding window', 'add incoming, drop outgoing')),
 ('Comment NOTES, and I will send you five more sliding window questions.', cta('5 more sliding-window questions')),
]
NARRATION, NB = build(S, 'num', A)
