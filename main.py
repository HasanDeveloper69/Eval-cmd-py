 
 ​import​ ​os 
 ​import​ ​discord 
 ​from​ ​discord​.​ext​ ​import​ ​commands 
 ​import​ ​requests 
  
  
 ​import​ ​datetime 
 ​import​ ​io 
 ​import​ ​contextlib 
 ​import​ ​textwrap 
  
 ​os​.​system​(​"pip install buttons"​) 
  
 ​from​ ​discord​.​ext​.​buttons​ ​import​ ​Paginator 
  
 ​prefix​ ​=​ ​"" 
  
 ​token​ ​=​ ​"" 
  
 ​client​ ​=​ ​discord​.​Client​() 
 ​client​ ​=​ ​commands​.​Bot​(​command_prefix​=​prefix​, ​case_insensitive​=​True​, ​help_command​=​None​, 
 ​  ​intents​=​discord​.​Intents​.​all​(), ​shard_count​=​1​) 
  
  
 ​def​ ​clean_code​(​content​): 
 ​    ​"""Automatically removes code blocks from the code.""" 
 ​     ​#remove ```py\n``` 
 ​    ​if​ ​content​.​startswith​(​"```"​) ​and​ ​content​.​endswith​(​"```"​): 
 ​        ​return​ ​"​\n​"​.​join​(​content​.​split​(​"​\n​"​)[​1​:])[:​-​3​] 
 ​    ​else​: 
 ​        ​return​ ​content 
  
  
  
 ​class​ ​Pag​(​Paginator​): 
 ​    ​async​ ​def​ ​teardown​(​ctx​): 
 ​        ​try​: 
 ​            ​await​ ​ctx​.​page​.​clear_reactions​() 
 ​        ​except​ ​discord​.​HTTPException​: 
 ​            ​pass 
  
 ​from​ ​traceback​ ​import​ ​format_exception 
  
 ​def​ ​botowner​(​ctx​): 
 ​  ​return​ ​ctx​.​message​.​author​.​id​ ​==​ ​362266240380698635 
 ​  
  
 ​@​commands​.​check​(​botowner​) 
 ​@​client​.​command​(​name​=​"eval"​, ​aliases​=​[​"exec"​, ​"execute"​, ​"codexe"​, ​"jsk"​], ​hidden​=​True​) 
 ​async​ ​def​ ​_eval​(​ctx​, *, ​code​): 
 ​    ​code​ ​=​ ​clean_code​(​code​) 
  
 ​    ​local_variables​ ​=​ { 
 ​        ​"discord"​: ​discord​, 
 ​        ​"commands"​: ​commands​, 
 ​        ​"bot"​: ​client​, 
 ​        ​"token"​: ​token​, 
 ​        ​"client"​: ​client​, 
 ​        ​"ctx"​: ​ctx​, 
 ​        ​"channel"​: ​ctx​.​channel​, 
 ​        ​"author"​: ​ctx​.​author​, 
 ​        ​"guild"​: ​ctx​.​guild​, 
 ​        ​"message"​: ​ctx​.​message​, 
 ​    } 
  
 ​    ​stdout​ ​=​ ​io​.​StringIO​() 
  
 ​    ​try​: 
 ​        ​with​ ​contextlib​.​redirect_stdout​(​stdout​): 
 ​            ​exec​( 
 ​                ​f"async def func():​\n​{​textwrap​.​indent​(​code​, ​'    '​)​}​"​, 
 ​                ​local_variables​, 
 ​            ) 
  
 ​            ​obj​ ​=​ ​await​ ​local_variables​[​"func"​]() 
 ​            ​result​ ​=​ ​f"​{​stdout​.​getvalue​()​}​\n​-- ​{​obj​}​\n​" 
  
 ​    ​except​ ​Exception​ ​as​ ​e​: 
 ​        ​result​ ​=​ ​""​.​join​(​format_exception​(​e​, ​e​, ​e​.​__traceback__​)) 
  
 ​    ​pager​ ​=​ ​Pag​( 
 ​        ​timeout​=​180​, 
 ​        ​use_defaults​=​True​, 
 ​        ​entries​=​[​result​[​i​ : ​i​ ​+​ ​2000​] ​for​ ​i​ ​in​ ​range​(​0​, ​len​(​result​), ​2000​)], 
 ​        ​length​=​1​, 
 ​        ​prefix​=​"py​\n​"​, 
 ​        ​suffix​=​""​, 
 ​    ) 
  
 ​    ​await​ ​pager​.​start​(​ctx​) 
  
  
 ​client​.​run​(​token​)
