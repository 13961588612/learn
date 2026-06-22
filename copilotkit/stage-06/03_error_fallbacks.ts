const FALLBACKS: Record<string, string> = {
  sse_disconnect: "连接中断，点击重试",
  a2ui_parse_error: "界面渲染失败，已显示文本回复",
  agent_5xx: "服务暂不可用",
  auth_401: "请重新登录",
};

function main() {
  console.log("=".repeat(50));
  console.log("03 - Error Fallbacks");
  console.log("=".repeat(50));
  Object.entries(FALLBACKS).forEach(([k, v]) => console.log(`  ${k}: ${v}`));
  console.log("\n[OK] 完成");
}

main();
