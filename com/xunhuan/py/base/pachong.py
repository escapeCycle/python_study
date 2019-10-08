
import re

content = '''
<td>
<a href="https://www.baidu.com/articles/zj.html" title="浙江省">浙江省主题介绍</a>
<a href="https://www.baidu.com//articles/gz.html" title="贵州省">贵州省主题介绍</a>
</td>
'''
res = r'<a .*?>(.*?)</a>'
mm = re.findall(res,content,re.S|re.M)
# for value in mm:
#     print(value)

content2 = '''
<div class="info">
    <div class="title">
            <a href=" " target="_blank">冶金西区</a>
          </div>
    <div class="houseInfo">
      <span class="houseIcon"></span>
            <a title="冶金西区网签"  href="https://lf.lianjia.com/chengjiao/c2011047821877/" >90天成交1套</a >
      <span class="cutLine">|</span><a title="冶金西区租房"  href="https://lf.lianjia.com/zufang/c2011047821877/" >8套正在出租</a >
    </div>
    <div class="positionInfo">
      <span class="positionIcon"></span>
      <a href="https://lf.lianjia.com/xiaoqu/yanjiao/" class="district" title="燕郊小区">燕郊</a >
      &nbsp;<a href="https://lf.lianjia.com/xiaoqu/tianyangcheng4dai/" class="bizcircle" title="天洋城4代小区">天洋城4代</a >&nbsp;
                  /&nbsp;1995年建成
          </div>
    <div class="title">
    <a href=" " target="_blank">ddd西区</a>
        <div class="agentInfo">
      <span class="agentIcon"></span>
      <a href="https://dianpu.lianjia.com/1000000020118766" class="agentName">易亚杰</a >
      <div class="agent_chat im-talk LOGCLICKDATA" data-lj_evtid="12951" data-lj_action_event="WebClick" data-lj_action_pid="lianjiaweb" data-lj_action_resblock_id="2011047821877" data-lj_action_resblock_name="冶金西区" data-lj_action_agent_name="易亚杰"  data-lj_action_agent_id="1000000020118766" data-lj_action_source_type="pc_xiaoqu_liebiao" data_lj_action_e_plan='{"u":1000000020118766,"v":"V1","s":"NATURAL","adId":100000131,"flow":"natural","b":"DisplayTopAgentBuilder","p":null,"sid":"1000000020118766_2011047821877","rid":"4696629365454131392"}'  data-ucid="1000000020118766" data-msg-payload="HI，您好。我正在看冶金西区小区" data-source-port="pc_lianjia_ershou_xiaoqu_liebiao">
        <i class="chatIcon"></i>
        <span>免费咨询</span>
      </div>
    </div>
        <div class="tagList">
                </div>
  </div>
  <div class="xiaoquListItemRight">
    <div class="xiaoquListItemPrice">
            <div class="totalPrice"><span>19320</span>元/m<sup>2</sup></div>
            <div class="priceDesc">
        8月二手房参考均价
      </div>
    </div>
        <div class="xiaoquListItemSellCount">
      <a title="冶金西区二手房" hre
'''
res = r'<div.*?title">.*?<a.*?>(.*?)</a>'
mm = re.findall(res,content2,re.S|re.M)
for value in mm:
    print(value)