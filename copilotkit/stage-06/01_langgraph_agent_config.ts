export type LangGraphAgentConfig = {
  deploymentUrl: string;
  graphId: string;
  configurable?: Record<string, string>;
};

export const langGraphConfig: LangGraphAgentConfig = {
  deploymentUrl: process.env.LANGGRAPH_DEPLOYMENT_URL ?? "http://localhost:8123",
  graphId: "research-agent",
  configurable: { authorization: "Bearer <from-onRequest>" },
};

function main() {
  console.log("=".repeat(50));
  console.log("01 - LangGraph Agent Config");
  console.log("=".repeat(50));
  console.log(JSON.stringify(langGraphConfig, null, 2));
  console.log("\n  Runtime: new LangGraphAgent({ deploymentUrl, graphId })");
  console.log("\n[OK] 完成");
}

main();
