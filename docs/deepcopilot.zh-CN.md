[鈫?杩斿洖](../README.zh-CN.md)

# 鎺ュ叆 Deep Copilot

**Deep Copilot** 鏄竴涓紑婧愮殑 AI 缂栫▼ Agent锛岀洿鎺ュ祵鍏?VS Code锛岀敱 DeepSeek V4锛圤penAI 鍏煎鍗忚锛夐┍鍔ㄣ€傛ā鍨嬮€氳繃宸ュ叿璋冪敤鏉ヨ鍐欐枃浠躲€佹悳绱唬鐮併€佹祻瑙堢綉椤点€佹墽琛?Shell 鍛戒护锛屾暣涓繃绋嬪疄鏃舵祦寮忓憟鐜板湪渚ц竟鏍忋€傛棤闇€鍚庣銆佹棤闇€ Docker銆佹棤闇€ Rust锛岀函 Node.js + VS Code API锛屾墦鍖呬负绾?94 KB 鐨勫崟鏂囦欢 bundle銆?

- **浠撳簱鍦板潃**锛歔github.com/ZhouChaunge/DeepCopilot](https://github.com/ZhouChaunge/DeepCopilot)
- **VS Code 鎵╁睍鍟嗗煄**锛氭悳绱?**Deep Copilot**锛堝彂甯冭€?*ZhouChaunge*锛?
- **鐜瑕佹眰**锛歏S Code 鈮?1.95.0

---

## 1. 瀹夎

### 鏂瑰紡 A 鈥?VS Code 鎵╁睍鍟嗗煄锛堟帹鑽愶級

1. 鎵撳紑 VS Code 鈫?**鎵╁睍** 闈㈡澘锛坄Ctrl/Cmd+Shift+X`锛夈€?
2. 鎼滅储 **Deep Copilot**銆?
3. 鐐瑰嚮**瀹夎**銆?

### 鏂瑰紡 B 鈥?瀹夎 VSIX 鍖?

浠?[GitHub Releases](https://github.com/ZhouChaunge/DeepCopilot/releases) 涓嬭浇鏈€鏂?`.vsix`锛岀劧鍚庯細

```bash
code --install-extension deep-copilot-<version>.vsix
```

---

## 2. 閰嶇疆 DeepSeek API Key

1. 鐐瑰嚮娲诲姩鏍忎腑鐨?**馃悑 Deep Copilot** 鍥炬爣锛屾墦寮€闈㈡澘銆?
2. 鐐瑰嚮闈㈡澘**鍙充笅瑙?* 馃攽 鎸夐挳銆?
3. 绮樿创浣犵殑 [DeepSeek API Key](https://platform.deepseek.com/api_keys) 骞朵繚瀛樸€?

> **鍥藉唴鐢ㄦ埛**锛氳嫢 `api.deepseek.com` 杩炴帴涓嶇ǔ瀹氾紝鍦?馃攽 寮圭獥鐨?**Base URL** 瀛楁濉叆 `https://api.deepseeki.com`銆?

---

## 3. 閫夋嫨 DeepSeek 妯″瀷

Deep Copilot 榛樿浣跨敤 `deepseek-v4-pro`銆傚湪 **VS Code 璁剧疆**锛坄Ctrl/Cmd+,`锛変腑鍒囨崲锛?

```jsonc
{
  "deepseekAgent.defaultModel": "deepseek-v4-pro"   // 鎴?"deepseek-v4-flash"
}
```

| 妯″瀷 | 璇存槑 |
|---|---|
| `deepseek-v4-pro` | 瀹屾暣娣卞害鎺ㄧ悊锛堟渶澶ф€濊€冨己搴︼級锛岄€傚悎澶嶆潅閲嶆瀯涓?Bug 鎺掓煡銆?|
| `deepseek-v4-flash` | 閫熷害鏇村揩銆佹垚鏈洿浣庯紝閫傚悎蹇€熺紪杈戜笌闂瓟銆?|

涓ゆ妯″瀷鍧囨敮鎸佹渶楂?**100 涓?token** 涓婁笅鏂囩獥鍙ｃ€侱eep Copilot 浼氳嚜鍔ㄧ鐞嗕笂涓嬫枃锛岃瑙乕搂 涓婁笅鏂囩鐞哴(#涓婁笅鏂囩鐞?銆?

---

## 4. 棣栨杩愯

鍦ㄤ晶杈规爮鐩存帴杈撳叆闇€姹傦紝Deep Copilot 鍚姩 Agent 寰幆锛氳皟鐢ㄥ伐鍏枫€佽鍙栫粨鏋溿€佹寔缁凯浠ｏ紝鐩村埌浠诲姟瀹屾垚銆?

```
鎶?src/auth/ 鐩綍涓嬬殑鎵€鏈夊洖璋冮鏍间唬鐮佹敼鎴?async/await
```

```
鎵惧嚭鎵€鏈夎皟鐢ㄤ簡搴熷純鍑芥暟 getUser() 鐨勫湴鏂癸紝骞惰縼绉诲埌 fetchUser()
```

```
淇 tests/api.test.ts 涓笁涓け璐ョ殑娴嬭瘯
```

> 榛樿鎯呭喌涓嬶紝姣忔鍐欐枃浠舵垨鎵ц Shell 鍛戒护閮戒細寮圭獥纭銆傚彲閫氳繃 [搂 瀹℃壒妯″紡](#瀹℃壒妯″紡) 璋冩暣銆?

---

## 5. 宸ュ叿闆?

Deep Copilot 缁欐ā鍨嬬殑宸ュ叿闆嗗埢鎰忎繚鎸佺簿绠€锛屽苟閬靛惊涓€涓叧閿殑璁捐鍘熷垯锛?*缂栬緫/鎿嶄綔宸ュ叿鎺掑湪鏈€鍓嶉潰**銆傝繖鏄负浜嗗鎶?DeepSeek 鍦?RLHF 璁粌涓舰鎴愮殑"鍏堣鍚庡姩"鍊惧悜鈥斺€旀妸鍔ㄤ綔宸ュ叿鍓嶇疆锛岃 Agent 鏇存灉鏂€?

| 宸ュ叿 | 璇存槑 |
|---|---|
| `apply_patch` | 搴旂敤缁熶竴鏍煎紡琛ヤ竵锛堝 hunk銆佸鏂囦欢锛夛紝闈炵畝鍗曠紪杈戠殑棣栭€夈€?|
| `str_replace_in_file` | 閫氳繃绮剧‘瀛楃涓插尮閰嶈繘琛屽師鍦版浛鎹紝閫傚悎灏忚寖鍥村敮涓€淇敼銆?|
| `write_file` | 鏂板缓鎴栬鍐欐枃浠讹紝浠呯敤浜庡叏閲忓啓鍏ャ€?|
| `run_shell` | 鍦ㄥ伐浣滃尯鏍圭洰褰曟墽琛?Shell 鍛戒护锛坣pm銆乬it銆佹祴璇曡繍琛屽櫒绛夛級銆?|
| `read_file` | 鎸夎鍙峰尯闂磋鍙栨枃浠跺唴瀹广€?|
| `grep_search` | 宸ヤ綔鍖虹骇姝ｅ垯鎼滅储锛坮ipgrep 椋庢牸锛夈€?|
| `find_files` | 鎸夋枃浠跺悕鎴?Glob 妯″紡鏌ユ壘鏂囦欢銆?|
| `list_dir` | 鍒楀嚭鐩綍鍐呭锛堥檺鍒舵繁搴︼級銆?|
| `web_search` | 閫氳繃 Tavily 鑱旂綉鎼滅储锛堥渶瑕乕鍏嶈垂 Tavily API Key](https://app.tavily.com)锛夈€?|
| `web_fetch` | 鎶撳彇浠绘剰鍏綉 URL 骞惰繑鍥炵函鏂囨湰鍐呭銆?|
| `spawn_agent` | 娲惧彂鍙瀛?Agent锛岀敤浜庡鏉傜殑澶氭枃浠舵帰绱换鍔°€?|
| `update_plan` | 鍚戜晶杈规爮 Todos 闈㈡澘鎺ㄩ€佺粨鏋勫寲浠诲姟璁″垝銆?|
| `revert_last_turn` | 鍥炴粴褰撳墠 Agent 杞瀵规墍鏈夋枃浠剁殑淇敼銆?|
| `open_file_in_editor` | 鍦ㄧ紪杈戝櫒涓墦寮€鏂囦欢骞惰烦鍒版寚瀹氳銆?|
| `mcp__<server>__<tool>` | 宸茶繛鎺?MCP 鏈嶅姟鍣ㄦ毚闇茬殑浠绘剰宸ュ叿銆?|

---

## 6. 鑱旂綉鑳藉姏

### 鑱旂綉鎼滅储锛坄web_search`锛?

鐢?[Tavily](https://app.tavily.com) 椹卞姩銆傚湪 馃攽 寮圭獥涓～鍏?Tavily API Key锛堜笌 DeepSeek Key 鍚屼竴寮圭獥锛夛紝鍗冲彲寮€鍚€傝缃悗锛孉gent 鍦ㄦ墽琛屼换鍔℃椂鍙互鑷富鎼滅储缃戦〉鈥斺€旀煡鏂囨。銆佹煡鎶ラ敊銆佹煡鏈€鏂?API 鍙樻洿銆?

### 缃戦〉鎶撳彇锛坄web_fetch`锛?

鏃犻渶棰濆 API Key銆傛姄鍙栦换鎰忓叕缃?URL锛孌eep Copilot 鍐呯疆 HTML 杞函鏂囨湰锛屾ā鍨嬫敹鍒扮殑鏄共鍑€鐨勬枃绔犳枃鏈€岄潪鍘熷 HTML 鏍囩銆傝嚜鍔ㄦ墽琛屼互涓嬪畨鍏ㄩ檺鍒讹細

- 鎷︽埅鍐呯綉/绉佹湁 IP 鑼冨洿锛堥槻 SSRF锛?
- 绂佹璺ㄥ煙閲嶅畾鍚?
- 鍝嶅簲鍐呭闄愬埗 2 MB
- 鎵€鏈?`http://` 璇锋眰闈欓粯鍗囩骇涓?`https://`

---

## 7. 瀹℃壒妯″紡

鎺у埗 Agent 鐨勮嚜涓绘潈闄愶細

| 妯″紡 | 琛屼负 |
|---|---|
| `manual` | 姣忔 `write_file` 鍜?`run_shell` 閮藉脊绐楃‘璁わ紙榛樿锛屾渶瀹夊叏锛?|
| `auto-edit` | 鍐欐枃浠惰嚜鍔ㄩ€氳繃锛孲hell 浠嶉渶纭 |
| `autopilot` | 鍏ㄩ儴鑷姩閫氳繃锛堜粎閫傚悎鍙椾俊浠诲伐浣滃尯锛?|
| `readonly` | 绂佹鎵€鏈夊啓鍏ヤ笌 Shell 鎿嶄綔 |

```jsonc
{ "deepseekAgent.approvalMode": "auto-edit" }
```

---

## 8. MCP 鏈嶅姟鍣ㄩ泦鎴?

Deep Copilot 鍐呯疆 MCP stdio 瀹㈡埛绔紝閫氳繃 `settings.json` 杩炴帴浠绘剰 MCP 鍏煎宸ュ叿鏈嶅姟鍣細

```jsonc
{
  "deepseekAgent.mcp.servers": [
    { "name": "my-db",  "command": "npx", "args": ["my-db-mcp-server"] },
    { "name": "jira",   "command": "node", "args": ["./tools/jira-mcp.js"] }
  ]
}
```

杩炴帴鍚庯紝宸ュ叿浠?`mcp__<server>__<tool>` 鐨勫舰寮忓嚭鐜板湪妯″瀷鐨?function-calling 鎺ュ彛涓€?

---

## 9. 涓婁笅鏂囩鐞?

Deep Copilot 鏀寔鏈€楂?**100 涓?token** 涓婁笅鏂囷紙DeepSeek V4 瀹屾暣绐楀彛锛夈€備袱濂楄嚜鍔ㄦ満鍒朵繚闅滃璇濆仴搴凤細

**鑷姩鍘嬬缉** 鈥?浼扮畻 token 瓒呰繃 `compactBudgetTokens`锛堥粯璁?`600000`锛夋椂锛岃緝鑰佺殑宸ュ叿缁撴灉琚浛鎹负绠€鐭憳瑕併€傞鏉＄敤鎴锋秷鎭缁堜繚鐣欍€傛帴杩?90 涓?token 鏃惰Е鍙戠揣鎬ュ帇缂╋紝闃叉 API 杩斿洖 HTTP 400 涓婁笅鏂囪秴闀块敊璇€?

**娴佸紡鍙傛暟棰勮** 鈥?妯″瀷鐢熸垚宸ュ叿璋冪敤鏃讹紝Deep Copilot 鍦?`path` 瀛楁鍒氬埌杈炬椂灏辩珛鍗虫樉绀?姝ｅ湪缂栬緫 `src/auth.ts`鈥?锛屾棤闇€绛夊緟瀹屾暣鍙傛暟鐢熸垚銆傝繖涓?GitHub Copilot 鐨勫疄鏃剁紪杈戦瑙堜綋楠屼竴鑷淬€?

---

## 10. 閰嶇疆鍙傝€?

鎵€鏈夎缃潎鍦?`deepseekAgent.*` 鍛藉悕绌洪棿涓嬶細

```jsonc
{
  "deepseekAgent.defaultModel":        "deepseek-v4-pro",
  "deepseekAgent.apiBaseUrl":          "",          // 鐣欑┖ = api.deepseek.com
  "deepseekAgent.approvalMode":        "manual",
  "deepseekAgent.interactionMode":     "agent",     // "agent" | "ask"
  "deepseekAgent.maxIterations":       15,
  "deepseekAgent.compactBudgetTokens": 600000,
  "deepseekAgent.postEditDiagnostics": true,        // 姣忔缂栬緫鍚庤拷鍔?LSP 璇婃柇
  "deepseekAgent.enableDebugLog":      true,        // 鍐欐棩蹇楀埌 .deep-copilot/logs/
  "deepseekAgent.mcp.servers":         []
}
```

---

## 11. 璁捐浜偣

### Skill 鐑彃鎷?

Skill 灏辨槸鐩綍閲岀殑 Markdown 鏂囦欢鈥斺€斾笉闇€瑕佹彃浠舵竻鍗曪紝涓嶉渶瑕侀噸杞芥墿灞曘€侱eep Copilot 杩愯鏃舵寜浼樺厛绾ч『搴忔壂鎻忎笁涓洰褰曪細

```
~/.deepcopilot/skills/   鈫?棣栨鍚姩鑷姩鍒涘缓
~/.claude/skills/        鈫?鍏煎 Claude Code
~/.copilot/skills/       鈫?鍏煎 GitHub Copilot
```

姣忎釜 Skill 鏄竴涓瓙鐩綍锛屽寘鍚甫 YAML frontmatter 鐨?`SKILL.md`锛?

```markdown
---
name: my-skill
description: 鏄剧ず鍦ㄦ枩鏉犲懡浠ゅ脊绐椾腑鐨勪竴琛岀畝浠?
argument-hint: 鍙€夋彁绀烘枃瀛?
---

... 缁欐ā鍨嬬殑鎸囦护鍐呭 ...
```

鎶婄洰褰曟墧杩涘幓锛屼笅涓€鏉℃秷鎭嵆鍙娇鐢ㄢ€斺€旀棤闇€閲嶅惎锛屾棤闇€閲嶈浇銆?

**娉ㄥ叆鍘熺悊**

Skill 鍐呭**涓嶆槸**浠ョ敤鎴锋秷鎭垨绯荤粺鎻愮ず鎻掑叆鐨勩€侱eep Copilot 鍦ㄧ敤鎴锋秷鎭箣鍓嶅悎鎴愪竴瀵?`read_file` 宸ュ叿璋冪敤 + 宸ュ叿缁撴灉骞舵敞鍏ュ璇濅笂涓嬫枃锛?

```
assistant  鈫? tool_call: read_file("~/.claude/skills/my-skill/SKILL.md")
tool       鈫? <SKILL.md 鍐呭>
user       鈫? <鐢ㄦ埛鐨勫疄闄呮秷鎭?
```

妯″瀷灏?Skill 瑙嗕负**鑷繁璇诲埌鐨?*淇℃伅锛岃€岄潪鐢ㄦ埛鏂藉姞鐨勬寚浠わ紝鎸囦护閬靛惊鐨勫彲闈犳€ц繙楂樹簬绯荤粺鎻愮ず鎴栫敤鎴锋秷鎭敞鍏ャ€傝繖涓?GitHub Copilot 鍐呴儴娉ㄥ叆 Skill 鐨勬柟寮忓畬鍏ㄤ竴鑷淬€?

涓夌洰褰曚箣闂撮噰鐢ㄣ€屽厛鍖归厤鑰呬紭鍏堛€嶇瓥鐣ワ細`~/.deepcopilot/skills/` 涓殑鍚屽悕 Skill 闈欓粯瑕嗙洊 Claude Code 鎴?GitHub Copilot 鐩綍涓殑瀵瑰簲椤癸紝璁╀綘缁存姢涓汉瑕嗙洊灞傝€屾棤闇€鏀瑰姩鍏变韩鏂囦欢銆傛潵鑷笁涓洰褰曠殑鎵€鏈?Skill 缁熶竴鍒楀湪 `/` 鍛戒护寮圭獥涓紝闄勫甫绠€浠嬪拰鎻愮ず鏂囧瓧銆?

### 鎰熺煡涓婁笅鏂囩紦瀛樼殑绯荤粺鎻愮ず

绯荤粺鎻愮ず鍦?`__DYNAMIC_BOUNDARY__` 鏍囪澶勪竴鍒嗕负浜岋細

- **闈欐€侀儴鍒?* 鈥?琛屼负鍘熷垯銆佸伐鍏疯鍒欍€佽姘旈鏍笺€傚湪鎵€鏈夎姹備腑瀹屽叏涓€鑷达紝鍙懡涓?DeepSeek 涓婁笅鏂囩紦瀛樸€傚悗缁疆娆″彧闇€鏀粯缂撳瓨鍛戒腑浠锋牸锛岃€岄潪瀹屾暣杈撳叆浠锋牸銆?
- **鍔ㄦ€侀儴鍒?* 鈥?姣忚疆閲嶆柊璁＄畻锛氬涓荤郴缁熶俊鎭€佸伐浣滃尯鎸囦护锛坄DEEPCOPILOT.md`锛夈€佺敤鎴疯蹇嗭紙`~/.deepcopilot/memory.md`锛夈€?

杩欎竴璁捐鏈€澶у寲浜嗛珮浠峰€奸潤鎬佸唴瀹圭殑缂撳瓨鍛戒腑鐜囷紝鍚屾椂淇濇寔浜嗕釜鎬у寲閮ㄥ垎鐨勫疄鏃舵€с€?

### 宸ヤ綔鍖虹骇宸ュ叿閽╁瓙

鍦ㄥ伐浣滃尯鏍圭洰褰曟斁缃?`.deepcopilot/hooks.json`锛屽彲灏?Shell 鍛戒护鎸傝浇鍒颁换鎰忓伐鍏蜂簨浠讹細

```jsonc
{
  "hooks": [
    {
      "event":      "after_tool",
      "tool":       "write_file",
      "run":        "npm test --reporter=dot",
      "on_failure": "inject_error"
    }
  ]
}
```

閽╁瓙杈撳嚭娉ㄥ叆鍥炴ā鍨嬩笂涓嬫枃銆侫gent 鐩存帴璇诲彇娴嬭瘯缁撴灉骞惰嚜鎴戠籂閿欙紝鏃犻渶浣犳墜鍔ㄥ鍒剁粓绔緭鍑恒€?

### 瀛?Agent 娲惧彂锛坄spawn_agent`锛?

瀵逛簬闇€瑕佽鍙栧ぇ閲忔枃浠剁殑浠诲姟锛堜緥濡?姊崇悊 `src/` 鏋舵瀯"銆?鎵惧嚭 `getUser()` 鐨勬墍鏈夎皟鐢ㄧ偣"锛夛紝Deep Copilot 鍙互娲惧彂鐙珛鐨勫彧璇诲瓙 Agent銆傛瘡涓瓙 Agent 鑾峰緱涓撳睘鐨?focused prompt锛屽湪鐙珛涓婁笅鏂囦腑杩愯锛岃繑鍥炵粨鏋勫寲 Markdown 鎽樿銆傚悓涓€杞娲惧彂鐨勫涓瓙 Agent 骞惰鎵ц銆?

### 澶氫細璇濆苟琛?

Agent 寰幆浠?session ID 涓洪敭鐙珛缁存姢銆傛煇涓細璇濈殑浠诲姟姝ｅ湪杩愯鏃讹紝鍙互鍒囨崲鍒板彟涓€涓細璇濆紑濮嬫柊瀵硅瘽銆備簨浠舵寔缁紦鍐诧紝鍒囧洖鍘熶細璇濆悗鑷姩鍥炴斁鍏ㄩ儴杩涘害銆?

### 闆跺悗绔灦鏋?

鍏ㄩ儴閫昏緫杩愯鍦?VS Code 鎵╁睍涓绘満鍐呫€傜敓浜ф瀯寤轰骇鐗╃害 94 KB锛岄浂杩愯鏃?npm 渚濊禆鈥斺€斾粎渚濊禆 VS Code API 涓?Node.js 鍐呯疆妯″潡銆俈S Code 涔嬪鏃犱换浣曢渶瑕佸畨瑁呫€佹洿鏂版垨淇濇寔杩愯鐨勭粍浠躲€?

