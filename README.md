# Python Programming Assignment 3

## 🎯 作业目标
通过 5 道编程题目，巩固 Python 中的：

条件判断语句（if / elif / else）；

循环语句（for / while）；

逻辑控制与格式化输出；

简单数据统计与文本处理。

### 任务 1：数字分类

任务：
输入一个整数 n，输出：

- ``Even``：偶数；
- ``Odd and multiple of 3``：奇数且是 3 的倍数；
- ``Odd``：其他奇数。

示例：

```bash
输入：9
输出：Odd and multiple of 3
```

📄 文件名：``src/q1_number_classify.py``
📦 函数名：``classify(n: int) -> str``

### 任务 2：累加与筛选

输入正整数 n（1 <= n <= 1000），计算并输出 1~n 中能被 3 或 5 整除但不能同时被两者整除的数字之和。

示例：

```bash
输入：10
输出：33
```

📄 文件名：``src/q2_sum_filter.py``
📦 函数名：``special_sum(n: int) -> int``

### 任务 3：九九乘法表

输出 1-9 的乘法表，每行 i 打印 1-i 的乘积，列之间用制表符 ``\t`` 分隔。

输出示例：

```bash
1*1=1
1*2=2	2*2=4
1*3=3	2*3=6	3*3=9
...
```

📄 文件名：``src/q3_multiplication_table.py``
📦 函数名：``table_lines() -> list[str]``

### 任务 4：猜数字游戏

程序随机生成一个 ``[1,100]`` 之间的整数；
用户反复输入猜测：

太大 → ``Too high!``

太小 → ``Too low!``

猜对 → ``Congratulations! You got it in X tries.``

示例：

```bash
Guess a number (1-100): 50
Too low!
Guess a number (1-100): 75
Too high!
Guess a number (1-100): 62
Congratulations! You got it in 3 tries.
```

📄 文件名：``src/q4_guess_number.py``
📦 函数名：``play(input_fn=input, print_fn=print)``

### 任务 5：求一元二次方程的实根

输入三个实数 $a$, $b$, $c$，表示方程

$$
ax^2 + bx + c = 0
$$

的系数。请计算并输出它的 **实根**。

- 若有两个不同实根，输出两个根，按从小到大排列； 
- 若有一个实根（判别式为 0），只输出一个； 
- 若无实根，输出 ``"No real roots"``。

示例：

```bash
输入：1 -3 2
输出：1.0 2.0
```

```bash
输入：1 2 1
输出：-1.0
```

```bash
输入：1 1 1
输出："No real roots"
```

📄 文件名：``src/q5_quadratic_solver.py``
📦 函数名：``solve_quadratic(a: float, b: float, c: float) -> list[float] | str``

✅ 提示： 使用 ``math.sqrt()`` 计算平方根。
✅ 要求： 若有两个根，返回排序后的浮点数列表。

## 本地运行与测试

### 运行单题

```bash
python src/q1_number_classify.py
```

### 运行全部测试

```bash
pip install -r requirements.txt
pytest -q
```

    GitHub Classroom 会自动运行这些测试，检测程序输出是否正确。

## 注意事项

- 请勿修改 `tests/` 文件夹里的内容。
- 代码要加注释，变量命名清晰。
- 所有题目必须使用函数封装； 
- 禁止抄袭（系统可检测相似度）； 
- 提交前确认测试全部通过。
