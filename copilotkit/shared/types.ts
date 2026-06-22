/**
 * 共享类型与工具（各 stage 可 import）
 */

export type AgUiEvent = {
  type: string;
  [key: string]: unknown;
};

export type A2UiMessage =
  | { kind: "createSurface"; surfaceId: string; catalogId: string }
  | { kind: "updateComponents"; surfaceId: string; components: unknown[] }
  | { kind: "updateDataModel"; surfaceId: string; path: string; value: unknown };

export function redactPii(value: string): string {
  return value.replace(/\b[\w.-]+@[\w.-]+\.\w+\b/g, "[email]").replace(/\d{11}/g, "[phone]");
}

export function assertNever(x: never): never {
  throw new Error(`Unexpected: ${JSON.stringify(x)}`);
}
