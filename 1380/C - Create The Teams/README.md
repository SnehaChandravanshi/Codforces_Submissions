<h2><a href="https://codeforces.com/contest/1380/problem/C" target="_blank" rel="noopener noreferrer">1380C — Create The Teams</a></h2>

| | |
|---|---|
| **Difficulty** | 1400 |
| **Language** | Python 3 |
| **Verdict** | ✅ Accepted |
| **Problem Link** | [Codeforces 1380C](https://codeforces.com/contest/1380/problem/C) |

## Topics
`brute force` `dp` `greedy` `implementation` `sortings`

---

## Problem Statement

<div class="header"><div class="title">C. Create The Teams</div><div class="time-limit"><div class="property-title">time limit per test</div>2 seconds</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>There are $$$n$$$ programmers that you want to split into several non-empty teams. The skill of the $$$i$$$-th programmer is $$$a_i$$$. You want to assemble the maximum number of teams from them. There is a restriction for each team: the number of programmers in the team multiplied by the minimum skill among all programmers in the team must be at least $$$x$$$.</p><p>Each programmer should belong to at most one team. Some programmers may be left without a team.</p><p>Calculate the maximum number of teams that you can assemble.</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains the integer $$$t$$$ ($$$1 \le t \le 1000$$$) — the number of test cases.</p><p>The first line of each test case contains two integers $$$n$$$ and $$$x$$$ ($$$1 \le n \le 10^5; 1 \le x \le 10^9$$$) — the number of programmers and the restriction of team skill respectively.</p><p>The second line of each test case contains $$$n$$$ integers $$$a_1, a_2, \dots , a_n$$$ ($$$1 \le a_i \le 10^9$$$), where $$$a_i$$$ is the skill of the $$$i$$$-th programmer.</p><p>The sum of $$$n$$$ over all inputs does not exceed $$$10^5$$$.</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case print one integer — the maximum number of teams that you can assemble. </p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id008246846950993756" id="id007198333342440346" class="input-output-copier">Copy</div></div><pre id="id008246846950993756">3
5 10
7 11 2 9 5
4 8
2 4 2 3
4 11
1 3 3 7
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id0003371910585146576" id="id004700007027812302" class="input-output-copier">Copy</div></div><pre id="id0003371910585146576">2
1
0
</pre></div></div></div>