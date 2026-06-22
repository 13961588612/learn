/**
 * 03_env_security_audit.ts - 环境变量安全审计
 *
 * 学习要点: OPENAI_API_KEY 不得出现在 NEXT_PUBLIC_* 或客户端 bundle
 */

const CLIENT_ENV = {
  NEXT_PUBLIC_APP_NAME: "company-agent-ui",
  NEXT_PUBLIC_API_BASE: "/api",
};

const SERVER_ENV = {
  OPENAI_API_KEY: "sk-***",
  LANGGRAPH_DEPLOYMENT_URL: "http://localhost:8123",
};

function audit(env: Record<string, string>): string[] {
  const issues: string[] = [];
  for (const [key, val] of Object.entries(env)) {
    if (key.startsWith("NEXT_PUBLIC_") && /sk-|api[_-]?key/i.test(val)) {
      issues.push(`泄漏风险: ${key} 含密钥模式`);
    }
    if (key.startsWith("NEXT_PUBLIC_") && key.includes("SECRET")) {
      issues.push(`命名违规: ${key} 不应使用 PUBLIC 前缀存 secret`);
    }
  }
  return issues;
}

function main() {
  console.log("=".repeat(50));
  console.log("03 - Env Security Audit");
  console.log("=".repeat(50));

  const bad = audit({
    NEXT_PUBLIC_OPENAI_API_KEY: "sk-leaked",
    NEXT_PUBLIC_APP_NAME: "demo",
  });
  const good = audit(CLIENT_ENV as Record<string, string>);

  console.log("\n  坏例子 issues:", bad.length ? bad : "none");
  console.log("  好例子 issues:", good.length ? good : "none");
  console.log("\n  服务端-only:", Object.keys(SERVER_ENV).join(", "));
  console.log("\n[OK] 完成");
}

main();
