F = {}
F["m1_1"]='''<div class="fig"><div class="fig-t">图：一句话进车机，中间过了五道手</div><div class="flow"><div class="box b">司机说话</div><div class="box c">语音转文字</div><div class="box p">模型理解「要什么」</div><div class="box o">填成结构化意图</div><div class="box g">导航执行</div></div><div class="fig-n">最容易出错的是第三道：它不懂「顺便」「不想」「最好」这些词背后的条件，只按字面往下接</div></div>
'''
F["m3_1"]='''<div class="fig"><div class="fig-t">图：Agent 的循环，和必须同时装上的四道刹车</div><div class="flow"><div class="box b">想一步</div><div class="box c">调工具</div><div class="box p">看结果</div><div class="box o">再想一步</div><div class="box r">⛔ 轮数 / 预算 / 去重 / 无新信息即停</div></div><div class="fig-n">没有出口的循环不叫智能，叫卡死。刹车要在设计的第一天就装上，不能等出了事故再补</div></div>
'''
F["m5_1"]='''<div class="fig"><div class="fig-t">图：记忆分三层，隔离键决定串不串号</div><div class="layers"><div class="layer l1">会话层：这一趟的对话与路线 → 熄火即清</div><div class="layer l3">个人层：偏好、常去地点 → 按人隔离</div><div class="layer l5">账户层：订单、保养、权益 → 按合同授权</div></div><div class="fig-n">同一辆车里坐着两个人，每一层「记住」都要先问一句：这是谁的</div></div>
'''
F["m7_1"]='''<div class="fig"><div class="fig-t">图：客户付一次，你付一年</div><div class="bars"><div class="bar-item"><div class="bar-h good" style="height:18%"></div><span>授权费<br>30 元 · 一次性</span></div><div class="bar-item"><div class="bar-h bad" style="height:100%"></div><span>AI 成本<br>4 元 × 12 个月</span></div></div><div class="fig-n">这个乘法做完，产品形态、定价方式、团队结构基本都定了。它不是财务问题，是产品问题</div></div>
'''
F["m8_2"]='''<div class="fig"><div class="fig-t">图：三种压缩，换掉的东西不一样</div><div class="flow"><div class="box b">蒸馏<br>换准确率</div><div class="box c">剪枝<br>换参数量</div><div class="box p">量化<br>换显存与带宽</div></div><div class="fig-n">三样都能让模型变小，但掉的分数掉在不同地方。先测清楚哪三分能掉、哪三分不能掉</div></div>
'''
F["m9_2"]='''<div class="fig"><div class="fig-t">图：口吻归微调，事实归检索，动作归代码</div><div class="flow"><div class="box p">微调 ← 说话像不像<br>德系冷淡 / 新势力热情</div><div class="box c">检索 ← 说得对不对<br>收费标准 / POI / 政策</div><div class="box g">代码 ← 能不能做<br>限速换算 / 支付</div></div><div class="fig-n">三者边界清楚，钱就花得清楚；边界一混，就会用最贵的方式去解决最便宜的问题</div></div>
'''
F["m10_2"]='''<div class="fig"><div class="fig-t">图：一句话、一张图、一秒视频，各值多少 token</div><div class="bars"><div class="bar-item"><div class="bar-h good" style="height:5%"></div><span>一句话<br>约 40 token</span></div><div class="bar-item"><div class="bar-h new" style="height:100%"></div><span>一张图<br>约 1000 token</span></div><div class="bar-item"><div class="bar-h bad" style="height:70%"></div><span>一秒视频<br>约 700 token</span></div></div><div class="fig-n">多模态的账，本质是把「像素」换成「token」。先算这个换算率，再谈体验</div></div>
'''
F["m11_2"]='''<div class="fig"><div class="fig-t">图：想得越久越准，但收益会递减</div><div class="bars"><div class="bar-item"><div class="bar-h old" style="height:58%"></div><span>直接答<br>58 分 · 1 倍成本</span></div><div class="bar-item"><div class="bar-h new" style="height:81%"></div><span>想 10 秒<br>81 分 · 3 倍成本</span></div><div class="bar-item"><div class="bar-h good" style="height:87%"></div><span>想 30 秒<br>87 分 · 8 倍成本</span></div></div><div class="fig-n">最后那 6 分值不值 5 倍的钱，由产品的错误代价决定，不由模型决定</div></div>
'''
F["m12_1"]='''<div class="fig"><div class="fig-t">图：优化到第三轮，边际收益开始塌</div><div class="bars"><div class="bar-item"><div class="bar-h bad" style="height:100%"></div><span>优化前<br>137 万</span></div><div class="bar-item"><div class="bar-h new" style="height:30%"></div><span>缓存 + 分流<br>41 万</span></div><div class="bar-item"><div class="bar-h old" style="height:26%"></div><span>再压 40%<br>得动硬件</span></div></div><div class="fig-n">软件优化的收益是有天花板的。到了某个点，瓶颈从算法变成硬件</div></div>
'''
F["m14_1"]='''<div class="fig"><div class="fig-t">图：写代码变便宜之后，最先涨的是技术债</div><div class="flow"><div class="box b">补全、生成测试</div><div class="box c">顺手多写 11 个工具函数</div><div class="box o">没人说得清哪个在用</div><div class="box r">债便宜，就会有人多借</div></div><div class="fig-n">所以流程要先立起来，再谈提速。否则提的是手速，欠的是本金</div></div>
'''
F["m15_1"]='''<div class="fig"><div class="fig-t">图：一套能力，三套配置，三份考卷</div><div class="layers"><div class="layer l1">底层能力：模型、检索、工具、护栏（一套）</div><div class="layer l3">客户配置：口吻、播报规范、权限（三套）</div><div class="layer l5">验收标准：德系零误报 / 新势力别太死板（三份）</div></div><div class="fig-n">差异抽成配置与评测标准，代码就不分叉；分叉的代码会拖死三家客户</div></div>
'''
F["m15_3"]='''<div class="fig"><div class="fig-t">图：一个 AI 功能的责任字段，五格都要有人名</div><div class="flow"><div class="box b">模型谁选</div><div class="box c">提示词谁改</div><div class="box p">数据谁供</div><div class="box o">上线谁批</div><div class="box r">回滚到哪版</div></div><div class="fig-n">五格填不满，这个功能就不该上线——因为它出事时没人接得住</div></div>
'''
