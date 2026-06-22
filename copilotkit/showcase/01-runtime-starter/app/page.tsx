export default function HomePage() {
  return (
    <main style={{ padding: 24, fontFamily: "system-ui" }}>
      <h1>CopilotKit Runtime Starter</h1>
      <p>打开右侧 Copilot 侧边栏，开始多轮对话（需配置 OPENAI_API_KEY）。</p>
      <ul>
        <li>Runtime: <code>app/api/copilotkit/route.ts</code></li>
        <li>Provider: <code>app/layout.tsx</code></li>
      </ul>
    </main>
  );
}
