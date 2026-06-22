/**
 * onRequest JWT 校验模式（route.ts hooks）
 */

export function validateAuthHeader(auth: string | null): { ok: boolean; userId?: string } {
  if (!auth?.startsWith("Bearer ")) return { ok: false };
  const token = auth.slice(7);
  if (token.length < 10) return { ok: false };
  return { ok: true, userId: "user-from-jwt" };
}

function main() {
  console.log("=".repeat(50));
  console.log("02 - Auth onRequest");
  console.log("=".repeat(50));
  console.log("  有效:", validateAuthHeader("Bearer eyJhbG..."));
  console.log("  无效:", validateAuthHeader(null));
  console.log("\n[OK] 完成");
}

main();
