/**
 * 04_ag_ui_event_parser.ts - 解析 AG-UI SSE 事件（教学用 NDJSON）
 */

import type { AgUiEvent } from "../shared/types.ts";

const SAMPLE_LINES = [
  '{"type":"message_start","message":{"role":"assistant"}}',
  '{"type":"content_block_delta","delta":{"text":"你好"}}',
  '{"type":"tool_call_start","toolCall":{"name":"navigateTo"}}',
  '{"type":"message_stop"}',
];

function parseLine(line: string): AgUiEvent | null {
  try {
    return JSON.parse(line) as AgUiEvent;
  } catch {
    return null;
  }
}

function summarize(events: AgUiEvent[]): void {
  for (const e of events) {
    const t = e.type as string;
    if (t === "content_block_delta") {
      const delta = e.delta as { text?: string };
      process.stdout.write(delta?.text ?? "");
    } else {
      console.log(`\n  [${t}]`);
    }
  }
}

function main() {
  console.log("=".repeat(50));
  console.log("04 - AG-UI Event Parser");
  console.log("=".repeat(50));
  console.log("\n  流式文本: ", "");
  const events = SAMPLE_LINES.map(parseLine).filter(Boolean) as AgUiEvent[];
  summarize(events);
  console.log("\n\n[OK] 完成");
}

main();
