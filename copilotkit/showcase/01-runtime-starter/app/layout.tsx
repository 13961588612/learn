import { CopilotKit } from "@copilotkit/react-core";
import { CopilotSidebar } from "@copilotkit/react-ui";
import "@copilotkit/react-ui/styles.css";
import type { ReactNode } from "react";

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="zh-CN">
      <body>
        <CopilotKit runtimeUrl="/api/copilotkit">
          {children}
          <CopilotSidebar defaultOpen={false} labels={{ title: "学习助手" }} />
        </CopilotKit>
      </body>
    </html>
  );
}
